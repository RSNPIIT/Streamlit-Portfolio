import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Ramrup Satpati | Ultra-Premium Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# 2. Global Styling Injection
# -----------------------------------------------------------------------------
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Hind+Siliguri:wght@600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">

<style>
/* Hide Default Streamlit Chrome */
[data-testid="stSidebar"], section[data-testid="stSidebar"], [data-testid="collapsedControl"] {
    display: none !important;
}
header[data-testid="stHeader"] {
    background: transparent !important;
}
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 3rem !important;
    max-width: 1280px !important;
}

:root {
    --bg-dark: #070a13;
    --card-glass: rgba(13, 19, 36, 0.85);
    --border-glass: rgba(56, 189, 248, 0.22);
    --border-hover: rgba(56, 189, 248, 0.65);
    --accent-cyan: #38bdf8;
    --accent-yellow: #facc15;
    --accent-emerald: #10b981;
    --accent-rose: #f43f5e;
}

body, .stApp {
    background-color: var(--bg-dark) !important;
    color: #f8fafc !important;
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
}

/* SECTION HEADER */
.section-header {
    text-align: center !important;
    margin-top: 30px;
    margin-bottom: 30px;
}
.section-title {
    font-size: 2.5rem;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.5px;
    margin-bottom: 6px;
}
.section-desc {
    color: #94a3b8;
    font-size: 1.05rem;
}

