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

backup_path = os.path.join(dir, 'backup')
backup_store_folders = [folder_name for folder_name in os.listdir(backup_path)]

date_to_analyze = sales['Data'].max()

for store_name in sales_by_store:
  if store_name not in backup_store_folders:
    os.mkdir(os.path.join(backup_path, store_name))

  file_name = '{}_{}.xlsx'.format(date_to_analyze.date(), store_name)
  file_path = os.path.join(backup_path, store_name, file_name)
  sales_by_store[store_name].to_excel(file_path)