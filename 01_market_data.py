import yfinance as yf
import pandas as pd

# Analiz edilecek hisse ve tarih aralığı
ticker = "AAPL"
start_date = "2025-01-01"
end_date = "2026-10-16"

print(f"[{ticker}] hisse verileri indiriliyor...")

# Veriyi indir
df_stock = yf.download(ticker, start=start_date, end=end_date)

# Sütun yapısını düzeltme
if isinstance(df_stock.columns, pd.MultiIndex):
    df_stock.columns = df_stock.columns.get_level_values(0)

# Sadece Kapanış (Close) fiyatını alma ve günlük yüzde getiriyi hesaplama
df_stock = df_stock[['Close']].copy()
df_stock['Daily_Return'] = df_stock['Close'].pct_change()

# Tarih indeksini sütuna çevirip formatlama
df_stock.reset_index(inplace=True)
df_stock.dropna(inplace=True)
df_stock['Date'] = pd.to_datetime(df_stock['Date']).dt.strftime('%Y-%m-%d')

print("\n--- İlk 5 Günlük Hisse Verisi ---")
print(df_stock.head())

# CSV olarak kaydetme
output_file = "apple_stock_prices.csv"
df_stock.to_csv(output_file, index=False)
print(f"\nBaşarılı! Veriler '{output_file}' dosyasına kaydedildi.")