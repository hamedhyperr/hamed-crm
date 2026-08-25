import streamlit as st
import pandas as pd

# تنظیمات صفحه و راست‌چین کردن کامل محیط
st.set_page_config(page_title="سیستم جامع مدیریت مشتریان صنعتی حامد", layout="wide")

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

st.title("🚀 سیستم پیشرفته اتوماسیون و بازاریابی صنعتی (CRM) - شهریار و حومه")
st.markdown("مدیریت هوشمند و ارتباط مستقیم با ده‌ها واحد صنعتی، کارگاه و تراشکاری منطقه")
st.markdown("---")

# دیتابیس جامع اصناف و کارگاه‌های صنعتی شهریار و شهرک‌های صنعتی اطراف
raw_data = [
    {'شناسه': 'IND-001', 'نام کسب‌وکار': 'تراشکاری پارس 1', 'حوزه فعالیت': 'ماشین‌آلات و تراشکاری', 'منطقه صنعتی': 'شهریار - شهرک صنعتی فاز ۱', 'وضعیت': 'مشتری جدید', 'شماره همراه': '989121111001', 'تلفن ثابت': '02165111001'},
    {'شناسه': 'IND-002', 'نام کسب‌وکار': 'کارگاه صنعتی آریا 2', 'حوزه فعالیت': 'قطعات خودرو', 'منطقه صنعتی': 'صفادشت - فاز ۱', 'وضعیت': 'تماس گرفته شد', 'شماره همراه': '989121111002', 'تلفن ثابت': '02165111002'},
    {'شناسه': 'IND-003', 'نام کسب‌وکار': 'صنایع فلزی مهر 3', 'حوزه فعالیت': 'فلزات و جوشکاری', 'منطقه صنعتی': 'شمس‌آباد - بلوار اصلی', 'وضعیت': 'ارسال کاتالوگ', 'شماره همراه': '989121111003', 'تلفن ثابت': '02165111003'},
    {'شناسه': 'IND-004', 'نام کسب‌وکار': 'قالب‌سازی توسعه 4', 'حوزه فعالیت': 'قالب‌سازی و تزریق پلاستیک', 'منطقه صنعتی': 'صفادشت - فاز ۲', 'وضعیت': 'قرارداد بسته شد', 'شماره همراه': '989121111004', 'تلفن ثابت': '02165111004'},
    {'شناسه': 'IND-005', 'نام کسب‌وکار': 'تولیدی قطعات پارت 5', 'حوزه فعالیت': 'ماشین‌آلات و تراشکاری', 'منطقه صنعتی': 'شهریار - بلوار شورا', 'وضعیت': 'در انتظار پاسخ', 'شماره همراه': '989121111005', 'تلفن ثابت': '02165111005'},
    {'شناسه': 'IND-006', 'نام کسب‌وکار': 'ماشین‌سازی پویان 6', 'حوزه فعالیت': 'خدمات برش و لیزر', 'منطقه صنعتی': 'شمس‌آباد - نبش صنعت', 'وضعیت': 'پیگیری بعدی', 'شماره همراه': '989121111006', 'تلفن ثابت': '02165111006'},
    {'شناسه': 'IND-007', 'نام کسب‌وکار': 'ریخته‌گری اصفهانی 7', 'حوزه فعالیت': 'ریخته‌گری و مدل‌سازی', 'منطقه صنعتی': 'صفادشت - فاز ۳', 'وضعیت': 'مشتری جدید', 'شماره همراه': '989121111007', 'تلفن ثابت': '02165111007'},
    {'شناسه': 'IND-008', 'نام کسب‌وکار': 'خدمات CNC تهران‌پارت 8', 'حوزه فعالیت': 'ماشین‌آلات و تراشکاری', 'منطقه صنعتی': 'شهریار - میدان نماز', 'وضعیت': 'تماس گرفته شد', 'شماره همراه': '989121111008', 'تلفن ثابت': '02165111008'},
    {'شناسه': 'IND-009', 'نام کسب‌وکار': 'برش لیزر البرز 9', 'حوزه فعالیت': 'خدمات برش و لیزر', 'منطقه صنعتی': 'ملارد - شهرک صنعتی', 'وضعیت': 'ارسال کاتالوگ', 'شماره همراه': '989121111009', 'تلفن ثابت': '02165111009'},
    {'شناسه': 'IND-010', 'نام کسب‌وکار': 'سازه‌های فلزی پایا 10', 'حوزه فعالیت': 'فلزات و جوشکاری', 'منطقه صنعتی': 'شهریار - شهرک صنعتی فاز ۱', 'وضعیت': 'قرارداد بسته شد', 'شماره همراه': '989121111010', 'تلفن ثابت': '02165111010'}
]

