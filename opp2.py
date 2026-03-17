import streamlit as st
from datetime import date
import time
import random
import streamlit.components.v1 as components

# הגדרות דף
st.set_page_config(page_title="עבור עידודו ❤️", page_icon="❤️", layout="wide")

# --- פונקציה לאפקט לבבות נופלים (JavaScript) ---
def rain_hearts():
    components.html(
        """
        <div id="hearts-container" style="position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:9999;"></div>
        <script>
            function createHeart() {
                const heart = document.createElement("div");
                heart.innerHTML = "❤️";
                heart.style.position = "fixed";
                heart.style.left = Math.random() * 100 + "vw";
                heart.style.top = "-5vh";
                heart.style.fontSize = (Math.random() * 20 + 10) + "px";
                heart.style.opacity = Math.random();
                heart.style.transform = `rotate(${Math.random() * 360}deg)`;
                heart.style.transition = "top 3s linear, opacity 3s";
                
                document.getElementById("hearts-container").appendChild(heart);
                
                setTimeout(() => {
                    heart.style.top = "105vh";
                    heart.style.opacity = "0";
                }, 100);
                
                setTimeout(() => {
                    heart.remove();
                }, 3000);
            }
            for(let i=0; i<50; i++) {
                setTimeout(createHeart, i * 100);
            }
        </script>
        """,
        height=0,
    )

# --- CSS חם, נקי ומותאם למובייל ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');

:root {
    --soft-cream: #FFF9F5; 
    --warm-text: #432818;  
    --accent-pink: #ffb5a7;
    --card-bg: #ffffff;
}

html, body, .main {
    direction: rtl;
    text-align: right;
    font-family: 'Assistant', sans-serif;
    background-color: var(--soft-cream);
    color: var(--warm-text);
}

.cute-card {
    background: var(--card-bg);
    padding: 20px;
    border-radius: 20px;
    border: 1px solid #f8ad9d;
    text-align: center;
    box-shadow: 0 4px 12px rgba(248, 173, 157, 0.15);
    margin-bottom: 15px;
}

.cute-card h3 {
    color: #f08080 !important;
    margin-bottom: 5px;
    font-size: 32px;
}

.cute-card p {
    color: var(--warm-text) !important;
    font-size: 18px;
    margin: 0;
}

@media (max-width: 768px) {
    [data-testid="column"] {
        width: 100% !important;
        flex: 1 1 100% !important;
    }
}
</style>
""", unsafe_allow_html=True)

# לוגיקת תאריכים
START_DATE = date(2026, 1, 1)
days_together = (date.today() - START_DATE).days

# ניהול State
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
if 'current_reason' not in st.session_state:
    st.session_state.current_reason = None

# --- ניווט עליון ---
st.write("### היי עידודו 👋")
page = st.selectbox(
    "לאן נטייל?",
    ["קודם כל", "סיבות לחייך", "קיר זיכרונות", "הפתעה חסויה 🔒"],
    label_visibility="visible"
)
st.divider()

# --- דף 1: קודם כל ---
if page == "קודם כל":
    st.title("הפינה שלנו ❤️")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="cute-card"><h3>{days_together}</h3><p>ימים שאנחנו ביחד</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="cute-card"><h3>8</h3><p>שנים של חברות אמת</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="cute-card"><h3>∞</h3><p>כמות המחשבות שלי עליך</p></div>', unsafe_allow_html=True)
    
    st.write("---")
    st.write("כיף שאתה כאן. האתר הזה הוא רק בשבילך.")

# --- דף 2: סיבות לחייך ---
elif page == "סיבות לחייך":
    st.title("למה אתה העידודו שלי? ❤️")
    
    reasons = [
        "בגלל החיוך שגורם לי לשכוח מהכל",
        "בגלל שאתה תמיד יודע מה להגיד כשקשה",
        "בגלל הדרך שבה אתה מצחיק אותי עד דמעות",
        "בגלל 8 שנים של חברות שהיא הבית שלי",
        "בגלל שאתה פשוט... אתה.",
        "בגלל המבט הזה ששמור רק לי",
        "בגלל שאתה החבר הכי טוב שיכולתי לבקש"
    ]
    
    st.write("תלחץ על הכפתור כדי לקבל קצת אהבה:")
    if st.button("לחץ כאן למשהו קטן וטוב ✨"):
        st.session_state.current_reason = random.choice(reasons)
        rain_hearts() # הלבבות יורדים כאן!
    
    if st.session_state.current_reason:
        st.markdown(f'<div class="cute-card"><h3>💖</h3><p>{st.session_state.current_reason}</p></div>', unsafe_allow_html=True)
    else:
        st.info("מחכה ללחיצה שלך...")

# --- דף 3: קיר זיכרונות ---
elif page == "קיר זיכרונות":
    st.title("הזיכרונות שלנו 📸")
    
    TOTAL_PHOTOS = 23  
    
    if 'photo_order' not in st.session_state:
        st.session_state.photo_order = list(range(1, TOTAL_PHOTOS + 1))
        random.shuffle(st.session_state.photo_order)

    placeholder = st.empty()
    current_photo = random.choice(st.session_state.photo_order)
    img_path = f"Image_{current_photo}.jpg"
    
    with placeholder.container():
        try:
            st.image(img_path, use_container_width=True)
            st.markdown(f"<p style='text-align:center;'>רגע מתוק #{current_photo}</p>", unsafe_allow_html=True)
        except:
            st.write(f"כאן תופיע תמונה מספר {current_photo}")
    
    if st.button("תמונה אחרת? 🔄"):
        st.rerun()

# --- דף 4: הפתעה חסויה ---
elif page == "הפתעה חסויה 🔒":
    st.title("כספת הלב 🔒")
    
    target_clicks = 5 
    
    if st.session_state.clicks < target_clicks:
        st.write("כדי לפתוח את המכתב הסודי, צריך למלא את מדד האהבה.")
        
        progress = st.session_state.clicks / target_clicks
        st.progress(progress)
        
        if st.button("שלח אהבה ❤️"):
            st.session_state.clicks += 1
            if st.session_state.clicks == target_clicks:
                st.toast("הכספת נפתחת...", icon="🔓")
            st.rerun()
            
    else:
        st.success("הכספת נפתחה! ❤️")
        rain_hearts() # לבבות יורדים בפתיחה!
        
        st.divider()
        st.subheader("המכתב שלי אליך")
        st.markdown("""
        <div style="background: white; padding: 20px; border-radius: 15px; border: 1px dashed #f08080; color: #432818; line-height: 1.6;">
        עידודו שלי,<br><br>
        אחרי 8 שנים, אני פשוט רוצה להגיד תודה על מי שאתה.<br>
        תודה שאתה תמיד שם, מצחיק, מקשיב ואוהב.<br><br>
        אני אוהבת אותך המון,<br>
        נאנה
        </div>
        """, unsafe_allow_html=True)
        st.snow()
        
        if st.button("לנעול מחדש? 🔐"):
            st.session_state.clicks = 0
            st.rerun()
