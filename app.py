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

st.title("🎯 ربات هوشمند بازاریابی باسلام")
st.markdown("سیستم کپی متن پیام و ورود سریع و بدون خطا به باسلام")
st.markdown("---")

# پنل سایدبار برای اطلاعات تماس
st.sidebar.header("📌 اطلاعات تماس شما")
phone_input = st.sidebar.text_input("شماره تماس / واتساپ:", "09164776687")
id_input = st.sidebar.text_input("آیدی اینستاگرام و تلگرام:", "hamedhyperr")

st.sidebar.markdown("---")

# متن استاندارد و تاثیرگذار پیام
message_to_copy = f"""سلام و وقتتون بخیر 
غرفه‌تون محصولات بسیار باارزش و باکیفیتی داره. مشخصه که برای تولید یا جمع‌آوری‌شون چقدر زحمت کشیدید.
با توجه به شرایط سخت اقتصادی این روزها و برای حمایت از کسب‌وکارهای باارزشی مثل شما، تصمیم گرفتم در راستای معرفی کارم، خدماتم رو با ۵۰ درصد تخفیف ویژه ارائه بدم.
من در زمینه تولید تیزرها و ویدیوهای تبلیغاتی حرفه‌ای فعالیت می‌کنم تا محصولات شما در باسلام و اینستاگرام بهتر دیده بشن و فروش چندبرابری داشته باشن.

نمونه کارها در اینستاگرام و تلگرام: {id_input}
تماس و واتساپ: {phone_input}

اگر مایلید نمونه‌کارهای متفاوتی برای غرفه‌تون داشته باشید و فروشتون رو متحول کنید، خوشحال می‌شم در ارتباط باشیم.
موفق و پرفروش باشید"""

st.subheader("💬 ابزار سریع کپی متن و ورود به باسلام")

col1, col2 = st.columns(2)

# دکمه اول: باز کردن صفحه اصلی باسلام بدون هیچ اروری
with col1:
    st.markdown(containers_html := f'<a href="https://basalam.com" target="_blank"><button style="width:100%;background-color:#FF5A5F;color:white;padding:16px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">🏪 باز کردن سایت باسلام</button></a>', unsafe_allow_html=True)
    
# دکمه دوم: کپی خودکار متن
with col2:
    encoded_text = urllib.parse.quote(message_to_copy)
    copy_html = f"""
    <button onclick="navigator.clipboard.writeText(decodeURIComponent(`{encoded_text}`)); alert('✅ متن با موفقیت کپی شد! حالا توی دایرکت باسلام دکمه Ctrl+V رو بزن.');" 
        style="width:100%;background-color:#28a745;color:white;padding:16px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">
        📋 کپی کردن خودکار متن پیام
    </button>
    """
    st.markdown(copy_html, unsafe_allow_html=True)

st.markdown('<div class="message-box">', unsafe_allow_html=True)
st.subheader("📝 متن نهایی پیام برای بازبینی:")
st.text_area("متن آماده:", message_to_copy, height=250)
st.markdown('</div>', unsafe_allow_html=True)
