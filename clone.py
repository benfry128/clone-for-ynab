import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()
YNAB_API_KEY = os.getenv('YNAB_API_KEY')

r = requests.get('https://api.ynab.com/v1/budgets', headers={'Authorization': f'Bearer {YNAB_API_KEY}'})
pprint(r.json())