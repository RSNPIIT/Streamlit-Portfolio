import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. Page Configuration & Navigation State
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Ramrup Satpati | Streamlit Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

query_page = st.query_params.get('page', None)
if query_page in ['home', 'python', 'rust', 'vue']:
    st.session_state['page'] = query_page

def set_page(page_name):
    st.session_state['page'] = page_name
    if page_name == 'home':
        st.query_params.clear()
    else:
        st.query_params['page'] = page_name

# -----------------------------------------------------------------------------
# 2. Strict CSS: Hide All Streamlit Chrome & Bottom Component Styles
# -----------------------------------------------------------------------------
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Caveat:wght@600;700&family=Hind+Siliguri:wght@600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">

<style>
/* Hide Streamlit Top Chrome & Header Elements Completely */
header, [data-testid="stHeader"], #MainMenu, footer, [data-testid="stDecoration"], [data-testid="stToolbar"], [data-testid="stStatusWidget"] {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
}
[data-testid="stSidebar"], section[data-testid="stSidebar"], [data-testid="collapsedControl"] {
    display: none !important;
}

.block-container {
    padding-top: 1rem !important;
    padding-bottom: 3rem !important;
    max-width: 1280px !important;
}

:root {
    --bg-dark: #070a13;
    --card-bg: rgba(13, 19, 36, 0.88);
    --border-card: rgba(56, 189, 248, 0.28);
    --border-hover: rgba(56, 189, 248, 0.75);
    --accent-cyan: #38bdf8;
    --accent-orange: #fb923c;
    --accent-yellow: #facc15;
}

body, .stApp {
    background-color: var(--bg-dark) !important;
    color: #f8fafc !important;
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
}

/* TOP NAVBAR */
.top-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 28px;
    background: rgba(13, 19, 36, 0.8);
    backdrop-filter: blur(18px);
    border: 1px solid var(--border-card);
    border-radius: 22px;
    margin-bottom: 20px;
}
.nav-brand {
    font-size: 1.25rem;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.5px;
}
.nav-brand span {
    color: var(--accent-cyan);
}
.nav-contacts {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    align-items: center;
}
.contact-chip {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(56, 189, 248, 0.1);
    border: 1px solid rgba(56, 189, 248, 0.3);
    border-radius: 30px;
    padding: 6px 16px;
    font-size: 0.84rem;
    font-weight: 600;
    color: #38bdf8;
    text-decoration: none !important;
    transition: all 0.25s ease;
}
.contact-chip:hover {
    background: rgba(56, 189, 248, 0.25);
    border-color: #38bdf8;
    color: #ffffff;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(56, 189, 248, 0.3);
}

/* ANIMATED GIANT TECH CARDS */
.giant-card {
    background: var(--card-bg);
    border: 1px solid var(--border-card);
    border-radius: 24px;
    padding: 35px 25px;
    text-align: center;
    transition: all 0.38s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.55);
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
    animation: cardEntrance 0.8s cubic-bezier(0.16, 1, 0.3, 1) ease-out;
}
.giant-card::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(56, 189, 248, 0.15), transparent);
    transition: 0.6s;
}
.giant-card:hover::before {
    left: 100%;
}
.giant-card:hover {
    transform: translateY(-12px) scale(1.025);
    border-color: var(--border-hover);
    box-shadow: 0 28px 60px rgba(56, 189, 248, 0.45);
}

@keyframes cardEntrance {
    0% { opacity: 0; transform: translateY(30px) scale(0.95); }
    100% { opacity: 1; transform: translateY(0) scale(1); }
}

.card-icon-wrapper {
    width: 90px;
    height: 90px;
    border-radius: 22px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.12);
    transition: all 0.35s ease;
}
.giant-card:hover .card-icon-wrapper {
    transform: scale(1.15) rotate(6deg);
    background: rgba(56, 189, 248, 0.15);
    border-color: rgba(56, 189, 248, 0.5);
    box-shadow: 0 0 25px rgba(56, 189, 248, 0.4);
}

.card-icon-img {
    width: 55px;
    height: 55px;
    object-fit: contain;
}
.card-title {
    font-size: 1.8rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 10px;
}
.card-desc {
    color: #94a3b8;
    font-size: 0.95rem;
    line-height: 1.55;
    margin-bottom: 24px;
    min-height: 70px;
}

/* STREAMLIT BUTTON STYLING OVERRIDE */
.stButton > button {
    border-radius: 14px !important;
    font-weight: 800 !important;
    letter-spacing: 0.5px !important;
    transition: all 0.35s ease !important;
    border: none !important;
    background: linear-gradient(135deg, #0284c7 0%, #06b6d4 50%, #f43f5e 100%) !important;
    background-size: 200% 200% !important;
    animation: gradientShift 4s ease infinite !important;
    color: #ffffff !important;
    box-shadow: 0 4px 20px rgba(2, 132, 199, 0.4) !important;
    position: relative;
    overflow: hidden;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stButton > button:hover {
    transform: translateY(-4px) scale(1.035) !important;
    box-shadow: 0 12px 35px rgba(6, 182, 212, 0.7) !important;
}

/* FAST WORD-BY-WORD STAGGERED REVEAL ANIMATIONS */
.section-header-wrapper {
    text-align: center;
    margin-top: 15px;
    margin-bottom: 35px;
}
.stagger-words-h2 {
    font-size: 2.3rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 8px;
}
.stagger-words-h2 span {
    display: inline-block;
    opacity: 0;
    transform: translateY(22px) scale(0.85);
    filter: blur(6px);
    animation: fastWordReveal 0.28s cubic-bezier(0.2, 0.9, 0.3, 1) forwards;
}
.stagger-words-h2 span:nth-child(1) { animation-delay: 0.04s; }
.stagger-words-h2 span:nth-child(2) { animation-delay: 0.08s; }
.stagger-words-h2 span:nth-child(3) { animation-delay: 0.12s; }
.stagger-words-h2 span:nth-child(4) { animation-delay: 0.16s; }
.stagger-words-h2 span:nth-child(5) { animation-delay: 0.20s; }
.stagger-words-h2 span:nth-child(6) { animation-delay: 0.24s; }

.stagger-words-p {
    color: #94a3b8;
    font-size: 1.05rem;
}
.stagger-words-p span {
    display: inline-block;
    opacity: 0;
    transform: translateY(14px);
    filter: blur(4px);
    animation: fastWordReveal 0.22s cubic-bezier(0.2, 0.9, 0.3, 1) forwards;
}
.stagger-words-p span:nth-child(1)  { animation-delay: 0.28s; }
.stagger-words-p span:nth-child(2)  { animation-delay: 0.31s; }
.stagger-words-p span:nth-child(3)  { animation-delay: 0.34s; }
.stagger-words-p span:nth-child(4)  { animation-delay: 0.37s; }
.stagger-words-p span:nth-child(5)  { animation-delay: 0.40s; }
.stagger-words-p span:nth-child(6)  { animation-delay: 0.43s; }
.stagger-words-p span:nth-child(7)  { animation-delay: 0.46s; }
.stagger-words-p span:nth-child(8)  { animation-delay: 0.49s; }
.stagger-words-p span:nth-child(9)  { animation-delay: 0.52s; }
.stagger-words-p span:nth-child(10) { animation-delay: 0.55s; }
.stagger-words-p span:nth-child(11) { animation-delay: 0.58s; }
.stagger-words-p span:nth-child(12) { animation-delay: 0.61s; }
.stagger-words-p span:nth-child(13) { animation-delay: 0.64s; }

@keyframes fastWordReveal {
    0% {
        opacity: 0;
        transform: translateY(22px) scale(0.85);
        filter: blur(6px);
    }
    100% {
        opacity: 1;
        transform: translateY(0) scale(1);
        filter: blur(0);
    }
}

/* LANGUAGE-SPECIFIC ANIMATED BACKGROUND GLOW ENERGY FIELDS */
.giant-card > * {
    position: relative;
    z-index: 2;
}

.python-glow-card {
    position: relative;
}
.python-glow-card::after {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(56, 189, 248, 0.18) 0%, rgba(2, 132, 199, 0.05) 50%, transparent 70%);
    animation: rotateAura 12s linear infinite;
    z-index: 1;
    pointer-events: none;
}

.rust-glow-card {
    position: relative;
}
.rust-glow-card::after {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(251, 146, 60, 0.20) 0%, rgba(234, 88, 12, 0.06) 50%, transparent 70%);
    animation: rotateAura 10s linear infinite reverse;
    z-index: 1;
    pointer-events: none;
}

