import streamlit as st
from datetime import date
import time

# הגדרות דף
st.set_page_config(page_title="עבור עידודו ❤️", page_icon="🔒", layout="wide")

# --- CSS מתקדם: RTL מלא ועיצוב הישגים ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');
    
    html, body, [data-testid="stSidebarNav"], .main {
        direction: rtl;
        text-align: right;
        font-family: 'Assistant', sans-serif;
        background: #f8fafc;
    }

    /* עיצוב כרטיסיית הישג */
    .achievement-card {
        background: white;
        padding: 20px;
        border-radius: 20px;
        border: 2px solid #e0f2fe;
        text-align: center;
        margin-bottom: 20px;
    }

    .achievement-icon {
        font-size: 40px;
        margin-bottom: 10px;
    }

    /* עיצוב ה-Easter Egg */
    .security-alert {
        background: #fef2f2;
        border-right: 10px solid #ef4444;
        padding: 20px;
        border-radius: 10px;
        color: #991b1b;
        font-weight: bold;
        text-align: right;
    }

    h1, h2, h3 { color: #0369a1 !important; text-align: right; }
    
    /* תיקון יישור לימין לכל האפליקציה */
    .stMarkdown, .stText, div[data-testid="stMarkdownContainer"] p {
        text-align: right;
        direction: rtl;
    }
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
        ["לוח הבקרה", "חדר הישגים", "זיכרונות רצים", "גישה חסויה 🔒"])
    st.divider()
    st.write("מזהה משתמש: **נאנה** ❤️")

# --- דף 1: לוח הבקרה ---
if page == "לוח הבקרה":
    st.title("סטטוס מערכת אהבה 📊")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("זמן כזוג רשמי", f"{days_together} ימים")
    with col2:
        st.metric("ותק היכרות", "8 שנים")
    
    st.divider()
    st.subheader("מד אהבה נוכחי:")
    st.progress(100)
    st.write("מערכת הנתונים מראה שאתה עדיין הדבר הכי טוב שקרה לנאנה.")

# --- דף 2: חדר הישגים ---
elif page == "חדר הישגים":
    st.title("הישגים שפתחנו יחד 🏆")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="achievement-card"><div class="achievement-icon">🎓</div><h4>שורדי המגמה</h4><p>עברנו את התיכון באותה מגמה בלי להשתגע.</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="achievement-card"><div class="achievement-icon">👯</div><h4>מהחבורה לזוגיות</h4><p>עברנו מסטטוס חברים מהחבורה להדבר האמיתי.</p></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="achievement-card"><div class="achievement-icon">⚡</div><h4>הווידוי של 12.12</h4><p>אומץ לב במסיבת גיוס ששינה לנו את החיים.</p></div>', unsafe_allow_html=True)

# --- דף 3: זיכרונות רצים ---
elif page == "זיכרונות רצים":
    st.title("הסיפור שלנו בתמונות 📸")
    st.write("התמונות מתחלפות כאן אוטומטית...")
    
    image_placeholder = st.empty()
    
    # הצגת 14 תמונות בלולאה (שימוש ב-PHOTO.jpg כברירת מחדל)
    for i in range(1, 15):
        image_placeholder.image("PHOTO.jpg", caption=f"זיכרון {i} מתוך 14")
        time.sleep(3) # החלפה כל 3 שניות
    
    st.success("הצגת הזיכרונות הושלמה!")

# --- דף 4: גישה חסויה ---
elif page == "גישה חסויה 🔒":
    st.title("אזור מאובטח 🔒")
    
    access = st.toggle("אישור סיווג ביטחוני")
    
    if access:
        st.markdown('<div class="security-alert">🚨 התראה ביטחונית: חל איסור על תמונות טקטי בלי הודעה מוקדמת! הלב של נאנה בסכנה.</div>', unsafe_allow_html=True)
        
        st.divider()
        st.subheader("הודעה חסויה מנאנה:")
        
        # כאן את מדביקה את המכתב במקום הטקסט למטה
        st.info("""
        עידודו שלי, שמונה שנים הן רק ההתחלה.
        אני אוהבת אותך יותר ממה שכל דף אינטרנט יכול להכיל.
        תודה על מי שאתה בשבילי.
        """)
        st.snow()
