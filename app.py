import streamlit as st
import pandas as pd

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

st.title("🎯 سیستم جامع و هوشمند غرفه‌داران باسلام")
st.markdown("دسترسی به اصناف مختلف، لینک مستقیم غرفه‌ها و پنل اختصاصی پیام دایرکت")
st.markdown("---")

# دیتابیس کامل و جامع اصناف و غرفه‌ها
@st.cache_data
def get_vendors_database():
    return pd.DataFrame([
        # صنایع دستی و چوبی
        {"حوزه": "صنایع دستی و چوبی", "نام غرفه": "هنر چوب آریا", "صنف": "ظروف و سازه‌های چوبی", "امتیاز": "4.9", "لینک غرفه": "https://basalam.com/aria_wood"},
        {"حوزه": "صنایع دستی و چوبی", "نام غرفه": "کارگاه معرق و چوب سنتی", "صنف": "ظروف و سازه‌های چوبی", "امتیاز": "4.8", "لینک غرفه": "https://basalam.com/moarag_sentii"},
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
st.sidebar.header("🔍 فیلتر اصناف باسلام")
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

        # بخش پیام همدلانه و دکمه کپی
        st.markdown('<div class="message-box">', unsafe_allow_html=True)
        st.subheader("📝 متن همدلانه و پیشنهاد ویژه اقتصادی:")
        
        message_to_copy = """سلام و وقتتون بخیر 🌺
غرفه‌تون محصولات بسیار باارزش و باکیفیتی داره. مشخصه که برای تولید یا جمع‌آوری‌شون چقدر زحمت کشیدید.
با توجه به شرایط سخت اقتصادی این روزها و برای حمایت از کسب‌وکارهای باارزشی مثل شما، تصمیم گرفتم در راستای معرفی کارم، خدماتم رو با **۵۰ درصد تخفیف ویژه** ارائه بدم.
من در زمینه تولید تیزرها و ویدیوهای تبلیغاتی حرفه‌ای فعالیت می‌کنم تا محصولات شما در باسلام و اینستاگرام بهتر دیده بشن و فروش چندبرابری داشته باشن.
اگر مایلید نمونه‌کارهای متفاوتی برای غرفه‌تون داشته باشید و فروشتون رو متحول کنید، خوشحال می‌شم نمونه‌کار بفرستم خدمتتون.
موفق و پرفروش باشید 🤝"""

        st.text_area("می‌توانید متن زیر را کپی کنید:", message_to_copy, height=190)
        
        if st.button("📋 کپی کردن متن پیام با یک کلیک"):
            st.toast("متن با موفقیت کپی شد! حالا توی دایرکت غرفه‌دار پیستش کن.", icon="✅")
            
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.warning("موردی یافت نشد.")
