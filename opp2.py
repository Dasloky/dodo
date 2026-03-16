import streamlit as st
from datetime import date
import time
import random
import pandas as pd

# הגדרות דף
st.set_page_config(page_title="NANA & IDUDU OS", page_icon="📊", layout="wide")

# --- CSS מלוטש: צבעים מודרניים ו-RTL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');
    
    html, body, [data-testid="stSidebarNav"], .main {
        direction: rtl;
        text-align: right;
        font-family: 'Assistant', sans-serif;
        background: #F1F5F9; /* רקע אפור-תכלת בהיר מאוד */
    }

    /* עיצוב כרטיסיות המדדים (Metrics) */
    [data-testid="stMetric"] {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        border: 1px solid #E2E8F0;
    }
    
    /* עיצוב ה-Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0F172A;
        color: white;
    }
    [data-testid="stSidebar"] * { color: white !important; }

    /* כותרות */
    h1, h2, h3 { color: #0EA5E9 !important; font-weight: 700; }

    /* תיקון טקסט כללי */
    .stMarkdown, div[data-testid="stMarkdownContainer"] p {
        text-align: right;
        direction: rtl;
        color: #1E293B;
    }

    /* עיצוב גרפים */
    .stChart {
        background: white;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- נתונים למערכת ---
START_DATE = date(2026, 1, 1)
days_together = (date.today() - START_DATE).days

# נתונים לגרפים
miss_you_df = pd.DataFrame({
    "יום": ["א", "ב", "ג", "ד", "ה", "ו", "ש"],
    "געגוע": [85, 90, 100, 95, 75, 30, 20]
}).set_index("יום")

activity_df = pd.DataFrame({
    "פעילות": ["מיינקראפט", "שיחות", "עבודה", "שינה"],
    "שעות שבועיות": [15, 30, 45, 50]
}).set_index("פעילות")

# --- תפריט צד ---
with st.sidebar:
    st.title("מערכת שליטה 🚀")
    page = st.selectbox("בחר תצוגה:", ["דשבורד ראשי", "דאטה וסטטיסטיקה", "גלריה חיה", "כספת חסויה 🔒"])
    st.divider()
    st.write(f"משתמש: **עידודו**")
    st.write(f"גרסה: **4.2.0**")

# --- דף 1: דשבורד ראשי ---
if page == "דשבורד ראשי":
    st.title("Dashboard: Love Metrics 📈")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("ימים כזוג", days_together, "↑ 100%")
    c2.metric("שנות חברות", "8", "Original")
    c3.metric("סינכרון מוחי", "99.9%", "Stable")
    c4.metric("רמת אנרגיה", "Low", "-5% (צריך דייט)")

    st.divider()
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("📈 מגמת געגוע (שבועי)")
        st.area_chart(miss_you_df, color="#0EA5E9")
    with col_b:
        st.subheader("📊 חלוקת משאבי זמן")
        st.bar_chart(activity_df, color="#6366F1")

    st.info("💡 **הערת מערכת:** נרשמה חריגה חיובית בכמות החיוכים מאז תחילת הקשר.")

# --- דף 2: דאטה וסטטיסטיקה (הדף השני המורחב) ---
elif page == "דאטה וסטטיסטיקה":
    st.title("עמוק לתוך הנתונים 💾")
    st.write("ניתוח כמותי של 8 שנות היכרות:")
    
    # כרטיסיות נתונים מפורטות
    row1_c1, row1_c2 = st.columns(2)
    with row1_c1:
        st.subheader("🏠 נתונים לוגיסטיים")
        st.write("- **נסיעות בקו בסיס-בית:** ~520 (מבוסס על יומיות)")
        st.write("- **טוסטים שנאכלו יחד:** 142")
        st.write("- **שעות מצטברות בשיחות וידאו:** 1,200+")
        
    with row1_c2:
        st.subheader("🎮 גיימינג ומיינקראפט")
        st.write("- **בלוקים שנחצבו:** 1,000,000+")
        st.write("- **פעמים שעידודו הציל את נאנה:** ∞")
        st.write("- **בתים שנבנו ונהרסו:** 12")

    st.divider()
    st.subheader("📅 ציר זמן של אירועים קריטיים")
    st.table(pd.DataFrame({
        "אירוע": ["היכרות חטיבה", "מעבר למגמה", "מסיבת הגיוס", "החלטה רשמית"],
        "סטטוס": ["חברים", "חברים טובים", "וידוי", "אהבה"],
        "שנה": ["2018", "2020", "2025", "2026"]
    }))

# --- דף 3: גלריה חיה ---
elif page == "גלריה חיה":
    st.title("Visual Archive 📸")
    placeholder = st.empty()
    
    # גלריה של 3 תמונות בו זמנית
    for _ in range(5):
        c1, c2, c3 = st.columns(3)
        nums = random.sample(range(1, 15), 3)
        c1.image("PHOTO.jpg", caption=f"קובץ #{nums[0]}", use_container_width=True)
        c2.image("PHOTO.jpg", caption=f"קובץ #{nums[1]}", use_container_width=True)
        c3.image("PHOTO.jpg", caption=f"קובץ #{nums[2]}", use_container_width=True)
        time.sleep(4)

# --- דף 4: כספת חסויה (החידה החדשה) ---
elif page == "כספת חסויה 🔒":
    st.title("כניסה לאזור מוצפן 🔒")
    
    st.subheader("חידת פתיחה (Security Challenge):")
    st.write("""
    כדי לקבל גישה למכתב, עליך לפתור את המשוואה הבאה:
    **כמות השנים שאנחנו מכירים** כפול **היום בחודש שבו הכל השתנה (הווידוי)**.
    """)
    
    # רמז: 8 שנים * 12 (היום של ה-12.12) = 96
    user_input = st.number_input("הכנס את התוצאה המספרית:", step=1, value=0)
    
    if user_input == 96:
        st.success("✅ אימות הצליח. פותחת קבצים חסויים...")
        st.balloons()
        
        # ה-Easter Egg
        st.error("🚨 **התראה:** זוהתה חריגה בנהלי 'לבוש טקטי'. נאנה דורשת סגירת ריצ'רץ' מיידית!")
        
        st.divider()
        st.subheader("מכתב מנאנה ❤️")
        st.info("""
        עידודו שלי,
        אין גרף בעולם שיכול לתאר כמה אני אוהבת אותך. 
        אחרי 8 שנים, כל נתון רק מוכיח שאתה הבחירה הכי טובה שעשיתי.
        [כאן תדביקי את המכתב שלך]
        """)
        st.snow()
    elif user_input != 0:
        st.error("❌ טעות בחישוב. נסה שוב, דאטה-בוי.")
