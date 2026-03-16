import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px

# --- SAYFA AYARLARI VE CSS ---
st.set_page_config(page_title="ArsaVev Kurumsal Zeka", page_icon="🏢", layout="wide")

# ArsaVev kırmızı tonlarını arayüze yediren özel tasarım (CSS)
st.markdown("""
    <style>
    .stButton>button {background-color: #d1121d; color: white; border-radius: 8px;}
    .stButton>button:hover {background-color: #a00d15; border-color: #a00d15;}
    .stTabs [data-baseweb="tab-list"] {gap: 20px;}
    .stTabs [data-baseweb="tab"] {padding: 10px 20px; font-weight: bold; border-radius: 5px 5px 0 0;}
    .stTabs [aria-selected="true"] {background-color: #fce8e9; border-bottom: 3px solid #d1121d;}
    </style>
""", unsafe_allow_html=True)

# --- ÜST BİLGİ VE LOGO ---
col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.image("https://arsavev.com/wp-content/uploads/2023/11/logo_arsavev.png", width=150)
with col_title:
    st.title("ArsaVev Kurumsal Zeka (BI) & Satış Otomasyonu")
    st.caption("Dijital Satış Ekipleri İçin Gerçek Zamanlı Portföy & Analitik Ekranı | V2.0 PRO")

st.markdown("---")

# --- SOL MENÜ (KONTROL PANELİ) ---
with st.sidebar:
    st.header("⚙️ Arama Parametreleri")
    musteri_adi = st.text_input("Müşteri Adı Soyadı", "Ahmet Yılmaz")
    
    st.subheader("Bölge & Bütçe")
    bolge = st.selectbox("Hedef Lokasyon", ["Çanakkale / Ayvacık", "İzmir / Dikili", "Sakarya / Sapanca", "Balıkesir / Edremit"])
    butce = st.slider("Maksimum Bütçe (Milyon TL)", min_value=1.0, max_value=10.0, value=2.5, step=0.1)
    
    st.subheader("Parsel Özellikleri")
    imar_durumu = st.selectbox("İmar Tipi", ["Konut İmarlı", "Ticari İmarlı", "Tarım / Ekolojik"])
    
    analiz_butonu = st.button("Sistemi Çalıştır 🚀", use_container_width=True)
    st.info("💡 Sistem, ArsaVev simülasyon veritabanı üzerinden makine öğrenmesi algoritmalarıyla en yüksek 'Yatırım Getirisi (ROI)' sunan portföyleri süzer.")

# --- ANA EKRAN (SEKMELİ YAPI) ---
# Sekmeleri oluşturuyoruz (Tıpkı profesyonel bir program gibi)
tab1, tab2, tab3 = st.tabs(["📊 Makro Analiz & Metrikler", "🗺️ İnteraktif Lokasyon Haritası", "📲 Satış/Teklif Çıktısı"])

