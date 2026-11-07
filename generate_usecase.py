import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Şema alanı oluşturma
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

# Sistem Sınırı Kutusu (System Boundary)
rect = patches.FancyBboxPatch((2.2, 0.5), 5.6, 6.0, boxstyle="round,pad=0.2", 
                             edgecolor="#2c3e50", facecolor="#f8f9fa", linewidth=2)
ax.add_patch(rect)
ax.text(5.0, 6.2, "Finansal Analiz ve Modelleme Sistemi", ha='center', va='center', 
        fontsize=12, fontweight='bold', color="#2c3e50")

# Sol Aktör: Kullanıcı / Yatırımcı
ax.plot(0.8, 4.0, marker='o', markersize=18, color='#2980b9')  # Baş
ax.plot([0.8, 0.8], [3.3, 3.8], color='#2980b9', lw=3)        # Gövde
ax.plot([0.3, 1.3], [3.6, 3.6], color='#2980b9', lw=2.5)      # Kollar
ax.plot([0.8, 0.4], [3.3, 2.6], color='#2980b9', lw=2.5)      # Sol bacak
ax.plot([0.8, 1.2], [3.3, 2.6], color='#2980b9', lw=2.5)      # Sağ bacak
ax.text(0.8, 2.2, "Yatırımcı / Kullanıcı\n(Aktör)", ha='center', va='top', 
        fontsize=10, fontweight='bold', color="#2c3e50")

# Sağ Aktör: Dış Sistemler (API & Modeller)
ax.plot(9.2, 4.0, marker='o', markersize=18, color='#27ae60')  # Baş
ax.plot([9.2, 9.2], [3.3, 3.8], color='#27ae60', lw=3)        # Gövde
ax.plot([8.7, 9.7], [3.6, 3.6], color='#27ae60', lw=2.5)      # Kollar
ax.plot([9.2, 8.8], [3.3, 2.6], color='#27ae60', lw=2.5)      # Sol bacak
ax.plot([9.2, 9.6], [3.3, 2.6], color='#27ae60', lw=2.5)      # Sağ bacak
ax.text(9.2, 2.2, "Yahoo Finance &\nFinBERT (Sistem)", ha='center', va='top', 
        fontsize=10, fontweight='bold', color="#2c3e50")

# Use Case Elipsleri
cases = [
    (5.0, 5.2, "UC-01: Hisse Senedi ve Tarih Seçimi"),
    (5.0, 4.0, "UC-02: Haber Başlıklarını LLM ile Skorlama"),
    (5.0, 2.8, "UC-03: OLS Regresyon Analizi Çalıştırma"),
    (5.0, 1.5, "UC-04: Streamlit Karar Destek Panosunu İnceleme")
]

for x, y, text in cases:
    ellipse = patches.Ellipse((x, y), 4.8, 0.85, edgecolor='#34495e', facecolor='#ffffff', linewidth=1.5)
    ax.add_patch(ellipse)
    ax.text(x, y, text, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#2c3e50')

# İlişki Çizgileri
# Kullanıcı bağlantıları
ax.annotate("", xy=(2.6, 5.2), xytext=(1.3, 3.6), arrowprops=dict(arrowstyle="-", color="#7f8c8d", lw=1.5))
ax.annotate("", xy=(2.6, 1.5), xytext=(1.3, 3.6), arrowprops=dict(arrowstyle="-", color="#7f8c8d", lw=1.5))

# Dış Sistem bağlantıları
ax.annotate("", xy=(7.4, 4.0), xytext=(8.7, 3.6), arrowprops=dict(arrowstyle="-", color="#7f8c8d", lw=1.5))
ax.annotate("", xy=(7.4, 2.8), xytext=(8.7, 3.6), arrowprops=dict(arrowstyle="-", color="#7f8c8d", lw=1.5))

# Elipsler arası <<include>> ilişkisi
ax.annotate("<<include>>", xy=(5.0, 4.45), xytext=(5.0, 4.8),
            arrowprops=dict(arrowstyle="->", linestyle="dashed", color="#e74c3c", lw=1.2),
            ha='center', va='center', fontsize=8, color="#e74c3c")
ax.annotate("<<include>>", xy=(5.0, 3.25), xytext=(5.0, 3.55),
            arrowprops=dict(arrowstyle="->", linestyle="dashed", color="#e74c3c", lw=1.2),
            ha='center', va='center', fontsize=8, color="#e74c3c")

plt.tight_layout()
plt.savefig("use_case_diagram.png", bbox_inches='tight')
print("Başarılı! 'use_case_diagram.png' dosyası oluşturuldu.")