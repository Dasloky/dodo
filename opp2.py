import streamlit as st
from datetime import date
import time
import random

# הגדרות דף
st.set_page_config(page_title="עבור עידודו ❤️", page_icon="❤️", layout="wide")

# --- ניהול State ---
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
if 'current_reason' not in st.session_state:
    st.session_state.current_reason = None
if 'last_page' not in st.session_state:
    st.session_state.last_page = "קצת עידו"
if 'balloons_fired' not in st.session_state:
    st.session_state.balloons_fired = False

TARGET_CLICKS = 2

# --- CSS מעוצב ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');
html, body, [data-testid="stAppViewContainer"] {
    direction: rtl;
    text-align: right;
    font-family: 'Assistant', sans-serif;
    background-color: #FFF9F5;
    color: #432818;
}
.cute-card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #f8ad9d;
    text-align: center;
    box-shadow: 0 4px 12px rgba(248, 173, 157, 0.15);
    margin-bottom: 20px;
}
.cute-card h3 { color: #f08080 !important; font-size: 32px; margin: 0; text-align: center !important; }
.cute-card p { font-size: 18px; margin: 10px 0 0 0; text-align: center !important; }
.heart-particle {
    position: fixed; color: #ffb5a7; font-size: 24px; pointer-events: none; z-index: 9999;
    animation: hearts-fall 3s linear forwards;
}
@keyframes hearts-fall {
    0% { top: -10%; transform: translateX(0) rotate(0deg); opacity: 1; }
    100% { top: 100%; transform: translateX(20px) rotate(360deg); opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

def trigger_hearts():
    heart_html = "".join([f'<div class="heart-particle" style="left:{random.randint(0, 95)}%; animation-delay:{random.uniform(0, 2)}s;">❤️</div>' for _ in range(20)])
    st.markdown(heart_html, unsafe_allow_html=True)

START_DATE = date(2026, 1, 1) 
days_together = (date.today() - START_DATE).days

st.write("### אתר ממש ממש מגניב")
current_page = st.selectbox("לאן נטייל?", ["קצת עידו", "יש לי להגיד לך משהו"], key="nav_bar")

if current_page != st.session_state.last_page:
    st.session_state.clicks = 0
    st.session_state.current_reason = None
    st.session_state.balloons_fired = False
    st.session_state.last_page = current_page
    st.rerun()

st.divider()

if current_page == "קצת עידו":
    st.title("📸")
    TOTAL_PHOTOS = 27
    photo_list = list(range(1, TOTAL_PHOTOS + 1))
    random.shuffle(photo_list)
    placeholder = st.empty()
    for num in photo_list:
        with placeholder.container():
            img_path = f"Image_{num}.jpg"
            try:
                st.image(img_path, use_container_width=True)
                st.markdown(f"<p style='text-align:right; color:#f08080;'>#{num}</p>", unsafe_allow_html=True)
            except: st.info(f"טוען #{num}...")
        time.sleep(4)
    st.rerun()

else:
    if not st.session_state.balloons_fired:
        st.balloons()
        st.session_state.balloons_fired = True
        
    st.title("כל מיני דברים חמודים")
    insult_count = 22 if st.session_state.clicks >= TARGET_CLICKS else 21

    c1, c2, c3 = st.columns(3)
    c1.markdown(f'<div class="cute-card"><h3>{max(0, days_together)}</h3><p>ימים ביחד</p></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="cute-card"><h3>{insult_count}</h3><p>הודעות חצופות</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="cute-card"><h3>∞</h3><p>מחשבות עליך</p></div>', unsafe_allow_html=True)
    
    st.divider()
    if st.button("כדי שתדע את מקומך קצת יותר טוב ✨"):
        reasons = ["בגלל החיוך", "בגלל שאתה יודע מה להגיד", "בגלל 8 שנים של חברות", "בגלל שאתה פשוט אתה"]
        st.session_state.current_reason = random.choice(reasons)
        trigger_hearts()
    
    if st.session_state.current_reason:
        st.markdown(f'<div class="cute-card"><h3>💖</h3><p>{st.session_state.current_reason}</p></div>', unsafe_allow_html=True)

    st.divider()
    st.subheader("תשיג את ההודעה 🔒")
    
    if st.session_state.clicks < TARGET_CLICKS:
        st.progress(st.session_state.clicks / TARGET_CLICKS)
        if st.button("חיבוקי ❤️"):
            st.session_state.clicks += 1
            st.rerun()
    else:
        st.success("טוב קבל אותה ❤️")
        trigger_hearts()
        
        # המכתב - שים לב לסגירה בסוף!
        letter_html = """
        <div style="background: white; padding: 30px; border-radius: 20px; border: 2px dashed #f08080; text-align: right; line-height: 1.8; direction: rtl; color: #333; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <div style="text-align: center; margin-bottom: 20px;">
                <span style="font-size: 30px;">🎂</span>
                <h2 style="color: #f08080; margin: 10px 0;">מזל טוב לעידודו שלי!</h2>
            </div>
            <p><b>לעידודו הלוחם שלא בלבנון 🪖🔥,</b></p>
            <p>אם אתה חושב שבגלל שזה היום הולדת שלך 🎂 אז אני ארחם עליך בהודעה הזאת?!?! אז אתה לגמרי צודק😘 כאילו לפחות חלקית😝</p>
            <p>כשאני עבדתי על המתנת יום הולדת שלך חפרתי לכל בן אדם אפשרי לבדוק מה הכי כדאי לעשות לך והיו לי כמה רעיונות וחלקם היו יותר קשים למישוש עקב המצב הבטחוני במדינת ישראל 🤪🚀🗡️⚔️ וגם כשעבדתי על המתנות שלך ראשאל זרק הערה שאני משקיעה קצת יותר מידי למישהו שאני יוצאת איתו רק חודשיים ולרגע חשבתי על זה ופשוט הבנתי שבשום שניה בשבילי זה לא הרגיש יותר מידי כי אני באמת כל כך נהנת לעשות לך דברים גם אם זה יצירות או אתרים שאני לא כזה טובה בהם🥲🩵💛</p>
            <div style="background: #fff5f5; border-right: 5px solid #f08080; padding: 15px; margin: 20px 0; border-radius: 5px; font-weight: bold;">
   ברגע זה אתה עוצר מלקרוא את ההודעה ומביא לי חיבוק כי אני באמת ממש ממש ממש חולמת עליו כל הזמן שאתה לא פה🫂 
    <span style="font-size: 0.5em; font-weight: normal; display: block; margin-top: 5px; color: #666;">
        ואם לא עצרת בזמן אז תביא כבר נשיקה... 👅אבל אם כן עצרת אז לא 🤷🏻‍♀️
    </span>
</div>
            <p>אחרי החיבוק החמים הנעים שקיבלתי אני אתחיל קצת קצת קצת לרדת עליך 😝🚨 אז עידו אני חושבת שפתחת איתי איזו תחרות שנצים כי מתחילת המלחמה במקום שאני אגיד לכולם חבר שלי ❤️מסכן לוחם סובל בלבנון אני פוחדת עליו🥶  אתה כל יום דופק שנצים🤨</p>
            <p>באמת אני אתחיל איתך תחרות מי עושה יותר שנצים במהלך היום😴 מדבר שאני לוקחת השיחות שלנו כמובן מאליו ועושה 20 דברים בו זמנית בהם אבל האדון שמדבר פה מתחיל לפתוח לי יוטיוב בזמן השיחה וגם לעשות דברים אחרים🧐 וואלה מתלונן אבל בעצמך עושה את אותו הדבר🫤 </p>
			<p>באמת ולא רק זה תמיד מתלונן לי שאני לא נותנת לו לדבר אבל ברגע שאני מחליטה לשתוק ומחזיקה את עצמי הכי חזק שיש צוחקת ונחנקת ממים כדי לא להשמיע קול ועל זה אתה גם מתלונן פתאום לא כיף לך באמת שום דבר שאני עושה לא מתאים לך 🫩 איזו אישה💅  </p>
            <hr style="border: 0; border-top: 1px dotted #f08080; margin: 25px 0;">
            <p>אז <b>דיווה שלי 👩🏼‍🎤 חיים שלי❤️ נשמה שלי 🌬️ </b> אתה אחד הדברים הטובים ביותר שקרו לי וכנראה באמת הצלתי איזה 10 קיסרים בחיים הקודמים שלי כדי לזכות בך כי עם חבר כזה הייתי מצילה גם בחיים האלה 10 קיסרים אם אקבל אותך בחיים הבאים שלי🥇🎎</p>
			<p>אני אוהבת אותך ממש ממש ממש ופיתחת אצלי רגשות שלא ידעתי שקיימים ממש הפשרת את הלב קרח שלי ❄️💙 </p>
<p>אני מתגעגעת אליך כל הזמן שאתה רחוק ורק רוצה שתהיה קרוב , אז בשביל להתמודד עם צער שכזה אני אצטרך להשתמש בנשקים ממש מסוכנים שזה שיחות וידיאו🤭</p>
<p>ואם אפילו צריך אני אבלגן את השיער שלי כדי להשאיר אותך עוד ❤️ מה אני אעשה מידי פעם אני פשוט מרושעת אבל אתה אמרת בעצמך אתה רוצה להציק למי שאתה אוהב 🤪📈 </p>
            <p style="font-size: 1.2em; font-weight: bold; color: #f08080; text-align: center;">אוהבת אותך הכי בעולם, זקן שלי 👴🏻</p>
            <div style="margin-top: 30px; border-top: 1px solid #eee; padding-top: 15px; font-size: 0.9em;">
                <b>מנסטיה טטרוצ׳יק 🎈</b><br>
                חברה של עידו המאגניב / הזאת שמשתמשת בקלפים מלוכלכים 💌<br>
                <i>תגיד בקול רם: "אני מלפפון ממש ירוק" 🥒</i><br>
                <b>ואני הולכת לקפוץ עליך ברגע זה!</b>
            </div>
        </div>
        """
        st.markdown(letter_html, unsafe_allow_html=True)
        
        if st.button("לנעול מחדש 🔐"):
            st.session_state.clicks = 0
            st.rerun()
