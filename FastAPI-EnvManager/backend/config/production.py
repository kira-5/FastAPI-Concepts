# Production-specific settings
class ProductionConfig:
    app_env = "production"
    DEBUG = False
    DATABASE_URL = "postgresql://user:password@localhost/dbname"
    LOG_LEVEL = "INFO"

    # Specify the allowed production host(s)
    ALLOWED_HOSTS = ["your-production-domain.com"]
