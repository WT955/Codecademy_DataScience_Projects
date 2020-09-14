import codecademylib
import pandas as pd

# 1
inventory = pd.read_csv('inventory.csv')

# 2 & 3
staten_island = inventory.head(10)

# 4
product_request = staten_island['product_description']

# 5
seed_request = inventory.loc[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]

# 6
inventory['in_stock'] = inventory.apply(lambda row: True if row['quantity'] > 0 else False, axis = 1)

# 7
total_value = lambda row: row.quantity * row.price
inventory['total_value'] = inventory.apply(total_value, axis = 1)

# 8
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

# 9
inventory['full_description'] = inventory.apply(combine_lambda, axis = 1)


print(inventory.head(10))