import streamlit as st
import pandas as pd
import datetime

# --- 1. ENTERPRISE SAYFA AYARLARI (Tam Ekran, Dar Marjin) ---
st.set_page_config(page_title="ArsaVev vHub Terminali", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

# Terminal & CRM Görünümü İçin Ultra-Kompakt CSS
st.markdown("""
    <style>
    .stApp {background-color: #f8fafc;}
    /* Gereksiz boşlukları yok et ki vHub sırasında ekrana sığsın */
    .block-container {padding-top: 1rem; padding-bottom: 1rem; max-width: 95%;}
    /* Tablo Tasarımı */
    [data-testid="stDataFrame"] {border: 1px solid #e2e8f0; border-radius: 4px;}
    /* Buton Tasarımı */
    .stButton>button {background-color: #0f172a; color: white; border-radius: 4px; font-weight: bold; height: 100%;}
    .stButton>button:hover {background-color: #d1121d; color: white; border-color: #d1121d;}
    /* Metin Alanı */
    .stTextArea textarea {background-color: #ffffff; border: 1px solid #cbd5e1; font-family: monospace; font-size: 13px;}
    </style>
""", unsafe_allow_html=True)

# --- 2. ÜST BİLGİ & CANLI SAAT ---
col_logo, col_title, col_time = st.columns([1, 6, 2])
with col_logo:
    st.image("https://arsavev.com/wp-content/uploads/2023/11/logo_arsavev.png", width=120)
with col_title:
    st.markdown("<h3 style='margin-bottom:0; color:#0f172a;'>vHub Canlı Satış & Veri Terminali</h3>", unsafe_allow_html=True)
    st.caption("Müşteri Görüşmesi Esnasında Anlık Veri Çekimi ve Teklif Otomasyonu")
with col_time:
    st.info(f"🟢 Sistem Aktif | {datetime.datetime.now().strftime('%d.%m.%Y - %H:%M')}")

st.markdown("---")

# --- 3. SİMÜLASYON VERİTABANI (Şirket CRM'i gibi çalışır) ---
# vHub'da müşteri bütçe verdiğinde saniyeler içinde buradan süzeceğiz.
veritabani = {
    "Proje Kodu": ["PRJ-AYV-01", "PRJ-DIK-04", "PRJ-SAP-02", "PRJ-EDR-09", "PRJ-CAN-03"],
    "Konsept": ["Tiny House Köyü", "Ekolojik Tarım", "Klasik İmarlı", "Ticari/Lojistik", "Ekolojik Tarım"],
    "Bölge": ["Çanakkale / Ayvacık", "İzmir / Dikili", "Sakarya / Sapanca", "Balıkesir / Edremit", "Çanakkale / Merkez"],
    "Min_Bütçe": [1500000, 1200000, 2500000, 4500000, 1800000],
    "Amortisman": ["4.2 Yıl", "5.1 Yıl", "3.8 Yıl", "6.2 Yıl", "4.5 Yıl"],
    "Kalan_Stok": [12, 5, 24, 2, 8]
}
df = pd.DataFrame(veritabani)

# --- 4. CANLI KONTROL PANELİ (Tek Satırda Hızlı Giriş) ---
st.markdown("#### 🔍 1. Müşteri Parametreleri (Anlık Filtreleme)")
c1, c2, c3, c4 = st.columns([2, 2, 2, 1])

with c1:
    musteri = st.text_input("Müşteri Adı", placeholder="Örn: Ahmet Bey", label_visibility="collapsed")
with c2:
    butce_girisi = st.number_input("Bütçe (TL)", min_value=500000, value=2000000, step=100000, label_visibility="collapsed")
with c3:
    secili_konsept = st.selectbox("İlgilenilen Konsept", ["Tümü", "Tiny House Köyü", "Ekolojik Tarım", "Klasik İmarlı", "Ticari/Lojistik"], label_visibility="collapsed")
with c4:
    sorgula = st.button("DATAYI ÇEK ⚡")

# --- 5. VERİ VE TEKLİF ÇIKTISI (vHub Sırasında Arka Planda Çalışacak Alan) ---
st.markdown("#### 📊 2. Eşleşen Portföy & Operasyonel Çıktı")

if sorgula:
    # Veriyi Filtrele
    if secili_konsept == "Tümü":
        filtrelenmis_df = df[df["Min_Bütçe"] <= butce_girisi].copy()
    else:
        filtrelenmis_df = df[(df["Min_Bütçe"] <= butce_girisi) & (df["Konsept"] == secili_konsept)].copy()
    
    # Bütçe formatını düzeltme (Görsellik için)
    filtrelenmis_df["Min_Bütçe"] = filtrelenmis_df["Min_Bütçe"].apply(lambda x: "{:,.0f} TL".format(x).replace(",", "."))
    
    col_data, col_teklif = st.columns([1.2, 1])
    
    with col_data:
        st.markdown("**Sistemdeki Uygun Projeler (CRM Eşleşmesi)**")
        if filtrelenmis_df.empty:
            st.warning("Bu bütçe ve kritere uygun aktif stok bulunamadı.")
        else:
            # Datacıların sevdiği temiz tablo görünümü
            st.dataframe(filtrelenmis_df, use_container_width=True, hide_index=True)
            
            # Seçilen en iyi projeyi belirle (Listeden ilkini alıyor simülasyon olarak)
            hedef_proje = filtrelenmis_df.iloc[0]["Bölge"]
            hedef_konsept = filtrelenmis_df.iloc[0]["Konsept"]
            hedef_stok = filtrelenmis_df.iloc[0]["Kalan_Stok"]
            
    with col_teklif:
        st.markdown("**Arka Plan Teklif Oluşturucu (Tek Tıkla Kopyala)**")
        if not filtrelenmis_df.empty:
            if musteri == "":
                musteri_hitap = "Değerli Müşterimiz"
            else:
                musteri_hitap = f"Sayın {musteri}"
                
            teklif_metni = f"""{musteri_hitap}, 

Az önce gerçekleştirdiğimiz vHub dijital sunumumuzda belirttiğiniz kriterler ve bütçeniz doğrultusunda, ArsaVev portföyündeki en uygun seçenek olarak "{hedef_proje}" lokasyonundaki "{hedef_konsept}" projemiz ön plana çıkmaktadır.

Sistemimizden çektiğim anlık veriye göre bu projede avantajlı fiyattan sunabileceğimiz yalnızca {hedef_stok} adet parsel stoğumuz kalmıştır. 

Görüşmemizde bahsettiğim detaylı yatırım raporunu ve tapu örneklerini incelemeniz adına tarafınıza iletiyorum. Karar sürecinizde her türlü sorunuz için bu numara üzerinden benimle iletişime geçebilirsiniz.

Saygılarımla,
Yaren Selin Arı
ArsaVev Dijital Uzman Yardımcısı
"""
            st.text_area("İletişim Metni (WhatsApp/Mail):", value=teklif_metni, height=220, label_visibility="collapsed")
            st.success("✅ Teklif metni ve veriler hazır. Kopyalayıp anında gönderebilirsiniz.")
else:
    st.info("👈 Müşteri görüşmesi sırasında bütçe bilgisini girip 'DATAYI ÇEK' butonuna basınız. İlgili projeler ve taslak teklif saniyeler içinde bu alanda belirecektir.")
