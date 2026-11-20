from __future__ import annotations

import json
import os
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.gzip import GZipMiddleware

from app import contact_store
from app import site_content as content
from app.routes import contact as contact_routes

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="FC Consulting Engineers")
app.include_router(contact_routes.router)
app.add_middleware(GZipMiddleware, minimum_size=500)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.on_event("startup")
def initialize_database():
    contact_store.init_db()


def get_site_url(request: Request) -> str:
    configured = os.environ.get("FCCE_SITE_URL", "").strip().rstrip("/")
    return configured or str(request.base_url).rstrip("/")


def organization_schema(site_url: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "@id": site_url + "/#organization",
        "name": "FC Consulting Engineers",
        "alternateName": "FCCE",
        "url": site_url + "/",
        "logo": site_url + "/static/img/FCCE%20Logo-hd.png",
        "image": site_url + content.HERO_IMAGE,
        "description": "Independent engineering and environmental consulting for sustainable energy, electrical power, renewable energy and environmental projects.",
        "email": content.EMAIL,
        "telephone": content.OFFICES[0]["phone"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Plot No. 43/793, Area 43",
            "addressLocality": "Lilongwe",
            "addressCountry": "MW",
            "postalCode": "31208",
        },
        "areaServed": ["Malawi", "Southern Africa", "Africa"],
        "slogan": "The future is green",
        "knowsAbout": ["Sustainable energy", "Electrical power", "Renewable energy", "Environmental assessment", "Project management"],
        "contactPoint": [{
            "@type": "ContactPoint",
            "telephone": content.OFFICES[0]["phone"],
            "contactType": "sales",
            "email": content.EMAIL,
            "availableLanguage": ["English"],
        }],
    }


def breadcrumb_schema(site_url: str, name: str, path: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": site_url + "/"},
            {"@type": "ListItem", "position": 2, "name": name, "item": site_url + path},
        ],
    }


def render(request: Request, template: str, status_code: int = 200, **context) -> HTMLResponse:
    site_url = get_site_url(request)
    path = str(request.url.path)
    canonical_url = site_url + path

    if request.url.query:
        canonical_url = site_url + path

    structured_data = context.pop("structured_data", organization_schema(site_url))
    context.update({
        "request": request,
        "current_year": 2026,
        "site": content,
        "nav": content.NAV,
        "offices": content.OFFICES,
        "email": content.EMAIL,
        "hero_image": content.HERO_IMAGE,
        "canonical_url": canonical_url,
        "social_image_url": site_url + "/static/img/media/solar-hillside.jpg",
        "structured_data": json.dumps(structured_data, ensure_ascii=False),
    })
    return templates.TemplateResponse(request=request, name=template, context=context, status_code=status_code)


@app.exception_handler(404)
async def custom_not_found(request: Request, exc):
    return render(request, "pages/not_found.html", page="404", status_code=404, robots="noindex,nofollow")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    site_url = get_site_url(request)
    home_schema = {
        "@context": "https://schema.org",
        "@graph": [
            organization_schema(site_url),
            {
                "@type": "WebSite",
                "@id": site_url + "/#website",
                "url": site_url + "/",
                "name": "FC Consulting Engineers",
                "publisher": {"@id": site_url + "/#organization"},
                "inLanguage": "en",
            },
        ],
    }
    return render(request, "pages/home.html", page="home", structured_data=home_schema)


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    site_url = get_site_url(request)
    return render(request, "pages/about.html", page="about", structured_data={
        "@context": "https://schema.org",
        "@graph": [organization_schema(site_url), breadcrumb_schema(site_url, "About", "/about")],
    })


@app.get("/services", response_class=HTMLResponse)
async def services(request: Request):
    site_url = get_site_url(request)
    return render(request, "pages/services.html", page="services", structured_data={
        "@context": "https://schema.org",
        "@graph": [organization_schema(site_url), breadcrumb_schema(site_url, "Services", "/services")],
    })


@app.get("/services/{slug}", response_class=HTMLResponse)
async def service_detail(request: Request, slug: str):
    service = next((s for s in content.SERVICES if s["slug"] == slug), None)
    if service is None:
        return render(request, "pages/not_found.html", page="404", status_code=404, robots="noindex,nofollow")

    site_url = get_site_url(request)
    service_schema = {
        "@context": "https://schema.org",
        "@graph": [
            organization_schema(site_url),
            {
                "@type": "Service",
                "name": service["title"],
                "description": service["body"],
                "provider": {"@id": site_url + "/#organization"},
                "url": site_url + "/services/" + slug,
                "areaServed": ["Malawi", "Southern Africa", "Africa"],
            },
            breadcrumb_schema(site_url, service["title"], "/services/" + slug),
        ],
    }
    return render(request, "pages/service_detail.html", page="services", service=service, structured_data=service_schema)


@app.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    site_url = get_site_url(request)
    return render(request, "pages/projects.html", page="projects", structured_data={
        "@context": "https://schema.org",
        "@graph": [organization_schema(site_url), breadcrumb_schema(site_url, "Projects", "/projects")],
    })


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    sent = request.query_params.get("sent") == "1"
    error = request.query_params.get("error") == "1"
    site_url = get_site_url(request)
    return render(request, "pages/contact.html", page="contact", sent=sent, form_error=error, structured_data={
        "@context": "https://schema.org",
        "@graph": [organization_schema(site_url), breadcrumb_schema(site_url, "Contact", "/contact")],
    })


@app.get("/robots.txt", response_class=PlainTextResponse)
async def robots(request: Request):
    site_url = get_site_url(request)
    text = "User-agent: *\nAllow: /\nDisallow: /health\n\nSitemap: " + site_url + "/sitemap.xml\n"
    return PlainTextResponse(text)


@app.get("/sitemap.xml", response_class=PlainTextResponse)
async def sitemap(request: Request):
    site_url = get_site_url(request)
    urls = ["/", "/about", "/services", "/projects", "/contact"]
    urls.extend("/services/" + service["slug"] for service in content.SERVICES)
    entries = []
    for path in urls:
        priority = "1.0" if path == "/" else ("0.9" if path in ("/services", "/projects") else "0.8")
        entries.append(
            "  <url><loc>" + site_url + path + "</loc><lastmod>2026-11-20</lastmod>"
            "<changefreq>monthly</changefreq><priority>" + priority + "</priority></url>"
        )
    xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + \
          "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n" + \
          "\n".join(entries) + "\n</urlset>"
    return PlainTextResponse(xml, media_type="application/xml")


@app.get("/health")
async def health():
    return {"status": "ok"}
