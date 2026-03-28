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
    file_name = "test.txt"
    
    with open(file_name, "w") as f:
        f.write("Hello from EC2")

    s3.upload_file(file_name, "cloud-homework-harsh-123", file_name)

    return {"status": "uploaded to s3"}