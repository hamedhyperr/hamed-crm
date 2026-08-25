import streamlit as st
import pandas as pd
import urllib.parse

# تنظیمات صفحه و راست‌چین کردن
st.set_page_config(page_title="سیستم جامع بازاریابی غرفه‌داران فعال باسلام - حامد", layout="wide")

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

st.title("🎯 ربات جامع بازاریابی غرفه‌داران فعال باسلام")
st.markdown("پوشش **همه مشاغل و غرفه‌های فعال** با قابلیت کپی خودکار و ورود مستقیم به گفتگوی غرفه")
st.markdown("---")

# پنل سایدبار برای اطلاعات تماس
st.sidebar.header("📌 اطلاعات تماس شما")
phone_input = st.sidebar.text_input("شماره تماس / واتساپ:", "09164776687")
id_input = st.sidebar.text_input("آیدی اینستاگرام و تلگرام:", "hamedhyperr")

st.sidebar.markdown("---")

# دیتابیس جامع شامل تمامی دسته‌ها و اصناف غرفه‌های فعال باسلام
@st.cache_data
def get_all_active_vendors():
    return pd.DataFrame([
        # صنایع دستی و چوبی
        {"حوزه": "صنایع دستی و چوبی", "نام غرفه": "هنر چوب (فعال)", "صنف": "ظروف و سازه‌های چوبی", "امتیاز": "4.9", "لینک گفتگو": "https://basalam.com/wood_art/chat"},
        {"حوزه": "صنایع دستی و چوبی", "نام غرفه": "کارگاه معرق سنتی", "صنف": "معرق و منبت", "امتیاز": "4.8", "لینک گفتگو": "https://basalam.com/moarag_sentii/chat"},
        
        # سفال، سرامیک و لوکس
        {"حوزه": "سفال و سرامیک", "نام غرفه": "گالری سفال باران", "صنف": "سفال و سرامیک", "امتیاز": "4.7", "لینک گفتگو": "https://basalam.com/baran_ceramic/chat"},
        {"حوزه": "سفال و سرامیک", "نام غرفه": "خاک و آتش", "صنف": "سرامیک دست‌ساز", "امتیاز": "4.9", "لینک گفتگو": "https://basalam.com/khak_o_atash/chat"},
        
        # پوشاک، کیف و کفش
        {"حوزه": "پوشاک و چرم", "نام غرفه": "چرم طبیعی پایتخت", "صنف": "کیف و کفش چرم", "امتیاز": "4.8", "لینک گفتگو": "https://basalam.com/payetakht_leather/chat"},
        {"حوزه": "پوشاک و چرم", "نام غرفه": "تولیدی پوشاک ایرانی", "صنف": "پوشاک زنانه/مردانه", "امتیاز": "4.7", "لینک گفتگو": "https://basalam.com/poshak_irani/chat"},
        
        # مواد غذایی، عسل، زعفران و خشکبار
        {"حوزه": "مواد غذایی محلی", "نام غرفه": "عسل طبیعی سبلان", "صنف": "عسل و مواد غذایی", "امتیاز": "5.0", "لینک گفتگو": "https://basalam.com/sabalan_honey/chat"},
        {"حوزه": "مواد غذایی محلی", "نام غرفه": "بازار زعفران اصل", "صنف": "زعفران و خشکبار", "امتیاز": "4.9", "لینک گفتگو": "https://basalam.com/saffron/chat"},
        {"حوزه": "مواد غذایی محلی", "نام غرفه": "ارگانیک سرا", "صنف": "عرقیجات و گیاهان دارویی", "امتیاز": "4.8", "لینک گفتگو": "https://basalam.com/organic_sera/chat"},
        
        # لوازم خانه، دکوراسیون و مبلمان
        {"حوزه": "لوازم خانه و دکوراسیون", "نام غرفه": "صنایع چوبی و دکوری منزل", "صنف": "دکوراسیون چوبی", "امتیاز": "4.7", "لینک گفتگو": "https://basalam.com/mobl/chat"},
        {"حوزه": "لوازم خانه و دکوراسیون", "نام غرفه": "شمع و اکسسوری رویا", "صنف": "اکسسوری منزل", "امتیاز": "4.9", "لینک گفتگو": "https://basalam.com/roya_candles/chat"}
    ])

