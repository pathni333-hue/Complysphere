from fastapi import FastAPI
from routers import auth, controls, evidence, matrix, reports

app = FastAPI(title="ComplySphere API")

app.include_router(auth.router, prefix="/auth")
app.include_router(controls.router, prefix="/controls")
app.include_router(evidence.router, prefix="/evidence")
app.include_router(matrix.router, prefix="/matrix")
app.include_router(reports.router, prefix="/reports")

@app.get("/")
def root():
    return {"message": "ComplySphere API is running"}
