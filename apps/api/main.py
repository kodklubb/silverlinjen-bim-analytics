
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.api.routes.quantities import router as quantity_router


app = FastAPI(
    title="Silverlinjen BIM Analytics API",
    description=(
        "OpenBIM Infrastructure Data Analytics API"
    ),
    version="0.1.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


app.include_router(
    quantity_router,
    prefix="/api/v1",
)


@app.get("/health", tags=["System"])
def health_check():
    return {
        "status": "healthy",
        "service": "silverlinjen-bim-api",
        "version": "0.1.0",
    }
