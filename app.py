import streamlit as st
import pandas as pd

# تنظیمات صفحه و راست‌چین کردن
st.set_page_config(page_title="سیستم هوشمند یابنده غرفه‌های باسلام - حامد", layout="wide")

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

st.title("🛒 سیستم هوشمند استخراج و ارتباط با غرفه‌داران باسلام")
st.markdown("پیدا کردن مشاغل و کسب‌وکارهایی که به خدمات تولید محتوا، تیزر و انیمیشن نیاز مبرم دارند")
st.markdown("---")

# دیتابیس نمونه و واقعی از غرفه‌های فعال باسلام در دسته‌بندی‌های نیازمند محتوا
data = [
    {"نام غرفه": "artisan-wood", "عنوان غرفه": "صنایع چوبی و لوکس هنر چوب", "حوزه فعالیت": "صنایع دستی و چوبی", "شهر": "تهران", "امتیاز": "4.8"},
    {"نام غرفه": "persian-rug-shop", "عنوان غرفه": "گالری فرش و تابلوفرش دستباف", "حوزه فعالیت": "صنایع دستی و هنری", "شهر": "اصفهان", "امتیاز": "4.9"},
    {"نام غرفه": "organic-honey-store", "عنوان غرفه": "عسل طبیعی و ارگانیک کوهستان", "حوزه فعالیت": "مواد غذایی محلی", "شهر": "خوانسار", "امتیاز": "4.7"},
    {"نام غرفه": "leather-craft-99", "عنوان غرفه": "کیف و چرم طبیعی دست‌دوز", "حوزه فعالیت": "پوشاک و چرم", "شهر": "تبریز", "امتیاز": "4.9"},
    {"نام غرفه": "ceramic-art-studio", "عنوان غرفه": "سفال و سرامیک دکوراتیو دست‌ساز", "حوزه فعالیت": "صنایع دستی و هنری", "شهر": "لشکرآباد", "امتیاز": "4.6"},
    {"نام غرفه": "Saffron-Royal", "عنوان غرفه": "زعفران ممتاز و خشکبار رویال", "حوزه فعالیت": "مواد غذایی محلی", "شهر": "مشهد", "امتیاز": "5.0"},
    {"نام غرفه": "modern-mobl-Tehran", "عنوان غرفه": "تولیدی مبل و صنایع چوبی مدرن", "حوزه فعالیت": "دکوراسیون منزل", "شهر": "تهران", "امتیاز": "4.7"},
    {"نام غرفه": "traditional-dress-iran", "عنوان غرفه": "پوشاک سنتی و لباس‌های محلی", "حوزه فعالیت": "پوشاک و کیف و کفش", "شهر": "شیراز", "امتیاز": "4.8"}
]

df = pd.DataFrame(data)

# فیلترها در سایدبار
st.sidebar.header("🔍 فیلتر اصناف باسلام")
selected_category = st.sidebar.selectbox("انتخاب حوزه فعالیت:", ["همه حوزه‌ها"] + list(df["حوزه فعالیت"].unique()))

if selected_category != "همه حوزه‌ها":
    df_filtered = df[df["حوزه فعالیت"] == selected_category]
else:
    df_filtered = df

st.subheader(f"📋 لیست غرفه‌های هدف ({len(df_filtered)} غرفه)")
st.dataframe(df_filtered, use_container_width=True)

st.markdown("---")
st.subheader("💬 ارسال پیام و ورود مستقیم به دایرکت (گفت‌وگوی باسلام)")

if len(df_filtered) > 0:
    target_store = st.selectbox("انتخاب غرفه جهت ارتباط مستقیم:", df_filtered["عنوان غرفه"].tolist())
    
    if target_store:
        row = df[df["عنوان غرفه"] == target_store].iloc[0]
        store_id = row["نام غرفه"]
        
        # ساخت لینک اختصاصی صفحه غرفه و دایرکت در باسلام
        basalam_chat_url = f"https://basalam.com/{store_id}/chat"
        basalam_profile_url = f"https://basalam.com/{store_id}"
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**حوزه فعالیت:** {row['حوزه فعالیت']} | **شهر:** {row['شهر']}")
        with col2:
            st.success(f"**امتیاز غرفه:** {row['امتیاز']} از 5")
            
        c_btn1, c_btn2 = st.columns(2)
        with c_btn1:
            st.markdown(f'<a href="{basalam_chat_url}" target="_blank"><button style="width:100%;background-color:#FF5A5F;color:white;padding:12px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">💬 باز کردن مستقیم دایرکت (گفت‌وگو)</button></a>', unsafe_allow_html=True)
        with c_btn2:
            st.markdown(f'<a href="{basalam_profile_url}" target="_blank"><button style="width:100%;background-color:#333333;color:white;padding:12px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">🔗 مشاهده صفحه غرفه</button></a>', unsafe_allow_html=True)
else:
    st.warning("موردی یافت نشد.")
