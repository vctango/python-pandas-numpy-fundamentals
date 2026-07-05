# Combines customer records and salary information using DataFrame concatenation and merging techniques.

import pandas as pd

existing_clients_df = pd.DataFrame(...)
new_clients_df = pd.DataFrame(...)
salary_data_df = pd.DataFrame(...)

all_clients_df = pd.concat([
    existing_clients_df,
    new_clients_df
])

client_master_df = pd.merge(
    all_clients_df,
    salary_data_df,
    on='Bank Client ID'
)

new_customer_df = pd.DataFrame(...)

updated_client_master_df = pd.concat(
    [client_master_df, new_customer_df],
    ignore_index=True
)
