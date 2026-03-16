import streamlit as st
from datetime import date
import time
import random
import pandas as pd

# הגדרות דף
st.set_page_config(page_title="מערכת עידודו v4.0", page_icon="📊", layout="wide")

# --- CSS מותאם ל-RTL ועיצוב דשבורד ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');
    
    html, body, [data-testid="stSidebarNav"], .main {
        direction: rtl;
        text-align: right;
        font-family: 'Assistant', sans-serif;
        background: #f1f5f9;
    }

    /* עיצוב כרטיסיות הנתונים */
    [data-testid="stMetric"] {
        background: white;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
    }

    h1, h2, h3 { color: #0284c7 !important; text-align: right; }
    
    .stMarkdown, div[data-testid="stMarkdownContainer"] p {
        text-align: right;
        direction: rtl;
    }
    
    /* עיצוב הגרפים */
    .stPlotlyChart {
        background: white;
        border-radius: 15px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- לוגיקה של נתונים ---
START_DATE = date(2026, 1, 1)
days_together = (date.today() - START_DATE).days

# נתונים לגרפים (דמה מצחיק)
miss_you_data = pd.DataFrame({
    'יום בשבוע': ['א', 'ב', 'ג', 'ד', 'ה', 'ו', 'שבת'],
    'מדד געגוע': [80, 85, 95, 100, 70, 20, 10] # יורד בסופ"ש כי נפגשים
})

time_split_data = pd.DataFrame({
    'פעילות': ['שיחות בטלפון', 'מחשבות עליך', 'עבודה/צבא', 'גיימינג/מיינקראפט'],
    'אחוז מהיום': [25, 40, 25, 10]
})

# --- תפריט צד ---
with st.sidebar:
    st.title("Mission Control 🚀")
    page = st.sidebar.selectbox("ניווט במערכת:", 
        ["דשבורד ראשי", "המספרים שלנו", "קיר זיכרונות", "כספת חסויה 🔒"])
    st.divider()
    st.write("שלום, **עידודו**")
    st.write("סטטוס: **מחובר**")

# --- דף 1: דשבורד ראשי מורחב ---
if page == "דשבורד ראשי":
    st.title("מרכז שליטה ובקרה - קשר נאנה & עידודו 📈")
    
    # שורת מדדים עליונה
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("ימים רשמיים", f"{days_together}")
    col2.metric("שנות היכרות", "8")
    col3.metric("בדיחות פרטיות", "∞")
    col4.metric("סטטוס קשר", "יציב מאוד")
    
    st.divider()
    
    # גרפים אינטראקטיביים
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("📊 מדד געגוע שבועי")
        st.line_chart(miss_you_data.set_index('יום בשבוע'))
        st.caption("שיא הגעגוע נרשם באמצע השבוע (בזמן היומיות)")

    with col_right:
        st.subheader("🍕 התפלגות מחשבות יומית")
        st.bar_chart(time_split_data.set_index('פעילות'))
        st.caption("נתונים מבוססים על ניתוח בזמן אמת של נאנה")

    st.divider()
    
    # אזור התראות
    st.subheader("🔔 התראות מערכת אחרונות")
    st.warning("התראה: רמת הסוכר בדם נמוכה - מומלץ להיפגש לדייט בקרוב.")
    st.success("דיווח: כל המערכות תקינות. רמת האהבה בשיא של כל הזמנים.")

# --- דף 2: המספרים שלנו ---
elif page == "המספרים שלנו":
    st.title("המספרים שמאחורי ה-8 שנים 🔢")
    c1, c2 = st.columns(2)
    with c1:
        st.info("כמות שעות מצטברת במיינקראפט: **יותר מדי**")
    with c2:
        st.info("כמות ויכוחים על המזגן: **0 (כי אנחנו מושלמים)**")

# --- דף 3: קיר זיכרונות ---
elif page == "קיר זיכרונות":
    st.title("ארכיון ויזואלי 📸")
    cols = st.columns(3)
    for i in range(3):
        with cols[i]:
            st.image("PHOTO.jpg", use_container_width=True, caption=f"זיכרון מתחלף {i+1}")
            time.sleep(0.1) # מניעת קפיצות

# --- דף 4: כספת חסויה (עם חידה) ---
elif page == "כספת חסויה 🔒":
    st.title("כניסה למורשים בלבד 🔒")
    password = st.text_input("הזן קוד גישה (תאריך הווידוי DD.MM):")
    
    if password == "12.12":
        st.balloons()
        st.write("### אישור גישה התקבל!")
        st.error("🚨 תזכורת: תמונות טקטי ללא התראה הן עבירה על החוק!")
        st.info("כאן המכתב הארוך שלך...")
    elif password != "":
        st.error("גישה נדחתה. הקוד שגוי.")
