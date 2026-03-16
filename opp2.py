import streamlit as st
from datetime import date
import time
import random
import pandas as pd

# הגדרות דף
st.set_page_config(page_title="NANA & IDUDU OS", page_icon="📊", layout="wide")

# --- CSS מעצב: פלטת צבעים יוקרתית ו-RTL מושלם ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* הגדרות גוף הדף */
    html, body, [data-testid="stSidebarNav"], .main {
        direction: rtl;
        text-align: right;
        font-family: 'Assistant', sans-serif;
        background-color: #F8FAFC; /* לבן-אפור נקי */
    }

    /* עיצוב כרטיסיות המדדים */
    div[data-testid="stMetric"] {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border-bottom: 4px solid #0EA5E9; /* קו תכלת תחתון */
    }

    /* כותרות */
    h1, h2, h3 {
        color: #0F172A !important; /* כחול כהה מאוד */
        font-weight: 700;
    }

    /* עיצוב ה-Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0F172A !important;
    }
    [data-testid="stSidebar"] * {
        color: #F8FAFC !important;
    }

    /* עיצוב כללי של בלוקים */
    .stAlert {
        border-radius: 12px;
    }
    
    /* ביטול שוליים מיותרים בגרפים */
    .stPlotlyChart {
        background: white;
        border-radius: 12px;
        padding: 15px;
    }
    
    /* טקסטים מיושרים לימין */
    .stMarkdown, div[data-testid="stMarkdownContainer"] p {
        text-align: right;
        direction: rtl;
    }
    </style>
    """, unsafe_allow_html=True)

# --- לוגיקה ונתונים ---
START_DATE = date(2026, 1, 1)
days_together = (date.today() - START_DATE).days

# נתונים לגרפים אסתטיים
miss_you_df = pd.DataFrame({
    "יום": ["א'", "ב'", "ג'", "ד'", "ה'", "ו'", "ש'"],
    "רמת געגוע": [70, 85, 100, 90, 75, 20, 15]
}).set_index("יום")

activity_dist = pd.DataFrame({
    "קטגוריה": ["שיחות", "מיינקראפט", "מחשבות", "עבודה"],
    "אחוז": [30, 15, 40, 15]
}).set_index("קטגוריה")

# --- תפריט צד ---
with st.sidebar:
    st.title("MISSION CONTROL")
    st.write("---")
    page = st.radio("תפריט מערכת:", 
                    ["Dashboard", "Data Analytics", "Visual Archive", "Classified 🔒"])
    st.write("---")
    st.caption("User: Ido | Admin: Nana")

# --- דף 1: Dashboard (עיצוב אסתטי נקי) ---
if page == "Dashboard":
    st.title("סטטוס מערכת בזמן אמת 📊")
    
    # שורת מדדים בסטייל נקי
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("ימי זוגיות", days_together)
    m2.metric("שנות היכרות", "8")
    m3.metric("סטטוס סנכרון", "חיובי")
    m4.metric("מדד אושר", "MAX")

    st.write("---")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("📈 ניתוח געגוע שבועי")
        st.area_chart(miss_you_df, color="#0EA5E9") # תכלת נקי
    with col_b:
        st.subheader("📊 התפלגות משאבים")
        st.bar_chart(activity_dist, color="#1E293B") # כחול כהה מקצועי
        
    st.success("דיווח מערכת: כל המדדים בטווח התקין. מומלץ להמשיך באותה מגמה.")

# --- דף 2: Data Analytics (מורחב) ---
elif page == "Data Analytics":
    st.title("ניתוח נתונים מצטבר 💾")
    
    tab1, tab2 = st.tabs(["סטטיסטיקות", "ציר זמן"])
    
    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            st.info("**נתוני גיימינג**")
            st.write("- שעות במיינקראפט: 500+")
            st.write("- בתים משותפים: 14")
            st.write("- מקרי 'נאנה הלכה לאיבוד במערה': ∞")
        with c2:
            st.info("**נתוני שירות (יומיות)**")
            st.write("- קילומטרז' מצטבר בנסיעות: 15,400 ק\"מ")
            st.write("- שיחות טלפון בזמן המתנה לאוטובוס: 1,240")
            st.write("- כריכים שעידודו שכח בבית: 12")

    with tab2:
        st.table(pd.DataFrame({
            "שנה": ["2018", "2020", "2025", "2026"],
            "שלב": ["היכרות חטיבה", "מעבר למגמה", "הלילה ב-12.12", "תחילת הדרך"],
            "תיאור": ["חברים לספסל הלימודים", "שותפות גורל במגמה", "מסיבת גיוס ששינתה הכל", "אנחנו."]
        }))

# --- דף 3: Visual Archive (החזרת התמונות המתחלפות) ---
elif page == "Visual Archive":
    st.title("ארכיון ויזואלי 📸")
    st.write("התמונות מתחלפות אוטומטית בכל 4 שניות...")
    
    # Placeholder יחיד לתמונה כדי לשמור על גודל קבוע ואסתטי
    image_spot = st.empty()
    
    for i in range(1, 15):
        # בחירת תמונה אקראית או לפי סדר (כרגע PHOTO.jpg)
        image_spot.image("PHOTO.jpg", 
                         caption=f"קובץ זיכרון #{i} מתוך 14", 
                         use_container_width=True)
        time.sleep(4)
    
    st.button("הפעל סבב נוסף")

# --- דף 4: Classified 🔒 (החידה החדשה) ---
elif page == "Classified 🔒":
    st.title("גישה למורשים בלבד 🔒")
    st.write("אנא פתור את החידה כדי לשחרר את הצפנת המכתב:")
    
    st.markdown("""
    > **החידה:**
    > קח את מספר השנים שאנחנו מכירים (8), 
    > הכפל אותו ביום בחודש שבו הכל השתנה (הווידוי), 
    > וחסר מהתוצאה את מספר האחים שלך.
    """)
    
    # חישוב: (8 * 12) - 2 = 94 (בהנחה שיש לו 2 אחים לפי הסיכום)
    ans = st.number_input("הזן תוצאה סופית:", value=0, step=1)
    
    if ans == 94:
        st.balloons()
        st.success("אימות הצליח. פותחת קבצים...")
        
        st.error("🚨 **התראה ביטחונית:** תמונות טקטי ללא אישור מהוות עבירה חמורה. נאנה דורשת הסברים!")
        
        st.write("---")
        st.subheader("המכתב שלי ❤️")
        st.write("""
        עידודו שלי,
        אחרי 8 שנים, המילים הן רק דאטה. מה שחשוב זה מה שיש בינינו.
        אני אוהבת אותך יותר מכל קוד שאי פעם אכתוב.
        
        [כאן תדביקי את המכתב שלך]
        """)
        st.snow()
    elif ans != 0:
        st.error("קוד שגוי. נסה שוב.")
