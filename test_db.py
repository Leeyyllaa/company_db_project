from app.db.session import engine

try:
    with engine.connect() as connection:
        print("🔗 اتصال به دیتابیس برقرار شد!")
except Exception as e:
    print("❌ خطا در اتصال به دیتابیس:")
    print(e)
