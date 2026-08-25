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

st.title("🎯 ربات جامع و هوشمند بازاریابی غرفه‌داران باسلام")
st.markdown("دسترسی به اصناف، لینک‌های مستقیم و دکمه واقعی کپی متن دایرکت")
st.markdown("---")

# پنل سایدبار برای مدیریت راه‌های ارتباطی
st.sidebar.header("📌 راه‌های ارتباطی و اطلاعات شما")
phone_num = st.sidebar.text_input("شماره تماس:", "09164776687")
whatsapp_num = st.sidebar.text_input("شماره واتساپ:", "989164776687")
telegram_id = st.sidebar.text_input("آیدی تلگرام:", "hamedhyperr")
instagram_id = st.sidebar.text_input("آیدی اینستاگرام:", "hamedhyperr")
site_link = st.sidebar.text_input("آدرس سایت:", "https://hamedhyperr.ir")
yt_link = st.sidebar.text_input("لینک یوتیوب:", "https://youtube.com/@HyperrTube")

st.sidebar.markdown("---")

# ساخت لینک‌های مستقیم و قابل کلیک
wa_url = f"https://wa.me/{whatsapp_num}"
tg_url = f"https://t.me/{telegram_id}"
ig_url = f"https://instagram.com/{instagram_id}"

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
selected_category = st.sidebar.selectbox("🔍 فیلتر اصناف باسلام بر اساس حوزه فعالیت:", ["همه حوزه‌ها"] + list(df_all["حوزه"].unique()))

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

        # بخش پیام همدلانه و دکمه واقعی کپی با جاوااسکریپت
        st.markdown('<div class="message-box">', unsafe_allow_html=True)
        st.subheader("📝 متن همدلانه و پیشنهاد ویژه اقتصادی (تخفیف ۵۰٪ همراه با نمونه‌کارها):")
        
        # متن کامل شامل لینک‌های کلیک‌پذیر و مشخص کردن نمونه‌کارها
        message_to_copy = f"""سلام و وقتتون بخیر 🌺
غرفه‌تون محصولات بسیار باارزش و باکیفیتی داره. مشخصه که برای تولید یا جمع‌آوری‌شون چقدر زحمت کشیدید.
با توجه به شرایط سخت اقتصادی این روزها و برای حمایت از کسب‌وکارهای باارزشی مثل شما، تصمیم گرفتم در راستای معرفی کارم، خدماتم رو با **۵۰ درصد تخفیف ویژه** ارائه بدم.
من در زمینه تولید تیزرها و ویدیوهای تبلیغاتی حرفه‌ای فعالیت می‌کنم تا محصولات شما در باسلام و اینستاگرام بهتر دیده بشن و فروش چندبرابری داشته باشن.

👇 اینها نمونه‌کارهای من هستند (برای مشاهده و بررسی لمس کنید):
🌐 وب‌سایت رسمی: {site_link}
🎥 نمونه‌کارها در یوتیوب: {yt_link}
📸 صفحه اینستاگرام (نمونه کار): {ig_url}

👇 برای ارتباط و هماهنگی مستقیم لمس کنید:
💬 چت در تلگرام: {tg_url}
🟢 چت در واتساپ: {wa_url}
📞 تماس تلفنی: {phone_num}

اگر مایلید نمونه‌کارهای متفاوتی برای غرفه‌تون داشته باشید و فروشتون رو متحول کنید، خوشحال می‌شم در ارتباط باشیم.
موفق و پرفروش باشید 🤝"""

        st.text_area("پیش‌نمایش متن دایرکت:", message_to_copy, height=330)
        
        # دکمه واقعی کپی با جاوااسکریپت
        safe_text = message_to_copy.replace('\n', '\\n').replace('"', '\\"')
        copy_button_html = f"""
        <button onclick="navigator.clipboard.writeText(`{safe_text}`);alert('متن با موفقیت کپی شد! حالا توی دایرکت پیستش کن.');" 
            style="width:100%;background-color:#28a745;color:white;padding:14px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;margin-top:10px;">
            📋 کپی کردن واقعی متن پیام (همراه با لینک‌های لمس‌شدنی و نمونه‌کارها)
        </button>
        """
        st.markdown(copy_button_html, unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.warning("موردی یافت نشد.")