df = pd.DataFrame(raw_data)

# بخش آماری بالای صفحه
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="📊 کل واحدهای ثبت‌شده", value=len(df))
with col2:
    st.metric(label="📍 مناطق صنعتی تحت پوشش", value=df["منطقه صنعتی"].nunique())
with col3:
    st.metric(label="⚙️ حوزه‌های فعالیت", value=df["حوزه فعالیت"].nunique())
with col4:
    st.metric(label="💼 قراردادهای بسته شده", value=len(df[df["وضعیت"] == "قرارداد بسته شد"]))

st.markdown("---")

# فیلترهای پیشرفته در سایدبار
st.sidebar.header("🔍 جستجو و فیلتر پیشرفته")

search_query = st.sidebar.text_input("جستجو بر اساس نام کسب‌وکار:", "")
selected_region = st.sidebar.selectbox("فیلتر بر اساس منطقه:", ["همه مناطق"] + list(df["منطقه صنعتی"].unique()))
selected_sector = st.sidebar.selectbox("فیلتر بر اساس حوزه فعالیت:", ["همه حوزه‌ها"] + list(df["حوزه فعالیت"].unique()))
selected_status = st.sidebar.selectbox("فیلتر بر اساس وضعیت:", ["همه وضعیت‌ها"] + list(df["وضعیت"].unique()))

# اعمال فیلترها روی جدول
df_filtered = df.copy()
if search_query:
    df_filtered = df_filtered[df_filtered["نام کسب‌وکار"].str.contains(search_query, na=False)]
if selected_region != "همه مناطق":
    df_filtered = df_filtered[df_filtered["منطقه صنعتی"] == selected_region]
if selected_sector != "همه حوزه‌ها":
    df_filtered = df_filtered[df_filtered["حوزه فعالیت"] == selected_sector]
if selected_status != "همه وضعیت‌ها":
    df_filtered = df_filtered[df_filtered["وضعیت"] == selected_status]

st.subheader(f"📋 لیست واحدهای صنعتی ({len(df_filtered)} مورد یافت شد)")

# نمایش جدول تعاملی و زیبا
st.dataframe(df_filtered, use_container_width=True, height=350)

st.markdown("---")
st.subheader("💬 ارتباط و ارسال پیام مستقیم به واحدهای صنعتی")

# انتخاب واحد صنعتی از لیست فیلتر شده برای ارتباط سریع
if len(df_filtered) > 0:
    target_company = st.selectbox("انتخاب واحد صنعتی جهت برقراری ارتباط:", df_filtered["نام کسب‌وکار"].tolist())
    
    if target_company:
        row = df_filtered[df_filtered["نام کسب‌وکار"] == target_company].iloc[0]
        c1, c2, c3 = st.columns(3)
        with c1:
            st.info(f"**حوزه فعالیت:** {row['حوزه فعالیت']}")
        with c2:
            st.warning(f"**منطقه صنعتی:** {row['منطقه صنعتی']}")
        with c3:
            st.success(f"**وضعیت پیگیری:** {row['وضعیت']}")
            
        phone = row["شماره همراه"]
        tel = row["تلفن ثابت"]
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            whatsapp_url = f"https://wa.me/{phone}?text=سلام، در خصوص خدمات صنعتی و تجهیزات مدرن خدمت شما تماس می‌گیرم."
            st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="width:100%;background-color:#25D366;color:white;padding:12px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">💬 ارسال پیام واتساپ ({phone})</button></a>', unsafe_allow_html=True)
        with col_btn2:
            st.markdown(f'<a href="tel:{tel}"><button style="width:100%;background-color:#007BFF;color:white;padding:12px;border:none;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;">📞 تماس تلفنی ثابت ({tel})</button></a>', unsafe_allow_html=True)
else:
    st.warning("موردی با این مشخصات یافت نشد.")
