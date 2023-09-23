import os


def get_app_config():
    app_env = os.environ.get("APP_ENV", "development")
    print(f"app_env_config:{app_env}")
    # app_env = os.getenv("APP_ENV", "development")

    if app_env == "production":
        from config.production import ProductionConfig

        return ProductionConfig
    else:
        from config.development import DevelopmentConfig

        return DevelopmentConfig
