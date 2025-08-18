import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import json

# 1. Get Apple stock data
print("Fetching Apple stock data...")  # Debug print
apple = yf.Ticker("AAPL")

# 2. Get company info
print("\nFetching company information...")
apple_info = apple.info

print("\nConverting company info to DataFrame...")
apple_info = apple.info
apple_info_df = pd.DataFrame.from_dict(apple_info, orient="index" ,columns = ["value"])
# print("\nApple Company Info DataFrame:")


# 3. Print type and country info
print(f"\nType of apple_info: {type(apple_info)}")
print(f"Apple's country: {apple_info.get('country', 'Not available')}")

# # 4. Get historical price data
# print("\nFetching historical price data...")
# apple_share_price_data = apple.history(period="max")
# print("\nFirst 5 rows of historical data:")
# print(apple_share_price_data.head())

# # 5. Reset index for plotting
# apple_share_price_data.reset_index(inplace=True)

# # 6. Plot opening prices
# print("\nGenerating price plot...")
# plt.figure(figsize=(12, 6))
# apple_share_price_data.plot(x="Date", y="Open", title="Apple's Historical Opening Prices")
# plt.savefig('apple_prices.png')  # Save the plot
# print("Price plot saved to apple_prices.png")

# # 7. Get and plot dividends
# print("\nFetching dividend data...")
# dividends = apple.dividends
# print("\nDividend data:")
# print(dividends.tail())  # Show last 5 dividend payments
# plt.figure(figsize=(12, 6))
# dividends.plot(title="Apple's Dividend History")
# plt.savefig('apple_dividends.png')
# print("Dividend plot saved to apple_dividends.png")
# print("\nScript completed successfully!")