import streamlit as st
from datetime import date
import time
import random

# הגדרות דף
st.set_page_config(page_title="מערכת עידודו ❤️", page_icon="🔒", layout="wide")

# --- CSS מותאם ל-RTL וגלריה ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');
    
    html, body, [data-testid="stSidebarNav"], .main {
        direction: rtl;
        text-align: right;
        font-family: 'Assistant', sans-serif;
        background: #f8fafc;
    }

    /* עיצוב כרטיסיות מספרים */
    .stat-card {
        background: white;
        padding: 25px;
        border-radius: 20px;
        border-bottom: 5px solid #0284c7;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }

    h1, h2, h3 { color: #0369a1 !important; text-align: right; }
    
    .stMarkdown, div[data-testid="stMarkdownContainer"] p {
        text-align: right;
        direction: rtl;
    }

    /* עיצוב התמונות בגלריה */
    .styled-img {
        border-radius: 15px;
        object-fit: cover;
    }
    </style>
    """, unsafe_allow_html=True)

# --- לוגיקה ---
START_DATE = date(2026, 1, 1)
days_together = (date.today() - START_DATE).days

# --- תפריט צד ---
with st.sidebar:
    st.title("מערכת עידודו v3.0")
    page = st.sidebar.selectbox("לאן תרצה לגשת?", 
        ["לוח הבקרה", "המספרים שלנו", "קיר זיכרונות חי", "כספת חסויה 🔒"])
    st.divider()
    st.write("נוצר על ידי נאנה ❤️")

# --- דף 1: לוח הבקרה ---
if page == "לוח הבקרה":
    st.title("מצב המערכת 📊")
    col1, col2 = st.columns(2)
    col1.metric("זמן כזוג", f"{days_together} ימים")
    col2.metric("ותק קשר", "8 שנים")
    st.divider()
    st.info("עידודו, המערכת מדווחת על רמות גבוהות של געגוע. מומלץ לשלוח הודעה לנאנה.")

# --- דף 2: המספרים שלנו (במקום הישגים) ---
elif page == "המספרים שלנו":
    st.title("8 שנים במספרים 🔢")
    st.write("כי כדאטה אנליסטית, אני אוהבת למדוד את מה שחשוב:")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="stat-card"><h3>∞</h3><p>הודעות "בוקר טוב"</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-card"><h3>2,920</h3><p>ימים של חברות אמת</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card"><h3>1</h3><p>וידוי אחד ב-12.12</p></div>', unsafe_allow_html=True)
    
    st.write("")
    st.markdown('<div class="stat-card" style="border-bottom-color: #f472b6;"><h3>99,999+</h3><p>בדיחות פרטיות שרק שנינו מבינים</p></div>', unsafe_allow_html=True)

# --- דף 3: קיר זיכרונות חי (3 תמונות בו זמנית) ---
elif page == "קיר זיכרונות חי":
    st.title("הזיכרונות שלנו 📸")
    st.write("התמונות מתעדכנות אוטומטית...")
    
    # יצירת 3 עמודות לתמונות
    col1, col2, col3 = st.columns(3)
    placeholder1 = col1.empty()
    placeholder2 = col2.empty()
    placeholder3 = col3.empty()
    
    # לולאה שרצה (נגיד 5 פעמים להדגמה)
    for _ in range(5):
        nums = random.sample(range(1, 15), 3) # הגרלת 3 מספרים שונים מתוך 14
        
        # שימוש ב-use_container_width לשליטה בגודל
        placeholder1.image("PHOTO.jpg", caption=f"רגע {nums[0]}", use_container_width=True)
        placeholder2.image("PHOTO.jpg", caption=f"רגע {nums[1]}", use_container_width=True)
        placeholder3.image("PHOTO.jpg", caption=f"רגע {nums[2]}", use_container_width=True)
        
        time.sleep(4) # מתחלף כל 4 שניות

# --- דף 4: כספת חסויה (עם חידה) ---
elif page == "כספת חסויה 🔒":
    st.title("הכספת 🔒")
    st.write("כדי להיכנס, אתה חייב להוכיח שזה אתה.")
    
    # החידה
    st.subheader("החידה:")
    st.write("באיזה תאריך (יום וחודש) הכל השתנה, במסיבת הגיוס ההיא?")
    
    user_answer = st.text_input("הכנס את התאריך (פורמט: DD.MM)", placeholder="למשל: 01.01")
    
    if user_answer == "12.12":
        st.success("הקוד התקבל. פותחת את הכספת...")
        st.balloons()
        
        # ה-Easter Egg של הבדיחה
        st.warning("⚠️ אזהרה: נמצאה חריגה בנהלי לבוש טקטי. נאנה דורשת הסברים (ותמונות עם ריצ'רץ' סגור)!")
        
        st.divider()
        st.subheader("המכתב שלי אליך:")
        st.info("""
        עידודו שלי,
        אין מספר או קוד שיכולים לתאר מה אתה בשבילי.
        אחרי 8 שנים, אני עדיין בוחרת בך כל יום מחדש.
        אוהבת אותך,
        נאנה.
        """)
        st.snow()
    elif user_answer != "":
        st.error("קוד שגוי. נסה להיזכר במסיבת גיוס של בן דוד...")
