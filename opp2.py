import streamlit as st
from datetime import date
import time

# הגדרות דף - חובה שיהיה בראש הקוד
st.set_page_config(page_title="עבור עידודו ❤️", page_icon="🔒", layout="wide")

# --- CSS מתקדם: RTL מלא, עיצוב "כרטיסיות הישגים" ואנימציות ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');
    
    html, body, [data-testid="stSidebarNav"], .main {
        direction: rtl;
        text-align: right;
        font-family: 'Assistant', sans-serif;
        background: #f8fafc;
    }

    /* עיצוב כרטיסיית הישג (Achievement) */
    .achievement-card {
        background: white;
        padding: 20px;
        border-radius: 20px;
        border: 2px solid #e0f2fe;
        text-align: center;
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    .achievement-card:hover {
        transform: scale(1.05);
        border-color: #0284c7;
    }

    .achievement-icon {
        font-size: 40px;
        margin-bottom: 10px;
    }

    /* עיצוב ה-Easter Egg (התראה ביטחונית) */
    .security-alert {
        background: #fef2f2;
        border-right: 10px solid #ef4444;
        padding: 20px;
        border-radius: 10px;
        color: #991b1b;
        font-weight: bold;
    }

    /* כותרות בכחול עידודו */
    h1, h2, h3 { color: #0369a1 !important; }

    /* יישור אלמנטים ב-Streamlit */
    div[data-testid="stVerticalBlock"] > div { direction: rtl; }
    
    /* עיצוב ה-Sidebar */
    section[data-testid="stSidebar"] { background-color: #e0f2fe; }
    </style>
    """, unsafe_allow_html=True)

# --- לוגיקה ---
START_DATE = date(2026, 1, 1)
days_together = (date.today() - START_DATE).days

# --- תפריט צד ---
with st.sidebar:
    st.title("מערכת עידודו v2.0")
    st.write(f"שלום, **עידודו** 👋")
    page = st.sidebar.selectbox("לאן תרצה לגשת?", 
        ["לוח הבקרה", "חדר הישגים (8 שנים)", "זיכרונות רצים", "גישה חסויה 🔒"])
    st.divider()
    st.write("מזהה משתמש: **נאנה** ❤️")

# --- דף 1: לוח הבקרה (Dashboard) ---
if page == "לוח הבקרה":
    st.title("סטטוס מערכת אהבה 📊")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("זמן כזוג רשמי", f"{days_together} ימים")
    with col2:
        st.metric("ותק היכרות", "8 שנים")
    
    st.divider()
    st.subheader("מד אהבה נוכחי:")
    st.progress(100, text="100% (חריגה מהגרף)")
    
    st.info("מערכת הנתונים מראה שאתה עדיין הדבר הכי טוב שקרה לנאנה.")

# --- דף 2: חדר הישגים (במקום ה-Bucket List) ---
elif page == "חדר הישגים (8 שנים)":
    st.title("הישגים שפתחנו יחד 🏆")
    st.write("8 שנים של חברות צברו לנו כמה תארים רציניים:")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""<div class="achievement-card">
            <div class="achievement-icon">🎓</div>
            <h4>שורדי המגמה</h4>
            <p>עברנו את התיכון באותה כיתה ובאותה מגמה בלי להשתגע.</p>
        </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""<div class="achievement-card">
            <div class="achievement-icon">👯</div>
            <h4>מהחבורה לזוגיות</h4>
            <p>הצלחנו לעבור מסטטוס 'חברים מהחבורה' לסטטוס 'הדבר האמיתי'.</p>
        </div>""", unsafe_allow_html=True)

    with col3:
        st.markdown("""<div
