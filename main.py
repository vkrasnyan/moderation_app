import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException
from moderation import check_nsfw_image

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()


@app.post("/moderate")
async def moderate_image(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Only .jpg and .png files are allowed.")

    try:
        status = await check_nsfw_image(file)
        return status
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
