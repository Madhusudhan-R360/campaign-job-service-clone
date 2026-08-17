from fastapi import FastAPI


app = FastAPI(
    title="Campaign Job Service Clone"
)


@app.get("/health")
async def health():

    return {
        "success": True
    }