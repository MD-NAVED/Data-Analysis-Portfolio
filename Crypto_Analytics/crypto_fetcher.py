import pandas as pd
import urllib.request
import json

print("Connecting to Live Finance API (Binance) for Bitcoin (BTC) Data...")

url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=30"

try:
    # Using built-in urllib to avoid installing 'requests'
    req = urllib.request.urlopen(url)
    data = json.loads(req.read().decode('utf-8'))
    
    # Binance returns a list of lists, we assign column names
    df = pd.DataFrame(data, columns=['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'CloseTime', 'QAV', 'NumTrades', 'TBBAV', 'TBQAV', 'Ignore'])
    
    # Keep only the important pricing details
    df = df[['Timestamp', 'Open', 'High', 'Low', 'Close']]
    
    # Convert string numbers to floats
    cols = ['Open', 'High', 'Low', 'Close']
    df[cols] = df[cols].apply(pd.to_numeric)
    
    # Convert the unix timestamp to Date format
    df['Date'] = pd.to_datetime(df['Timestamp'], unit='ms')
    
    # Rearrange and drop the old Timestamp
    df = df[['Date', 'Open', 'High', 'Low', 'Close']]
    
    # Save to a fresh CSV file
    df.to_csv('live_bitcoin_data.csv', index=False)
    
    print("SUCCESS: 'live_bitcoin_data.csv' is ready!")
    print(df.head())
except Exception as e:
    print(f"API Connection Failed: {e}")
