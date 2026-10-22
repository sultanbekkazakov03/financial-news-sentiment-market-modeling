# Finansal Haber Metinleri ve Piyasa Eğilimi Modellemesi

Bu proje, **Veri Madenciliği ve İş Zekası** dersi kapsamında geliştirilen bir karar destek ve piyasa eğilimi analiz sistemidir.

## Projenin Amacı
Güncel finansal haberlerin ve borsa bültenlerinin şirket hisse fiyat hareketleri üzerindeki etkisini Büyük Dil Modelleri (FinBERT / LLM) ve istatistiksel ekonometri modelleri (Çoklu Regresyon) ile modellemek ve yatırımcılara interaktif bir risk panosu sunmaktır.

## 👥 Ekip ve Görev Dağılımı

Vize proje gereksinimleri ve teknik modüller doğrultusunda ekip üyelerinin çalışma alanları aşağıdadır:

| No | Öğrenci Adı Soyadı | Öğrenci No | Akademik Rapor Sorumluluğu | Teknik Modül / Kod Sorumluluğu |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Gizem Doğan** | 95240148 | **Analiz Raporu:** Sektörel motivasyon, problem tanımı ve uçtan uca çözüm yaklaşımı | Veri akış analizi ve model çıktı raporlama süreçleri |
| 2 | **Zamıra Babahanova** | 95230102 | **Müşteri & Genel Gereksinim Raporu:** Paydaş beklentileri, fonksiyonel (FR) ve genel (NFR) gereksinimler | Yahoo Finance piyasa veri hattı entegrasyonu (`01_market_data.py`) |
| 3 | **Zeynep Karakaya** | 95230042 | **Use Case Diyagramları:** Sistem aktörleri, kullanım senaryoları ve süreç akış şeması | FinBERT LLM haber duygu analizi hattı (`02_sentiment_analysis.py`) |
| 4 | **Begench Rejepov** | 95230197 | **Kabul Kriterleri & Test Caseleri:** Metrik kabul sınırları (AC-01..04) ve test senaryoları (TC-01..25) | Ekonometrik regresyon modeli ve istatistiksel analiz (`03_regression_model.py`) |
| 5 | **Sultanbek Kazakov** | 95230117 | **İş Zekası & Dokümantasyon Mimarisi:** Karar destek panosu tasarımı ve vize dokümantasyon entegrasyonu | Streamlit web karar destek paneli ve Plotly görselleştirmeleri (`app.py`) |

## Kullanılan Teknolojiler
* **Programlama Dili:** Python 3.10+
* **Veri Analitiği & Modelleme:** Pandas, NumPy, Scikit-learn, Statsmodels
* **Doğal Dil İşleme (NLP / LLM):** Hugging Face Transformers (FinBERT), LLM API
* **Görselleştirme / Dashboard:** Matplotlib, Seaborn, Streamlit

## Dokümantasyon

Vize teslimi kapsamında hazırlanan Analiz Raporu, Müşteri/Sistem Gereksinimleri, Use Case Senaryoları, Kabul Kriterleri ve Test Senaryolarının tamamını içeren kapsamlı proje raporuna [`docsvize_dokumantasyonu.md`](docsvize_dokumantasyonu.md) dosyası üzerinden ulaşabilirsiniz.
