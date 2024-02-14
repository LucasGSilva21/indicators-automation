import os
import pandas as pd

dir = os.path.dirname(os.path.abspath(__file__))
emails_path = os.path.join(dir, 'data', 'emails.xlsx')
stores_path = os.path.join(dir, 'data', 'lojas.csv')
sales_path = os.path.join(dir, 'data', 'vendas.xlsx')

emails = pd.read_excel(emails_path)
stores = pd.read_csv(stores_path, sep=';', encoding='latin1')
sales = pd.read_excel(sales_path)

sales = sales.merge(stores, on='ID Loja')
sales_by_store = {}
for store in stores['Loja']:
  sales_by_store[store] = sales.loc[sales['Loja'] == store,:]

date_to_analyze = sales['Data'].max()

backup_path = os.path.join(dir, 'backup')
backup_store_folders = [folder_name for folder_name in os.listdir(backup_path)]

print(backup_store_folders)
