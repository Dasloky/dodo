import streamlit as st
from datetime import date
import random

# הגדרות דף
st.set_page_config(page_title="עידודו & נאנה", page_icon="💙", layout="wide")

# --- CSS מתקדם (Glassmorphism + RTL + קריאות גבוהה) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');
    
    html, body, [data-testid="stSidebarNav"], .main {
        direction: rtl;
        text-align: right;
        font-family: 'Assistant', sans-serif;
        background: linear-gradient(135deg, #eef2ff 0%, #f8fafc 100%);
    }

    /* עיצוב כרטיסיות (Cards) */
    .memory-card {
        background: rgba(255, 255, 255, 0.85);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(2, 132, 199, 0.1);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        color: #1e293b;
    }

    /* כותרות */
    h1, h2, h3 {
        color: #0369a1 !important;
        font-weight: 700;
        text-align: right;
    }

    /* כפתורים מעוגלים */
    .stButton>button {
        border-radius: 50px;
        background: linear-gradient(90deg, #0284c7 0%, #38bdf8 100%);
        color: white !important;
        border: none;
        padding: 12px 30px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(2, 132, 199, 0.3);
    }

    /* בועת צ'אט למכתבים */
    .chat-container {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }
    .chat-bubble {
        background-color: #e0f2fe;
        padding: 20px;
        border-radius: 20px 20px 0px 20px;
        margin: 10px 0;
        max-width: 90%;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        color: #0f172a;
        line-height: 1.6;
        border-right: 4px solid #0284c7;
    }

    /* יישור אלמנטים */
    div[data-testid="stVerticalBlock"] > div {
        direction: rtl;
    }
    </style>
    """, unsafe_allow_html=True)

# --- לוגיקה ונתונים ---
START_DATE = date(2026, 1, 1)
days_together = (date.today() - START_DATE).days

reasons_to_love = [
    "כי אתה יודע להצחיק אותי גם כשאני הכי עייפה בעולם",
    "כי אתה הפרמדיק הכי חתיך (במיוחד במדים)",
    "בגלל הדרך שבה אתה תמיד תומך בי",
    "כי אנחנו צוות מנצח עוד מהמגמה בתיכון",
    "כי אין עוד אחד בעולם שקורא לי נאנה כמוך"
]

# --- תפריט צד ---
with st.sidebar:
    st.title("העולם של עידודו 🧭")
    page = st.radio("לאן נטוס היום?", ["הדאשבורד שלנו", "סיפור ה-8 שנים", "הגלריה", "המכתבים הסודיים"])
    st.divider()
    st.write("באהבה מנאנה ❤️")

# --- דף 1: דאשבורד ---
if page == "הדאשבורד שלנו":
    st.title("הסטטיסטיקה של הלב 📊")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("ימים כזוג רשמי", f"{days_together}")
    col2.metric("שנות חברות", "8")
    col3.metric("רמת סינכרון", "100%")
    
    st.divider()
    
    # הבדיחה הפרטית
    st.markdown("""
    <div class="memory-card" style="border-right: 6px solid #ef4444;">
        <h4 style="color: #ef4444; margin:0;">⚠️ התראת בטיחות של נאנה</h4>
        <p>חל איסור מוחלט על שליחת תמונות 'טקטי' (ריצ'רץ' פתוח + יד מאחורי הראש) ללא הודעה מוקדמת. 
        הלב שלי לא עומד בזה!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("למה אני אוהבת אותך?")
    if st.button("לחץ לסיבה אקראית 💡"):
        st.info(random.choice(reasons_to_love))
        st.balloons()

# --- דף 2: סיפור ה-8 שנים ---
elif page == "סיפור ה-8 שנים":
    st.title("מכיתה ח' ועד היום ⏳")
    
    st.markdown("""
    <div class="memory-card">
        <h3>🎒 הילדות והחטיבה</h3>
        <p>מי היה מאמין שהחבורה ההיא בתיכון והבחירה באותה מגמה יובילו אותנו לכאן?</p>
    </div>
    <div class="memory-card">
        <h3>🎆 12.12 - רגע השינוי</h3>
        <p>מסיבת הגיוס של בן דוד. הרגע שבו הכל נאמר והלבבות נפגשו.</p>
    </div>
    <div class="memory-card">
        <h3>🥂 1.1.2026</h3>
        <p>היום שבו הפכנו רשמית לסיפור אהבה.</p>
    </div>
    """, unsafe_allow_html=True)

# --- דף 3: הגלריה ---
elif page == "הגלריה":
    st.title("זיכרונות בתמונות 📸")
    
    tab1, tab2 = st.tabs(["אנחנו יחד (11)", "עידודו (3)"])
    
    with tab1:
        cols = st.columns(2)
        for i in range(1, 12):
            with cols[i % 2]:
                st.image("PHOTO.jpg", caption=f"רגע שלנו #{i}")
                
    with tab2:
        cols_he = st.columns(3)
        for i in range(1, 4):
            with cols_he[i-1]:
                st.image("PHOTO.jpg", caption=f"עידודו החתיך #{i}")

# --- דף 4: המכתבים הסודיים ---
elif page == "המכתבים הסודיים":
    st.title("המכתב של נאנה 💌")
    st.write("משהו קטן בתגובה למילים שלך...")
    
    if st.toggle("לחץ לפתיחת המכתב"):
        st.markdown("""
        <div class="chat-container">
            <div class="chat-bubble">
                <b>נאנה כותבת:</b><br><br>
                עידודו שלי, שמונה שנים הן רק ההקדמה למה שמחכה לנו.<br>
                תודה שאתה תמיד שם, מהמגמה בתיכון ועד היום.<br>
                אני אוהבת אותך יותר ממה שאפשר לכתוב באתר (אפילו כזה שבניתי לבד).<br><br>
                [כאן תדביקי את כל הטקסט הארוך שלך]
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.snow()
