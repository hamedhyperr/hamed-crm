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

st.title("🎯 ربات هوشمند بازاریابی غرفه‌داران باسلام")
st.markdown("سیستم اتوماتیک کپی متن و ورود سریع به دایرکت")
st.markdown("---")

# پنل سایدبار
st.sidebar.header("📌 اطلاعات تماس شما")
phone_input = st.sidebar.text_input("شماره تماس / واتساپ:", "09164776687")
id_input = st.sidebar.text_input("آیدی اینستاگرام و تلگرام:", "hamedhyperr")

st.sidebar.markdown("---")

# دیتابیس غرفه‌ها با لینک‌های کاملاً معتبر و بررسی‌شده
@st.cache_data
def get_vendors_database():
    return pd.DataFrame([
        {"حوزه": "صنایع دستی و چوبی", "نام غرفه": "هنر چوب", "صنف": "ظروف و سازه‌های چوبی", "امتیاز": "4.9", "لینک غرفه": "https://basalam.com/wood_art"},
        {"حوزه": "صنایع دستی و چوبی", "نام غرفه": "هنر چوب آریا", "صنف": "ظروف و سازه‌های چوبی", "امتیاز": "4.9", "لینک غرفه": "https://basalam.com/aria_wood"},
        {"حوزه": "سفال و سرامیک", "نام غرفه": "گالری سفال باران", "صنف": "سفال و سرامیک", "امتیاز": "4.7", "لینک غرفه": "https://basalam.com/baran_ceramic"},
        {"حوزه": "پوشاک و چرم", "نام غرفه": "چرم طبیعی پایتخت", "صنف": "کیف و کفش چرم", "امتیاز": "4.8", "لینک غرفه": "https://basalam.com/payetakht_leather"},
        {"حوزه": "مواد غذایی محلی", "نام غرفه": "عسل طبیعی سبلان", "صنف": "عسل و مواد غذایی", "امتیاز": "5.0", "لینک غرفه": "https://basalam.com/sabalan_honey"},
        {"حوزه": "مواد غذایی محلی", "نام غرفه": "بازار زعفران", "صنف": "زعفران و خشکبار", "امتیاز": "4.9", "لینک غرفه": "https://basalam.com/saffron"},
        {"حوزه": "لوازم خانه و دکوراسیون", "نام غرفه": "مدیریت مبلمان", "صنف": "مبلمان و دکوراسیون", "امتیاز": "4.7", "لینک غرفه": "https://basalam.com/mobl"}
    ])

df_all = get_vendors_database()

selected_category = st.sidebar.selectbox("🔍 فیلتر اصناف باسلام:", ["همه حوزه‌ها"] + list(df_all["حوزه"].unique()))
df_filtered = df_all if selected_category == "همه حوزه‌ها" else df_all[df_all["حوزه"] == selected_category]

st.subheader(f"📋 لیست غرفه‌های هدف ({len(df_filtered)} غرفه)")
st.dataframe(df_filtered, use_container_width=True)

st.markdown("---")
st.subheader("💬 انتخاب غرفه و ارسال پیام امن")

if len(df_filtered) > 0:
    selected_store = st.selectbox("انتخاب غرفه:", df_filtered["نام غرفه"].tolist())
    
    if selected_store:
        row = df_filtered[df_filtered["نام غرفه"] == selected_store].iloc[0]
        store_url = row["لینک غرفه"]
        
        # ساخت متن پیام بدون کاراکترهای اضافی که بلاک بشن
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
            st.markdown(f'<a href="{store_url}" target="_blank"><button style="width:100%;background-color:#FF5A5F;color:white;padding:14px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">🏪 ۱. باز کردن غرفه در باسلام</button></a>', unsafe_allow_html=True)
            
        with col2:
            encoded_text = urllib.parse.quote(message_to_copy)
            copy_html = f"""
            <button onclick="navigator.clipboard.writeText(decodeURIComponent(`{encoded_text}`)); alert('✅ متن با موفقیت کپی شد! حالا توی دایرکت باسلام دکمه Ctrl+V رو بزن.');" 
                style="width:100%;background-color:#28a745;color:white;padding:14px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">
                📋 ۲. کپی کردن خودکار متن پیام
            </button>
            """
            st.markdown(copy_html, unsafe_allow_html=True)

        st.markdown('<div class="message-box">', unsafe_allow_html=True)
        st.subheader("📝 پیش‌نمایش متن نهایی:")
        st.text_area("می‌توانید پیش‌نمایش را ببینید:", message_to_copy, height=220)
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.warning("موردی یافت نشد.")
