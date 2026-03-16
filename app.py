import streamlit as st
import pandas as pd
import plotly.express as px
import time

# --- 1. SAYFA AYARLARI ---
st.set_page_config(page_title="ArsaVev Kurumsal BI", page_icon="🏢", layout="wide", initial_sidebar_state="expanded")

# --- 2. ARSAVEV MARKA KİMLİĞİ & CSS (SİHİRLİ KISIM) ---
st.markdown("""
    <style>
    /* Kurumsal Font: Montserrat */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif !important;
    }

    /* Uygulama Arka Planı (Açık Gri - Profesyonel BI Görünümü) */
    .stApp {
        background-color: #f4f6f9;
    }

    /* Sol Menü (Sidebar) Şık Tasarım */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }

    /* KPI Metrik Kartları (Gölge, Kenarlık ve Marka Rengi Aksanı) */
    [data-testid="stMetric"] {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 15px 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.04);
        border-left: 4px solid #d1121d; /* ArsaVev Kırmızısı */
    }
    [data-testid="stMetricLabel"] {
        color: #64748b;
        font-weight: 600;
        font-size: 14px;
    }
    [data-testid="stMetricValue"] {
        color: #0f172a;
        font-weight: 700;
    }

    /* Aksiyon Butonu (Gradient Kırmızı) */
    .stButton>button {
        background: linear-gradient(135deg, #d1121d 0%, #900b12 100%);
        color: white;
        border: none;
        border-radius: 6px;
        padding: 12px 24px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(209, 18, 29, 0.25);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(209, 18, 29, 0.4);
    }

    /* Streamlit Default Üst ve Alt Bilgilerini Gizleme (Tam Uygulama Hissi) */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {background-color: transparent;}
    
    /* Sekme Tasarımı */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #ffffff;
        padding: 5px 10px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.03);
    }
    .stTabs [data-baseweb="tab"] {
        color: #475569;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        color: #d1121d !important;
        border-bottom-color: #d1121d !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. HEADER & LOGO ---
col_logo, col_text = st.columns([1, 6])
with col_logo:
    st.image("https://arsavev.com/wp-content/uploads/2023/11/logo_arsavev.png", width=130)
with col_text:
    st.markdown("<h2 style='color: #0f172a; margin-bottom: 0px;'>Dijital Lead & Dönüşüm Paneli</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 15px;'>ArsaVev Kurumsal BI (Business Intelligence) ve Satış Otomasyon Ekranı</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- 4. SOL MENÜ (VERİ GİRİŞİ) ---
with st.sidebar:
    st.markdown("<h3 style='color: #0f172a;'>🎯 Lead Girdisi</h3>", unsafe_allow_html=True)
    
    lead_adi = st.text_input("Lead Adı Soyadı", "Örn: Caner Taşkın")
    lead_kaynagi = st.selectbox("Trafik Kaynağı", ["Instagram Meta Ads", "Google Search", "Web Formu", "Influencer"])
    ilgi_alani = st.selectbox("İlgilenilen Konsept", ["Tiny House Köyü", "Ekolojik Tarım", "Ticari Yatırım", "Klasik Parsel"])
    
    analiz_butonu = st.button("AI Profil Analizini Başlat ⚡", use_container_width=True)
    
    st.markdown("---")
    st.caption("🔒 Tasarım tamamen ArsaVev marka yönergelerine (UI/UX) uygun olarak özelleştirilmiştir.")

# --- 5. ANA EKRAN (ANALİZ VE ÇIKTILAR) ---
if analiz_butonu:
    if not lead_adi or lead_adi == "Örn: Caner Taşkın":
        st.warning("Lütfen analize başlamak için müşteri adını giriniz.")
    else:
        with st.spinner("Dijital veriler işleniyor, marka renklerine uygun rapor oluşturuluyor..."):
            time.sleep(1.5)
            
        if ilgi_alani == "Tiny House Köyü":
            uygun_proje = "Ayvacık Tiny House Yaşam Projesi"
            kapanis = "%42"
        elif ilgi_alani == "Ekolojik Tarım":
            uygun_proje = "Dikili Eko-Tarım Arazileri"
            kapanis = "%38"
        else:
            uygun_proje = "Edremit Vizyon Yatırım Projesi"
            kapanis = "%55"

        # Sekmeli Yapı
        tab1, tab2 = st.tabs(["📊 Kurumsal Dashboard", "📲 Müşteri İletişim Aksiyonu"])
        
        with tab1:
            st.markdown(f"<h4 style='color: #d1121d;'>{lead_adi} - Lead Kalite ve Proje Eşleşmesi</h4>", unsafe_allow_html=True)
            
            # KPI Kartları
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Sıcaklık Skoru", "88/100", "A Sınıfı Lead")
            c2.metric("Eşleşen Proje", uygun_proje)
            c3.metric(f"{lead_kaynagi} Dönüşümü", kapanis, "+%4 Trend")
            c4.metric("Önerilen Temas", "İlk 15 Dk", "Acil Aranmalı", delta_color="inverse")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Grafikler (Marka Renkleriyle)
            col_g1, col_g2 = st.columns(2)
            
            with col_g1:
                st.markdown("**Kampanya Dönüşüm Hacmi**")
                df_bar = pd.DataFrame({
                    'Projeler': ['Tiny House', 'Eko Tarım', 'Klasik', 'Ticari'],
                    'Lead Sayısı': [120, 85, 200, 45]
                })
                # Kırmızı tonlarıyla grafik
                fig_bar = px.bar(df_bar, x='Projeler', y='Lead Sayısı', color_discrete_sequence=['#d1121d'])
                fig_bar.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
                st.plotly_chart(fig_bar, use_container_width=True)
                
            with col_g2:
                st.markdown("**Kanal Kaynak Dağılımı**")
                df_pie = pd.DataFrame({
                    'Kaynak': ['Meta Ads', 'Google Search', 'Web Form', 'Organik'],
                    'Yüzde': [45, 30, 15, 10]
                })
                # ArsaVev Kırmızısı ve kurumsal griler
                fig_pie = px.pie(df_pie, values='Yüzde', names='Kaynak', hole=0.6, color_discrete_sequence=['#d1121d', '#334155', '#94a3b8', '#cbd5e1'])
                fig_pie.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
                st.plotly_chart(fig_pie, use_container_width=True)

        with tab2:
            st.markdown("#### Satış Ekibi Otomasyon Çıktısı")
            st.info("Bu metin müşterinin ilgilendiği proje konseptine göre otomatik şekillenmiştir.")
            
            wp_metni = f"""Merhaba {lead_adi} Bey/Hanım, 
Ben ArsaVev Dijital Satış Ekibinden Yaren Selin.

'{lead_kaynagi}' üzerinden yayınladığımız '{ilgi_alani}' kampanyamızı incelediğinizi görüyorum. Dijital ekosistemimizdeki ilgi alanlarınıza en uygun ve lansman döneminde olan **{uygun_proje}** için şu an özel avantajlar sunuyoruz.

Projemizin detayları ve güncel fiyatlandırmaları hakkında size kısa bir dijital sunum yapmak isterim. Gün içinde ne zaman müsaitsiniz?

Saygılarımla,
Yaren Selin Arı
ArsaVev Dijital Uzman Yardımcısı
"""
            st.text_area("Müşteriye Doğrudan İletilecek Metin:", value=wp_metni, height=280)

else:
    st.info("👈 Sistem hazır. Analiz başlatmak için sol paneli kullanınız.")
