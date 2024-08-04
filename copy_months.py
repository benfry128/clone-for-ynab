import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()
YNAB_API_KEY = os.getenv('YNAB_API_KEY2')
YNAB_URL = 'https://api.ynab.com/v1'
s = requests.Session()
s.headers.update({'Authorization': f'Bearer {YNAB_API_KEY}'})

old_id = '277f14e0-7fa0-4761-b14c-fbaa345e4175'
new_id = '8d414a6a-5201-469b-b5a8-a4e42afefe5e'

old_budget = s.get(f'{YNAB_URL}/budgets/{old_id}').json()['data']['budget']
new_budget = s.get(f'{YNAB_URL}/budgets/{new_id}').json()['data']['budget']

new_cat_dict = {cat['name']: cat['id'] for cat in new_budget['categories'] if not cat['deleted']}

months = old_budget['months']
months.reverse()
pprint(months[0])  # 18313a53-6626-41db-9439-95bbbaef140a
input("HI")

for month in months:
    m = month['month']
    if '2024' in m and int(m[5:7]) > :
        for cat in month['categories']:
            if cat['budgeted']:
                cat_dict = {
                    'category': {
                        'budgeted': cat['budgeted']
                    }
                }
                result = s.patch(f'{YNAB_URL}/budgets/{new_id}/months/{m}/categories/{new_cat_dict[cat['name']]}', json=cat_dict)
                print(result.json())
