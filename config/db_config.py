from dotenv import load_dotenv
import os


load_dotenv(dotenv_path='C:\\MAIN\\it\\projects\\py\\InforceTestTask\\.env')

DB_PARAMS = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}

print(DB_PARAMS)

