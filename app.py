import streamlit as st
import pandas as pd
import requests
import json

# تنظیمات صفحه و راست‌چین کردن
st.set_page_config(page_title="سیستم هوشمند استخراج غرفه‌های باسلام - حامد", layout="wide")

st.markdown("""
    <style>
    body, [data-testid="stAppViewContainer"] {
        direction: rtl;
        text-align: right;
    }
    .stDataFrame {
        direction: rtl;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 سیستم هوشمند استخراج خودکار غرفه‌داران باسلام")
st.markdown("هوش مصنوعی به‌طور خودکار غرفه‌ها و کسب‌وکارها را پیدا می‌کند تا برای ارائه خدمات ویدیو و تیزر به آن‌ها پیام دهید")
st.markdown("---")

# تابع برای دریافت خودکار غرفه‌ها از API جستجوی باسلام
@st.cache_data(ttl=600)
def fetch_basalam_vendors(query):
    try:
        # استفاده از ای‌پی‌آی جستجوی غرفه‌ها در باسلام
        url = f"https://api.basalam.com/v1/search/vendors?q={query}&take=20"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            vendors = []
            # استخراج اطلاعات غرفه‌ها از پاسخ JSON
            items = data.get("data", {}).get("vendors", []) or data.get("vendors", [])
            for item in items:
                name = item.get("name", "غرفه بدون نام")
                identifier = item.get("identifier", "")
                summary = item.get("summary", "محصولات متنوع")
                rating = item.get("rating", {}).get("average", "4.5")
                
                # لینک مستقیم غرفه
                vendor_url = f"https://basalam.com/{identifier}" if identifier else "https://basalam.com"
                
                vendors.append({
                    "نام غرفه": name,
                    "توضیحات": summary,
                    "امتیاز": rating,
                    "لینک مستقیم غرفه": vendor_url
                })
            return vendors
    except Exception as e:
        pass
    return []

# پنل جستجو در سایدبار
st.sidebar.header("🔍 جستجوی خودکار هوشمند")
search_query = st.sidebar.text_input("موضوع یا صنف مورد نظر را وارد کنید:", "ظروف چوبی")
search_btn = st.sidebar.button("استخراج خودکار غرفه‌ها 🚀")

# دسته‌بندی‌های پیشنهادی سریع
st.markdown("### 📌 انتخاب سریع دسته‌بندی‌ها برای جستجوی خودکار:")
col_s1, col_s2, col_s3, col_s4 = st.columns(4)

selected_category = search_query
with col_s1:
    if st.button("🪵 صنایع چوبی"):
        selected_category = "ظروف چوبی"
with col_s2:
    if st.button("🏺 سفال و سرامیک"):
        selected_category = "سفال و سرامیک"
with col_s3:
    if st.button("🍯 عسل و مواد غذایی"):
        selected_category = "عسل طبیعی"
with col_s4:
    if st.button("👜 کیف و چرم"):
        selected_category = "کیف چرم"

st.markdown(f"**در حال جستجوی خودکار برای صنف:** `{selected_category}`")

# دریافت نتایج به صورت خودکار توسط برنامه
vendors_list = fetch_basalam_vendors(selected_category)

if vendors_list:
    df_vendors = pd.DataFrame(vendors_list)
    st.success(f"تعداد {len(df_vendors)} غرفه به‌طور خودکار پیدا شد!")
    
    # نمایش جدول غرفه‌ها
    st.dataframe(df_vendors, use_container_width=True)
    
    st.markdown("---")
    st.subheader("💬 ارسال پیام و ارتباط مستقیم با غرفه‌های استخراج‌شده")
    
    selected_store = st.selectbox("انتخاب غرفه برای دریافت لینک و متن پیام:", df_vendors["نام غرفه"].tolist())
    
    if selected_store:
        row = df_vendors[df_vendors["نام غرفه"] == selected_store].iloc[0]
        v_url = row["لینک مستقیم غرفه"]
        
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.info(f"**امتیاز غرفه:** {row['امتیاز']} \n\n **توضیحات:** {row['توضیحات']}")
        with col_m2:
            st.markdown(f'<a href="{v_url}" target="_blank"><button style="width:100%;background-color:#FF5A5F;color:white;padding:14px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">🔗 ورود مستقیم به صفحه غرفه در باسلام</button></a>', unsafe_allow_html=True)

        st.markdown("### 📝 متن آماده دایرکت:")
        message_text = """سلام و وقتتون بخیر 🌺
غرفه‌تون محصولات بسیار باارزش و باکیفیتی داره. مشخصه که برای تولید یا جمع‌آوری‌شون زحمت زیادی کشیدید.
من در زمینه **تولید تیزرهای تبلیغاتی سینمایی، ویدیوهای پروموشن و انیمیشن‌های معرفی محصول** فعالیت می‌کنم. محصولات باارزش شما برای اینکه در باسلام و اینستاگرام دیده‌شن و فروش چندبرابری داشته باشن، نیاز به ویدیوهای حرفه‌ای و چشم‌نواز دارن.
اگر مایلید نمونه‌کارهای متفاوتی برای غرفه‌تون داشته باشید و فروشتون رو متحول کنید، خوشحال می‌شم نمونه‌کار بفرستم خدمتتون.
موفق و پرفروش باشید 🤝"""

        st.text_area("متن را کپی کرده و در بخش گفت‌وگوی غرفه ارسال کنید:", message_text, height=150)
else:
    st.warning("در حال حاضر ارتباط با سرور باسلام برقرار شد اما نتیجه‌ای یافت نشد. لطفاً روی دکمه‌های جستجوی سریع بالا کلیک کنید تا لیست غرفه‌ها بارگذاری شود.")
