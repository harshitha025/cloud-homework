from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Cloud app is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

import boto3

s3 = boto3.client('s3')

@app.get("/upload")
def upload():
    try:
        file_name = "test.txt"
        with open(file_name, "w") as f:
            f.write("Hello from EC2")

        s3.upload_file(file_name, "cloud-homework-harsh-123", file_name)

        return {"status": "uploaded to s3"}
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/info")
def info():
    return {
        "service": "Cloud Homework API",
        "deployment": "Docker on EC2",
        "status": "running"
    }