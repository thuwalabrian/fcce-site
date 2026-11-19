"""Contact form submission endpoint."""

from __future__ import annotations

import re

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse

from app import contact_store

router = APIRouter()

EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
MAX_LEN = 2000


def _clean(value: str | None, limit: int = MAX_LEN) -> str:
    return (value or "").strip()[:limit]


def _validate(name: str, email: str, message: str) -> list[str]:
    errors: list[str] = []
    if not name:
        errors.append("Please enter your full name.")
    if not email:
        errors.append("Please enter your email address.")
    elif not EMAIL_RE.match(email):
        errors.append("Please enter a valid email address.")
    if not message:
        errors.append("Please tell us a little about your project.")
    return errors


def _wants_json(request: Request) -> bool:
    accept = request.headers.get("accept", "")
    requested_with = request.headers.get("x-requested-with", "")
    return "application/json" in accept or requested_with.lower() == "fetch"


@router.post("/contact")
async def submit_contact(
    request: Request,
    name: str = Form(""),
    organisation: str = Form(""),
    email: str = Form(""),
    phone: str = Form(""),
    address: str = Form(""),
    city: str = Form(""),
    country: str = Form(""),
    service: str = Form(""),
    message: str = Form(""),
):
    name = _clean(name, 200)
    organisation = _clean(organisation, 200)
    email = _clean(email, 254)
    phone = _clean(phone, 50)
    address = _clean(address, 300)
    city = _clean(city, 100)
    country = _clean(country, 100)
    service = _clean(service, 100)
    message = _clean(message)

    errors = _validate(name, email, message)
    if errors:
        if _wants_json(request):
            return JSONResponse({"ok": False, "errors": errors}, status_code=422)
        return RedirectResponse(url="/contact?error=1#callback", status_code=303)

    submission_id = contact_store.save_submission(
        name=name,
        email=email,
        message=message,
        organisation=organisation,
        phone=phone,
        service=service,
        address=address,
        city=city,
        country=country,
    )

    if _wants_json(request):
        return JSONResponse(
            {
                "ok": True,
                "id": submission_id,
                "message": "Thank you — your request has been received. We’ll be in touch within one working day.",
            },
            status_code=201,
        )

    return RedirectResponse(url="/contact?sent=1#callback", status_code=303)