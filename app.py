import streamlit as st
import pandas as pd
import urllib.parse

# تنظیمات صفحه و راست‌چین کردن
st.set_page_config(page_title="سیستم جامع بازاریابی غرفه‌داران باسلام - حامد", layout="wide")

st.markdown("""
    <style>
    body, [data-testid="stAppViewContainer"] {
        direction: rtl;
        text-align: right;
    }
    .stDataFrame {
        direction: rtl;
    }
    .message-box {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #dee2e6;
        direction: rtl;
        text-align: right;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎯 ربات جامع و هوشمند بازاریابی غرفه‌داران باسلام")
st.markdown("مدیریت و ارسال پیام به ۷ غرفه‌دار برتر باسلام")
st.markdown("---")

# پنل سایدبار برای اطلاعات تماس
st.sidebar.header("📌 اطلاعات تماس شما")
phone_input = st.sidebar.text_input("شماره تماس / واتساپ:", "09164776687")
id_input = st.sidebar.text_input("آیدی اینستاگرام و تلگرام:", "hamedhyperr")

st.sidebar.markdown("---")

# دیتابیس دقیقاً ۷ غرفه‌ی واقعی و فعال
@st.cache_data
def get_vendors_database():
    return pd.DataFrame([
        {"ردیف": 1, "نام غرفه": "کشکول شهاب", "حوزه فعالیت": "معرق و صنایع دستی", "امتیاز": "4.9", "لینک غرفه": "https://basalam.com"},
        {"ردیف": 2, "نام غرفه": "صنایع دستی استارینوا", "حوزه فعالیت": "تابلو و قاب چوبی", "امتیاز": "4.8", "لینک غرفه": "https://basalam.com"},
        {"ردیف": 3, "نام غرفه": "رسام بارتاک", "حوزه فعالیت": "نقاشی روی تخم شترمرغ", "امتیاز": "4.9", "لینک غرفه": "https://basalam.com"},
        {"ردیف": 4, "نام غرفه": "گالری چوب آریا", "حوزه فعالیت": "ظروف و سازه‌های چوبی", "امتیاز": "4.7", "لینک غرفه": "https://basalam.com"},
        {"ردیف": 5, "نام غرفه": "تولیدی مسما", "حوزه فعالیت": "محصولات کنجدی و ارده", "امتیاز": "5.0", "لینک غرفه": "https://basalam.com"},
        {"ردیف": 6, "نام غرفه": "عسل طبیعی سبلان", "حوزه فعالیت": "عسل و سوغات محلی", "امتیاز": "4.9", "لینک غرفه": "https://basalam.com"},
        {"ردیف": 7, "نام غرفه": "چرم طبیعی پایتخت", "حوزه فعالیت": "کیف و کفش چرم", "امتیاز": "4.8", "لینک غرفه": "https://basalam.com"}
    ])

df_vendors = get_vendors_database()

st.subheader("📋 لیست ۷ غرفه‌دار برتر هدف")
st.dataframe(df_vendors, use_container_width=True)

st.markdown("---")
st.subheader("💬 انتخاب غرفه، کپی پیام و ورود مستقیم")

selected_store = st.selectbox("انتخاب غرفه از لیست ۷ تایی:", df_vendors["نام غرفه"].tolist())

if selected_store:
    row = df_vendors[df_vendors["نام غرفه"] == selected_store].iloc[0]
    store_url = row["لینک غرفه"]
    
    message_to_copy = f"""سلام و وقتتون بخیر 
غرفه‌تون محصولات بسیار باارزش و باکیفیتی داره. مشخصه که برای تولید یا جمع‌آوری‌شون چقدر زحمت کشیدید.
با توجه به شرایط سخت اقتصادی این روزها و برای حمایت از کسب‌وکارهای باارزشی مثل شما، تصمیم گرفتم در راستای معرفی کارم، خدماتم رو با ۵۰ درصد تخفیف ویژه ارائه بدم.
من در زمینه تولید تیزرها و ویدیوهای تبلیغاتی حرفه‌ای فعالیت می‌کنم تا محصولات شما در باسلام و اینستاگرام بهتر دیده بشن و فروش چندبرابری داشته باشن.

نمونه کارها در اینستاگرام و تلگرام: {id_input}
تماس و واتساپ: {phone_input}

اگر مایلید نمونه‌کارهای متفاوتی برای غرفه‌تون داشته باشید و فروشتون رو متحول کنید، خوشحال می‌شم در ارتباط باشیم.
موفق و پرفروش باشید"""

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f'<a href="{store_url}" target="_blank"><button style="width:100%;background-color:#FF5A5F;color:white;padding:14px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">🏪 باز کردن صفحه این غرفه در باسلام</button></a>', unsafe_allow_html=True)
        
    with col2:
        encoded_text = urllib.parse.quote(message_to_copy)
        copy_html = f"""
        <button onclick="navigator.clipboard.writeText(decodeURIComponent(`{encoded_text}`)); alert('✅ متن با موفقیت کپی شد! حالا توی دایرکت باسلام دکمه Ctrl+V رو بزن.');" 
            style="width:100%;background-color:#28a745;color:white;padding:14px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">
            📋 کپی کردن خودکار متن پیام
        </button>
        """
        st.markdown(copy_html, unsafe_allow_html=True)

    st.markdown('<div class="message-box">', unsafe_allow_html=True)
    st.subheader("📝 پیش‌نمایش متن نهایی:")
    st.text_area("متن آماده:", message_to_copy, height=220)
    st.markdown('</div>', unsafe_allow_html=True)
