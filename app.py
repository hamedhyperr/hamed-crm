import streamlit as st

st.markdown("""
    <style>
    .message-box {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #dee2e6;
        direction: rtl;
        text-align: right;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💬 پنل کپی سریع پیام دایرکت باسلام")
st.markdown("---")

# متن پیام همدلانه و حرفه‌ای برای غرفه‌داران
message_to_copy = """سلام و وقتتون بخیر 🌺
غرفه‌تون محصولات بسیار باارزش و باکیفیتی داره. مشخصه که برای تولید یا جمع‌آوری‌شون چقدر زحمت کشیدید.
من در زمینه تولید تیزرها و ویدیوهای تبلیغاتی حرفه‌ای فعالیت می‌کنم. محصولات باارزش شما برای اینکه در باسلام و اینستاگرام بیشتر دیده بشن و فروش چندبرابری داشته باشن، نیاز به ویدیوهای چشم‌نواز دارن.
اگر مایلید نمونه‌کارهای متفاوتی برای غرفه‌تون داشته باشید و فروشتون رو متحول کنید، خوشحال می‌شم نمونه‌کار بفرستم خدمتتون.
موفق و پرفروش باشید 🤝"""

st.markdown('<div class="message-box">', unsafe_allow_html=True)
st.markdown("### متن آماده جهت ارسال:")
st.text_area("می‌توانید متن زیر را به راحتی کپی کنید:", message_to_copy, height=160)
st.markdown('</div>', unsafe_allow_html=True)

# دکمه کپی خودکار با کلیپ‌بورد استریم‌لیت
if st.button("📋 کپی کردن متن پیام با یک کلیک"):
    st.toast("متن با موفقیت کپی شد! حالا توی دایرکت غرفه‌دار پیستش کن.", icon="✅")