if analiz_butonu:
    with st.spinner("Büyük veri setleri taranıyor ve yapay zeka analizleri tamamlanıyor..."):
        time.sleep(2) # İşlem yapıyormuş hissi
        
    # --- SEKMELERİN İÇERİĞİ ---
    
    # 1. SEKME: ANALİZ VE GRAFİKLER
    with tab1:
        st.subheader(f"📌 {bolge} - Bölgesel Performans Özeti")
        
        # Metrikler
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Bölge Yapay Zeka Skoru", "9.2/10", "+0.4 Yükseliş")
        m2.metric("Ortalama ROI (Amortisman)", "4.1 Yıl", "Bölge ortalamasından %15 daha iyi", delta_color="normal")
        m3.metric("Öngörülen Yıllık Prim", "%65", "+%12 Son 6 Ay")
        m4.metric("Eşleşen Parsel Sayısı", "3 Adet", "Stok Kritik Seviyede", delta_color="off")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Grafikler (Plotly ile çok estetik)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Aylara Göre m² Birim Fiyat Endeksi (TL)**")
            # Rastgele ama inandırıcı veri
            aylar = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara']
            fiyatlar = [1500, 1550, 1620, 1680, 1790, 1850, 1950, 2100, 2250, 2400, 2550, 2750]
            df_trend = pd.DataFrame({'Ay': aylar, 'm² Fiyatı': fiyatlar})
            
            fig = px.area(df_trend, x='Ay', y='m² Fiyatı', color_discrete_sequence=['#d1121d'])
            fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), height=300)
            st.plotly_chart(fig, use_container_width=True)
            
        with c2:
            st.markdown("**Bölgedeki Alıcı Profil Dağılımı**")
            # Pasta grafik
            df_profil = pd.DataFrame({
                'Profil': ['Yatırımcı', 'Oturum Amaçlı', 'Ticari', 'Yabancı Yatırımcı'],
                'Oran': [45, 30, 15, 10]
            })
            fig2 = px.pie(df_profil, values='Oran', names='Profil', hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
            fig2.update_layout(margin=dict(l=0, r=0, t=0, b=0), height=300)
            st.plotly_chart(fig2, use_container_width=True)

    # 2. SEKME: HARİTA
    with tab2:
        st.subheader("📍 Eşleşen Portföylerin Konum Dağılımı")
        st.markdown("Aşağıdaki harita, kriterlerinize uygun olan arsaların konumlarını göstermektedir (Simülasyon verisidir).")
        
        # Seçilen bölgeye göre koordinat (Küçük bir detay ama harika görünür)
        if "Çanakkale" in bolge:
            lat, lon = 39.6, 26.4 # Ayvacık civarı
        elif "İzmir" in bolge:
            lat, lon = 39.0, 26.8 # Dikili civarı
        elif "Sakarya" in bolge:
            lat, lon = 40.7, 30.2 # Sapanca
        else:
            lat, lon = 39.5, 27.9 # Default Balıkesir
            
        # Harita için veri oluşturma
        df_map = pd.DataFrame(
            np.random.randn(3, 2) / [50, 50] + [lat, lon],
            columns=['lat', 'lon']
        )
        st.map(df_map, zoom=10)

    # 3. SEKME: TEKLİF ÇIKTISI
    with tab3:
        st.subheader("📲 Optimize Edilmiş Dijital Satış Teklifi")
        st.success(f"{musteri_adi} kişisi için kişiselleştirilmiş analiz metni hazırlandı. Kopyalayarak WhatsApp üzerinden paylaşabilirsiniz.")
        
        teklif = f"""🏢 ARSAVEV KURUMSAL YATIRIM ANALİZİ

Sayın {musteri_adi},

Dijital satış sistemlerimizin {butce} Milyon TL bütçe hedefinize özel gerçekleştirdiği tarama sonucunda; en yüksek getiri potansiyeline sahip lokasyon **{bolge}** olarak belirlenmiştir.

📊 Bölge Performans Metrikleri:
• Son 12 Aylık m² Değer Artışı: %65
• Emsal ROI (Amortisman): 4.1 Yıl (Bölge ortalamasının üstünde)
• İmar Durumu: {imar_durumu}

📍 Sistem Seçimi:
Yapay zeka altyapımız, bölgedeki altyapı projeleri ve demografik genişleme verilerini baz alarak sizin için 'Düşük Risk - Yüksek Getiri' endeksinde 3 farklı parsel eşleştirmesi yapmıştır.

ArsaVev veri odaklı yatırım vizyonuyla, bu parsellerin detaylı konumları ve tapu bilgileri üzerinden dijital sunum yapmak isterim. İncelemek isterseniz randevu planlayabiliriz.

Saygılarımla,
Yaren Selin Arı
ArsaVev Dijital Uzman Yardımcısı
"""
        st.text_area("Metni Kopyalayınız:", value=teklif, height=350)

else:
    # Henüz butona basılmadıysa ekranda görünecek karşılama mesajı
    st.info("👈 Analizi başlatmak için sol menüden müşteri parametrelerini belirleyip 'Sistemi Çalıştır' butonuna basınız.")
