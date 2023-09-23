from fastapi import FastAPI
from config.config import get_app_config

app = FastAPI()
config = get_app_config()


@app.get("/")
def read_root():
    print(config)
    return {"message": f"App Environment: {config.app_env}"}


if __name__ == "__main__":
    import uvicorn

    # Determine whether to enable auto-reloading based on the configuration
    should_reload = config.app_env == "development"

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=should_reload,
    )
