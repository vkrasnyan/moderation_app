import os
import requests
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()

API_USER = os.getenv("SIGHTENGINE_USER")
API_SECRET = os.getenv("SIGHTENGINE_SECRET")

async def check_nsfw_image(file):
    if not API_USER or not API_SECRET:
        raise Exception("Missing Sightengine credentials")

    file_bytes = await file.read()
    response = requests.post(
        "https://api.sightengine.com/1.0/check.json",
        files={"media": ("image.jpg", file_bytes)},
        data={
            "models": "nudity-2.1",  # nudity
            "api_user": API_USER,
            "api_secret": API_SECRET,
        }
    )
    if response.status_code != 200:
        raise Exception("Sightengine API error")

    result = response.json()

    nudity = result.get("nudity", {})
    sexual_activity = nudity.get("sexual_activity", 0)
    sexual_display = nudity.get("sexual_display", 0)
    erotica = nudity.get("erotica", 0)


    nsfw_score = max(sexual_activity, sexual_display, erotica)

    if nsfw_score > 0.7:
        return JSONResponse(content={"status": "REJECTED", "reason": "NSFW content"})
    return JSONResponse(content={"status": "OK"})