.vue-glow-card {
    position: relative;
}
.vue-glow-card::after {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(52, 211, 153, 0.18) 0%, rgba(16, 185, 129, 0.05) 50%, transparent 70%);
    animation: rotateAura 14s linear infinite;
    z-index: 1;
    pointer-events: none;
}

@keyframes rotateAura {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* PROJECT DETAILS PAGE STYLING */
.repo-card {
    background: var(--card-bg);
    border: 1px solid var(--border-card);
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 14px 35px rgba(0, 0, 0, 0.5);
    transition: all 0.35s ease;
    animation: cardEntrance 0.6s ease-out;
}
.repo-card:hover {
    border-color: var(--border-hover);
    transform: translateY(-5px);
    box-shadow: 0 20px 45px rgba(56, 189, 248, 0.3);
}
.badge-pill {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 700;
    margin-right: 6px;
    margin-bottom: 10px;
    text-transform: uppercase;
    transition: transform 0.2s ease;
}
.badge-pill:hover {
    transform: scale(1.08);
}
.badge-cyan { background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); }
.badge-emerald { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }
.badge-amber { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); }
.badge-rose { background: rgba(244, 63, 94, 0.15); color: #fb7185; border: 1px solid rgba(244, 63, 94, 0.4); }

.project-link {
    color: #38bdf8;
    font-weight: 700;
    text-decoration: none !important;
    transition: all 0.25s ease;
}
.project-link:hover {
    color: #34d399;
    text-shadow: 0 0 12px rgba(52, 211, 153, 0.6);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. Top Navbar
# -----------------------------------------------------------------------------
st.markdown("""
<style>
.nav-bengali-name {
    font-size: 0.95rem;
    color: #fb923c;
    font-family: 'Hind Siliguri', sans-serif;
    margin-left: 8px;
    display: inline-block;
    position: relative;
    cursor: pointer;
    text-shadow: 0 0 10px rgba(251, 146, 60, 0.9), 0 0 20px rgba(249, 115, 22, 0.7);
    transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.nav-bengali-name .nav-bn {
    display: inline-block;
    transition: opacity 0.3s ease, transform 0.3s ease;
}
.nav-bengali-name .nav-or {
    position: absolute;
    left: 0; top: 0;
    white-space: nowrap;
    opacity: 0;
    transform: scale(0.8);
    transition: opacity 0.3s ease, transform 0.3s ease;
    color: #facc15;
    text-shadow: 0 0 12px #facc15, 0 0 25px #f59e0b;
}
.nav-bengali-name:hover {
    transform: scale(1.3) translateY(-2px);
}
.nav-bengali-name:hover .nav-bn {
    opacity: 0;
    transform: scale(0.8);
}
.nav-bengali-name:hover .nav-or {
    opacity: 1;
    transform: scale(1);
}
</style>
<div class="top-nav">
    <div class="nav-brand">RAMRUP <span>SATPATI</span> <span class="nav-bengali-name"><span class="nav-bn">রামরূপ সাতপতি</span><span class="nav-or">ରାମରୂପ ସତପତି</span></span></div>
    <div class="nav-contacts">
        <a href="https://www.linkedin.com/in/ramrup-satpati-683970341" target="_blank" class="contact-chip">💼 LinkedIn</a>
        <a href="https://www.kaggle.com" target="_blank" class="contact-chip">📊 Kaggle</a>
        <a href="https://github.com/RSNPIIT" target="_blank" class="contact-chip">🐙 GitHub</a>
        <a href="mailto:ramrupsatpati@gmail.com" class="contact-chip">✉️ Email</a>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. VIEW ROUTER
# -----------------------------------------------------------------------------
current_page = st.session_state.get('page', 'home')

# -----------------------------------------------------------------------------
# PAGE 1: HOME VIEW (Ultra-Clean Sleek Badge Tag for 'a.k.a RSNPIIT')
# -----------------------------------------------------------------------------
if current_page == 'home':
    
    # Hero Component with Clean Modern Tag for 'a.k.a RSNPIIT'
    cyber_core_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Caveat:wght@600;700&family=Hind+Siliguri:wght@600;700&family=Plus+Jakarta+Sans:wght@400;700;800;900&display=swap" rel="stylesheet">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                background: #070a13;
                color: #f8fafc;
                font-family: 'Plus Jakarta Sans', sans-serif;
                overflow: hidden;
                width: 100vw;
                height: 420px;
                position: relative;
            }

            #webgl-canvas {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: 1;
            }

            .center-halo {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                width: 440px;
                height: 440px;
                background: radial-gradient(circle, rgba(56, 189, 248, 0.35) 0%, rgba(2, 132, 199, 0.14) 45%, transparent 70%);
                z-index: 2;
                pointer-events: none;
                filter: blur(18px);
            }

            .hero-layout {
                position: relative;
                z-index: 10;
                width: 100%;
                height: 100%;
                display: grid;
                grid-template-columns: 1fr 310px 1fr;
                align-items: center;
                padding: 0 45px;
            }

            .left-col {
                text-align: right;
                padding-right: 20px;
            }
            .small-tag { color: #38bdf8; font-size: 1.2rem; font-weight: 600; margin-bottom: 2px; }
            .main-name { font-size: 3.3rem; font-weight: 900; line-height: 1.05; color: #ffffff; letter-spacing: -1px; }

            /* NEON INTENSE GLOWING BENGALI -> ODIA SCRIPT MORPH */
            .bengali-name {
                font-size: 2.2rem;
                font-weight: 800;
                color: #ffedd5;
                font-family: 'Hind Siliguri', sans-serif;
                text-shadow: 0 0 10px #fb923c, 0 0 22px #f97316, 0 0 38px #ea580c, 0 0 60px rgba(234, 88, 12, 0.85);
                margin-top: 4px;
                display: inline-block;
                position: relative;
                cursor: pointer;
                transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            }
            .bengali-name .text-bn {
                display: inline-block;
                transition: opacity 0.35s ease, transform 0.35s ease;
            }
            .bengali-name .text-or {
                position: absolute;
                right: 0;
                top: 0;
                white-space: nowrap;
                opacity: 0;
                transform: scale(0.7) rotate(-3deg);
                transition: opacity 0.35s ease, transform 0.35s ease;
                color: #facc15;
                text-shadow: 0 0 12px #facc15, 0 0 25px #f59e0b, 0 0 45px #d97706, 0 0 65px rgba(217, 119, 6, 0.9);
            }

            .bengali-name.active-hover, .bengali-name:hover {
                transform: scale(1.28) translateY(-4px);
            }
            .bengali-name.active-hover .text-bn, .bengali-name:hover .text-bn {
                opacity: 0;
                transform: scale(0.7) rotate(3deg);
            }
            .bengali-name.active-hover .text-or, .bengali-name:hover .text-or {
                opacity: 1;
                transform: scale(1) rotate(0deg);
            }

            /* GLOWING BEVELED EASTER EGG BADGE FOR 'a.k.a RSNPIIT' -> 'a.k.a РСНПИИТ' */
            .aka-tag {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                background: linear-gradient(145deg, rgba(56, 189, 248, 0.20), rgba(2, 132, 199, 0.08));
                border: 1px solid rgba(56, 189, 248, 0.5);
                border-top: 1px solid rgba(255, 255, 255, 0.45);
                border-bottom: 1px solid rgba(2, 132, 199, 0.7);
                color: #94a3b8;
                font-size: 0.88rem;
                font-weight: 700;
                letter-spacing: 2px;
                text-transform: uppercase;
                padding: 6px 18px;
                border-radius: 20px;
                margin-top: 8px;
                box-shadow: 0 4px 16px rgba(56, 189, 248, 0.28), inset 0 1px 2px rgba(255, 255, 255, 0.3);
                position: relative;
                cursor: pointer;
                overflow: hidden;
                white-space: nowrap;
                transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            }

            .aka-tag .aka-bn-wrap {
                display: inline-flex;
                align-items: center;
                gap: 6px;
                opacity: 1;
                transform: translateY(0) scale(1);
                transition: opacity 0.3s ease, transform 0.3s ease;
            }
            .aka-tag .aka-bn-wrap span {
                color: #38bdf8;
                font-weight: 800;
                text-shadow: 0 0 12px rgba(56, 189, 248, 0.7);
            }

            .aka-tag .aka-or-wrap {
                display: inline-flex;
                align-items: center;
                gap: 6px;
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%) scale(0.85);
                opacity: 0;
                transition: opacity 0.3s ease, transform 0.3s ease;
            }
            .aka-tag .aka-or-wrap .cyrillic-highlight {
                color: #f43f5e;
                font-weight: 800;
                text-shadow: 0 0 12px #f43f5e, 0 0 25px #e11d48;
            }

            .aka-tag.aka-hover, .aka-tag:hover {
                transform: scale(1.09) translateY(-2px);
                border-color: #38bdf8;
                box-shadow: 0 6px 24px rgba(56, 189, 248, 0.55), 0 0 35px rgba(244, 63, 94, 0.45), inset 0 1px 3px rgba(255, 255, 255, 0.5);
            }
            .aka-tag.aka-hover .aka-bn-wrap, .aka-tag:hover .aka-bn-wrap {
                opacity: 0;
                transform: translateY(-16px) scale(0.85);
            }
            .aka-tag.aka-hover .aka-or-wrap, .aka-tag:hover .aka-or-wrap {
                opacity: 1;
                transform: translate(-50%, -50%) scale(1);
            }

            .right-col {
                text-align: left;
                padding-left: 20px;
            }
            .role-tag { color: #94a3b8; font-size: 1.2rem; font-weight: 600; margin-bottom: 2px; }
            .role-highlight { font-size: 2.5rem; font-weight: 900; line-height: 1.08; background: linear-gradient(135deg, #38bdf8, #06b6d4, #f43f5e); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }

            /* GLOWING CALLIGRAPHY SCRIPT FOR 'Jack of all Trades' -> 'সর্বকাজে দক্ষ ব্যক্তি' */
            .sub-tagline {
                font-family: 'Great Vibes', 'Caveat', cursive;
                font-size: 2.4rem;
                font-weight: 700;
                color: #facc15;
                text-transform: none;
                letter-spacing: 1px;
                margin-top: 4px;
                text-shadow: 0 0 15px rgba(250, 204, 21, 0.7), 0 0 30px rgba(245, 158, 11, 0.4);
                transform: rotate(-2deg);
                display: inline-block;
                position: relative;
                cursor: pointer;
                transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            }

            .sub-tagline .text-en {
                display: inline-block;
                transition: opacity 0.35s ease, transform 0.35s ease;
            }

            .sub-tagline .text-bn {
                position: absolute;
                left: 0;
                top: 0;
                white-space: nowrap;
                opacity: 0;
                transform: scale(0.7) rotate(-3deg);
                transition: opacity 0.35s ease, transform 0.35s ease;
                font-family: 'Hind Siliguri', sans-serif;
                color: #38bdf8;
                text-shadow: 0 0 12px #38bdf8, 0 0 25px #0284c7, 0 0 45px rgba(2, 132, 199, 0.9);
            }

            .sub-tagline.active-hover, .sub-tagline:hover {
                transform: scale(1.18) rotate(0deg) translateY(-3px);
            }

            .sub-tagline.active-hover .text-en, .sub-tagline:hover .text-en {
                opacity: 0;
                transform: scale(0.7) rotate(3deg);
            }

            .sub-tagline.active-hover .text-bn, .sub-tagline:hover .text-bn {
                opacity: 1;
                transform: scale(1) rotate(0deg);
            }
        </style>
    </head>
    <body>
        <canvas id="webgl-canvas"></canvas>
        <div class="center-halo"></div>

        <div class="hero-layout">
            <div class="left-col">
                <div class="small-tag">Hello! I'm</div>
                <div class="main-name">RAMRUP<br>SATPATI</div>
                <div class="bengali-name" id="bengaliNameBox">
                    <span class="text-bn">রামরূপ সাতপতি</span>
                    <span class="text-or">ରାମରୂପ ସତପତି</span>
                </div>
                <div>
                    <div class="aka-tag" id="akaTagBox">
                        <span class="aka-bn-wrap">a.k.a <span>RSNPIIT</span></span>
                        <span class="aka-or-wrap">a.k.a <span class="cyrillic-highlight">РСНПИИТ</span></span>
                    </div>
                </div>
            </div>
            <div></div>
            <div class="right-col">
                <div class="role-tag">A Full Stack</div>
                <div class="role-highlight">SYSTEMS & AI<br>ENGINEER</div>
                <div class="sub-tagline" id="taglineBox">
                    <span class="text-en">Jack of all Trades</span>
                    <span class="text-bn">সর্বকাজে দক্ষ ব্যক্তি</span>
                </div>
            </div>
        </div>

        <script>
            document.addEventListener('DOMContentLoaded', () => {
                const canvas = document.getElementById('webgl-canvas');
                const scene = new THREE.Scene();

                const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
                camera.position.set(0, 0, 12.8);

                const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
                renderer.setSize(window.innerWidth, window.innerHeight);
                renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

                const ambient = new THREE.AmbientLight(0x0f172a, 2.4);
                scene.add(ambient);

                const cyanLight = new THREE.PointLight(0x38bdf8, 3.5, 50);
                cyanLight.position.set(6, 6, 10);
                scene.add(cyanLight);

                const roseLight = new THREE.PointLight(0xf43f5e, 3.5, 50);
                roseLight.position.set(-6, -6, 10);
                scene.add(roseLight);

                // Cosmic Stars
                const starCount = 260;
                const starGeo = new THREE.BufferGeometry();
                const starPositions = new Float32Array(starCount * 3);

                for (let i = 0; i < starCount; i++) {
                    starPositions[i * 3] = THREE.MathUtils.randFloatSpread(35);
                    starPositions[i * 3 + 1] = THREE.MathUtils.randFloatSpread(25);
                    starPositions[i * 3 + 2] = THREE.MathUtils.randFloat(-10, 5);
                }

                starGeo.setAttribute('position', new THREE.BufferAttribute(starPositions, 3));
                const starMat = new THREE.PointsMaterial({
                    color: 0x38bdf8,
                    size: 0.12,
                    transparent: true,
                    opacity: 0.75
                });
                const starField = new THREE.Points(starGeo, starMat);
                scene.add(starField);

                // 3D Cyber Core
                const coreGroup = new THREE.Group();

                const innerGeo = new THREE.SphereGeometry(2.85, 32, 32);
                const innerMat = new THREE.MeshPhongMaterial({
                    color: 0x0284c7,
                    emissive: 0x0369a1,
                    specular: 0x38bdf8,
                    shininess: 85,
                    flatShading: true
                });
                const innerSphere = new THREE.Mesh(innerGeo, innerMat);
                coreGroup.add(innerSphere);

                const outerGeo = new THREE.IcosahedronGeometry(4.2, 2);
                const outerMat = new THREE.MeshBasicMaterial({
                    color: 0x38bdf8,
                    wireframe: true,
                    transparent: true,
                    opacity: 0.48
                });
                const outerShell = new THREE.Mesh(outerGeo, outerMat);
                coreGroup.add(outerShell);

                const particleCount = 120;
                const particleGeo = new THREE.BufferGeometry();
                const positions = new Float32Array(particleCount * 3);

                for (let i = 0; i < particleCount; i++) {
                    const angle = (i / particleCount) * Math.PI * 2;
                    const radius = THREE.MathUtils.randFloat(5.2, 6.8);
                    positions[i * 3] = Math.cos(angle) * radius;
                    positions[i * 3 + 1] = THREE.MathUtils.randFloat(-1.1, 1.1);
                    positions[i * 3 + 2] = Math.sin(angle) * radius;
                }

                particleGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
                const particleMat = new THREE.PointsMaterial({
                    color: 0xfacc15,
                    size: 0.15,
                    transparent: true,
                    opacity: 0.9
                });
                const particleRing = new THREE.Points(particleGeo, particleMat);
                coreGroup.add(particleRing);

                scene.add(coreGroup);

                let mouseX = 0, mouseY = 0;
                let targetX = 0, targetY = 0;
                const nameBox = document.getElementById('bengaliNameBox');
                const akaTagBox = document.getElementById('akaTagBox');
                const taglineBox = document.getElementById('taglineBox');

                // Target Colors for Smooth Lerp Transition
                let targetInnerColor = new THREE.Color(0x0284c7);
                let targetOuterColor = new THREE.Color(0x38bdf8);
                let targetParticleColor = new THREE.Color(0xfacc15);
                let lastColorShiftTime = 0;

                window.addEventListener('mousemove', (e) => {
                    mouseX = (e.clientX / window.innerWidth - 0.5) * 1.5;
                    mouseY = (e.clientY / window.innerHeight - 0.5) * 1.5;

                    // Name Box Proximity
                    if (nameBox) {
                        const rect = nameBox.getBoundingClientRect();
                        const centerX = rect.left + rect.width / 2;
                        const centerY = rect.top + rect.height / 2;
                        const dist = Math.hypot(e.clientX - centerX, e.clientY - centerY);
                        if (dist < 150) {
                            nameBox.classList.add('active-hover');
                        } else {
                            nameBox.classList.remove('active-hover');
                        }
                    }

                    // AKA Tag Proximity Easter Egg
                    if (akaTagBox) {
                        const rect = akaTagBox.getBoundingClientRect();
                        const centerX = rect.left + rect.width / 2;
                        const centerY = rect.top + rect.height / 2;
                        const dist = Math.hypot(e.clientX - centerX, e.clientY - centerY);
                        if (dist < 120) {
                            akaTagBox.classList.add('aka-hover');
                        } else {
                            akaTagBox.classList.remove('aka-hover');
                        }
                    }

                    // Sub-tagline Proximity (Jack of all Trades -> সর্বকাজে দক্ষ ব্যক্তি)
                    if (taglineBox) {
                        const rect = taglineBox.getBoundingClientRect();
                        const centerX = rect.left + rect.width / 2;
                        const centerY = rect.top + rect.height / 2;
                        const dist = Math.hypot(e.clientX - centerX, e.clientY - centerY);
                        if (dist < 150) {
                            taglineBox.classList.add('active-hover');
                        } else {
                            taglineBox.classList.remove('active-hover');
                        }
                    }

                    // 3D Core Globe Mouse Proximity (230px Radius)
                    const globeCenterX = window.innerWidth / 2;
                    const globeCenterY = window.innerHeight / 2;
                    const distToGlobe = Math.hypot(e.clientX - globeCenterX, e.clientY - globeCenterY);

                    if (distToGlobe < 230) {
                        const now = Date.now();
                        if (now - lastColorShiftTime > 350) {
                            lastColorShiftTime = now;
                            targetInnerColor = new THREE.Color(Math.random(), Math.random(), Math.random());
                            targetOuterColor = new THREE.Color(Math.random(), Math.random(), Math.random());
                            targetParticleColor = new THREE.Color(Math.random(), Math.random(), Math.random());
                        }
                    } else {
                        targetInnerColor.setHex(0x0284c7);
                        targetOuterColor.setHex(0x38bdf8);
                        targetParticleColor.setHex(0xfacc15);
                    }
                });

                window.addEventListener('resize', () => {
                    camera.aspect = window.innerWidth / window.innerHeight;
                    camera.updateProjectionMatrix();
                    renderer.setSize(window.innerWidth, window.innerHeight);
                });

                let clock = new THREE.Clock();
                function animate() {
                    requestAnimationFrame(animate);
                    const time = clock.getElapsedTime();

                    innerSphere.rotation.y = time * 0.35;
                    outerShell.rotation.y = -time * 0.25;
                    outerShell.rotation.x = time * 0.18;
                    particleRing.rotation.y = time * 0.45;

                    starField.rotation.y = time * 0.03;
                    starField.rotation.x = Math.sin(time * 0.02) * 0.05;

                    targetX += (mouseX - targetX) * 0.05;
                    targetY += (mouseY - targetY) * 0.05;
                    coreGroup.rotation.y = targetX;
                    coreGroup.rotation.x = targetY;

                    // Smooth Lerp Color Shift on Proximity
                    innerMat.color.lerp(targetInnerColor, 0.08);
                    innerMat.emissive.lerp(targetInnerColor, 0.08);
                    outerMat.color.lerp(targetOuterColor, 0.08);
                    particleMat.color.lerp(targetParticleColor, 0.08);
                    cyanLight.color.lerp(targetOuterColor, 0.08);
                    roseLight.color.lerp(targetInnerColor, 0.08);

                    renderer.render(scene, camera);
                }
                animate();
            });
        </script>
    </body>
    </html>
    """
    
    components.html(cyber_core_html, height=420, scrolling=False)

    # Section Header with Fast Word-by-Word Staggered Reveal Animation
    st.markdown("""
    <div class="section-header-wrapper">
        <h2 class="stagger-words-h2">
            <span>What</span> <span>I</span> <span>Bring</span> <span>to</span> <span>the</span> <span>Table</span>
        </h2>
        <p class="stagger-words-p">
            <span>Why</span> <span>Choose</span> <span>Me</span> <span>—</span> 
            <span>Select</span> <span>an</span> <span>ecosystem</span> <span>below</span> 
            <span>to</span> <span>explore</span> <span>repositories</span> <span>&</span> <span>applications</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Unified Cosmic Background & Tech Cards Component (Zero Margins / Seamless Borderless Canvas)
    cards_cosmic_background_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                background: transparent;
                overflow: hidden;
                width: 100%;
                height: 540px;
                position: relative;
                font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
                color: #f8fafc;
            }

            #cosmicCanvas {
                position: absolute;
                top: 0; left: 0;
                width: 100%; height: 100%;
                z-index: 1;
                display: block;
            }

            .cards-overlay {
                position: absolute;
                top: 0; left: 0;
                width: 100%; height: 100%;
                z-index: 10;
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 24px;
                padding: 10px 20px;
                pointer-events: none;
            }

            .giant-card {
                pointer-events: auto;
                flex: 1;
                max-width: 380px;
                height: 490px;
                background: rgba(13, 19, 36, 0.88);
                border: 1px solid rgba(56, 189, 248, 0.28);
                border-radius: 24px;
                padding: 30px 22px;
                text-align: center;
                transition: all 0.38s cubic-bezier(0.4, 0, 0.2, 1);
                box-shadow: 0 16px 40px rgba(0, 0, 0, 0.55);
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: space-between;
                position: relative;
                overflow: hidden;
                backdrop-filter: blur(12px);
                animation: cardEntrance 0.8s cubic-bezier(0.16, 1, 0.3, 1) ease-out;
            }

            .giant-card::before {
                content: '';
                position: absolute;
                top: 0; left: -100%;
                width: 100%; height: 100%;
                background: linear-gradient(90deg, transparent, rgba(56, 189, 248, 0.15), transparent);
                transition: 0.6s;
            }
            .giant-card:hover::before {
                left: 100%;
            }
            .giant-card:hover {
                transform: translateY(-10px) scale(1.025);
                border-color: rgba(56, 189, 248, 0.75);
                box-shadow: 0 28px 60px rgba(56, 189, 248, 0.45);
            }

            @keyframes cardEntrance {
                0% { opacity: 0; transform: translateY(30px) scale(0.95); }
                100% { opacity: 1; transform: translateY(0) scale(1); }
            }

            .giant-card > * {
                position: relative;
                z-index: 2;
            }

            .card-icon-wrapper {
                width: 82px;
                height: 82px;
                border-radius: 20px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 16px auto;
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.12);
                transition: all 0.35s ease;
            }
            .giant-card:hover .card-icon-wrapper {
                transform: scale(1.15) rotate(6deg);
                background: rgba(56, 189, 248, 0.15);
                border-color: rgba(56, 189, 248, 0.5);
                box-shadow: 0 0 25px rgba(56, 189, 248, 0.4);
            }

            .card-icon-img {
                width: 48px;
                height: 48px;
                object-fit: contain;
            }
            .card-title {
                font-size: 1.7rem;
                font-weight: 800;
                margin-bottom: 10px;
            }
            .card-desc {
                color: #94a3b8;
                font-size: 0.93rem;
                line-height: 1.55;
                margin-bottom: 18px;
                min-height: 70px;
            }

            .card-btn {
                width: 100%;
                padding: 13px 18px;
                border-radius: 14px;
                font-size: 0.92rem;
                font-weight: 800;
                letter-spacing: 0.5px;
                transition: all 0.35s ease;
                border: none;
                background: linear-gradient(135deg, #0284c7 0%, #06b6d4 50%, #f43f5e 100%);
                background-size: 200% 200%;
                animation: gradientShift 4s ease infinite;
                color: #ffffff;
                box-shadow: 0 4px 20px rgba(2, 132, 199, 0.4);
                cursor: pointer;
                outline: none;
            }

            @keyframes gradientShift {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .card-btn:hover {
                transform: translateY(-3px) scale(1.03);
                box-shadow: 0 12px 35px rgba(6, 182, 212, 0.7);
            }

            /* Rotational Glow Auras behind Cards */
            .python-glow-card::after {
                content: '';
                position: absolute;
                top: -50%; left: -50%;
                width: 200%; height: 200%;
                background: radial-gradient(circle, rgba(56, 189, 248, 0.18) 0%, rgba(2, 132, 199, 0.05) 50%, transparent 70%);
                animation: rotateAura 12s linear infinite;
                z-index: 1;
                pointer-events: none;
            }
            .rust-glow-card::after {
                content: '';
                position: absolute;
                top: -50%; left: -50%;
                width: 200%; height: 200%;
                background: radial-gradient(circle, rgba(251, 146, 60, 0.20) 0%, rgba(234, 88, 12, 0.06) 50%, transparent 70%);
                animation: rotateAura 10s linear infinite reverse;
                z-index: 1;
                pointer-events: none;
            }
            .vue-glow-card::after {
                content: '';
                position: absolute;
                top: -50%; left: -50%;
                width: 200%; height: 200%;
                background: radial-gradient(circle, rgba(52, 211, 153, 0.18) 0%, rgba(16, 185, 129, 0.05) 50%, transparent 70%);
                animation: rotateAura 14s linear infinite;
                z-index: 1;
                pointer-events: none;
            }

            @keyframes rotateAura {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
    </head>
    <body>
        <canvas id="cosmicCanvas"></canvas>

        <div class="cards-overlay">
            <!-- CARD 1: PYTHON -->
            <div class="giant-card python-glow-card">
                <div>
                    <div class="card-icon-wrapper">
                        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" class="card-icon-img" alt="Python">
                    </div>
                    <div class="card-title" style="color: #38bdf8;">Python & AI/ML</div>
                    <div class="card-desc">
                        Full-stack Flask web apps, PyTorch Deep Learning MCQ Solver, Gradient Boosting ML price prediction, Healthcare HMS, and Open Source Monorepo.
                    </div>
                </div>
                <button class="card-btn" onclick="navigateTo('python')">Explore Python Projects 🐍</button>
            </div>

            <!-- CARD 2: RUST -->
            <div class="giant-card rust-glow-card">
                <div>
                    <div class="card-icon-wrapper">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Rust_programming_language_black_logo.svg" class="card-icon-img" style="filter: invert(1);" alt="Rust">
                    </div>
                    <div class="card-title" style="color: #fb923c;">Rust Systems</div>
                    <div class="card-desc">
                        Low-level systems programming, memory safety without GC, high-concurrency CLI tools, zero-cost abstraction patterns, and monorepo collection.
                    </div>
                </div>
                <button class="card-btn" onclick="navigateTo('rust')">Explore Rust Projects 🦀</button>
            </div>

            <!-- CARD 3: VUE -->
            <div class="giant-card vue-glow-card">
                <div>
                    <div class="card-icon-wrapper">
                        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vuejs/vuejs-original.svg" class="card-icon-img" alt="Vue.js">
                    </div>
                    <div class="card-title" style="color: #34d399;">Vue.js Frontend</div>
                    <div class="card-desc">
                        Reactive web user interfaces, single-page application (SPA) architectures, custom component libraries, and frontend monorepo applications.
                    </div>
                </div>
                <button class="card-btn" onclick="navigateTo('vue')">Explore Vue.js Projects ⚡</button>
            </div>
        </div>

        <script>
            function navigateTo(page) {
                try {
                    window.top.location.search = '?page=' + page;
                } catch(e) {
                    window.parent.location.search = '?page=' + page;
                }
            }

            const canvas = document.getElementById('cosmicCanvas');
            const ctx = canvas.getContext('2d');
            let w = canvas.width = window.innerWidth;
            let h = canvas.height = 540;

            window.addEventListener('resize', () => {
                w = canvas.width = window.innerWidth;
                h = canvas.height = 540;
            });

            // 1. Shooting Asteroids / Comets
            class Asteroid {
                constructor() {
                    this.reset();
                }
                reset() {
                    this.x = Math.random() * (w + 400) - 100;
                    this.y = -60;
                    this.length = Math.random() * 160 + 100;
                    this.speed = Math.random() * 8 + 5.5;
                    this.angle = Math.PI / 4 + (Math.random() - 0.5) * 0.25;
                    this.size = Math.random() * 2.8 + 1.5;
                    const colors = ['#38bdf8', '#fb923c', '#facc15', '#34d399', '#f43f5e'];
                    this.color = colors[Math.floor(Math.random() * colors.length)];
                }
                update() {
                    this.x -= Math.cos(this.angle) * this.speed;
                    this.y += Math.sin(this.angle) * this.speed;
                    if (this.x < -200 || this.y > h + 200) {
                        this.reset();
                    }
                }
                draw() {
                    ctx.save();
                    const tailX = this.x + Math.cos(this.angle) * this.length;
                    const tailY = this.y - Math.sin(this.angle) * this.length;
                    
                    const grad = ctx.createLinearGradient(this.x, this.y, tailX, tailY);
                    grad.addColorStop(0, this.color);
                    grad.addColorStop(0.35, this.color);
                    grad.addColorStop(1, 'transparent');
                    
                    ctx.beginPath();
                    ctx.moveTo(this.x, this.y);
                    ctx.lineTo(tailX, tailY);
                    ctx.strokeStyle = grad;
                    ctx.lineWidth = this.size;
                    ctx.lineCap = 'round';
                    ctx.stroke();

                    // Blazing Head
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.size * 1.8, 0, Math.PI * 2);
                    ctx.fillStyle = '#ffffff';
                    ctx.shadowBlur = 18;
                    ctx.shadowColor = this.color;
                    ctx.fill();
                    ctx.restore();
                }
            }

            // 2. Supernova Star Explosions
            class Supernova {
                constructor(x, y, color) {
                    this.x = x;
                    this.y = y;
                    this.color = color;
                    this.particles = [];
                    const particleCount = 55;
                    for (let i = 0; i < particleCount; i++) {
                        const angle = Math.random() * Math.PI * 2;
                        const speed = Math.random() * 4.8 + 1.2;
                        this.particles.push({
                            x: this.x,
                            y: this.y,
                            vx: Math.cos(angle) * speed,
                            vy: Math.sin(angle) * speed,
                            size: Math.random() * 3.2 + 1,
                            alpha: 1.0,
                            decay: Math.random() * 0.018 + 0.012
                        });
                    }
                }
                update() {
                    this.particles.forEach(p => {
                        p.x += p.vx;
                        p.y += p.vy;
                        p.alpha -= p.decay;
                    });
                }
                draw() {
                    this.particles.forEach(p => {
                        if (p.alpha > 0) {
                            ctx.save();
                            ctx.beginPath();
                            ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                            ctx.fillStyle = p.alpha > 0.5 ? '#ffffff' : this.color;
                            ctx.shadowBlur = 14;
                            ctx.shadowColor = this.color;
                            ctx.globalAlpha = p.alpha;
                            ctx.fill();
                            ctx.restore();
                        }
                    });
                }
                isFinished() {
                    return this.particles.every(p => p.alpha <= 0);
                }
            }

            const asteroids = Array.from({ length: 9 }, () => new Asteroid());
            let supernovas = [];

            // Trigger Supernova explosions behind cards periodically across 540px depth
            let lastExplosion = 0;
            function triggerRandomSupernova(time) {
                if (time - lastExplosion > 1400) {
                    lastExplosion = time;
                    const cardPositions = [
                        { x: w * 0.20, color: '#38bdf8' }, // Python Cyan
                        { x: w * 0.50, color: '#fb923c' }, // Rust Orange
                        { x: w * 0.80, color: '#34d399' }  // Vue Emerald
                    ];
                    const pos = cardPositions[Math.floor(Math.random() * cardPositions.length)];
                    const spawnY = Math.random() * (h - 80) + 40;
                    supernovas.push(new Supernova(pos.x, spawnY, pos.color));
                }
            }

            // Interactive Mouse Explosions
            window.addEventListener('mousemove', (e) => {
                if (Math.random() > 0.65) {
                    const colors = ['#38bdf8', '#fb923c', '#facc15', '#34d399'];
                    const color = colors[Math.floor(Math.random() * colors.length)];
                    supernovas.push(new Supernova(e.clientX, e.clientY, color));
                }
            });

            function animate(time) {
                ctx.clearRect(0, 0, w, h);

                // Update & Draw Asteroids
                asteroids.forEach(a => {
                    a.update();
                    a.draw();
                });

                // Periodic Supernovas
                triggerRandomSupernova(time);

                // Update & Draw Supernovas
                supernovas.forEach((s, idx) => {
                    s.update();
                    s.draw();
                    if (s.isFinished()) {
                        supernovas.splice(idx, 1);
                    }
                });

                requestAnimationFrame(animate);
            }
            requestAnimationFrame(animate);
        </script>
    </body>
    </html>
    """
    components.html(cards_cosmic_background_html, height=540, scrolling=False)

    # Bottom Animation Canvas: Interactive Cyber Grid Horizon & Floating Tech Matrix
    bottom_cyber_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { background: transparent; overflow: hidden; width: 100vw; height: 160px; position: relative; }
            canvas { width: 100%; height: 100%; display: block; }
        </style>
    </head>
    <body>
        <canvas id="cyberCanvas"></canvas>
        <script>
            const canvas = document.getElementById('cyberCanvas');
            const ctx = canvas.getContext('2d');
            let w = canvas.width = window.innerWidth;
            let h = canvas.height = 160;

            window.addEventListener('resize', () => {
                w = canvas.width = window.innerWidth;
                h = canvas.height = 160;
            });

            // Floating Tech Badges / Glyphs
            const badges = [
                { text: '🐍 Python & AI/ML', x: w * 0.12, y: 140, speed: 0.35, alpha: 0.85, scale: 0.95 },
                { text: '🦀 Rust Systems', x: w * 0.32, y: 150, speed: 0.42, alpha: 0.88, scale: 1.0 },
                { text: '⚡ Vue.js Frontend', x: w * 0.58, y: 135, speed: 0.38, alpha: 0.88, scale: 1.0 },
                { text: '🧠 PyTorch & GenAI', x: w * 0.78, y: 145, speed: 0.32, alpha: 0.78, scale: 0.9 },
                { text: '🛡️ Memory Safety', x: w * 0.45, y: 155, speed: 0.48, alpha: 0.75, scale: 0.85 },
            ];

            // Cyber Energy Particles
            const particles = [];
            for(let i = 0; i < 55; i++) {
                particles.push({
                    x: Math.random() * w,
                    y: Math.random() * h,
                    size: Math.random() * 2.5 + 1.2,
                    speedY: -(Math.random() * 0.6 + 0.3),
                    speedX: (Math.random() - 0.5) * 0.4,
                    hue: Math.random() > 0.5 ? 199 : (Math.random() > 0.5 ? 25 : 155),
                    alpha: Math.random() * 0.8 + 0.2
                });
            }

            let mouseX = w / 2;
            window.addEventListener('mousemove', (e) => {
                mouseX = e.clientX;
            });

            function drawHorizonGrid(time) {
                // Top Horizon Ambient Glow
                const grad = ctx.createLinearGradient(0, 0, 0, h);
                grad.addColorStop(0, 'rgba(7, 10, 19, 0)');
                grad.addColorStop(0.4, 'rgba(14, 165, 233, 0.06)');
                grad.addColorStop(1, 'rgba(56, 189, 248, 0.16)');
                ctx.fillStyle = grad;
                ctx.fillRect(0, 0, w, h);

                // Perspective Cyber Grid
                ctx.save();
                ctx.strokeStyle = 'rgba(56, 189, 248, 0.14)';
                ctx.lineWidth = 1;

                // Horizontal Perspective Lines
                for(let y = 15; y < h; y += 20) {
                    ctx.beginPath();
                    ctx.moveTo(0, y);
                    ctx.lineTo(w, y);
                    ctx.stroke();
                }

                // Perspective Vanishing Lines Toward Dynamic Center
                const horizonY = 5;
                const centerX = w / 2 + (mouseX - w/2) * 0.06;
                const lineCount = 32;
                for(let i = -lineCount/2; i <= lineCount/2; i++) {
                    const startX = centerX + (i * 48);
                    ctx.beginPath();
                    ctx.moveTo(centerX, horizonY);
                    ctx.lineTo(startX, h);
                    ctx.strokeStyle = `rgba(56, 189, 248, ${0.06 + (1 - Math.abs(i)/(lineCount/2)) * 0.10})`;
                    ctx.stroke();
                }
                ctx.restore();
            }

            function animate(time) {
                ctx.clearRect(0, 0, w, h);

                // 1. Draw Perspective Grid
                drawHorizonGrid(time);

                // 2. Rising Cyber Embers
                particles.forEach(p => {
                    p.y += p.speedY;
                    p.x += p.speedX;
                    p.alpha -= 0.0025;
                    if (p.y < 0 || p.alpha <= 0) {
                        p.x = Math.random() * w;
                        p.y = h;
                        p.alpha = Math.random() * 0.8 + 0.2;
                    }
                    ctx.save();
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                    ctx.fillStyle = `hsla(${p.hue}, 90%, 65%, ${p.alpha})`;
                    ctx.shadowBlur = 10;
                    ctx.shadowColor = `hsla(${p.hue}, 90%, 65%, 0.8)`;
                    ctx.fill();
                    ctx.restore();
                });

                // 3. Floating Tech Glyphs
                badges.forEach(b => {
                    b.y -= b.speed;
                    b.x += Math.sin(time * 0.0018 + b.y * 0.04) * 0.35;
                    if (b.y < -20) {
                        b.y = h + 20;
                        b.x = Math.random() * (w - 120) + 60;
                    }
                    ctx.save();
                    ctx.font = `600 ${13 * b.scale}px 'Plus Jakarta Sans', sans-serif`;
                    ctx.fillStyle = `rgba(255, 255, 255, ${b.alpha * 0.85})`;
                    ctx.shadowBlur = 10;
                    ctx.shadowColor = 'rgba(56, 189, 248, 0.6)';
                    ctx.fillText(b.text, b.x, b.y);
                    ctx.restore();
                });

                requestAnimationFrame(animate);
            }
            requestAnimationFrame(animate);
        </script>
    </body>
    </html>
    """
    components.html(bottom_cyber_html, height=160, scrolling=False)

# -----------------------------------------------------------------------------
# PAGE 2: PYTHON REPOSITORIES VIEW
# -----------------------------------------------------------------------------
elif current_page == 'python':
    st.markdown("""
    <div style="margin-bottom: 25px;">
        <h1 style="font-size: 2.8rem; font-weight: 800; color: #38bdf8; margin-bottom: 4px;">🐍 Python & AI/ML Ecosystem</h1>
        <p style="color: #94a3b8; font-size: 1.1rem;">Artificial Intelligence, Deep Learning models, Full-Stack web platforms & Open Source Monorepo</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="repo-card">
            <span class="badge-pill badge-cyan">Monorepo Collection</span>
            <span class="badge-pill badge-amber">GNU GPLv3</span>
            <h3 style="color: #ffffff; margin: 8px 0 10px 0;">🐍 Python Projects Monorepo</h3>
            <p style="color: #94a3b8; font-size: 0.94rem; margin-bottom: 16px;">
                Centralized open-source monorepo consolidating AI/ML, NLP, Deep Learning, Cybersecurity tools, and automation scripts.
            </p>
            <a href="https://github.com/RSNPIIT/Python-Projects" target="_blank" class="project-link">
                🔗 github.com/RSNPIIT/Python-Projects &rarr;
            </a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="repo-card">
            <span class="badge-pill badge-cyan">Smart Infrastructure</span>
            <span class="badge-pill badge-emerald">Flask + SQLite</span>
            <span class="badge-pill badge-amber">GNU GPLv3</span>
            <h3 style="color: #ffffff; margin: 8px 0 10px 0;">🚗 ParkSmart Vehicle Parking App</h3>
            <p style="color: #94a3b8; font-size: 0.94rem; margin-bottom: 16px;">
                Production-ready parking platform featuring role-based portals, spot grid maps, automated duration billing, and WebGL visualizations.
            </p>
            <a href="https://github.com/24f3004027/vehicle-parking-appv1" target="_blank" class="project-link">
                💻 View Repository on GitHub &rarr;
            </a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="repo-card">
            <span class="badge-pill badge-cyan">Healthcare Tech</span>
            <span class="badge-pill badge-emerald">Flask + SQLAlchemy</span>
            <span class="badge-pill badge-amber">GNU GPLv3</span>
            <h3 style="color: #ffffff; margin: 8px 0 10px 0;">🏥 PulseCare Hospital Management System</h3>
            <p style="color: #94a3b8; font-size: 0.94rem; margin-bottom: 16px;">
                Full-stack clinical portal managing patient appointments, doctor schedules, clinical care notes, and admin metrics.
            </p>
            <div style="display: flex; gap: 16px;">
                <a href="https://24f3004027.github.io/HMS-MAD-Projectv1/" target="_blank" class="project-link">🌐 Live Showcase</a>
                <a href="https://github.com/24f3004027/HMS-MAD-Projectv1" target="_blank" class="project-link">💻 GitHub Repo</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="repo-card">
            <span class="badge-pill badge-rose">PyTorch &bull; GenAI</span>
            <span class="badge-pill badge-emerald">Grade S (Rank 60)</span>
            <h3 style="color: #ffffff; margin: 8px 0 10px 0;">🧠 DL Smart MCQ Solver</h3>
            <p style="color: #94a3b8; font-size: 0.94rem; margin-bottom: 16px;">
                PyTorch BiGRU with Multi-Head Self-Attention and 10-Seed Ensembling for context-augmented multiple choice question answering.
            </p>
            <div style="display: flex; gap: 16px;">
                <a href="https://24f3004027.github.io/Deep_Learning_Project/" target="_blank" class="project-link">🌐 Live Site</a>
                <a href="https://github.com/24f3004027/Deep_Learning_Project" target="_blank" class="project-link">💻 GitHub Repo</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="repo-card">
            <span class="badge-pill badge-rose">Machine Learning</span>
            <span class="badge-pill badge-emerald">Grade S (RMSLE 0.1866)</span>
            <h3 style="color: #ffffff; margin: 8px 0 10px 0;">🚜 MLP Equipment Price Prediction</h3>
            <p style="color: #94a3b8; font-size: 0.94rem; margin-bottom: 16px;">
                End-to-end 5-Seed Gradient Boosting regression pipeline with extensive feature engineering for auction pricing estimation.
            </p>
            <a href="https://github.com/24f3004027/MLP_Project" target="_blank" class="project-link">
                💻 GitHub Repository &rarr;
            </a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="repo-card">
            <span class="badge-pill badge-cyan">Web Automation</span>
            <span class="badge-pill badge-emerald">Flask Architecture</span>
            <h3 style="color: #ffffff; margin: 8px 0 10px 0;">📋 Placement Portal V2</h3>
            <p style="color: #94a3b8; font-size: 0.94rem; margin-bottom: 16px;">
                Automated campus recruitment portal streamlining company drive listings, student resumes, and selection pipelines.
            </p>
            <a href="https://github.com/24f3004027/Placement_Portal_Application_V2" target="_blank" class="project-link">
                💻 GitHub Repository &rarr;
            </a>
        </div>
        """, unsafe_allow_html=True)

    if st.button("&larr; Back to Home Overview", key="back_python"):
        set_page('home')
        st.rerun()

# -----------------------------------------------------------------------------
# PAGE 3: RUST REPOSITORIES VIEW
# -----------------------------------------------------------------------------
elif current_page == 'rust':
    st.markdown("""
    <div style="margin-bottom: 25px;">
        <h1 style="font-size: 2.8rem; font-weight: 800; color: #fb923c; margin-bottom: 4px;">🦀 Rust Systems Ecosystem</h1>
        <p style="color: #94a3b8; font-size: 1.1rem;">Low-level systems programming, memory safety without GC, CLI utilities & zero-cost abstractions</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="repo-card" style="max-width: 850px;">
        <span class="badge-pill badge-amber">Systems Programming</span>
        <span class="badge-pill badge-cyan">Memory Safety & Concurrency</span>
        <h2 style="color: #ffffff; margin: 10px 0;">🦀 Rust Projects Monorepo</h2>
        <p style="color: #94a3b8; font-size: 1.05rem; line-height: 1.6; margin-bottom: 24px;">
            A centralized monorepo collection of high-concurrency tools, memory-safe CLI utilities, custom parsers, zero-cost abstraction patterns, and low-level systems explorations built with Rust.
        </p>
        <a href="https://github.com/RSNPIIT/Rust-Projects" target="_blank" class="project-link" style="font-size: 1.15rem;">
            🔗 Open Repository: github.com/RSNPIIT/Rust-Projects &rarr;
        </a>
    </div>
    """, unsafe_allow_html=True)

    if st.button("&larr; Back to Home Overview", key="back_rust"):
        set_page('home')
        st.rerun()

# -----------------------------------------------------------------------------
# PAGE 4: VUE.JS REPOSITORIES VIEW
# -----------------------------------------------------------------------------
elif current_page == 'vue':
    st.markdown("""
    <div style="margin-bottom: 25px;">
        <h1 style="font-size: 2.8rem; font-weight: 800; color: #34d399; margin-bottom: 4px;">⚡ Vue.js Frontend Ecosystem</h1>
        <p style="color: #94a3b8; font-size: 1.1rem;">Reactive web applications, custom component libraries, and modern single-page interfaces</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="repo-card" style="max-width: 850px;">
        <span class="badge-pill badge-emerald">Frontend Framework</span>
        <span class="badge-pill badge-cyan">Reactive Component UI</span>
        <h2 style="color: #ffffff; margin: 10px 0;">⚡ Vue.js Projects Monorepo</h2>
        <p style="color: #94a3b8; font-size: 1.05rem; line-height: 1.6; margin-bottom: 24px;">
            Central repository of reactive web frontend applications, single-page application (SPA) architectures, custom UI component suites, and state management implementations built with Vue.js.
        </p>
        <a href="https://github.com/RSNPIIT/Vue-Projects" target="_blank" class="project-link" style="font-size: 1.15rem;">
            🔗 Open Repository: github.com/RSNPIIT/Vue-Projects &rarr;
    </div>
    """, unsafe_allow_html=True)

    if st.button("&larr; Back to Home Overview", key="back_vue"):
        set_page('home')
        st.rerun()

# -----------------------------------------------------------------------------
# 5. Clean Footer Notice
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; font-size: 0.88rem; padding-bottom: 20px;">
    RAMRUP SATPATI &bull; Released under GNU General Public License v3.0 (GNU GPLv3) &copy; 2026
</div>
""", unsafe_allow_html=True)