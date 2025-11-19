import os
from dotenv import load_dotenv

# این خط فایل .env را می‌خواند
load_dotenv()

class Settings:
    def __init__(self) -> None:
        # مقدار DATABASE_URL را از فایل .env می‌گیرد
        self.database_url: str | None = os.getenv("DATABASE_URL")

# یک شیء سراسری برای استفاده در بقیه‌ی پروژه
settings = Settings()
