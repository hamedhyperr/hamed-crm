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

st.title("🎯 سیستم مستقیم استخراج غرفه‌ها و دایرکت باسلام")
st.markdown("ورود مستقیم به لیست **غرفه‌داران** (نه محصولات) در تمام حوزه‌ها برای ارسال پیشنهاد همکاری")
st.markdown("---")

# لیست لینک‌های مستقیماً مختص "غرفه‌ها" در باسلام (تب غرفه‌ها در سرچ)
database = [
    {"حوزه": "صنایع دستی و چوبی", "عنوان غرفه/صنف": "تولیدکنندگان ظروف و مصنوعات چوبی", "لینک مستقیم غرفه‌ها": "https://basalam.com/search/vendors?q=صنایع%20چوبی"},
    {"حوزه": "صنایع دستی و هنری", "عنوان غرفه/صنف": "سفال، سرامیک و دکوریجات", "لینک مستقیم غرفه‌ها": "https://basalam.com/search/vendors?q=سفال%20و%20سرامیک"},
    {"حوزه": "صنایع دستی و هنری", "عنوان غرفه/صنف": "تابلوفرش، گلیم و جاجیم", "لینک مستقیم غرفه‌ها": "https://basalam.com/search/vendors?q=فرش%20و%20گلیم"},
    {"حوزه": "صنایع دستی و هنری", "عنوان غرفه/صنف": "زیورآلات و بدلیجات دست‌ساز", "لینک مستقیم غرفه‌ها": "https://basalam.com/search/vendors?q=زیورآلات%20دستساز"},
    {"حوزه": "پوشاک و چرم", "عنوان غرفه/صنف": "کیف و کفش چرم دست‌دوز", "لینک مستقیم غرفه‌ها": "https://basalam.com/search/vendors?q=کیف%20چرم"},
    {"حوزه": "پوشاک و چرم", "عنوان غرفه/صنف": "پوشاک سنتی و محلی", "لینک مستقیم غرفه‌ها": "https://basalam.com/search/vendors?q=پوشاک%20سنتی"},
    {"حوزه": "مواد غذایی محلی", "عنوان غرفه/صنف": "تولیدکنندگان عسل طبیعی", "لینک مستقیم غرفه‌ها": "https://basalam.com/search/vendors?q=عسل%20طبیعی"},
    {"حوزه": "مواد غذایی محلی", "عنوان غرفه/صنف": "زعفران و خشکبار", "لینک مستقیم غرفه‌ها": "https://basalam.com/search/vendors?q=زعفران"},
    {"حوزه": "مواد غذایی محلی", "عنوان غرفه/صنف": "عرقیجات و گیاهان دارویی", "لینک مستقیم غرفه‌ها": "https://basalam.com/search/vendors?q=عرقیجات%20گیاهی"},
    {"حوزه": "لوازم خانه و دکوراسیون", "عنوان غرفه/صنف": "تولیدی‌های مبلمان و دکوراسیون", "لینک مستقیم غرفه‌ها": "https://basalam.com/search/vendors?q=مبلمان%20و%20دکوراسیون"},
    {"حوزه": "لوازم خانه و دکوراسیون", "عنوان غرفه/صنف": "اکسسوری، شمع و ظروف تزئینی", "لینک مستقیم غرفه‌ها": "https://basalam.com/search/vendors?q=اکسسوری%20منزل"}
]

df = pd.DataFrame(database)

# فیلتر سایدبار
st.sidebar.header("🔍 فیلتر اصناف")
selected_cat = st.sidebar.selectbox("انتخاب حوزه:", ["همه حوزه‌ها"] + list(df["حوزه"].unique()))

if selected_cat != "همه حوزه‌ها":
    df_filtered = df[df["حوزه"] == selected_cat]
else:
    df_filtered = df

st.subheader(f"📋 لیست اصناف باسلام ({len(df_filtered)} حوزه کلیدی)")
st.dataframe(df_filtered, use_container_width=True)

st.markdown("---")
st.subheader("🚀 باز کردن لیست غرفه‌داران در باسلام")

selected_row = st.selectbox("انتخاب صنف مورد نظر:", df_filtered["عنوان غرفه/صنف"].tolist())

if selected_row:
    row_data = df[df["عنوان غرفه/صنف"] == selected_row].iloc[0]
    target_link = row_data["لینک مستقیم غرفه‌ها"]
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**حوزه فعالیت:** {row_data['حوزه']}")
    with col2:
        # دکمه‌ای که مستقیماً تب غرفه‌ها را باز می‌کند
        st.markdown(f'<a href="{target_link}" target="_blank"><button style="width:100%;background-color:#FF5A5F;color:white;padding:14px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">🏪 مشاهده لیست غرفه‌داران این صنف</button></a>', unsafe_allow_html=True)

    st.markdown("### 📝 متن آماده دایرکت (برای ارسال در گفت‌وگوی غرفه):")
    
    message_text = """سلام و وقتتون بخیر 🌺
غرفه‌تون محصولات بسیار باارزش و باکیفیتی داره. مشخصه که برای تولید یا جمع‌آوری‌شون زحمت زیادی کشیدید.
من در زمینه **تولید تیزرهای تبلیغاتی سینمایی، ویدیوهای پروموشن و انیمیشن‌های معرفی محصول** فعالیت می‌کنم. محصولات باارزش شما برای اینکه در باسلام و اینستاگرام دیده‌شن و فروش چندبرابری داشته باشن، نیاز به ویدیوهای حرفه‌ای و چشم‌نواز دارن.
اگر مایلید نمونه‌کارهای متفاوتی برای غرفه‌تون داشته باشید و فروشتون رو متحول کنید، خوشحال می‌شم نمونه‌کار بفرستم خدمتتون.
موفق و پرفروش باشید 🤝"""

    st.text_area("این متن را کپی کنید و با کلیک روی دکمه «گفت‌وگو» در صفحه هر غرفه، برایشان بفرستید:", message_text, height=160)
