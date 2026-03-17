import streamlit as st
import pandas as pd
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(
    page_title="Mkopo Rafiki",
    page_icon="💰",
    layout="centered"
)

# العنوان الرئيسي
st.markdown("""
<h1 style='text-align: center; color: #2ecc71;'>💰 Mkopo Rafiki</h1>
<h3 style='text-align: center;'>Tafuta mkopo unaofaa biashara yako kwa dakika 1</h3>
<hr style='margin-bottom: 30px;'>
""", unsafe_allow_html=True)

# قائمة البنوك (سنحدثها لاحقاً)
BANKS = [
    {
        "name": "KCB Bank Uganda",
        "min_income": 500000,
        "max_loan": 50000000,
        "interest": "14% - 18%",
        "contact": "0782-123456",
        "logo": "🏦",
        "requirements": ["Dhamana (Collateral)", "Kipato cha utulivu"]
    },
    {
        "name": "dfcu Bank",
        "min_income": 300000,
        "max_loan": 20000000,
        "interest": "15% - 19%",
        "contact": "0800-123456",
        "logo": "🏛️",
        "requirements": ["Akaunti ya dfcu", "Biashara iliyosajiliwa"]
    },
    {
        "name": "Finance Trust Bank",
        "min_income": 200000,
        "max_loan": 10000000,
        "interest": "16% - 20%",
        "contact": "0755-789012",
        "logo": "🏪",
        "requirements": ["Kikundi cha wanawake (SACCO)", "Dhamana ya kijamii"]
    },
    {
        "name": "Centenary Bank",
        "min_income": 150000,
        "max_loan": 5000000,
        "interest": "13% - 17%",
        "contact": "0777-456789",
        "logo": "🏫",
        "requirements": ["Akaunti ya Centenary", "Biashara ya kilimo"]
    },
    {
        "name": "Pride Microfinance",
        "min_income": 100000,
        "max_loan": 3000000,
        "interest": "18% - 22%",
        "contact": "0700-111222",
        "logo": "💼",
        "requirements": ["Kikundi cha Pride", "Biashara ndogo"]
    }
]

# واجهة الإدخال (بالسواحلية)
st.markdown("### 📋 Jaza maelezo yako")

col1, col2 = st.columns(2)

with col1:
    income = st.number_input(
        "💰 Mapato yako kwa mwezi (UGX)",
        min_value=0,
        step=100000,
        value=500000,
        format="%d"
    )
    
    purpose = st.selectbox(
        "🎯 Madhumuni ya mkopo",
        ["Biashara", "Kilimo", "Binafsi", "Elimu", "Nyumba"]
    )

with col2:
    amount = st.number_input(
        "💵 Kiasi unachohitaji (UGX)",
        min_value=0,
        step=500000,
        value=1000000,
        format="%d"
    )
    
    collateral = st.radio(
        "🔒 Je, una dhamana? (Collateral)",
        ["Ndiyo", "Hapana", "Sijui"]
    )

# معلومات إضافية
with st.expander("➕ Maelezo zaidi (si lazima)"):
    business_type = st.text_input("Aina ya biashara yako")
    location = st.text_input("Mahali unapoishi (Mji/Kijiji)")
    phone = st.text_input("Namba ya simu")

# زر البحث
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔍 Tafuta benki zinazofaa", type="primary", use_container_width=True):
    
    st.markdown("---")
    st.markdown("### ✅ Benki zinazokufaa")
    
    found = False
    results = []
    
    for bank in BANKS:
        if income >= bank["min_income"]:
            if amount <= bank["max_loan"]:
                found = True
                results.append(bank)
                
                # حساب نسبة الموافقة (تقديرية)
                approval_rate = min(100, (income / bank["min_income"]) * 50 + 50)
                
                # عرض البنك
                with st.container():
                    st.markdown(f"""
                    <div style='border: 1px solid #ddd; border-radius: 10px; padding: 15px; margin-bottom: 15px; background-color: {"#f0fff0" if approval_rate > 80 else "#f9f9f9"};'>
                        <h4>{bank['logo']} {bank['name']}</h4>
                        <p>💰 <b>Kiasi cha juu:</b> {bank['max_loan']:,} UGX</p>
                        <p>📊 <b>Riba:</b> {bank['interest']}</p>
                        <p>✅ <b>Uwezekano wa kufaulu:</b> {approval_rate:.0f}%</p>
                        <p>📞 <b>Wasiliana:</b> {bank['contact']}</p>
                        <p>📋 <b>Mahitaji:</b> {', '.join(bank['requirements'])}</p>
                    </div>
                    """, unsafe_allow_html=True)
    
    if not found:
        st.error("❌ Pole, hakuna benki inayokufaa sasa. Jaribu kuongeza mapato yako au kupunguza kiasi unachohitaji.")
        
        # اقتراح بدائل
        st.info("💡 Unaweza kujaribu:\n- Kuomba mkopo mdogo\n- Kuungana na kikundi (SACCO)\n- Kutafuta dhamana")
    
    # حفظ البحث
    if phone:
        st.markdown("---")
        st.success(f"📱 Asante {phone}. Tutakujulisha wakati kuna benki mpya zinazoingia!")
        
        # هنا يمكن إضافة كود لحفظ البيانات في ملف أو قاعدة بيانات

# شريط جانبي بمعلومات مفيدة
with st.sidebar:
    st.markdown("### ℹ️ Habari")
    st.markdown("""
    **Mkopo Rafiki** inakusaidia:
    - Kupata benki inayokufaa
    - Kulinganisha riba
    - Kuwasiliana moja kwa moja
    
    **Huduma yetu ni bure kabisa!**
    """)
    
    st.markdown("---")
    st.markdown("### 📞 Wasiliana nasi")
    st.markdown("WhatsApp: 07XXXXXXXX")
    st.markdown("Email: info@mkoporafiki.ug")
    
    st.markdown("---")
    st.markdown("### 🏦 Benki Washirika")
    for bank in BANKS[:3]:
        st.markdown(f"{bank['logo']} {bank['name']}")

# تذييل
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026 Mkopo Rafiki. Haki zote zimehifadhiwa.</p>", unsafe_allow_html=True)
