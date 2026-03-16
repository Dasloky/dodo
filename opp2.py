import streamlit as st
import pandas as pd
from datetime import date

# הגדרות דף
st.set_page_config(page_title="מזל טוב!", page_icon="🎁", layout="wide")

# --- הזרקת CSS לטיפול בעברית (RTL) ---
st.markdown("""
    <style>
    .main {
        direction: rtl;
        text-align: right;
    }
    div[data-testid="stSidebarNav"] {
        direction: rtl;
        text-align: right;
    }
    div[data-testid="stMarkdownContainer"] p {
        text-align: right;
    }
    /* יישור כפתורים לימין */
    .stButton>button {
        float: right;
    }
    </style>
    """, unsafe_allow_index=True)

# --- פונקציות עזר ---
def calculate_days_together(start_date):
    today = date.today()
    delta = today - start_date
    return delta.days

# תאריך תחילת הקשר (שני את זה לתאריך שלכם)
anniversary = date(2022, 5, 15) 

# --- כותרת ראשית ---
st.title("🎂 יום הולדת שמח, אהוב שלי!")
st.balloons()

# --- תפריט צד ---
st.sidebar.title("הניווט שלנו")
page = st.sidebar.radio("בחר לאן לעבור:", 
    ["הבית שלנו", "סיפור האהבה שלנו (Timeline)", "גלריית רגעים", "כמה אתה מכיר אותי?", "הקדשה מהלב"])

if page == "הבית שלנו":
    st.header("ברוך הבא לממלכה הקטנה שלנו")
    
    # מדד האושר האינטראקטיבי
    st.subheader("מדד האהבה היומי")
    love_level = st.slider("כמה אני אוהבת אותך היום?", 0, 100, 100)
    if love_level > 90:
        st.success(f"נכון! {love_level}% זה המינימום!")
    
    # סטטיסטיקה של הקשר
    days = calculate_days_together(anniversary)
    col1, col2, col3 = st.columns(3)
    col1.metric("ימים יחד", f"{days}")
    col2.metric("חוויות משותפות", "אינסוף")
    col3.metric("חיוכים שגרמת לי", "מיליון +")

elif page == "סיפור האהבה שלנו (Timeline)":
    st.header("הדרך שעברנו יחד")
    
    # יצירת ציר זמן בעזרת מכולות (Containers)
    with st.container():
        st.subheader("📍 הפעם הראשונה שנפגשנו")
        st.write("זוכר את המדים, את המבוכה הקלה ואת החיוך הראשון?")
        st.divider()
        
        st.subheader("📍 הטיול הגדול הראשון")
        st.write("כשגילינו שגם כשמאבדים את הדרך, הכי כיף ללכת לאיבוד ביחד.")
        st.divider()
        
        st.subheader("📍 הרגע שידעתי...")
        st.write("זה היה ערב רגיל לגמרי, אבל פתאום הכל הרגיש נכון.")

elif page == "גלריית רגעים":
    st.header("התמונות שעושות לי חיוך")
    
    # שימוש בטאבים לתצוגה נוחה
    tab1, tab2, tab3 = st.tabs(["דייטים", "טיולים", "סתם ככה"])
    
    with tab1:
        st.write("כאן תשימי תמונות מדייטים")
        # st.image("images/date1.jpg", caption="הערב ההוא במסעדה", width=400)
    with tab2:
        st.write("כאן תשימי תמונות מטיולים")
        # st.image("images/trip.jpg", use_column_width=True)
    with tab3:
        st.write("הרגעים הקטנים של היום-יום")

elif page == "כמה אתה מכיר אותי?":
    st.header("שאלון האוהבים הגדול")
    
    q1 = st.selectbox("מה היה האוכל הראשון שבישלנו יחד?", ["פסטה שרופה", "פיצה", "סלט מושקע", "חביתה"])
    if q1 == "פסטה שרופה": # דוגמה
        st.write("✅ בול! וזה עדיין היה טעים.")
    
    q2 = st.text_input("מה המילה שאני הכי אוהבת שאתה אומר?")
    if st.button("בדוק"):
        if "אוהב" in q2:
            st.write("❤️ צדקת, אין על המילה הזו.")
        else:
            st.write("הממ... קרוב, אבל תנסה שוב.")

elif page == "הקדשה מהלב":
    st.header("הקדשה אישית")
    st.write("""
    כאן את יכולה לכתוב לו את כל המילים הכי יפות שיש. 
    כמה את גאה בו, כמה את שמחה שהוא לצידך, ואיך את מחכה לכל מה שיבוא.
    """)
    
    # כפתור שמפעיל אפקט "שלג" בסוף
    if st.button("לחץ כאן להפתעה אחרונה"):
        st.snow()
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") # סתם שיר לדוגמה
        st.write("יום הולדת שמח, אהבת חיי!")