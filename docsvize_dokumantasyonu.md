YÖNETİM BİLİŞİM SİSTEMLERİ BÖLÜMÜ 
Veri Madenciliği Ve İş Zekası Dersi 
Finansal Haber Metinleri ve Piyasa Eğilimi Modellemesi 
• Zamıra Babahanova - 95230102 
• Zeynep Karakaya - 95230042 
• Begench Rejepov - 95230197 
• Sultanbek Kazakov - 95230117 
• Gizem Doğan - 95240148 
GitHub Repo Bağlantısı 
https://github.com/sultanbekkazakov03/financial-news
sentiment-market-modeling  
1 
VİZE PROJE RAPORU 
1. Analiz Raporu 
1.1. Problem Tanımı ve Giriş 
Modern finansal piyasalarda hisse senedi fiyat hareketleri yalnızca 
geçmiş bilanço verileri ve teknik göstergelerle açıklanamaz. Anlık 
haber akışları, piyasa bültenleri, analist yorumları ve makroekonomik 
duyurular yatırımcı kararlarını doğrudan etkileyerek piyasada volatilite 
yaratır. 
Buna karşın, her gün yüzlerce küresel haber metni yayınlanmakta olup 
bireysel veya kurumsal yatırımcıların bu yoğun bilgi akışını manuel 
olarak takip etmesi, metinlerdeki piyasa eğilimini anlık puanlaması ve 
fiyat hareketleriyle korelasyonunu kurması imkansız hale gelmiştir. 
1.2. Çözüm Yaklaşımı 
Bu projede, metin madenciliği (Text Mining) ve ekonometrik zaman 
serisi analizini birleştiren bir karar destek sistemi geliştirilmiştir: 
1. Piyasa Verisi Toplama: Finans piyasası verileri (günlük kapanış 
fiyatları ve getiri oranları) Yahoo Finance API altyapısı üzerinden 
çekilir. 
2. LLM ile Duygu Analizi (FinBERT): Finans terminolojisi üzerine 
özelleştirilmiş Doğal Dil İşleme modeli (FinBERT) kullanılarak 
haber başlıkları okunur; pozitif, negatif ve nötr olasılıkları 
hesaplanarak her güne ait bileşik bir duygu skoru (Sentiment 
Index) elde edilir. 
3. Ekonometrik Regresyon Modellemesi: Haber duygu skorları ile 
hisse senedi günlük getiri oranları tarih bazında birleştirilir. En 
Küçük Kareler Yöntemi (OLS - Linear Regression) ile duygu 
skorunun fiyat üzerindeki etkisi (𝐵𝑒𝑡𝑎, 𝑅2, p-değeri) istatistiksel 
olarak ölçülür. 
4. İş Zekası Paneli (Streamlit): Sonuçlar, yatırımcıların zaman serisi 
ve dağılım grafiklerini anlık inceleyebileceği interaktif bir web 
panosu üzerinden sunulur. 
2 
2. Müşteri (Paydaş) Gereksinimleri 
• Hedef Kitle: Bireysel borsa yatırımcıları, portföy yöneticileri ve 
risk analistleri. 
• Paydaş Beklentileri: 
o Karmaşık finansal haberlerin otomatik analiz edilerek 
sayısal bir güven/duygu endeksine dönüştürülmesi. 
o İlgili günlerdeki haber yoğunluğu ve yönü (pozitif/negatif) 
ile hisse getirisinin yan yana görselleştirilmesi. 
o Modelin güvenilirlik ve hata metriklerinin (MSE, 𝑅2) şeffaf 
bir şekilde sunulması. 
3. Sistem Gereksinimleri 
3.1. Fonksiyonel Gereksinimler (Functional Requirements) 
• FR-01 (Veri İndirme): Sistem, hedeflenen hisse senedi için (örn. 
Apple - AAPL) belirlenen tarih aralığında geçmiş fiyat verilerini 
ve 
günlük yüzde değişimini (Daily_Return) otomatik 
hesaplamalıdır. 
• FR-02 (Metin Ön İşleme & Duygu Skorlaması): Finansal haber 
başlıkları tokenize edilerek FinBERT modeline aktarılmalı ve -1.0 
ile +1.0 arasında standart bir sayısal duygu skoru üretilmelidir. 
• FR-03 (Tarihsel Eşleştirme): Hisse işlem günleri ile haber tarihleri 
birleştirilerek eksik ve geçersiz veri içeren kayıtlar elenmelidir. 
• FR-04 (İstatistiksel Analiz): Scikit-learn ve Statsmodels 
kütüphaneleri kullanılarak katsayı, standart hata, t-istatistiği ve 𝑅2 
hesaplanmalıdır. 
• FR-05 (Karar Destek Gösterge Paneli): Streamlit üzerinde 
grafikler, KPI kutuları ve veri filtreleme tabloları dinamik olarak 
çalıştırılmalıdır. 
3 
3.2. Fonksiyonel Olmayan Gereksinimler (Non-Functional 
Requirements) 
• NFR-01 (Modüler Mimari): Veri çekme, duygu analizi, regresyon 
ve web arayüzü birbirinden bağımsız çalıştırılabilir modüller 
halinde yapılandırılmalıdır. 
• NFR-02 (Doğruluk ve Tutarlılık): Alan odaklı finansal terimleri 
(bullish, bearish, downgrade vb.) doğru anlamlandırabilen 
önceden eğitilmiş modeller tercih edilmelidir. 
• NFR-03 (Performans): Web paneli hafif ve hızlı yüklenmeli; veri 
güncellemelerini anlık yansıtabilmelidir. 
4. Use Case Senaryoları ve Akış Şeması 
4.1. Use Case Listesi 
• UC-01 (Piyasa Verisi İnceleme): Kullanıcı belirli bir hisse ve 
zaman aralığı için fiyat trendini görüntüler. 
• UC-02 (Haber Duygu Analizi): Sistem finansal haber akışını 
LLM üzerinden tarayarak günlük duyarlılık endeksini çıkarır. 
• UC-03 (Regresyon Modeli Çalıştırma): Model, duygu skorları ile 
hisse getirisi arasındaki ilişkiyi ekonometrik olarak modeller. 
• UC-04 (İş Zekası Paneli Kullanımı): Kullanıcı interaktif arayüz 
üzerinden KPI metriklerini, saçılım grafiğini ve ham veri 
tablosunu inceler. 
4 
4.2. Use Case Akış Şeması 
5. Kabul Kriterleri (Acceptance Criteria) 
• AC-01: Piyasa verisi ve haber tablosu tarih (Date) anahtarı 
üzerinden eksiksiz eşleştirilmelidir. 
• AC-02: LLM duygu analiz skoru her haber başlığı için [-1.0000, 
+1.0000] aralığında sürekli bir değişken olmalıdır. 
• AC-03: Regresyon modelinde katsayı (𝐵𝑒𝑡𝑎), 𝑅2 ve Hata Kareler 
Ortalaması (MSE) değerleri üretilmeli ve doğrulanmalıdır. 
• AC-04: Streamlit web arayüzü yerel sunucuda hatasız ayağa 
kalkmalı, KPI metriklerini ve Plotly interaktif grafiklerini 
eksiksiz render etmelidir. 
5 
6 
 
6. Test Senaryoları ve Sonuçları 
Test 
ID 
Test 
Senaryosu Test Adımları Beklenen Çıktı Gerçekleşen 
Durum 
TC
01 
Yahoo Finance 
Veri Çekme 
01_market_data.py 
çalıştırılır 
Fiyat ve Daily_Return 
sütunları içeren CSV 
oluşur 
Başarılı 
(Geçti) 
TC
02 
FinBERT 
LLM 
Puanlama 
02_sentiment_analysis.py 
çalıştırılır 
Başlıklar duygu 
skoru ve etiketleri 
alır (scored_news.csv) 
Başarılı 
(Geçti) 
TC
03 
Regresyon 
Modellemesi 
03_regression_model.py 
çalıştırılır 
OLS özet tablosu ve 
regression_plot.png 
üretilir 
Başarılı 
(Geçti) 
TC
04 
Web 
Dashboard 
Çalıştırma 
streamlit run app.py 
çalıştırılır 
Web tarayıcısında 
KPI ve grafik panosu 
açılır 
Başarılı 
(Geçti) 
 
