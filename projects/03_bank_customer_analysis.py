# Filters and analyzes customer financial data to identify high-net-worth clients and calculate combined net worth metrics.

import pandas as pd

customer_df = pd.DataFrame({
    'customer_id': [111, 222, 333, 444],
    'customer_name': ['Chanel', 'Steve', 'Mitch', 'Ryan'],
    'net_worth': [3500, 29000, 10000, 2000],
    'years_with_bank': [3, 4, 9, 5]
})

high_net_worth_customers = (
    customer_df[
        customer_df['net_worth'] >= 5000
    ]
)

total_high_net_worth = (
    high_net_worth_customers['net_worth']
    .sum()
)

print(total_high_net_worth)
