import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. Streamlit Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Ramrup Satpati | রামরূপ সাতপতি",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# 2. Global CSS Styling & Centered Layout Enforcements
# -----------------------------------------------------------------------------
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<style>
    /* Hide Default Streamlit Chrome */
    [data-testid="stSidebar"], section[data-testid="stSidebar"], [data-testid="collapsedControl"] {
        display: none !important;
    }
    header[data-testid="stHeader"] {
        background: transparent !important;
    }
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
        max-width: 1200px !important;
    }

    :root {
        --bg-dark: #060b17;
        --card-glass: rgba(10, 18, 36, 0.82);
        --border-glass: rgba(56, 189, 248, 0.28);
        --border-hover: rgba(56, 189, 248, 0.65);
        --accent-cyan: #38bdf8;
        --accent-blue: #0284c7;
        --accent-rose: #f43f5e;
        --accent-amber: #f59e0b;
        --accent-emerald: #10b981;
    }

    body, .stApp {
        background-color: var(--bg-dark) !important;
        color: #f8fafc !important;
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
    }

    /* CENTERED HERO CONTAINER */
    .hero-container {
        text-align: center !important;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 10px;
        margin-bottom: 30px;
    }

    .hero-badge {
        background: rgba(56, 189, 248, 0.12);
        border: 1px solid rgba(56, 189, 248, 0.4);
        color: #38bdf8;
        font-weight: 700;
        padding: 8px 22px;
        border-radius: 30px;
        font-size: 0.88rem;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 18px;
        backdrop-filter: blur(12px);
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.25);
        animation: pulse-glow 3s infinite alternate;
    }

    @keyframes pulse-glow {
        0% { box-shadow: 0 0 15px rgba(56, 189, 248, 0.2); }
        100% { box-shadow: 0 0 30px rgba(56, 189, 248, 0.5); }
    }

    /* CENTERED TITLES */
    .hero-title {
        font-size: 4.2rem;
        font-weight: 800;
        letter-spacing: -1px;
        line-height: 1.08;
        background: linear-gradient(135deg, #ffffff 0%, #38bdf8 35%, #06b6d4 70%, #f43f5e 100%);
        background-size: 200% 200%;
        animation: gradient-shift 6s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
        text-align: center !important;
    }

    @keyframes gradient-shift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .hero-bengali {
        font-size: 2.8rem;
        font-weight: 700;
        color: #fb923c;
        text-shadow: 0 0 25px rgba(251, 146, 60, 0.4);
        margin-bottom: 12px;
        font-family: 'Hind Siliguri', sans-serif;
        text-align: center !important;
    }

    /* CENTERED SUBTEXT - NO SIDE BORDER */
    .hero-subtext {
        font-size: 1.4rem;
        font-weight: 700;
        color: #94a3b8;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 28px;
        border: none !important;
        border-left: none !important;
        padding-left: 0 !important;
        text-align: center !important;
    }

    /* CENTERED SOCIAL CHIPS */
    .connect-bar {
        display: flex;
        flex-wrap: wrap;
        justify-content: center !important;
        align-items: center;
        gap: 14px;
        margin-bottom: 25px;
        width: 100%;
    }
    .connect-chip {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(10, 18, 36, 0.85);
        border: 1px solid rgba(56, 189, 248, 0.35);
        border-radius: 9999px;
        padding: 9px 22px;
        font-size: 0.92rem;
        font-weight: 600;
        color: #38bdf8;
        text-decoration: none !important;
        backdrop-filter: blur(12px);
        transition: all 0.3s ease;
    }
    .connect-chip:hover {
        background: rgba(56, 189, 248, 0.25);
        border-color: #38bdf8;
        color: #ffffff;
        transform: translateY(-3px) scale(1.04);
        box-shadow: 0 10px 25px rgba(56, 189, 248, 0.35);
    }

    /* CENTERED SECTION TITLE */
    .section-title-container {
        text-align: center !important;
        margin-top: 20px;
        margin-bottom: 30px;
    }
    .section-title {
        font-size: 2.4rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 6px;
    }
    .section-desc {
        color: #94a3b8;
        font-size: 1.05rem;
    }

    /* CENTERED STREAMLIT TABS */
    .stTabs [data-baseweb="tab-list"] {
        justify-content: center !important;
        gap: 14px;
        background: rgba(10, 18, 36, 0.7);
        padding: 10px;
        border-radius: 18px;
        border: 1px solid var(--border-glass);
        margin-bottom: 25px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        border-radius: 14px;
        color: #94a3b8;
        font-weight: 700;
        font-size: 1rem;
        padding: 0 28px;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #0284c7, #06b6d4) !important;
        color: #ffffff !important;
        box-shadow: 0 6px 24px rgba(2, 132, 199, 0.45);
    }

    /* GLASS CARDS */
    .glass-card {
        background: var(--card-glass);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid var(--border-glass);
        border-radius: 22px;
        padding: 26px;
        margin-bottom: 24px;
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6);
        transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        text-align: left;
    }
    .glass-card:hover {
        transform: translateY(-6px);
        border-color: var(--border-hover);
        box-shadow: 0 25px 50px rgba(56, 189, 248, 0.28);
    }

    .pill-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 5px 14px;
        border-radius: 30px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-right: 6px;
        margin-bottom: 12px;
        text-transform: uppercase;
    }
    .pill-cyan { background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); }
    .pill-emerald { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }
    .pill-amber { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); }
    .pill-rose { background: rgba(244, 63, 94, 0.15); color: #fb7185; border: 1px solid rgba(244, 63, 94, 0.4); }

    .repo-link {
        color: #38bdf8;
        font-weight: 700;
        text-decoration: none !important;
        transition: all 0.2s ease;
    }
    .repo-link:hover {
        color: #34d399;
        text-shadow: 0 0 12px rgba(52, 211, 153, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. 3D WebGL Cityscape Interactive Animation Component (100% Guaranteed Render)
# -----------------------------------------------------------------------------
animation_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background: #060b17; overflow: hidden; width: 100vw; height: 320px; }
        #canvas3d { width: 100%; height: 100%; display: block; }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>
    <canvas id="canvas3d"></canvas>
    <script>
        window.addEventListener('DOMContentLoaded', () => {
            const canvas = document.getElementById('canvas3d');
            const scene = new THREE.Scene();
            scene.fog = new THREE.FogExp2(0x060b17, 0.008);

            const camera = new THREE.PerspectiveCamera(55, canvas.clientWidth / canvas.clientHeight, 1, 1000);
            camera.position.set(0, 38, 130);
            camera.lookAt(0, 10, -50);

            const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
            renderer.setSize(canvas.clientWidth, canvas.clientHeight);
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

            // Ambient & Directional Cyber Lights
            const ambient = new THREE.AmbientLight(0x0f172a, 2.5);
            scene.add(ambient);

            const cyanLight = new THREE.DirectionalLight(0x38bdf8, 1.8);
            cyanLight.position.set(60, 100, 50);
            scene.add(cyanLight);

            // Ground Matrix Grid
            const grid = new THREE.GridHelper(500, 45, 0x0284c7, 0x0f2942);
            grid.position.y = -0.5;
            scene.add(grid);

            // 1. 3D City Buildings
            const buildingGroup = new THREE.Group();
            const bldgMat = new THREE.MeshPhongMaterial({
                color: 0x0a1428,
                specular: 0x38bdf8,
                shininess: 35,
                flatShading: true
            });
            const edgeMat = new THREE.LineBasicMaterial({ color: 0x0ea5e9, transparent: true, opacity: 0.45 });

            const cityBounds = 150;
            for (let x = -cityBounds; x <= cityBounds; x += 22) {
                for (let z = -cityBounds; z <= 40; z += 22) {
                    if (Math.abs(x) < 18 || Math.abs(z + 30) < 12) continue;
                    if (Math.random() > 0.82) continue;

                    const height = THREE.MathUtils.randFloat(18, 75);
                    const width = THREE.MathUtils.randFloat(10, 15);
                    const depth = THREE.MathUtils.randFloat(10, 15);

                    const geo = new THREE.BoxGeometry(width, height, depth);
                    const building = new THREE.Mesh(geo, bldgMat);
                    building.position.set(x + THREE.MathUtils.randFloat(-2, 2), height / 2, z);

                    const edges = new THREE.LineSegments(new THREE.EdgesGeometry(geo), edgeMat);
                    building.add(edges);

                    if (height > 45) {
                        const beaconGeo = new THREE.SphereGeometry(0.8, 6, 6);
                        const beaconMat = new THREE.MeshBasicMaterial({ color: Math.random() > 0.5 ? 0x38bdf8 : 0xf43f5e });
                        const beacon = new THREE.Mesh(beaconGeo, beaconMat);
                        beacon.position.y = height / 2 + 1;
                        building.add(beacon);
                    }
                    buildingGroup.add(building);
                }
            }
            scene.add(buildingGroup);

            // 2. Animated Vehicles (Neon Light Beams)
            const vehicleCount = 65;
            const vehicles = [];
            const carGeo = new THREE.BoxGeometry(1.2, 0.6, 3.2);
            const redMat = new THREE.MeshBasicMaterial({ color: 0xf43f5e });
            const blueMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });

            for (let i = 0; i < vehicleCount; i++) {
                const isNorth = Math.random() > 0.5;
                const laneX = isNorth ? THREE.MathUtils.randFloat(2.5, 7.5) : THREE.MathUtils.randFloat(-7.5, -2.5);
                const car = new THREE.Mesh(carGeo, isNorth ? blueMat : redMat);

                car.position.set(laneX, 0.4, THREE.MathUtils.randFloat(-180, 100));
                car.userData = {
                    speed: (isNorth ? -1 : 1) * THREE.MathUtils.randFloat(0.5, 1.1),
                    minZ: -200,
                    maxZ: 110
                };
                scene.add(car);
                vehicles.push(car);
            }

            // Interactive Parallax
            let mouseX = 0, mouseY = 0;
            let targetX = 0, targetY = 38;

            window.addEventListener('mousemove', (e) => {
                mouseX = (e.clientX / window.innerWidth - 0.5) * 20;
                mouseY = (e.clientY / window.innerHeight - 0.5) * 10;
            });

            window.addEventListener('resize', () => {
                camera.aspect = canvas.clientWidth / canvas.clientHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(canvas.clientWidth, canvas.clientHeight);
            });

            let clock = new THREE.Clock();
            function animate() {
                requestAnimationFrame(animate);
                const delta = clock.getDelta();

                vehicles.forEach(car => {
                    car.position.z += car.userData.speed;
                    if (car.position.z < car.userData.minZ) car.position.z = car.userData.maxZ;
                    if (car.position.z > car.userData.maxZ) car.position.z = car.userData.minZ;
                });

                targetX += (mouseX - targetX) * 0.04;
                targetY += ((38 - mouseY) - targetY) * 0.04;
                camera.position.x = targetX;
                camera.position.y = targetY;
                camera.lookAt(0, 12, -40);

                renderer.render(scene, camera);
            }
            animate();
        });
    </script>
</body>
</html>
"""

# Render 3D Canvas Header Animation
components.html(animation_html, height=320, scrolling=False)

# -----------------------------------------------------------------------------
# 4. Centered Hero Header Section
# -----------------------------------------------------------------------------
st.markdown("""
<div class="hero-container">
    <div class="hero-badge">
        <span>✨ Full-Stack Systems, AI/ML & CyberSec Engineer</span>
    </div>
    <div class="hero-title">RAMRUP SATPATI</div>
    <div class="hero-bengali">রামরূপ সাতপতি</div>
    <div class="hero-subtext">JACK OF ALL TRADES &bull; RSNPIIT</div>
    
    <div class="connect-bar">
        <a href="https://github.com/RSNPIIT" target="_blank" class="connect-chip">
            <svg height="16" width="16" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.28.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
            GitHub: RSNPIIT
        </a>
        <a href="https://github.com/24f3004027" target="_blank" class="connect-chip">
            💻 IITM Repos: 24f3004027
        </a>
        <a href="https://www.linkedin.com/in/ramrup-satpati-683970341" target="_blank" class="connect-chip">
            💼 LinkedIn Profile
        </a>
        <a href="mailto:ramrupsatpati@gmail.com" class="connect-chip">
            ✉️ Email Contact
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. Centered Projects Section & Centered Tabs
# -----------------------------------------------------------------------------
st.markdown("""
<div class="section-title-container">
    <div class="section-title">🚀 Portfolio Repositories & Projects</div>
    <div class="section-desc">Full-stack web applications, machine learning architectures, and systems repositories</div>
</div>
""", unsafe_allow_html=True)

tab_python, tab_rust, tab_vue = st.tabs(["🐍 Python & AI/ML Projects", "🦀 Rust Systems Projects", "⚡ Vue.js Projects"])

# TAB 1: PYTHON & AI/ML
with tab_python:
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        # Monorepo
        st.markdown("""
        <div class="glass-card">
            <span class="pill-badge pill-cyan">Monorepo Collection</span>
            <span class="pill-badge pill-amber">GNU GPLv3</span>
            <h3 style="color: #ffffff; margin: 6px 0 10px 0; font-weight: 700;">🐍 Python Projects Monorepo</h3>
            <p style="color: #94a3b8; font-size: 0.94rem; margin-bottom: 16px; line-height: 1.55;">
                Centralized open-source repository consolidating systems, utilities, and experiments across AI/ML, Natural Language Processing, Deep Learning, and Cybersecurity.
            </p>
            <a href="https://github.com/RSNPIIT/Python-Projects" target="_blank" class="repo-link">
                🔗 github.com/RSNPIIT/Python-Projects &rarr;
            </a>
        </div>
        """, unsafe_allow_html=True)

        # ParkSmart App
        st.markdown("""
        <div class="glass-card">
            <span class="pill-badge pill-cyan">Smart Infrastructure</span>
            <span class="pill-badge pill-emerald">Flask + SQLite</span>
            <span class="pill-badge pill-amber">GNU GPLv3</span>
            <h3 style="color: #ffffff; margin: 6px 0 10px 0; font-weight: 700;">🚗 ParkSmart Vehicle Parking App</h3>
            <p style="color: #94a3b8; font-size: 0.94rem; margin-bottom: 16px; line-height: 1.55;">
                Production-ready parking platform featuring role-based portals, interactive spot grid maps, automated duration-based tariff billing, and 3D WebGL cityscape visualization.
            </p>
            <a href="https://github.com/24f3004027/vehicle-parking-appv1" target="_blank" class="repo-link">
                💻 View Repository on GitHub &rarr;
            </a>
        </div>
        """, unsafe_allow_html=True)

        # PulseCare HMS
        st.markdown("""
        <div class="glass-card">
            <span class="pill-badge pill-cyan">Healthcare Tech</span>
            <span class="pill-badge pill-emerald">Flask + SQLAlchemy</span>
            <span class="pill-badge pill-amber">GNU GPLv3</span>
            <h3 style="color: #ffffff; margin: 6px 0 10px 0; font-weight: 700;">🏥 PulseCare Hospital Management System</h3>
            <p style="color: #94a3b8; font-size: 0.94rem; margin-bottom: 16px; line-height: 1.55;">
                Clinical portal managing patient appointments, doctor schedules, administrative analytics, and automated clinical notes recording.
            </p>
            <div style="display: flex; gap: 16px;">
                <a href="https://24f3004027.github.io/HMS-MAD-Projectv1/" target="_blank" class="repo-link">🌐 Live Showcase</a>
                <a href="https://github.com/24f3004027/HMS-MAD-Projectv1" target="_blank" class="repo-link">💻 GitHub Repo</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # DL Smart MCQ Solver
        st.markdown("""
        <div class="glass-card">
            <span class="pill-badge pill-rose">PyTorch &bull; GenAI</span>
            <span class="pill-badge pill-emerald">Grade S (Rank 60)</span>
            <h3 style="color: #ffffff; margin: 6px 0 10px 0; font-weight: 700;">🧠 DL Smart MCQ Solver</h3>
            <p style="color: #94a3b8; font-size: 0.94rem; margin-bottom: 16px; line-height: 1.55;">
                Deep Learning model using BiGRU with Multi-Head Self-Attention and 10-Seed Ensembling for context-augmented multiple choice question answering.
            </p>
            <div style="display: flex; gap: 16px;">
                <a href="https://24f3004027.github.io/Deep_Learning_Project/" target="_blank" class="repo-link">🌐 Live Site</a>
                <a href="https://github.com/24f3004027/Deep_Learning_Project" target="_blank" class="repo-link">💻 GitHub Repo</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # MLP Price Prediction
        st.markdown("""
        <div class="glass-card">
            <span class="pill-badge pill-rose">Machine Learning</span>
            <span class="pill-badge pill-emerald">Grade S (RMSLE 0.1866)</span>
            <h3 style="color: #ffffff; margin: 6px 0 10px 0; font-weight: 700;">🚜 MLP Equipment Price Prediction</h3>
            <p style="color: #94a3b8; font-size: 0.94rem; margin-bottom: 16px; line-height: 1.55;">
                End-to-end 5-Seed Gradient Boosting regression pipeline with feature engineering for auction pricing prediction.
            </p>
            <a href="https://github.com/24f3004027/MLP_Project" target="_blank" class="repo-link">
                💻 GitHub Repository &rarr;
            </a>
        </div>
        """, unsafe_allow_html=True)

        # Placement Portal
        st.markdown("""
        <div class="glass-card">
            <span class="pill-badge pill-cyan">Web Automation</span>
            <span class="pill-badge pill-emerald">Flask Architecture</span>
            <h3 style="color: #ffffff; margin: 6px 0 10px 0; font-weight: 700;">📋 Placement Portal V2</h3>
            <p style="color: #94a3b8; font-size: 0.94rem; margin-bottom: 16px; line-height: 1.55;">
                Automated campus recruitment portal streamlining company drive listings, student resumes, and interview selection pipelines.
            </p>
            <a href="https://github.com/24f3004027/Placement_Portal_Application_V2" target="_blank" class="repo-link">
                💻 GitHub Repository &rarr;
            </a>
        </div>
        """, unsafe_allow_html=True)

# TAB 2: RUST
with tab_rust:
    st.markdown("""
    <div style="display: flex; justify-content: center;">
        <div class="glass-card" style="max-width: 800px; width: 100%;">
            <span class="pill-badge pill-amber">Systems Programming</span>
            <span class="pill-badge pill-cyan">Memory Safety & Concurrency</span>
            <h2 style="color: #ffffff; margin: 8px 0 12px 0; font-weight: 800;">🦀 Rust Projects Monorepo</h2>
            <p style="color: #94a3b8; font-size: 1rem; margin-bottom: 20px; line-height: 1.6;">
                A dedicated collection of low-level systems programming tools, high-concurrency utilities, CLI parsers, zero-cost abstraction patterns, and memory safety explorations built in Rust.
            </p>
            <a href="https://github.com/RSNPIIT/Rust-Projects" target="_blank" class="repo-link" style="font-size: 1.1rem;">
                🔗 Open Repository: github.com/RSNPIIT/Rust-Projects &rarr;
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# TAB 3: VUE
with tab_vue:
    st.markdown("""
    <div style="display: flex; justify-content: center;">
        <div class="glass-card" style="max-width: 800px; width: 100%;">
            <span class="pill-badge pill-emerald">Frontend Framework</span>
            <span class="pill-badge pill-cyan">Reactive UI Components</span>
            <h2 style="color: #ffffff; margin: 8px 0 12px 0; font-weight: 800;">⚡ Vue.js Projects Monorepo</h2>
            <p style="color: #94a3b8; font-size: 1rem; margin-bottom: 20px; line-height: 1.6;">
                Central repository of reactive web frontend applications, custom component libraries, state management patterns, and interactive single-page interfaces (SPA) built with Vue.js.
            </p>
            <a href="https://github.com/RSNPIIT/Vue-Projects" target="_blank" class="repo-link" style="font-size: 1.1rem;">
                🔗 Open Repository: github.com/RSNPIIT/Vue-Projects &rarr;
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. Centered Future Horizons Notice & Footer
# -----------------------------------------------------------------------------
st.markdown("""
<div class="glass-card" style="margin-top: 35px; border-color: rgba(56, 189, 248, 0.4); text-align: center; padding: 35px;">
    <h3 style="color: #38bdf8; font-weight: 800; font-size: 1.8rem; margin-bottom: 8px;">
        Learning much more and <span style="color: #ffffff;">A lot more to come...</span>
    </h3>
    <p style="color: #94a3b8; font-weight: 700; font-size: 1.25rem; margin-bottom: 0;">
        stay tuned 🔥
    </p>
</div>

<div style="text-align: center; margin-top: 40px; padding-bottom: 20px; color: #64748b; font-size: 0.85rem;">
    RAMRUP SATPATI (রামরূপ সাতপতি) &bull; Released under GNU General Public License v3.0 (GNU GPLv3) &copy; 2026
</div>
""", unsafe_allow_html=True)