import uvicorn
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os

from database import engine
from routers import clients, matters, documents, billing

# Import your models here (after defining them)
# from models import Base

app = FastAPI(title="Legal Case Management System", version="1.0.0", openapi_url="/openapi.json", docs_url="/docs")

# CORS Configuration
origins = ["*"]  # Replace with your allowed origins in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Database Initialization (You might need to adapt this based on your model)
# Base.metadata.create_all(bind=engine)

# Router Registration
app.include_router(clients.router)
app.include_router(matters.router)
app.include_router(documents.router)
app.include_router(billing.router)

# Health Check Endpoint
@app.get('/health')
def health_check():
    return {'status': 'ok'}

# Exception Handling
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={'detail': exc.detail})

# Static File Serving
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

    @app.get("/{{file_path:path}}")
    async def serve_frontend(file_path: str):
        if file_path.startswith("api/") or file_path.startswith("static/") or file_path == "":
            return None  # Let API routes and static files handle it
        static_file = os.path.join("static", file_path)
        if os.path.isfile(static_file):
            return FileResponse(static_file)
        return FileResponse("static/index.html")  # SPA routing

# Main execution block
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
