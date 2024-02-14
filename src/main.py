import os
import pandas as pd

dir = os.path.dirname(os.path.abspath(__file__))
emailsPath = os.path.join(dir, 'data', 'emails.xlsx')
storesPath = os.path.join(dir, 'data', 'lojas.csv')
salesPath = os.path.join(dir, 'data', 'vendas.xlsx')

emails = pd.read_excel(emailsPath)
stores = pd.read_csv(storesPath, sep=';', encoding='latin1')
sales = pd.read_excel(salesPath)

print(emails)
print(stores)
print(sales)
