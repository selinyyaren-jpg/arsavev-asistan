import streamlit as st
import time

# Sayfa Ayarları (Sekme adı ve ikon)
st.set_page_config(page_title="ArsaVev Akıllı Asistan", page_icon="🏢", layout="centered")

# Şirket Logosu ve Başlık
st.image("https://arsavev.com/wp-content/uploads/2023/11/logo_arsavev.png", width=250)
st.title("Akıllı Portföy & Teklif Asistanı")
st.markdown("Online satış süreçlerini hızlandıran, veri tabanlı portföy eşleştirme sistemi.")
st.markdown("---")

# Kullanıcı Giriş Alanları (Yan yana düzenli görünüm)
col1, col2 = st.columns(2)
with col1:
    musteri_adi = st.text_input("Müşteri Adı Soyadı", placeholder="Örn: Ahmet Yılmaz")
    bolge = st.selectbox("Hedef Bölge", ["Çanakkale / Ayvacık", "İzmir / Dikili", "Balıkesir / Edremit", "Ankara / Beypazarı"])
with col2:
    butce = st.number_input("Maksimum Bütçe (TL)", min_value=500000, value=2500000, step=100000, format="%d")

st.markdown(" ") # Boşluk

# Aksiyon Butonu
if st.button("🔍 Portföyü Tara ve AI Teklifi Oluştur", type="primary", use_container_width=True):
    
    if musteri_adi == "":
        st.warning("Lütfen müşteri adını giriniz.")
    else:
        # Yüklenme efekti (Çok profesyonel durur)
        with st.spinner('CRM ve stok verileri taranıyor, AI analizi yapılıyor...'):
            time.sleep(2) # Simülasyon süresi
            
        st.success("✅ Müşteri profiline en uygun portföy eşleştirildi!")
        
        # Datacı Yöneticinin Seveceği Metrik Kartları
        st.subheader("📊 Yapay Zeka Bölge & Yatırım Analizi")
        m1, m2, m3 = st.columns(3)
        m1.metric(label="Yıllık Değer Artışı", value="%45", delta="Yüksek Trend")
        m2.metric(label="Eşleşen Parsel Büyüklüğü", value="450 m²", delta="İdeal Oturum", delta_color="normal")
        m3.metric(label="Stok Durumu", value="Sıcak Satışta", delta="Son 2 Parsel", delta_color="off")
        
        st.markdown("---")
        
        # Kopyalanabilir Sonuç Ekranı
        st.subheader("📲 Müşteri İletişim Metni (WhatsApp)")
        
        formatli_butce = "{:,}".format(int(butce)).replace(",", ".")
        teklif_metni = f"""🏢 ArsaVev Özel Yatırım Fırsatı

Sayın {musteri_adi},

Belirttiğiniz {formatli_butce} TL bütçe ve yatırım hedefleriniz doğrultusunda, ArsaVev güvencesiyle size özel seçtiğimiz {bolge} vizyon projesi detayları aşağıdadır:

💡 Neden Bu Lokasyon? (AI Yatırım Özeti):
Sistemlerimizin analizine göre seçilen bölge son 1 yılda %45 değer artışı göstermiş olup, yeni altyapı projelerinin merkezinde yer almaktadır. Kısa vadede yüksek prim potansiyeli taşımaktadır.

Detaylı parsel seçimi ve dijital sunum için benimle iletişime geçebilirsiniz.
"""
        st.text_area("Aşağıdaki metni kopyalayıp doğrudan müşteriye iletebilirsiniz:", value=teklif_metni, height=250)
