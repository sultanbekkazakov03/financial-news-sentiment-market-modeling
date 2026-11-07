import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

print("FinBERT modeli Hugging Face üzerinden yükleniyor (ilk seferde indirme yapacaktır)...")

# 1. FinBERT modelini ve tokenizer'ı yükleme
model_name = "ProsusAI/finbert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

# 2. Haber dosyasını okuma
news_df = pd.read_csv("financial_news.csv")
print(f"Toplam {len(news_df)} adet haber başlığı işleniyor...\n")

scores = []
labels = []

# 3. Her bir başlık için duygu analizi yapma
for headline in news_df['Headline']:
    inputs = tokenizer(headline, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    
    # FinBERT etiket sıralaması: [Pozitif, Negatif, Nötr]
    pos_prob = probs[0][0].item()
    neg_prob = probs[0][1].item()
    neutral_prob = probs[0][2].item()
    
    # Bileşik Duygu Skoru: Pozitif olasılığı - Negatif olasılığı (-1 ile +1 arası)
    compound_score = pos_prob - neg_prob
    
    # En yüksek olasılıklı sınıfı belirleme
    if compound_score > 0.15:
        pred_label = "Positive"
    elif compound_score < -0.15:
        pred_label = "Negative"
    else:
        pred_label = "Neutral"
        
    scores.append(round(compound_score, 4))
    labels.append(pred_label)

# 4. Sonuçları tabloya ekleme ve kaydetme
news_df['Sentiment_Score'] = scores
news_df['Sentiment_Label'] = labels

print("--- FinBERT Duygu Analizi Sonuçları ---")
print(news_df[['Date', 'Headline', 'Sentiment_Score', 'Sentiment_Label']])

output_filename = "scored_news.csv"
news_df.to_csv(output_filename, index=False)
print(f"\nBaşarılı! Puanlanan haberler '{output_filename}' dosyasına kaydedildi.")