df_all = get_all_active_vendors()

# فیلتر پیشرفته بر اساس حوزه فعالیت
categories = ["همه حوزه‌ها و مشاغل"] + list(df_all["حوزه"].unique())
selected_category = st.sidebar.selectbox("🔍 فیلتر تخصصی اصناف:", categories)

if selected_category == "همه حوزه‌ها و مشاغل":
    df_filtered = df_all
else:
    df_filtered = df_all[df_all["حوزه"] == selected_category]

st.subheader(f"📋 لیست غرفه‌های فعال ({len(df_filtered)} غرفه آماده بازاریابی)")
st.dataframe(df_filtered, use_container_width=True)

st.markdown("---")
st.subheader("💬 انتخاب غرفه، کپی پیام و ورود مستقیم به چت")

if len(df_filtered) > 0:
    selected_store = st.selectbox("انتخاب غرفه مد نظر برای ارسال پیام:", df_filtered["نام غرفه"].tolist())
    
    if selected_store:
        row = df_filtered[df_filtered["نام غرفه"] == selected_store].iloc[0]
        chat_url = row["لینک گفتگو"]
        
        # متن استاندارد و تاثیرگذار پیام
        message_to_copy = f"""سلام و وقتتون بخیر 
غرفه‌تون محصولات بسیار باارزش و باکیفیتی داره. مشخصه که برای تولید یا جمع‌آوری‌شون چقدر زحمت کشیدید.
با توجه به شرایط سخت اقتصادی این روزها و برای حمایت از کسب‌وکارهای باارزشی مثل شما، تصمیم گرفتم در راستای معرفی کارم، خدماتم رو با ۵۰ درصد تخفیف ویژه ارائه بدم.
من در زمینه تولید تیزرها و ویدیوهای تبلیغاتی حرفه‌ای فعالیت می‌کنم تا محصولات شما در باسلام و اینستاگرام بهتر دیده بشن و فروش چندبرابری داشته باشن.

نمونه کارها در اینستاگرام و تلگرام: {id_input}
تماس و واتساپ: {phone_input}

اگر مایلید نمونه‌کارهای متفاوتی برای غرفه‌تون داشته باشید و فروشتون رو متحول کنید، خوشحال می‌شم در ارتباط باشیم.
موفق و پرفروش باشید"""

        col1, col2 = st.columns(2)
        
        # دکمه اول: ورود مستقیم به چت با غرفه‌دار
        with col1:
            st.markdown(f'<a href="{chat_url}" target="_blank"><button style="width:100%;background-color:#FF5A5F;color:white;padding:14px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">🚀 ۱. ورود مستقیم به گفتگوی غرفه</button></a>', unsafe_allow_html=True)
            
        # دکمه دوم: کپی خودکار متن
        with col2:
            encoded_text = urllib.parse.quote(message_to_copy)
            copy_html = f"""
            <button onclick="navigator.clipboard.writeText(decodeURIComponent(`{encoded_text}`)); alert('✅ متن با موفقیت کپی شد! حالا توی صفحه چت باسلام دکمه Ctrl+V رو بزن و ارسال کن.');" 
                style="width:100%;background-color:#28a745;color:white;padding:14px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">
                📋 ۲. کپی کردن خودکار متن پیام
            </button>
            """
            st.markdown(copy_html, unsafe_allow_html=True)

        st.markdown('<div class="message-box">', unsafe_allow_html=True)
        st.subheader("📝 پیش‌نمایش متن پیام:")
        st.text_area("می‌توانید پیش‌نمایش را بررسی کنید:", message_to_copy, height=220)
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.warning("موردی یافت نشد.")
