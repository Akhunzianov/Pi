import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
import logging
from telegram.ext import Updater


load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

ip = os.getenv('ip')
PGUSER = os.getenv('PGUSER')
PGPASSWORD = os.getenv('PGPASSWORD')
DATABASE = os.getenv('DATABASE')

POSTGRES_URI = F'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()