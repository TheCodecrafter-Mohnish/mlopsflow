import os
from dotenv import load_dotenv

load_dotenv()

PYTHON_KEY= os.getenv('PYTHON_KEY')
print(PYTHON_KEY)