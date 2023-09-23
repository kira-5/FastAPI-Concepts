# Development-specific settings
class DevelopmentConfig:
    app_env = "development"
    DEBUG = True
    DATABASE_URL = "sqlite:///dev.db"
    LOG_LEVEL = "DEBUG"

    # CORS (Cross-Origin Resource Sharing) settings for development
    ALLOWED_HOSTS = ["*"]  # Allow all hosts during development for convenience
