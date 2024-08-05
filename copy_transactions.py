import os
from dotenv import load_dotenv
import requests

load_dotenv()
OLD_ID = os.getenv('OLD_BUDGET_ID')
NEW_ID = os.getenv('NEW_BUDGET_ID')

YNAB_URL = 'https://api.ynab.com/v1'

s = requests.Session()
s.headers.update({'Authorization': f'Bearer {input('All right bro we need an API key: ')}'})

new_budget = s.get(f'{YNAB_URL}/budgets/{NEW_ID}').json()['data']['budget']

new_cat_dict = {cat['name']: cat['id'] for cat in new_budget['categories'] if not cat['deleted']}
new_acc_dict = {acc['name']: acc['id'] for acc in new_budget['accounts']}

transactions_dict = {'transactions': []}

transactions = s.get(f'{YNAB_URL}/budgets/{OLD_ID}/transactions').json()['data']['transactions']
for t in transactions:
    starting_balance = t['payee_name'] == 'Starting Balance'
    transfer = 'Transfer' in t['payee_name']
    if not t['subtransactions']:
        transactions_dict['transactions'].append({
            'account_id': new_acc_dict[t['account_name']],
            'date': t['date'],
            'amount': t['amount'],
            'payee_name': t['payee_name'] if not starting_balance and not transfer else t['payee_name'].replace('a', '@', 1),
            'category_id': new_cat_dict[t['category_name']] if not transfer else new_cat_dict['Transfers'],
            'memo': t['memo'],
            'cleared': t['cleared'],
            'approved': t['approved'],
            'flag_color': t['flag_color']
        })
    for sub in t['subtransactions']:
        transfer = sub['payee_name'] and 'Transfer' in sub['payee_name']

        transactions_dict['transactions'].append({
            'account_id': new_acc_dict[t['account_name']],
            'date': t['date'],
            'amount': sub['amount'],
            'payee_name': sub['payee_name'] if not starting_balance and not transfer else sub['payee_name'].replace('a', '@', 1),
            'category_id': new_cat_dict[sub['category_name']],
            'memo': sub['memo'],
            'cleared': t['cleared'],
            'approved': t['approved'],
            'flag_color': t['flag_color']
        })

result = s.post(f'{YNAB_URL}/budgets/{NEW_ID}/transactions', json=transactions_dict)
if 'error' in result.json():
    print(result.json())
