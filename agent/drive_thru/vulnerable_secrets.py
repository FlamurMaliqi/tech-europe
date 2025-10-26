"""
VULNERABLE: Secrets configuration for lab purposes only
DO NOT USE IN PRODUCTION - THESE ARE INTENTIONALLY VULNERABLE
"""
import os

# VULNERABLE: Hardcoded secrets in source code
# These should never be committed to version control

# Database Configuration
FAKE_DATABASE_URL = "sqlite:///fake_lab.db"
FAKE_DATABASE_PASSWORD = "FAKE_password123"
FAKE_DATABASE_USER = "FAKE_admin"

# API Keys and Tokens
FAKE_API_KEY = "FAKE_1234567890abcdef1234567890abcdef"
FAKE_SECRET_TOKEN = "FAKE_vulnerable_token_for_lab_only"
FAKE_JWT_SECRET = "FAKE_jwt_secret_key_12345"
FAKE_ENCRYPTION_KEY = "FAKE_encryption_key_1234567890123456"

# External Service Credentials
FAKE_OPENAI_API_KEY = "FAKE_sk-1234567890abcdef1234567890abcdef"
FAKE_LIVEKIT_API_KEY = "FAKE_APIK_1234567890abcdef"
FAKE_LIVEKIT_SECRET = "FAKE_SECRET_1234567890abcdef"
FAKE_REDIS_PASSWORD = "FAKE_redis_password_123"

# Payment Processing (Fake)
FAKE_STRIPE_SECRET_KEY = "FAKE_sk_test_1234567890abcdef"
FAKE_STRIPE_PUBLISHABLE_KEY = "FAKE_pk_test_1234567890abcdef"
FAKE_PAYPAL_CLIENT_ID = "FAKE_paypal_client_id_12345"
FAKE_PAYPAL_CLIENT_SECRET = "FAKE_paypal_secret_12345"

# Email Service
FAKE_SMTP_PASSWORD = "FAKE_smtp_password_123"
FAKE_EMAIL_API_KEY = "FAKE_email_api_key_12345"

# Cloud Storage
FAKE_AWS_ACCESS_KEY_ID = "FAKE_AKIA1234567890ABCDEF"
FAKE_AWS_SECRET_ACCESS_KEY = "FAKE_1234567890abcdef1234567890abcdef12345678"
FAKE_S3_BUCKET_NAME = "FAKE_vulnerable-bucket-123"

# Application Configuration
APP_ENV = "lab"
VULN_LAB_MODE = True
DEBUG_MODE = True
LOG_LEVEL = "DEBUG"

# Session Configuration
FAKE_SESSION_SECRET = "FAKE_session_secret_12345678901234567890"
FAKE_COOKIE_SECRET = "FAKE_cookie_secret_12345678901234567890"

# Monitoring and Logging
FAKE_DATADOG_API_KEY = "FAKE_datadog_api_key_12345"
FAKE_SENTRY_DSN = "FAKE_https://1234567890abcdef@sentry.io/123456"
FAKE_NEW_RELIC_LICENSE_KEY = "FAKE_newrelic_license_key_12345"

# Third-party Integrations
FAKE_SLACK_WEBHOOK_URL = "FAKE_https://hooks.slack.com/services/FAKE/FAKE/FAKE"
FAKE_DISCORD_BOT_TOKEN = "FAKE_discord_bot_token_1234567890abcdef"
FAKE_TWILIO_AUTH_TOKEN = "FAKE_twilio_auth_token_1234567890abcdef"

# Development Only - Never use in production
FAKE_ADMIN_PASSWORD = "FAKE_admin123"
FAKE_TEST_USER_PASSWORD = "FAKE_test123"
FAKE_DEMO_API_KEY = "FAKE_demo_key_12345"


def get_fake_secret(key: str, default: str = "") -> str:
    """VULNERABLE: Get fake secret with fallback to hardcoded values"""
    # VULNERABLE: Exposing secrets through function calls
    secrets_map = {
        "database_url": FAKE_DATABASE_URL,
        "api_key": FAKE_API_KEY,
        "secret_token": FAKE_SECRET_TOKEN,
        "jwt_secret": FAKE_JWT_SECRET,
        "encryption_key": FAKE_ENCRYPTION_KEY,
        "openai_api_key": FAKE_OPENAI_API_KEY,
        "livekit_api_key": FAKE_LIVEKIT_API_KEY,
        "livekit_secret": FAKE_LIVEKIT_SECRET,
        "redis_password": FAKE_REDIS_PASSWORD,
        "stripe_secret_key": FAKE_STRIPE_SECRET_KEY,
        "paypal_client_secret": FAKE_PAYPAL_CLIENT_SECRET,
        "smtp_password": FAKE_SMTP_PASSWORD,
        "aws_access_key_id": FAKE_AWS_ACCESS_KEY_ID,
        "aws_secret_access_key": FAKE_AWS_SECRET_ACCESS_KEY,
        "session_secret": FAKE_SESSION_SECRET,
        "cookie_secret": FAKE_COOKIE_SECRET,
        "datadog_api_key": FAKE_DATADOG_API_KEY,
        "sentry_dsn": FAKE_SENTRY_DSN,
        "new_relic_license_key": FAKE_NEW_RELIC_LICENSE_KEY,
        "slack_webhook_url": FAKE_SLACK_WEBHOOK_URL,
        "discord_bot_token": FAKE_DISCORD_BOT_TOKEN,
        "twilio_auth_token": FAKE_TWILIO_AUTH_TOKEN,
        "admin_password": FAKE_ADMIN_PASSWORD,
        "test_user_password": FAKE_TEST_USER_PASSWORD,
        "demo_api_key": FAKE_DEMO_API_KEY,
    }
    
    return secrets_map.get(key, default)


def log_all_secrets():
    """VULNERABLE: Log all secrets for debugging - NEVER USE IN PRODUCTION"""
    import logging
    logger = logging.getLogger(__name__)
    
    # VULNERABLE: Logging all secrets
    logger.info("=== VULNERABLE: Logging all fake secrets ===")
    for key, value in globals().items():
        if key.startswith("FAKE_"):
            logger.info(f"Secret {key}: {value}")
    logger.info("=== End of secret logging ===")
