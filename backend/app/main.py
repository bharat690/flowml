from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.routes import upload, train, export, workflow
from app.core.config import settings
from app.core.database import init_db

app = FastAPI(
    title="FlowML API",
    description="Visual ML Workflow Builder Backend",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/api/upload", tags=["Upload"])
app.include_router(train.router, prefix="/api/train", tags=["Train"])
app.include_router(export.router, prefix="/api/export", tags=["Export"])
app.include_router(workflow.router, prefix="/api/workflow", tags=["Workflow"])


@app.on_event("startup")
async def startup_event():
    await init_db()


@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}


@app.get("/")
async def root():
    return {"message": "FlowML API is running", "docs": "/api/docs"}