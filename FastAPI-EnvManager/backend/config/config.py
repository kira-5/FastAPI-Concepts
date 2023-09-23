import os
from dotenv import load_dotenv


def get_app_config():
    # Check if the APP_ENV=production command-line argument is provided
    if "APP_ENV" in os.environ:
        app_env = os.environ["APP_ENV"]
        print(f"app_env_command: {app_env}")
    else:
        # If not provided, check if it's defined in the .env file

        # Load environment variables from .env
        load_dotenv()
        app_env = os.environ.get("APP_ENV", "development")
        # app_env = os.getenv("APP_ENV", "development")
        print(f"app_env_env: {app_env}")

    if app_env == "production":
        from config.production import ProductionConfig

        return ProductionConfig
    else:
        from config.development import DevelopmentConfig

        return DevelopmentConfig
