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

# دیتابیس اصلاح‌شده با لینک‌های جستجوی مستقیم و درست در باسلام
data = [
    {"عنوان غرفه": "صنایع چوبی و لوکس هنر چوب", "حوزه فعالیت": "صنایع دستی و چوبی", "شهر": "تهران", "امتیاز": "4.8", "لینک جستجو": "https://basalam.com/search?q=صنایع+چوبی"},
    {"عنوان غرفه": "گالری فرش و تابلوفرش دستباف", "حوزه فعالیت": "صنایع دستی و هنری", "شهر": "اصفهان", "امتیاز": "4.9", "لینک جستجو": "https://basalam.com/search?q=فرش+دستباف"},
    {"عنوان غرفه": "عسل طبیعی و ارگانیک کوهستان", "حوزه فعالیت": "مواد غذایی محلی", "شهر": "خوانسار", "امتیاز": "4.7", "لینک جستجو": "https://basalam.com/search?q=عسل+طبیعی"},
    {"عنوان غرفه": "کیف و چرم طبیعی دست‌دوز", "حوزه فعالیت": "پوشاک و چرم", "شهر": "تبریز", "امتیاز": "4.9", "لینک جستجو": "https://basalam.com/search?q=کیف+چرم"},
    {"عنوان غرفه": "سفال و سرامیک دکوراتیو دست‌ساز", "حوزه فعالیت": "صنایع دستی و هنری", "شهر": "لشکرآباد", "امتیاز": "4.6", "لینک جستجو": "https://basalam.com/search?q=سفال+و+سرامیک"},
    {"عنوان غرفه": "زعفران ممتاز و خشکبار رویال", "حوزه فعالیت": "مواد غذایی محلی", "شهر": "مشهد", "امتیاز": "5.0", "لینک جستجو": "https://basalam.com/search?q=زعفران"},
    {"عنوان غرفه": "تولیدی مبل و صنایع چوبی مدرن", "حوزه فعالیت": "دکوراسیون منزل", "شهر": "تهران", "امتیاز": "4.7", "لینک جستجو": "https://basalam.com/search?q=مبل+و+دکوراسیون"},
    {"عنوان غرفه": "پوشاک سنتی و لباس‌های محلی", "حوزه فعالیت": "پوشاک و کیف و کفش", "شهر": "شیراز", "امتیاز": "4.8", "لینک جستجو": "https://basalam.com/search?q=پوشاک+سنتی"}
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
st.dataframe(df_filtered[["عنوان غرفه", "حوزه فعالیت", "شهر", "امتیاز"]], use_container_width=True)

st.markdown("---")
st.subheader("💬 ورود مستقیم به صفحه جستجو و غرفه‌های باسلام")

if len(df_filtered) > 0:
    target_store = st.selectbox("انتخاب صنف جهت بررسی غرفه‌ها:", df_filtered["عنوان غرفه"].tolist())
    
    if target_store:
        row = df[df["عنوان غرفه"] == target_store].iloc[0]
        search_url = row["Lnk"] if "Lnk" in row else row["لینک جستجو"]
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**حوزه فعالیت:** {row['حوزه فعالیت']} | **شهر:** {row['شهر']}")
        with col2:
            st.success(f"**امتیاز میانگین صنف:** {row['امتیاز']} از 5")
            
        st.markdown(f'<a href="{search_url}" target="_blank"><button style="width:100%;background-color:#FF5A5F;color:white;padding:14px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">🚀 جستجو و مشاهده غرفه‌ها و ارسال پیام در باسلام</button></a>', unsafe_allow_html=True)
else:
    st.warning("موردی یافت نشد.")
