import re, os, time
import datetime

class Config:
    BOT_TOKEN = os.environ.get('7716433955:AAFyRm41MWU-K0MslxcRWvE5tOYFMCS3pO8')
    API_HASH = os.environ.get('25278a8394b5914ee1b8d6a6c79d572d')
    API_ID = int(os.environ.get(API_ID, '27692015'))
    OWNER_ID = int(os.environ.get('7092511418')) #Admin UserId
    DB_URI = os.environ.get('mongodb+srv://Premium:aloksingh@cluster0.4ykpo.mongodb.net/?retryWrites=true&w=majority') #May Be In Future.
    
