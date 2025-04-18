import os,vt
from dotenv import load_dotenv

load_dotenv()

VT_API_KEY = os.getenv("VT_API_KEY")


if VT_API_KEY is None:
    raise ValueError("VT_API_KEY is not set. Please check your .env file.")

