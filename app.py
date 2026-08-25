import streamlit as st
import pandas as pd

# تنظیمات صفحه و راست‌چین کردن
st.set_page_config(page_title="سیستم جامع بازاریابی دایرکت باسلام - حامد", layout="wide")

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

st.title("🎯 سیستم هوشمند و امن جستجوی غرفه‌داران باسلام")
st.markdown("دسترسی سریع به ده‌ها غرفه فعال در تمامی حوزه‌ها برای پیشنهاد خدمات ویدیو و تیزر")
st.markdown("---")

# لیست کامل اصناف با لینک‌های دقیق و تست‌شده جستجوی غرفه‌ها در باسلام
database = [
    # صنایع دستی و هنری
    {"حوزه": "صنایع دستی و چوبی", "صنف": "ظروف و مصنوعات چوبی", "لینک مستقیم جستجوی غرفه‌ها": "https://basalam.com/search?q=ظروف+چوبی&et=vendor"},
    {"حوزه": "صنایع دستی و هنری", "صنف": "سفال، سرامیک و ظروف دکوری", "لینک مستقیم جستجوی غرفه‌ها": "https://basalam.com/search?q=سفال+و+سرامیک&et=vendor"},
    {"حوزه": "صنایع دستی و هنری", "صنف": "تابلوفرش، گلیم و جاجیم", "لینک مستقیم جستجوی غرفه‌ها": "https://basalam.com/search?q=فرش+و+گلیم&et=vendor"},
    {"حوزه": "صنایع دستی و هنری", "صنف": "زیورآلات و بدلیجات دست‌ساز", "لینک مستقیم جستجوی غرفه‌ها": "https://basalam.com/search?q=زیورآلات+دستساز&et=vendor"},
    
    # پوشاک و چرم
    {"حوزه": "پوشاک و چرم", "صنف": "کیف و کفش چرم دست‌دوز", "لینک مستقیم جستجوی غرفه‌ها": "https://basalam.com/search?q=کیف+چرم&et=vendor"},
    {"حوزه": "پوشاک و چرم", "صنف": "پوشاک سنتی و محلی", "لینک مستقیم جستجوی غرفه‌ها": "https://basalam.com/search?q=پوشاک+سنتی&et=vendor"},
    
    # مواد غذایی محلی
    {"حوزه": "مواد غذایی محلی", "صنف": "عسل طبیعی و ارگانیک", "لینک مستقیم جستجوی غرفه‌ها": "https://basalam.com/search?q=عسل+طبیعی&et=vendor"},
    {"حوزه": "مواد غذایی محلی", "صنف": "زعفران و خشکبار ممتاز", "لینک مستقیم جستجوی غرفه‌ها": "https://basalam.com/search?q=زعفران&et=vendor"},
    {"حوزه": "مواد غذایی محلی", "صنف": "عرقیجات و گیاهان دارویی", "لینک مستقیم جستجوی غرفه‌ها": "https://basalam.com/search?q=عرقیجات&et=vendor"},
    
    # لوازم خانه و دکوراسیون
    {"حوزه": "لوازم خانه و دکوراسیون", "صنف": "مبلمان و صنایع چوبی منزل", "لینک مستقیم جستجوی غرفه‌ها": "https://basalam.com/search?q=مبلمان&et=vendor"},
    {"حوزه": "لوازم خانه و دکوراسیون", "صنف": "اکسسوری، شمع و ظروف تزئینی", "لینک مستقیم جستجوی غرفه‌ها": "https://basalam.com/search?q=اکسسوری+منزل&et=vendor"}
]

df = pd.DataFrame(database)

# فیلتر سایدبار
st.sidebar.header("🔍 فیلتر اصناف باسلام")
selected_cat = st.sidebar.selectbox("انتخاب حوزه:", ["همه حوزه‌ها"] + list(df["حوزه"].unique()))

if selected_cat != "همه حوزه‌ها":
    df_filtered = df[df["حوزه"] == selected_cat]
else:
    df_filtered = df

st.subheader(f"📋 لیست اصناف باسلام ({len(df_filtered)} صنف کلیدی)")
st.dataframe(df_filtered, use_container_width=True)

st.markdown("---")
st.subheader("🚀 باز کردن لیست غرفه‌داران")

selected_row = st.selectbox("انتخاب صنف مورد نظر جهت ورود:", df_filtered["صنف"].tolist())

if selected_row:
    row_data = df[df["صنف"] == selected_row].iloc[0]
    target_link = row_data["لینک مستقیم جستجوی غرفه‌ها"]
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**حوزه فعالیت:** {row_data['حوزه']} \n\n **صنف:** {row_data['صنف']}")
    with col2:
        st.markdown(f'<a href="{target_link}" target="_blank"><button style="width:100%;background-color:#FF5A5F;color:white;padding:14px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">🏪 باز کردن مستقیم صفحه غرفه‌ها در باسلام</button></a>', unsafe_allow_html=True)

    st.markdown("### 📝 متن آماده دایرکت (برای ارسال در گفت‌وگوی غرفه):")
    
    message_text = """سلام و وقتتون بخیر 🌺
غرفه‌تون محصولات بسیار باارزش و باکیفیتی داره. مشخصه که برای تولید یا جمع‌آوری‌شون زحمت زیادی کشیدید.
من در زمینه **تولید تیزرهای تبلیغاتی سینمایی، ویدیوهای پروموشن و انیمیشن‌های معرفی محصول** فعالیت می‌کنم. محصولات باارزش شما برای اینکه در باسلام و اینستاگرام دیده‌شن و فروش چندبرابری داشته باشن، نیاز به ویدیوهای حرفه‌ای و چشم‌نواز دارن.
اگر مایلید نمونه‌کارهای متفاوتی برای غرفه‌تون داشته باشید و فروشتون رو متحول کنید، خوشحال می‌شم نمونه‌کار بفرستم خدمتتون.
موفق و پرفروش باشید 🤝"""

    st.text_area("این متن را کپی کنید و در دایرکت غرفه‌دار قرار دهید:", message_text, height=160)
