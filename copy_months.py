import os
from dotenv import load_dotenv
import requests

load_dotenv()
OLD_ID = os.getenv('OLD_BUDGET_ID')
NEW_ID = os.getenv('NEW_BUDGET_ID')

# change these to the first year and month you want to copy from
# if your network gets throttled for sending too many requests, wait a while, replace these with the last month that was updated, and keep moving
FIRST_YEAR = 2020
FIRST_MONTH = 1

YNAB_URL = 'https://api.ynab.com/v1'

s = requests.Session()
s.headers.update({'Authorization': f'Bearer {input('All right bro we need a new API key: ')}'})

old_budget = s.get(f'{YNAB_URL}/budgets/{OLD_ID}').json()['data']['budget']
new_budget = s.get(f'{YNAB_URL}/budgets/{NEW_ID}').json()['data']['budget']

new_cat_dict = {cat['name']: cat['id'] for cat in new_budget['categories'] if not cat['deleted']}

months = old_budget['months']
months.reverse()

total = 0

for month in months:
    m = month['month']
    if int(m[0:4]) >= FIRST_YEAR and int(m[5:7]) >= FIRST_MONTH:
        for cat in month['categories']:
            if cat['budgeted']:
                cat_dict = {
                    'category': {
                        'budgeted': cat['budgeted']
                    }
                }
                result = s.patch(f'{YNAB_URL}/budgets/{NEW_ID}/months/{m}/categories/{new_cat_dict[cat['name']]}', json=cat_dict)
                if 'error' in result.json():
                    print(result.json())
                else:
                    print(f'Copied category {cat['name']} from month {m}.')
                total += 1
                if total > 190:
                    s.headers.update({'Authorization': f'Bearer {input('All right bro we need a new API key: ')}'})
                    total = 0
