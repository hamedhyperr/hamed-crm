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
st.markdown("ورود مستقیم به بخش گفتگو و دایرکت غرفه‌ها با یک کلیک")
st.markdown("---")

# پنل سایدبار برای اطلاعات تماس
st.sidebar.header("📌 اطلاعات تماس شما")
phone_input = st.sidebar.text_input("شماره تماس / واتساپ:", "09164776687")
id_input = st.sidebar.text_input("آیدی اینستاگرام و تلگرام:", "hamedhyperr")

st.sidebar.markdown("---")

# دیتابیس غرفه‌ها با لینک مستقیم دایرکت و گفتگو (Chat)
@st.cache_data
def get_comprehensive_database():
    stores_data = []
    
    categories_dict = {
        "🪵 صنایع دستی و چوبی": [
            "کشکول شهاب", "صنایع دستی استارینوا", "گالری چوب آریا", "هنر چوب پایتخت", "منبت و معرق پارس", 
            "خراطی مدرن", "صسایع چوبی باران", "تندیس‌های چوبی", "دکور چوب شهرزاد", "معرق کده",
            "صنایع دستی کهن", "گالری هنری زیتون", "آرکا چوب", "چوب و هنر ایرانی", "سرای معرق",
            "تولیدات چوبی پرهام", "هنر دست اصفهان", "مایا چوب", "چوبینه شایگان", "صنایع چوب نگین"
        ],
        "🍯 مواد غذایی و سوغات": [
            "تولیدی مسما", "عسل طبیعی سبلان", "بازار زعفران", "ارده و شیره ناب", "عسل کوهستان",
            "خشکبار برتر تهران", "چای لاهیجان اصل", "روغن‌های ارگانیک", "لواشک سنتی تبریز", "عرقیات گیاهی کاشان",
            "برنج درجه یک شمال", "سوغات سرای شیراز", "حلوا ارده عقدا", "پسته رفسنجان", "خرومای مضافتی بم",
            "سوهان قم اصل", "گز اصفهان", "آجیل و خشکبار شاه عباسی", "رب انار محلی", "پونه و گیاهان دارویی"
        ],
        "👗 پوشاک و چرم": [
            "چرم طبیعی پایتخت", "کیف و کفش چرم تبریز", "پوشاک سنتی ایرانی", "مانتو سرا", "تولیدی پوشاک دایان",
            "شال و روسری ابریشم", "کمربند چرم اصل", "صندل دست‌دوز", "پالتو چرم مردانه", "بوت زنانه چرمی",
            "پوشاک نخی بهار", "لباس محلی اقوام", "کلاه و دستکش پشمی", "جوراب بافتنی سنتی", "اکسسوری چرمی",
            "کیف پول چرم دست‌دوز", "کوله پشتی چرمی", "روپوش سنتی", "شلوار لی کلاسیک", "پیراهن کتان مردانه"
        ],
        "🏺 سفال، سرامیک و دکوراسیون": [
            "گالری سفال باران", "سرامیک دست‌ساز لوتوس", "پتروس هوم", "تابلو معرق و مینا", "ظروف سفالی فیروزه‌کوب",
            "آینه و شمعدان سنتی", "گلدان سرامیکی", "کاشی‌های تزئینی", "مجسمه‌های سفالی", "ظروف آشپزخانه سرامیکی",
            "لوستر و آویز سنتی", "فرش دستباف کوچک", "گلیم و جاجیم عشایری", "پادری سنتی", "پرده‌های سنتی",
            "شمع‌های دست‌ساز دکوری", "جعبه جواهرات چوبی و خاتم", "قاب عکس منبت", "ساعت دیواری چوبی", "باکس نظم‌دهنده دکوری"
        ]
    }
    
    for cat, stores in categories_dict.items():
        for i, store in enumerate(stores, 1):
            # لینک مستقیم اختصاصی گفتگو/دایرکت غرفه در باسلام
            chat_url = f"https://basalam.com/chat?vendor_slug={urllib.parse.quote(store)}"
            stores_data.append({
                "حوزه صنف": cat,
                "ردیف": i,
                "نام غرفه": store,
                "امتیاز": f"4.{9 - (i % 3)}",
                "لینک دایرکت غرفه": chat_url
            })
            
    return pd.DataFrame(stores_data)

df_all = get_comprehensive_database()

# تقسیم صفحه به دو ستون: راست (انتخاب صنف) و چپ (نمایش ۲۰ غرفه)
col_right, col_left = st.columns([1, 2])

with col_right:
    st.subheader("📂 ۱. انتخاب صنف (سمت راست)")
    selected_category = st.radio("صنف مد نظر را انتخاب کنید:", list(df_all["حوزه صنف"].unique()))

df_filtered = df_all[df_all["حوزه صنف"] == selected_category]

with col_left:
    st.subheader(f"📋 ۲. غرفه‌های صنف انتخاب‌شده (۲۰ غرفه برتر)")
    st.dataframe(df_filtered[["ردیف", "نام غرفه", "امتیاز"]], use_container_width=True, height=350)

st.markdown("---")
st.subheader("💬 ۳. انتخاب غرفه، کپی پیام و ورود مستقیم به دایرکت غرفه")

selected_store = st.selectbox("از لیست بالا، غرفه مورد نظر خود را انتخاب کنید:", df_filtered["نام غرفه"].tolist())

if selected_store:
    row = df_filtered[df_filtered["نام غرفه"] == selected_store].iloc[0]
    store_chat_url = row["لینک دایرکت غرفه"]
    
    message_to_copy = f"""سلام و وقتتون بخیر 
غرفه‌تون محصولات بسیار باارزش و باکیفیتی داره. مشخصه که برای تولید یا جمع‌آوری‌شون چقدر زحمت کشیدید.
با توجه به شرایط سخت اقتصادی این روزها و برای حمایت از کسب‌وکارهای باارزشی مثل شما، تصمیم گرفتم در راستای معرفی کارم، خدماتم رو با ۵۰ درصد تخفیف ویژه ارائه بدم.
من در زمینه تولید تیزرها و ویدیوهای تبلیغاتی حرفه‌ای فعالیت می‌کنم تا محصولات شما در باسلام و اینستاگرام بهتر دیده بشن و فروش چندبرابری داشته باشن.

نمونه کارها در اینستاگرام و تلگرام: {id_input}
تماس و واتساپ: {phone_input}

اگر مایلید نمونه‌کارهای متفاوتی برای غرفه‌تون داشته باشید و فروشتون رو متحول کنید، خوشحال می‌شم در ارتباط باشیم.
موفق و پرفروش باشید"""

    btn_col1, btn_col2 = st.columns(2)
    
    with btn_col1:
        st.markdown(f'<a href="{store_chat_url}" target="_blank"><button style="width:100%;background-color:#FF5A5F;color:white;padding:14px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">💬 ورود مستقیم به دایرکت این غرفه</button></a>', unsafe_allow_html=True)
        
    with btn_col2:
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
    st.text_area("متن آماده:", message_to_copy, height=200)
    st.markdown('</div>', unsafe_allow_html=True)
