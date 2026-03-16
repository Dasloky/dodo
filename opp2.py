import streamlit as st
from datetime import date
import random

# הגדרות דף
st.set_page_config(page_title="עידודו & נאנה", page_icon="💙", layout="wide")

# --- CSS מודרני (Glassmorphism + RTL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');
    
    html, body, [data-testid="stSidebarNav"], .main {
        direction: rtl;
        text-align: right;
        font-family: 'Assistant', sans-serif;
        background: #f0f9ff;
    }

    /* כרטיסיות זיכרון */
    .st-emotion-cache-1r6slb0 { /* תיקון למכולות של Streamlit */
        border-radius: 20px;
    }

    .memory-card {
        background: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(2, 132, 199, 0.1);
        border: 1px solid #e0f2fe;
        margin-bottom: 20px;
    }

    h1, h2, h3 { color: #0369a1 !important; }

    /* עיצוב כפתורים */
    .stButton>button {
        border-radius: 30px;
        background: #0284c7;
        color: white !important;
        border: none;
        padding: 10px 20px;
        transition: 0.3s;
    }
    .stButton>button:hover { background: #0369a1; }
    </style>
    """, unsafe_allow_html=True)

# --- לוגיקה ---
START_DATE = date(2026, 1, 1)
days_together = (date.today() - START_DATE).days

# --- תפריט צד ---
with st.sidebar:
    st.title("האזור של עידודו 🧭")
    page = st.radio("לאן נלך?", ["הדאשבורד שלנו", "ה-Bucket List שלנו", "מכונת זמן של תמונות", "המכתב הסודי"])
    st.divider()
    st.write("באהבה מנאנה ❤️")

# --- דף 1: דאשבורד ---
if page == "הדאשבורד שלנו":
    st.title("הנתונים של האהבה שלנו 📊")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("ימים רשמיים", f"{days_together}")
    col2.metric("שנות חברות", "8")
    col3.metric("סינכרון", "100%")
    
    st.divider()
    
    # הבדיחה הפרטית (הבטחנו להשאיר!)
    st.error("⚠️ אזהרת בטיחות של נאנה")
    st.write("**עידודו, חל איסור על תמונות טקטי עם יד מאחורי הראש בלי אזהרה מראש. תודה.**")
    
    st.divider()
    st.subheader("כמה אני אוהבת אותך היום?")
    st.pills("", ["קצת", "הרבה", "הכי בעולם", "אין לתאר"], index=3)

# --- דף 2: Bucket List (במקום ההיסטוריה) ---
elif page == "ה-Bucket List שלנו":
    st.title("התוכניות שלנו לעתיד ✈️")
    st.write("אז הכרנו 8 שנים, עכשיו הגיע הזמן לכבוש את העולם:")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### הרפתקאות")
        st.checkbox("טיול ארוך בחו\"ל (כשיהיה חופש מהיומיות)", value=False)
        st.checkbox("צניחה חופשית (או משהו פחות מפחיד)", value=False)
        st.checkbox("ללמוד לבשל משהו שהוא לא טוסט", value=True) # דוגמה למשהו שכבר קרה
        
    with col_b:
        st.write("### רגעים קטנים")
        st.checkbox("לילה שלם של מרתון סרטים בלי להירדם", value=False)
        st.checkbox("למצוא את ה'מסעדה שלנו'", value=False)
        st.checkbox("פשוט להיות אנחנו, כל יום", value=True)

# --- דף 3: מכונת זמן של תמונות ---
elif page == "מכונת זמן של תמונות":
    st.title("זיכרונות בלחיצת כפתור 📸")
    st.write("יש לנו המון תמונות... לחץ על הכפתור כדי לקבל זיכרון אקראי:")
    
    if st.button("תפתיעי אותי!"):
        # הגרלת מספר תמונה מ-1 עד 14
        random_photo_num = random.randint(1, 14)
        st.image("PHOTO.jpg", caption=f"זיכרון מספר {random_photo_num} (במציאות כאן תהיה תמונה אחרת)")
        st.balloons()
    else:
        st.info("לחץ על הכפתור למעלה כדי לראות תמונה מתוך ה-14 שלנו!")

# --- דף 4: המכתב הסודי ---
elif page == "המכתב הסודי":
    st.title("המכתב של נאנה 💌")
    
    if st.toggle("לעיני עידודו בלבד"):
        st.markdown(f"""
        <div style="background-color: white; padding: 30px; border-radius: 20px; border-right: 5px solid #0284c7; color: #1e293b;">
            <b>הודעה מנאנה:</b><br><br>
            עידודו שלי, שמונה שנים הן רק ההתחלה למה שמחכה לנו.<br>
            אני אוהבת אותך יותר מכל קוד בעולם.<br><br>
            [כאן תדביקי את המכתב הארוך שלך]
        </div>
        """, unsafe_allow_html=True)
        st.snow()
