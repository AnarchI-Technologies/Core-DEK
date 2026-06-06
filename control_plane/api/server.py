from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "system": "LumenCore DEK",
        "status": "ONLINE"
    }

@app.get("/health")
def health():
    return {
        "cluster": "HEALTHY"
    }
