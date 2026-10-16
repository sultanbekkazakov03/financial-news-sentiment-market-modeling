import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

print("Veriler yükleniyor ve birleştiriliyor...")

# 1. Dosyaları okuma
df_stock = pd.read_csv("apple_stock_prices.csv")
df_news = pd.read_csv("scored_news.csv")

# 2. Tarih sütununu baz alarak inner join ile birleştirme
merged_df = pd.merge(df_stock, df_news, on="Date", how="inner")

print(f"\nEşleşen toplam gün sayısı: {len(merged_df)}")
print("\n--- Eşleştirilmiş Veri Tablosu ---")
print(merged_df[['Date', 'Close', 'Daily_Return', 'Sentiment_Score', 'Sentiment_Label']])

# Birleştirilmiş temiz veriyi kaydetme
merged_df.to_csv("merged_market_sentiment.csv", index=False)

# 3. Regresyon Değişkenlerini Belirleme
# X = Bağımsız Değişken (Duygu Skoru), y = Bağımlı Değişken (Günlük Getiri)
X = merged_df[['Sentiment_Score']]
y = merged_df['Daily_Return']

# 4. Scikit-learn ile Regresyon Modeli
model_sk = LinearRegression()
model_sk.fit(X, y)
y_pred = model_sk.predict(X)

coef = model_sk.coef_[0]
intercept = model_sk.intercept_
r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)

print("\n================ REGRESYON SONUÇLARI (Scikit-Learn) ================")
print(f"Model Denklemi : Daily_Return = ({coef:.6f} * Sentiment_Score) + ({intercept:.6f})")
print(f"Katsayı (Beta) : {coef:.6f}")
print(f"R-Kare (R^2)   : {r2:.4f}")
print(f"Hata Kare (MSE): {mse:.6f}")
print("====================================================================")

# 5. Statsmodels ile Detaylı Akademik İstatistik Özeti (p-value, t-stat vb.)
X_stat = sm.add_constant(X)
model_sm = sm.OLS(y, X_stat).fit()

print("\n================ DETAYLI İSTATİSTİK RAPORU (OLS Summary) ================")
print(model_sm.summary())
print("=========================================================================\n")

# 6. Saçılım ve Regresyon Doğrusu Grafiğini Kaydetme
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Gerçekleşen Günler')
plt.plot(X, y_pred, color='red', linewidth=2, label='Regresyon Doğrusu')
plt.title('Haber Duygu Skoru vs. Günlük Hisse Getirisi (AAPL)')
plt.xlabel('FinBERT Duygu Skoru (Sentiment)')
plt.ylabel('Günlük Hisse Getirisi (Daily Return)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("regression_plot.png")
print("Regresyon grafiği 'regression_plot.png' adıyla kaydedildi.")