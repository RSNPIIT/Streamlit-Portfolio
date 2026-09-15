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

def set_page(page_name):
    st.session_state['page'] = page_name

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
}
.giant-card::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(56, 189, 248, 0.1), transparent);
    transition: 0.5s;
}
.giant-card:hover::before {
    left: 100%;
}
.giant-card:hover {
    transform: translateY(-10px) scale(1.02);
    border-color: var(--border-hover);
    box-shadow: 0 25px 50px rgba(56, 189, 248, 0.35);
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
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: transform 0.3s ease;
}
.giant-card:hover .card-icon-wrapper {
    transform: scale(1.1) rotate(5deg);
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
    transition: all 0.3s ease !important;
    border: none !important;
    background: linear-gradient(135deg, #0284c7 0%, #06b6d4 50%, #f43f5e 100%) !important;
    background-size: 200% 200% !important;
    animation: gradientShift 4s ease infinite !important;
    color: #ffffff !important;
    box-shadow: 0 4px 20px rgba(2, 132, 199, 0.4) !important;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.03) !important;
    box-shadow: 0 10px 30px rgba(6, 182, 212, 0.6) !important;
}

/* PROJECT DETAILS PAGE STYLING */
.repo-card {
    background: var(--card-bg);
    border: 1px solid var(--border-card);
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 14px 35px rgba(0, 0, 0, 0.5);
    transition: all 0.3s ease;
}
.repo-card:hover {
    border-color: var(--border-hover);
    transform: translateY(-4px);
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
}
.badge-cyan { background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); }
.badge-emerald { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }
.badge-amber { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); }
.badge-rose { background: rgba(244, 63, 94, 0.15); color: #fb7185; border: 1px solid rgba(244, 63, 94, 0.4); }

.project-link {
    color: #38bdf8;
    font-weight: 700;
    text-decoration: none !important;
}
.project-link:hover {
    color: #34d399;
    text-shadow: 0 0 10px rgba(52, 211, 153, 0.5);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. Top Navbar
# -----------------------------------------------------------------------------
st.markdown("""
<div class="top-nav">
    <div class="nav-brand">RAMRUP <span>SATPATI</span> <span style="font-size: 0.9rem; color: #fb923c; font-family: 'Hind Siliguri'; margin-left: 6px;">রামরূপ সাতপতি</span></div>
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
# PAGE 1: HOME VIEW (Glowing Script Font for 'Jack of all Trades')
# -----------------------------------------------------------------------------
if current_page == 'home':
    
    # Hero Component with Glowing Calligraphy Script for 'Jack of all Trades'
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
            .bengali-name { font-size: 2.1rem; font-weight: 700; color: #fb923c; font-family: 'Hind Siliguri', sans-serif; text-shadow: 0 0 18px rgba(251, 146, 60, 0.4); margin-top: 4px; }

            .right-col {
                text-align: left;
                padding-left: 20px;
            }
            .role-tag { color: #94a3b8; font-size: 1.2rem; font-weight: 600; margin-bottom: 2px; }
            .role-highlight { font-size: 2.5rem; font-weight: 900; line-height: 1.08; background: linear-gradient(135deg, #38bdf8, #06b6d4, #f43f5e); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }

            /* GLOWING ELEGANT CALLIGRAPHY SCRIPT FOR 'JACK OF ALL TRADES' */
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
                <div class="bengali-name">রামরূপ সাতপতি</div>
            </div>
            <div></div>
            <div class="right-col">
                <div class="role-tag">A Full Stack</div>
                <div class="role-highlight">SYSTEMS & AI<br>ENGINEER</div>
                <div class="sub-tagline">Jack of all Trades</div>
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

                window.addEventListener('mousemove', (e) => {
                    mouseX = (e.clientX / window.innerWidth - 0.5) * 1.5;
                    mouseY = (e.clientY / window.innerHeight - 0.5) * 1.5;
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

                    renderer.render(scene, camera);
                }
                animate();
            });
        </script>
    </body>
    </html>
    """
    
    components.html(cyber_core_html, height=420, scrolling=False)

    # Section Header
    st.markdown("""
    <div style="text-align: center; margin-top: 15px; margin-bottom: 30px;">
        <h2 style="font-size: 2.3rem; font-weight: 800; color: #ffffff;">What I Bring to the Table</h2>
        <p style="color: #94a3b8; font-size: 1.05rem;">Why Choose Me — Select an ecosystem below to explore repositories & applications</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3, gap="large")

    # CARD 1: PYTHON
    with c1:
        st.markdown("""
        <div class="giant-card">
            <div class="card-icon-wrapper">
                <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" class="card-icon-img" alt="Python">
            </div>
            <div class="card-title" style="color: #38bdf8;">Python & AI/ML</div>
            <div class="card-desc">
                Full-stack Flask web apps, PyTorch Deep Learning MCQ Solver, Gradient Boosting ML price prediction, Healthcare HMS, and Open Source Monorepo.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Explore Python Projects 🐍", key="btn_python", use_container_width=True, type="primary"):
            set_page('python')
            st.rerun()

    # CARD 2: RUST (CRISP RELIABLE LOGO)
    with c2:
        st.markdown("""
        <div class="giant-card">
            <div class="card-icon-wrapper">
                <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Rust_programming_language_black_logo.svg" class="card-icon-img" style="filter: invert(1);" alt="Rust">
            </div>
            <div class="card-title" style="color: #fb923c;">Rust Systems</div>
            <div class="card-desc">
                Low-level systems programming, memory safety without GC, high-concurrency CLI tools, zero-cost abstraction patterns, and monorepo collection.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Explore Rust Projects 🦀", key="btn_rust", use_container_width=True, type="primary"):
            set_page('rust')
            st.rerun()

    # CARD 3: VUE
    with c3:
        st.markdown("""
        <div class="giant-card">
            <div class="card-icon-wrapper">
                <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vuejs/vuejs-original.svg" class="card-icon-img" alt="Vue.js">
            </div>
            <div class="card-title" style="color: #34d399;">Vue.js Frontend</div>
            <div class="card-desc">
                Reactive web user interfaces, single-page application (SPA) architectures, custom component libraries, and frontend monorepo applications.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Explore Vue.js Projects ⚡", key="btn_vue", use_container_width=True, type="primary"):
            set_page('vue')
            st.rerun()

    # Bottom Animation Canvas: Swaying Coastal Palm Trees + Rising Particles
    bottom_palm_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { background: transparent; overflow: hidden; width: 100vw; height: 130px; }
            canvas { width: 100%; height: 100%; display: block; }
        </style>
    </head>
    <body>
        <canvas id="palmCanvas"></canvas>
        <script>
            const canvas = document.getElementById('palmCanvas');
            const ctx = canvas.getContext('2d');
            let w = canvas.width = window.innerWidth;
            let h = canvas.height = 130;

            window.addEventListener('resize', () => {
                w = canvas.width = window.innerWidth;
                h = canvas.height = 130;
            });

            // Particles
            const embers = [];
            for (let i = 0; i < 45; i++) {
                embers.push({
                    x: Math.random() * w,
                    y: Math.random() * h,
                    size: Math.random() * 2.2 + 1,
                    vy: -(Math.random() * 0.7 + 0.3),
                    vx: (Math.random() - 0.5) * 0.4,
                    alpha: Math.random() * 0.7 + 0.2
                });
            }

            function drawPalmTree(x, height, angleSway, scale = 1.0) {
                ctx.save();
                ctx.translate(x, h);
                ctx.scale(scale, scale);

                ctx.beginPath();
                ctx.moveTo(0, 0);
                const controlX = angleSway * 18;
                ctx.quadraticCurveTo(controlX, -height * 0.5, angleSway * 25, -height);
                ctx.lineWidth = 7;
                ctx.strokeStyle = '#0f2942';
                ctx.lineCap = 'round';
                ctx.stroke();

                ctx.lineWidth = 3;
                ctx.strokeStyle = '#0284c7';
                ctx.stroke();

                const topX = angleSway * 25;
                const topY = -height;
                const leafAngles = [-0.8, -0.4, 0, 0.4, 0.8, -1.1, 1.1];

                leafAngles.forEach((baseAngle, idx) => {
                    ctx.save();
                    ctx.translate(topX, topY);
                    const finalAngle = baseAngle + angleSway * 0.4 + Math.sin(Date.now() * 0.002 + idx) * 0.05;
                    ctx.rotate(finalAngle);

                    ctx.beginPath();
                    ctx.moveTo(0, 0);
                    ctx.quadraticCurveTo(25, -15, 55, 10);
                    ctx.lineWidth = 3.5;
                    ctx.strokeStyle = idx % 2 === 0 ? '#38bdf8' : '#0284c7';
                    ctx.stroke();
                    ctx.restore();
                });

                ctx.restore();
            }

            function animate(time) {
                ctx.clearRect(0, 0, w, h);

                embers.forEach(p => {
                    p.y += p.vy;
                    p.x += p.vx;
                    p.alpha -= 0.003;
                    if (p.y < 0 || p.alpha <= 0) {
                        p.x = Math.random() * w;
                        p.y = h;
                        p.alpha = Math.random() * 0.7 + 0.3;
                    }
                    ctx.save();
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                    ctx.fillStyle = `rgba(56, 189, 248, ${p.alpha})`;
                    ctx.shadowBlur = 8;
                    ctx.shadowColor = '#38bdf8';
                    ctx.fill();
                    ctx.restore();
                });

                const sway1 = Math.sin(time * 0.0018) * 0.8;
                const sway2 = Math.sin(time * 0.0022 + 1) * 0.7;

                drawPalmTree(60, 95, sway1, 0.9);
                drawPalmTree(120, 110, sway2, 1.05);

                drawPalmTree(w - 120, 110, sway1, 1.05);
                drawPalmTree(w - 60, 95, sway2, 0.9);

                requestAnimationFrame(animate);
            }
            requestAnimationFrame(animate);
        </script>
    </body>
    </html>
    """
    components.html(bottom_palm_html, height=130, scrolling=False)

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
        </a>
    </div>
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