# Analyzes a stock portfolio by calculating position values and total portfolio worth using Pandas DataFrames and mathematical operations.

import pandas as pd

portfolio_df = pd.DataFrame({
    'ticker': ['AAPL', 'MSFT', 'NVDA'],
    'shares_owned': [50, 25, 10],
    'share_price': [210.50, 485.75, 160.20]
})

portfolio_df['position_value'] = (
    portfolio_df['shares_owned']
    * portfolio_df['share_price']
)

total_portfolio_value = (
    portfolio_df['position_value'].sum()
)

print(portfolio_df)
print(f"Total Portfolio Value: ${total_portfolio_value:,.2f}")
