from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app import site_content as content
from app import contact_store
from app.routes import contact as contact_routes

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="FC Consulting Engineers")
app.include_router(contact_routes.router)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.on_event("startup")
def initialize_database():
    contact_store.init_db()


def render(request: Request, template: str, status_code: int = 200, **context) -> HTMLResponse:
    context.update(
        {
            "request": request,
            "current_year": 2026,
            "site": content,
            "nav": content.NAV,
            "offices": content.OFFICES,
            "email": content.EMAIL,
            "hero_image": content.HERO_IMAGE,
        }
    )
    return templates.TemplateResponse(request=request, name=template, context=context, status_code=status_code)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return render(request, "pages/home.html", page="home")


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return render(request, "pages/about.html", page="about")


@app.get("/services", response_class=HTMLResponse)
async def services(request: Request):
    return render(request, "pages/services.html", page="services")


@app.get("/services/{slug}", response_class=HTMLResponse)
async def service_detail(request: Request, slug: str):
    service = next((s for s in content.SERVICES if s["slug"] == slug), None)
    if service is None:
        return render(request, "pages/not_found.html", page="404", status_code=404)
    return render(request, "pages/service_detail.html", page="services", service=service)


@app.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    return render(request, "pages/projects.html", page="projects")


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    sent = request.query_params.get("sent") == "1"
    error = request.query_params.get("error") == "1"
    return render(request, "pages/contact.html", page="contact", sent=sent, form_error=error)


@app.get("/health")
async def health():
    return {"status": "ok"}