/* CENTERED STREAMLIT TABS */
.stTabs [data-baseweb="tab-list"] {
    justify-content: center !important;
    gap: 12px;
    background: rgba(13, 19, 36, 0.75);
    padding: 8px;
    border-radius: 16px;
    border: 1px solid var(--border-glass);
    margin-bottom: 30px;
}
.stTabs [data-baseweb="tab"] {
    height: 48px;
    border-radius: 12px;
    color: #94a3b8;
    font-weight: 700;
    font-size: 0.98rem;
    padding: 0 28px;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #0284c7, #06b6d4) !important;
    color: #ffffff !important;
    box-shadow: 0 6px 20px rgba(2, 132, 199, 0.45);
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
# 3. Ultra-Premium 3D Interactive Hero Component (YouTube Tutorial Inspired)
# -----------------------------------------------------------------------------
hero_component_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>3D Ultra-Premium Hero</title>
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Hind+Siliguri:wght@600;700&family=Plus+Jakarta+Sans:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background-color: #070a13;
            color: #f8fafc;
            font-family: 'Plus Jakarta Sans', sans-serif;
            overflow: hidden;
            width: 100vw;
            height: 620px;
            position: relative;
        }

        /* Top Navbar */
        .top-navbar {
            position: absolute;
            top: 20px;
            left: 0;
            width: 100%;
            padding: 0 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 20;
        }
        .nav-email {
            font-size: 0.88rem;
            color: #94a3b8;
            font-weight: 600;
            letter-spacing: 0.5px;
        }
        .nav-links {
            display: flex;
            gap: 30px;
        }
        .nav-link-item {
            color: #e2e8f0;
            text-decoration: none;
            font-size: 0.82rem;
            font-weight: 800;
            letter-spacing: 2px;
            text-transform: uppercase;
            transition: color 0.3s;
        }
        .nav-link-item:hover {
            color: #38bdf8;
        }

        /* Far Left Floating Social Sidebar */
        .social-sidebar {
            position: absolute;
            left: 35px;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            flex-direction: column;
            gap: 24px;
            z-index: 20;
        }
        .social-icon-btn {
            color: #94a3b8;
            text-decoration: none;
            font-size: 0.85rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.3s;
        }
        .social-icon-btn:hover {
            color: #38bdf8;
            transform: translateX(4px);
        }

        /* 3D WebGL Canvas */
        #webgl-canvas {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
        }

        /* Center Glow Halo */
        .center-halo {
            position: absolute;
            top: 45%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 480px;
            height: 480px;
            background: radial-gradient(circle, rgba(56, 189, 248, 0.28) 0%, rgba(2, 132, 199, 0.12) 45%, transparent 70%);
            z-index: 2;
            pointer-events: none;
            filter: blur(20px);
        }

        /* Hero Content Grid (Left & Right Text Columns) */
        .hero-layout {
            position: relative;
            z-index: 10;
            width: 100%;
            height: 100%;
            display: grid;
            grid-template-columns: 1fr 340px 1fr;
            align-items: center;
            padding: 0 70px;
        }

        /* Left Content Column */
        .left-col {
            text-align: right;
            padding-right: 30px;
        }
        .small-tag {
            color: #38bdf8;
            font-size: 1.15rem;
            font-weight: 600;
            margin-bottom: 4px;
        }
        .main-name {
            font-size: 3.2rem;
            font-weight: 900;
            line-height: 1.05;
            color: #ffffff;
            letter-spacing: -1px;
            margin-bottom: 4px;
        }
        .bengali-name {
            font-size: 2.2rem;
            font-weight: 700;
            color: #fb923c;
            font-family: 'Hind Siliguri', sans-serif;
            text-shadow: 0 0 20px rgba(251, 146, 60, 0.4);
        }

        /* Right Content Column */
        .right-col {
            text-align: left;
            padding-left: 30px;
        }
        .role-tag {
            color: #94a3b8;
            font-size: 1.15rem;
            font-weight: 600;
            margin-bottom: 4px;
        }
        .role-highlight {
            font-size: 2.5rem;
            font-weight: 900;
            line-height: 1.1;
            background: linear-gradient(135deg, #38bdf8, #06b6d4, #f43f5e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
            margin-bottom: 6px;
        }
        .sub-tagline {
            color: #e2e8f0;
            font-size: 1rem;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        /* Bottom Giant Typography Composition */
        .bottom-banner {
            position: absolute;
            bottom: 30px;
            left: 0;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: baseline;
            gap: 20px;
            z-index: 15;
            pointer-events: none;
        }
        .script-yellow-left {
            font-family: 'Caveat', cursive;
            font-size: 3.2rem;
            color: #facc15;
            transform: rotate(-6deg);
            text-shadow: 0 0 15px rgba(250, 204, 21, 0.4);
        }
        .giant-portfolio-text {
            font-size: 5.5rem;
            font-weight: 900;
            letter-spacing: 4px;
            color: #ffffff;
            text-transform: uppercase;
            text-shadow: 0 10px 40px rgba(0, 0, 0, 0.8), 0 0 30px rgba(56, 189, 248, 0.3);
        }
        .script-yellow-right {
            font-family: 'Caveat', cursive;
            font-size: 3.2rem;
            color: #facc15;
            transform: rotate(6deg);
            text-shadow: 0 0 15px rgba(250, 204, 21, 0.4);
        }

        /* Bottom Gradient Fade */
        .bottom-fade {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 140px;
            background: linear-gradient(to bottom, transparent 0%, #070a13 100%);
            z-index: 3;
            pointer-events: none;
        }
    </style>
</head>
<body>

    <!-- Top Navbar -->
    <div class="top-navbar">
        <div class="nav-email">ramrupsatpati@gmail.com</div>
        <div class="nav-links">
            <a href="#about" class="nav-link-item">ABOUT</a>
            <a href="#work" class="nav-link-item">WORK</a>
            <a href="#repos" class="nav-link-item">REPOSITORIES</a>
            <a href="mailto:ramrupsatpati@gmail.com" class="nav-link-item">CONTACT</a>
        </div>
    </div>

    <!-- Vertical Social Bar -->
    <div class="social-sidebar">
        <a href="https://github.com/RSNPIIT" target="_blank" class="social-icon-btn">🐙 GitHub</a>
        <a href="https://github.com/24f3004027" target="_blank" class="social-icon-btn">💻 IITM</a>
        <a href="https://www.linkedin.com/in/ramrup-satpati-683970341" target="_blank" class="social-icon-btn">💼 LinkedIn</a>
    </div>

    <!-- WebGL Canvas & Glow -->
    <canvas id="webgl-canvas"></canvas>
    <div class="center-halo"></div>
    <div class="bottom-fade"></div>

    <!-- Hero Content Layout -->
    <div class="hero-layout">
        <!-- Left Column -->
        <div class="left-col">
            <div class="small-tag">Hello! I'm</div>
            <div class="main-name">RAMRUP<br>SATPATI</div>
            <div class="bengali-name">রামরূপ সাতপতি</div>
        </div>

        <!-- Center 3D Space (Canvas renders behind this gap) -->
        <div></div>

        <!-- Right Column -->
        <div class="right-col">
            <div class="role-tag">A Full Stack</div>
            <div class="role-highlight">SYSTEMS & AI<br>ENGINEER</div>
            <div class="sub-tagline">Jack of all Trades</div>
        </div>
    </div>

    <!-- Bottom Giant Typography -->
    <div class="bottom-banner">
        <span class="script-yellow-left">Jack of all Trades</span>
        <span class="giant-portfolio-text">PORTFOLIO</span>
        <span class="script-yellow-right">RSNPIIT</span>
    </div>

    <!-- Three.js 3D Cyber Core Animation -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const canvas = document.getElementById('webgl-canvas');
            const scene = new THREE.Scene();

            const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 0, 14);

            const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

            // Lighting
            const ambient = new THREE.AmbientLight(0x0f172a, 2.0);
            scene.add(ambient);

            const cyanLight = new THREE.PointLight(0x38bdf8, 3, 50);
            cyanLight.position.set(5, 5, 10);
            scene.add(cyanLight);

            const roseLight = new THREE.PointLight(0xf43f5e, 3, 50);
            roseLight.position.set(-5, -5, 10);
            scene.add(roseLight);

            // 3D Core Sphere with Icosahedron Wireframe Outer Shell
            const coreGroup = new THREE.Group();

            // Inner Glowing Sphere
            const innerGeo = new THREE.SphereGeometry(2.8, 32, 32);
            const innerMat = new THREE.MeshPhongMaterial({
                color: 0x0284c7,
                emissive: 0x0369a1,
                specular: 0x38bdf8,
                shininess: 80,
                flatShading: true
            });
            const innerSphere = new THREE.Mesh(innerGeo, innerMat);
            coreGroup.add(innerSphere);

            // Outer Wireframe Cyber Shell
            const outerGeo = new THREE.IcosahedronGeometry(4.2, 2);
            const outerMat = new THREE.MeshBasicMaterial({
                color: 0x38bdf8,
                wireframe: true,
                transparent: true,
                opacity: 0.45
            });
            const outerShell = new THREE.Mesh(outerGeo, outerMat);
            coreGroup.add(outerShell);

            // Orbiting Particle Ring
            const particleCount = 120;
            const particleGeo = new THREE.BufferGeometry();
            const positions = new Float32Array(particleCount * 3);

            for (let i = 0; i < particleCount; i++) {
                const angle = (i / particleCount) * Math.PI * 2;
                const radius = THREE.MathUtils.randFloat(5.2, 7.5);
                positions[i * 3] = Math.cos(angle) * radius;
                positions[i * 3 + 1] = THREE.MathUtils.randFloat(-1.2, 1.2);
                positions[i * 3 + 2] = Math.sin(angle) * radius;
            }

            particleGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
            const particleMat = new THREE.PointsMaterial({
                color: 0xfacc15,
                size: 0.15,
                transparent: true,
                opacity: 0.85
            });
            const particleRing = new THREE.Points(particleGeo, particleMat);
            coreGroup.add(particleRing);

            scene.add(coreGroup);

            // Mouse Interactive Tilt
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

                // Rotate 3D Core
                innerSphere.rotation.y = time * 0.3;
                outerShell.rotation.y = -time * 0.2;
                outerShell.rotation.x = time * 0.15;
                particleRing.rotation.y = time * 0.4;

                // Mouse Parallax Smooth Interpolation
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

# Render Ultra-Premium Hero Component
components.html(hero_component_html, height=620, scrolling=False)

# -----------------------------------------------------------------------------
# 4. Centered Repositories Subsection Header
# -----------------------------------------------------------------------------
st.markdown("""
<div class="section-header">
    <div class="section-title">🚀 Portfolio Repositories & Systems</div>
    <div class="section-desc">Full-stack web applications, machine learning architectures, and systems repositories</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. Centered Project Tabs
# -----------------------------------------------------------------------------
tab_python, tab_rust, tab_vue = st.tabs(["🐍 Python & AI/ML Projects", "🦀 Rust Systems Projects", "⚡ Vue.js Projects"])

# TAB 1: PYTHON & AI/ML
with tab_python:
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
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
# 6. Future Horizons Notice & Footer
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