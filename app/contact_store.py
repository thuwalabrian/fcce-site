"""Persist contact-form submissions in PostgreSQL or SQLite."""

from __future__ import annotations

import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_DB_PATH = Path(__file__).resolve().parent.parent / "data" / "contact_submissions.db"


def _database_url() -> str:
    url = os.environ.get("DATABASE_URL") or os.environ.get("POSTGRES_URL") or ""
    if url.startswith("postgres://"):
        url = "postgresql://" + url[len("postgres://") :]
    return url


def _sqlite_path() -> Path:
    configured = os.environ.get("FCCE_DB_PATH")
    return Path(configured) if configured else DEFAULT_DB_PATH


def _postgres_connect():
    try:
        import psycopg
    except ImportError as exc:
        raise RuntimeError("PostgreSQL configured but psycopg is not installed") from exc
    return psycopg.connect(_database_url(), connect_timeout=10)


def _sqlite_connect() -> sqlite3.Connection:
    path = _sqlite_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    if _database_url():
        with _postgres_connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS contact_submissions (
                        id BIGSERIAL PRIMARY KEY,
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
        return

    with _sqlite_connect() as conn:
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
    values = (name, organisation, email, phone, address, city, country, service, message, created_at)

    if _database_url():
        with _postgres_connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO contact_submissions
                        (name, organisation, email, phone, address, city, country, service, message, created_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id
                    """,
                    values,
                )
                return int(cursor.fetchone()[0])

    with _sqlite_connect() as conn:
        cursor = conn.execute(
            """
            INSERT INTO contact_submissions
                (name, organisation, email, phone, address, city, country, service, message, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            values,
        )
        conn.commit()
        return int(cursor.lastrowid)


def count_submissions() -> int:
    init_db()
    if _database_url():
        with _postgres_connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM contact_submissions")
                return int(cursor.fetchone()[0])

    with _sqlite_connect() as conn:
        row = conn.execute("SELECT COUNT(*) AS n FROM contact_submissions").fetchone()
        return int(row["n"])
