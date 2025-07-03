import random
from fastapi.responses import JSONResponse

async def check_nsfw_image(file):
    await file.read()
    nsfw_score = random.uniform(0, 1)  # мок nsfw_score

    if nsfw_score > 0.7:
        return JSONResponse(content={"status": "REJECTED", "reason": "NSFW content"})
    return JSONResponse(content={"status": "OK"})

# async def check_nsfw_image(file):
#     DEEP_AI_API_KEY = os.getenv("DEEP_AI_API_KEY")
#     if not DEEP_AI_API_KEY:
#         raise Exception("Missing DEEP_AI_API_KEY environment variable")
#
#     response = requests.post(
#         "https://api.deepai.org/api/nsfw-detector",
#         files={"image": await file.read()},
#         headers={"api-key": DEEP_AI_API_KEY},
#     )
#
#     if response.status_code != 200:
#         raise Exception("Failed to connect to DeepAI API")
#
#     result = response.json()
#     nsfw_score = result.get("output", {}).get("nsfw_score")
#
#     if nsfw_score is None:
#         raise Exception("Invalid response from DeepAI")
#
#     if nsfw_score > 0.7:
#         return JSONResponse(content={"status": "REJECTED", "reason": "NSFW content"})
#     return JSONResponse(content={"status": "OK"})
