import os
from dotenv import load_dotenv
import requests

load_dotenv()

OLD_ID = os.getenv('OLD_BUDGET_ID')
NEW_ID = os.getenv('NEW_BUDGET_ID')
YNAB_API_KEY = os.getenv('YNAB_API_KEY')

YNAB_URL = 'https://api.ynab.com/v1'
RATE_LIMIT = 190

s = requests.Session()
s.headers.update({'Authorization': f'Bearer {YNAB_API_KEY}'})

old_budget = s.get(f'{YNAB_URL}/budgets/{OLD_ID}').json()['data']['budget']

total = 0

for month in old_budget['months']:
    for cat in month['categories']:
        if cat['budgeted']:
            total += 1

print(total)
