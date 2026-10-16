import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Sayfa yapılandırması
st.set_page_config(
    page_title="Finansal Haber Duygu & Piyasa Paneli",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Finansal Haber Metinleri ve Piyasa Eğilimi Modellemesi")
st.markdown("**Veri Madenciliği ve İş Zekası Dersi Karar Destek Paneli**")
st.markdown("---")

# Veri Kontrolü
data_file = "merged_market_sentiment.csv"

if not os.path.exists(data_file):
    st.error("Birleştirilmiş veri dosyası (merged_market_sentiment.csv) bulunamadı! Lütfen önce önceki adımları çalıştırın.")
    st.stop()

# Veriyi oku
df = pd.read_csv(data_file)

# Üst KPI / Özet Metrikleri
col1, col2, col3, col4 = st.columns(4)

son_fiyat = df['Close'].iloc[-1]
ortalama_duygu = df['Sentiment_Score'].mean()
pozitif_sayisi = (df['Sentiment_Label'] == 'Positive').sum()
negatif_sayisi = (df['Sentiment_Label'] == 'Negative').sum()

with col1:
    st.metric(label="Son Kapanış Fiyatı (AAPL)", value=f"${son_fiyat:.2f}")
with col2:
    st.metric(label="Ortalama Duygu Skoru", value=f"{ortalama_duygu:.3f}")
with col3:
    st.metric(label="Pozitif Haber Sayısı", value=f"{pozitif_sayisi} adet")
with col4:
    st.metric(label="Negatif Haber Sayısı", value=f"{negatif_sayisi} adet")

st.markdown("---")

# Grafikler Bölümü
tab1, tab2, tab3 = st.tabs(["📊 Zaman Serisi Karşılaştırması", "🎯 Regresyon İlişkisi", "📑 Ham Veri Tablosu"])

with tab1:
    st.subheader("Hisse Fiyat Hareketi ve Haber Duygu Skoru")
    
    # Çift eksenli veya alt alta iki interaktif grafik
    fig_price = px.line(df, x='Date', y='Close', title='AAPL Günlük Kapanış Fiyatı ($)', markers=True)
    fig_price.update_traces(line_color='#2980b9')
    st.plotly_chart(fig_price, use_container_width=True)

    # Duygu Skoru Bar Grafiği
    df['Color'] = df['Sentiment_Score'].apply(lambda x: '#2ecc71' if x > 0 else ('#e74c3c' if x < 0 else '#95a5a6'))
    fig_sentiment = go.Figure()
    fig_sentiment.add_trace(go.Bar(
        x=df['Date'],
        y=df['Sentiment_Score'],
        marker_color=df['Color'],
        name='Duygu Skoru'
    ))
    fig_sentiment.update_layout(
        title="FinBERT Günlük Haber Duygu Endeksi (-1.0 ile +1.0 arası)",
        xaxis_title="Tarih",
        yaxis_title="Duygu Skoru",
        template="plotly_white"
    )
    st.plotly_chart(fig_sentiment, use_container_width=True)

with tab2:
    st.subheader("İstatistiksel Modelleme ve Regresyon Saçılımı")
    st.write("Duygu skorlarının günlük getiri (Daily Return) üzerindeki etkisini gösteren saçılım grafiği:")
    
    if os.path.exists("regression_plot.png"):
        st.image("regression_plot.png", caption="Linear Regression (OLS) Analiz Grafiği")
    else:
        st.info("Regresyon grafiği bulunamadı.")

with tab3:
    st.subheader("LLM Tarafından Etiketlenen ve Eşleştirilen Veri Tablosu")
    st.dataframe(df[['Date', 'Headline', 'Sentiment_Score', 'Sentiment_Label', 'Close', 'Daily_Return']], use_container_width=True)