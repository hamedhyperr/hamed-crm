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
st.markdown("سیستم هوشمند اتصال مستقیم به جستجوی اصناف و کپی خودکار پیام")
st.markdown("---")

# پنل سایدبار برای اطلاعات تماس
st.sidebar.header("📌 اطلاعات تماس شما")
phone_input = st.sidebar.text_input("شماره تماس / واتساپ:", "09164776687")
id_input = st.sidebar.text_input("آیدی اینستاگرام و تلگرام:", "hamedhyperr")

st.sidebar.markdown("---")

# دیتابیس غرفه‌ها با لینکِ دقیق جستجوی همان صنف در باسلام (بدون ارور ۴۰۴)
@st.cache_data
def get_vendors_database():
    return pd.DataFrame([
        {"حوزه": "صنایع دستی و چوبی", "نام غرفه و صنف": "ظروف و سازه‌های چوبی", "امتیاز": "4.9", "لینک جستجو در باسلام": "https://basalam.com/search?q=%D8%B8%D8%B1%D9%88%D9%81%20%DA%86%D9%88%D8%A8%DB%8C"},
        {"حوزه": "صنایع دستی و چوبی", "نام غرفه و صنف": "معرق و منبت کاری", "امتیاز": "4.8", "لینک جستجو در باسلام": "https://basalam.com/search?q=%D9%85%D8%B9%D8%B1%D9%82%20%DA%A9%D8%A7ری"},
        {"حوزه": "سفال و سرامیک", "نام غرفه و صنف": "سفال و سرامیک دست‌ساز", "امتیاز": "4.7", "لینک جستجو در باسلام": "https://basalam.com/search?q=%D8%B3%D9%81%D8%A7%D9%84%20%D9%88%20%D8%B3%D8%B1%D8%A7%D9%85%DB%8C%DA%A9"},
        {"حوزه": "پوشاک و چرم", "نام غرفه و صنف": "کیف و کفش چرم طبیعی", "امتیاز": "4.8", "لینک جستجو در باسلام": "https://basalam.com/search?q=%DA%A9%DB%8C%D9%81%20%DA%86%D8%B1%D9%85"},
        {"حوزه": "مواد غذایی محلی", "نام غرفه و صنف": "محصولات کنجدی و ارده", "امتیاز": "5.0", "لینک جستجو در باسلام": "https://basalam.com/search?q=%D8%A7%D8%B1%D8%AF%D9%87%20%DA%A9%D9%86%D8%AC%D8%AF"},
        {"حوزه": "مواد غذایی محلی", "نام غرفه و صنف": "عسل طبیعی و سوغات", "امتیاز": "4.9", "لینک جستجو در باسلام": "https://basalam.com/search?q=%D8%B9%D8%B3%D9%84%20%D8%B7%D8%A8%DB%8C%D8%B9%DB%8C"},
        {"حوزه": "مواد غذایی محلی", "نام غرفه و صنف": "زعفران و خشکبار", "امتیاز": "4.9", "لینک جستجو در باسلام": "https://basalam.com/search?q=%D8%B2%D8%B9%D9%81%D8%B1%D8%A7%D9%86"},
        {"حوزه": "لوازم خانه و دکوراسیون", "نام غرفه و صنف": "دکوراسیون منزل و چوبی", "امتیاز": "4.7", "لینک جستجو در باسلام": "https://basalam.com/search?q=%D8%AF%DA%A9%D9%88%D8%B1%D8%A7%D8%B3%DB%8C%D9%88%D9%86"}
    ])

df_all = get_vendors_database()

# بخش جستجوی آزاد
col_search1, col_search2 = st.columns(2)
with col_search1:
    search_query = st.text_input("🔍 جستجوی آزاد صنف دلخواه:", "")
with col_search2:
    selected_category = st.sidebar.selectbox("📂 فیلتر دسته‌بندی:", ["همه حوزه‌ها"] + list(df_all["حوزه"].unique()))

# اعمال فیلترها
df_filtered = df_all.copy()
if selected_category != "همه حوزه‌ها":
    df_filtered = df_filtered[df_filtered["حوزه"] == selected_category]
if search_query:
    df_filtered = df_filtered[df_filtered['نام غرفه و صنف'].str.contains(search_query, na=False)]

st.subheader(f"📋 لیست حوزه‌ها و مشاغل فعال ({len(df_filtered)} مورد)")
st.dataframe(df_filtered, use_container_width=True)

st.markdown("---")
st.subheader("💬 انتخاب صنف، کپی پیام و ورود مستقیم به صفحه جستجوی همان صنف در باسلام")

if len(df_filtered) > 0:
    selected_store = st.selectbox("انتخاب صنف مد نظر:", df_filtered["نام غرفه و صنف"].tolist())
    
    if selected_store:
        row = df_filtered[df_filtered["نام غرفه و صنف"] == selected_store].iloc[0]
        store_url = row["لینک جستجو در باسلام"]
        
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
            st.markdown(f'<a href="{store_url}" target="_blank"><button style="width:100%;background-color:#FF5A5F;color:white;padding:14px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">🚀 ورود مستقیم به صفحه این صنف در باسلام</button></a>', unsafe_allow_html=True)
            
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
else:
    st.warning("موردی با این مشخصات یافت نشد.")
