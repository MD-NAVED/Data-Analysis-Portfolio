import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Crypto_Analytics/live_bitcoin_data.csv')
df['Moving_Average_5'] = df['Close'].rolling(window=5).mean()



# import matplotlib.pyplot as plt

# # Graph ka size thoda bada karte hain (10 width, 5 height)
# plt.figure(figsize=(10, 5))

# # Pehli line: Asli Price (Red color, thodi halki yani alpha=0.5)
# plt.plot(df['Date'], df['Close'], label='Original Bitcoin Price', color='red', alpha=0.5)

# # Dusri Line: Aapka banaya hua Moving Average (Blue color, thodi moti)
# plt.plot(df['Date'], df['Moving_Average_5'], label='5-Day Moving Average', color='blue', linewidth=2)

# plt.title('Bitcoin Price Trend (Real-time Binance Data)')
# plt.legend()       # Label box dikhane ke liye

# # X-axis par Date theek se fit ho uske liye:
# plt.gcf().autofmt_xdate() 

# plt.show()         # Graph ko screen par pop-up karein

plt.figure(figsize=(10,5))
plt.plot(df['Date'],df['Close'],label='Original Bitcoin Price',color='red',alpha=0.5)
plt.plot(df['Date'],df['Moving_Average_5'],label='5-Day Moving Average',color='blue',linewidth=2)
plt.title('Bitcoin Price Trend (Real-time Binance Data)')
plt.legend()
plt.gcf().autofmt_xdate()
plt.savefig('Crypto_Analytics/btc_trend_chart.png', dpi=300, bbox_inches='tight')
plt.show()
