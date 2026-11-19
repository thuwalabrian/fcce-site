"""Persist contact-form submissions in a small SQLite database."""

from __future__ import annotations

import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_DB_PATH = Path(__file__).resolve().parent.parent / "data" / "contact_submissions.db"


def _db_path() -> Path:
    configured = os.environ.get("FCCE_DB_PATH")
    return Path(configured) if configured else DEFAULT_DB_PATH


def _connect() -> sqlite3.Connection:
    path = _db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with _connect() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS contact_submissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                organisation TEXT,
                email TEXT NOT NULL,
                phone TEXT,
                address TEXT,
                city TEXT,
                country TEXT,
                service TEXT,
                message TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        existing = {row["name"] for row in conn.execute("PRAGMA table_info(contact_submissions)")}
        for column in ("address", "city", "country"):
            if column not in existing:
                conn.execute(f"ALTER TABLE contact_submissions ADD COLUMN {column} TEXT")
        conn.commit()


def save_submission(
    *, name: str, email: str, message: str,
    organisation: str = "", phone: str = "", address: str = "",
    city: str = "", country: str = "", service: str = "",
) -> int:
    init_db()
    created_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with _connect() as conn:
        cursor = conn.execute(
            """
            INSERT INTO contact_submissions
                (name, organisation, email, phone, address, city, country, service, message, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (name, organisation, email, phone, address, city, country, service, message, created_at),
        )
        conn.commit()
        return int(cursor.lastrowid)


def count_submissions() -> int:
    init_db()
    with _connect() as conn:
        row = conn.execute("SELECT COUNT(*) AS n FROM contact_submissions").fetchone()
        return int(row["n"])