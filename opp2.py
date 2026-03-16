import streamlit as st
from datetime import date

# הגדרות דף
st.set_page_config(page_title="עבור עידודו ❤️", page_icon="💙", layout="centered")

# --- עיצוב CSS (מתוקן וסגור הרמטית) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;700&display=swap');
    
    html, body, [data-testid="stSidebarNav"], .main {
        direction: rtl;
        text-align: right;
        font-family: 'Assistant', sans-serif;
        background-color: #F8FAFC;
    }
    
    div[data-testid="stMarkdownContainer"] p, h1, h2, h3, h4, li, span {
        text-align: right;
        color: #1E293B !important; 
    }

    h1, h2 {
        color: #0284C7 !important;
    }

    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background-color: #0284C7;
        color: white !important;
        border: none;
        padding: 10px;
        font-weight: bold;
    }

    .easter-egg {
        background-color: #FFFFFF;
        padding: 25px;
        border-right: 6px solid #0284C7;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
        color: #1E293B;
        line-height: 1.6;
    }
    
    div[data-testid="stVerticalBlock"] > div {
        direction: rtl;
    }
    </style>
    """, unsafe_allow_html=True)

# --- לוגיקה ---
START_DATE = date(2026, 1, 1)
days_together = (date.today() - START_DATE).days

# --- תפריט צד ---
st.sidebar.title("הניווט שלנו 🧭")
menu = st.sidebar.radio("בחר דף:", ["דף הבית", "המסע שלנו (8 שנים!)", "גלריית רגעים", "הקדשה מהלב"])

if menu == "דף הבית":
    st.balloons()
    st.title(f"מזל טוב, עידודו שלי! 🎂")
    st.write("נאנה בנתה לך אתר קטן, כי הגיע הזמן.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("ימים של אהבה רשמית", f"{days_together}")
    with col2:
        st.metric("שנים של חברות", "8")
    
    st.divider()
    st.error("⚠️ אזהרת בטיחות של נאנה")
    st.write("**חובה לשלוח הודעת אזהרה מראש לפני שליחת תמונות 'טקטי'. זה מסוכן לבריאות שלי.**")
    
    st.divider()
    st.subheader("כמה אני אוהבת אותך היום?")
    option = st.pills("", ["קצת", "הרבה", "הכי בעולם", "אין לתאר"], index=3)

elif menu == "המסע שלנו (8 שנים!)":
    st.header("מכיתה ח' ועד היום... 🗺️")
    st.info("**🎒 ימי החטיבה והתיכון:** מאותה חבורה, לאותה מגמה ועד היום.")
    st.info("**🎆 12.12:** הלילה במסיבת הגיוס של בן דוד שלך ששינה הכל.")
    st.success("**🥂 1.1.2026:** הפכנו רשמית ל'אנחנו'.")

elif menu == "גלריית רגעים":
    st.header("התמונות שלנו 📸")
    tab1, tab2 = st.tabs(["אנחנו יחד", "עידודו"])
    with tab1:
        st.write("🖼️ כאן תעלי את התמונות שלכם יחד")
    with tab2:
        st.write("🌟 כאן תעלי את התמונות שלו")

elif menu == "הקדשה מהלב":
    st.header("משהו ממני אלייך 💌")
    st.write("עידודו שלי, שמונה שנים הן רק ההתחלה.")
    
    st.write("---")
    if st.toggle("נאנה, יש לי הודעה ממך?"):
        st.markdown("""
        <div class="easter-egg">
        <b>תגובה למכתב שלך:</b><br><br>
        כאן תדביקי את המכתב הארוך שלך.
        <br><br>
        <b>אוהבת אותך, נאנה.</b>
        </div>
        """, unsafe_allow_html=True)
        st.snow()
