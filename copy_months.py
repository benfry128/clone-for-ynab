import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()
OLD_ID = os.getenv('OLD_BUDGET_ID')
NEW_ID = os.getenv('NEW_BUDGET_ID')
YNAB_API_KEY = os.getenv('YNAB_API_KEY')

YNAB_URL = 'https://api.ynab.com/v1'

s = requests.Session()
s.headers.update({'Authorization': f'Bearer {YNAB_API_KEY}'})

old_budget = s.get(f'{YNAB_URL}/budgets/{OLD_ID}').json()['data']['budget']
new_budget = s.get(f'{YNAB_URL}/budgets/{NEW_ID}').json()['data']['budget']

new_cat_dict = {cat['name']: cat['id'] for cat in new_budget['categories'] if not cat['deleted']}

months = old_budget['months']
months.reverse()
pprint(months[0])
input("HI")

for month in months:
    m = month['month']
    for cat in month['categories']:
        if cat['budgeted']:
            cat_dict = {
                'category': {
                    'budgeted': cat['budgeted']
                }
            }
            result = s.patch(f'{YNAB_URL}/budgets/{NEW_ID}/months/{m}/categories/{new_cat_dict[cat['name']]}', json=cat_dict)
            print(result.json())
