from dotenv import load_dotenv
import os

# Загружаем переменные среды из папки secrets
load_dotenv("secrets/.env")

# Теперь вы можете безопасно использовать переменные среды
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")

print("DB User:", db_user)
print("DB Password:", db_pass)
