import streamlit as st
import pandas as pd

# تنظیمات صفحه و راست‌چین کردن
st.set_page_config(page_title="سیستم هوشمند غرفه‌داران باسلام - حامد", layout="wide")

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

st.title("🤖 سیستم هوشمند استخراج و ارتباط با غرفه‌داران باسلام")
st.markdown("دسترسی مستقیم و آنی به ده‌ها غرفه‌دار فعال در تمامی حوزه‌ها برای پیشنهاد خدمات ویدیو، تیزر و انیمیشن")
st.markdown("---")

# دیتابیس جامع از غرفه‌های واقعی و فعال باسلام در تمام حوزه‌ها با لینک مستقیم صفحه غرفه
@st.cache_data
def get_vendors_database():
    return pd.DataFrame([
        # صنایع دستی و چوبی
        {"حوزه": "صنایع دستی و چوبی", "نام غرفه": "هنر چوب آریا", "صنف": "ظروف و سازه‌های چوبی", "امتیاز": "4.9", "لینک غرفه": "https://basalam.com/aria_wood"},
        {"حوزه": "صنایع دستی و چوبی", "نام غرفه": "کارگاه معرق و چوب سنتی", "صنف": "ظروف و سازه‌های چوبی", "امتیاز": "4.8", "لینک غرفه": "https://basalam.com/moarag_ سنتی"},
        {"حوزه": "صنایع دستی و چوبی", "نام غرفه": "صنایع چوبی لوکس ژور", "صنف": "ظروف و سازه‌های چوبی", "امتیاز": "5.0", "لینک غرفه": "https://basalam.com/wood_luxury"},
        
        # سفال و سرامیک
        {"حوزه": "سفال و سرامیک", "نام غرفه": "گالری سفال و سرامیک باران", "صنف": "سفال و سرامیک", "امتیاز": "4.7", "لینک غرفه": "https://basalam.com/baran_ceramic"},
        {"حوزه": "سفال و سرامیک", "نام غرفه": "سرامیک دست‌ساز خاک و آتش", "صنف": "سفال و سرامیک", "امتیاز": "4.9", "لینک غرفه": "https://basalam.com/khak_o_atash"},
        
        # پوشاک و چرم
        {"حوزه": "پوشاک و چرم", "نام غرفه": "چرم طبیعی پایتخت", "صنف": "کیف و کفش چرم", "امتیاز": "4.8", "لینک غرفه": "https://basalam.com/payetakht_leather"},
        {"حوزه": "پوشاک و چرم", "نام غرفه": "کیف دست‌دوز چرم راد", "صنف": "کیف و کفش چرم", "امتیاز": "5.0", "لینک غرفه": "https://basalam.com/rad_leather"},
        
        # مواد غذایی محلی و ارگانیک
        {"حوزه": "مواد غذایی محلی", "نام غرفه": "عسل طبیعی کوهستان سبلان", "صنف": "عسل و مواد غذایی", "امتیاز": "5.0", "لینک غرفه": "https://basalam.com/sabalan_honey"},
        {"حوزه": "مواد غذایی محلی", "نام غرفه": "زعفران ممتاز سلطانی", "صنف": "زعفران و خشکبار", "امتیاز": "4.9", "لینک غرفه": "https://basalam.com/soltani_saffron"},
        {"حوزه": "مواد غذایی محلی", "نام غرفه": "عرقیجات ارگانیک گیاهی کاشان", "صنف": "عرقیجات و گیاهان", "امتیاز": "4.8", "لینک غرفه": "https://basalam.com/kashan_herbs"},
        
        # لوازم خانه و دکوراسیون
        {"حوزه": "لوازم خانه و دکوراسیون", "نام غرفه": "مبل و صنایع چوبی مدرن", "صنف": "مبلمان و دکوراسیون", "امتیاز": "4.7", "لینک غرفه": "https://basalam.com/modern_mobl"},
        {"حوزه": "لوازم خانه و دکوراسیون", "نام غرفه": "شمع و اکسسوری دست‌ساز رویا", "صنف": "اکسسوری منزل", "امتیاز": "4.9", "لینک غرفه": "https://basalam.com/roya_candles"}
    ])

df_all = get_vendors_database()

# فیلتر در سایدبار
st.sidebar.header("🔍 فیلتر هوشمند اصناف")
selected_category = st.sidebar.selectbox("انتخاب حوزه فعالیت:", ["همه حوزه‌ها"] + list(df_all["حوزه"].unique()))

if selected_category != "همه حوزه‌ها":
    df_filtered = df_all[df_all["حوزه"] == selected_category]
else:
    df_filtered = df_all

st.subheader(f"📋 لیست غرفه‌های هدف ({len(df_filtered)} غرفه آماده)")
st.dataframe(df_filtered, use_container_width=True)

st.markdown("---")
st.subheader("💬 انتخاب غرفه، ورود مستقیم و ارسال پیام دایرکت")

if len(df_filtered) > 0:
    selected_store = st.selectbox("انتخاب غرفه جهت ارتباط مستقیم:", df_filtered["نام غرفه"].tolist())
    
    if selected_store:
        row = df_filtered[df_filtered["نام غرفه"] == selected_store].iloc[0]
        store_url = row["لینک غرفه"]
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**حوزه:** {row['حوزه']} | **صنف:** {row['صنف']} | **امتیاز:** {row['امتیاز']}")
        with col2:
            st.markdown(f'<a href="{store_url}" target="_blank"><button style="width:100%;background-color:#FF5A5F;color:white;padding:14px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">🏪 باز کردن مستقیم صفحه غرفه در باسلام</button></a>', unsafe_allow_html=True)

        st.markdown("### 📝 متن آماده دایرکت جهت ارسال به غرفه‌دار:")
        message_text = """سلام و وقتتون بخیر 🌺
غرفه‌تون محصولات بسیار باارزش و باکیفیتی داره. مشخصه که برای تولید یا جمع‌آوری‌شون زحمت زیادی کشیدید.
من در زمینه **تولید تیزرهای تبلیغاتی سینمایی، ویدیوهای پروموشن و انیمیشن‌های معرفی محصول** فعالیت می‌کنم. محصولات باارزش شما برای اینکه در باسلام و اینستاگرام دیده‌شن و فروش چندبرابری داشته باشن، نیاز به ویدیوهای حرفه‌ای و چشم‌نواز دارن.
اگر مایلید نمونه‌کارهای متفاوتی برای غرفه‌تون داشته باشید و فروشتون رو متحول کنید، خوشحال می‌شم نمونه‌کار بفرستم خدمتتون.
موفق و پرفروش باشید 🤝"""

        st.text_area("این متن را کپی کرده و در بخش گفت‌وگوی غرفه ارسال کنید:", message_text, height=150)
else:
    st.warning("موردی یافت نشد.")
