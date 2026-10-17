import os

DATABASE_URL = os.environ.get("DATABASE_URL", "")
RABBITMQ_URL = os.environ.get("RABBITMQ_URL", "")
REDIS_URL = os.environ.get("REDIS_URL", "")
CORE_URL = os.environ.get("CORE_URL", "http://core:8000")
DISPATCH_URL = os.environ.get("DISPATCH_URL", "http://dispatch:8000")
TRACKING_URL = os.environ.get("TRACKING_URL", "http://tracking:8000")
