import streamlit as st

# -----------------------------------------------------------------------------
# 1. Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Ramrup Satpati | রামরূপ সাতপতি",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# 2. Advanced 3D Cyber Cityscape Canvas & Glassmorphism Styling Injection
# -----------------------------------------------------------------------------
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

<style>
    /* Completely hide Streamlit Chrome & Sidebar */
    [data-testid="stSidebar"], section[data-testid="stSidebar"], [data-testid="collapsedControl"] {
        display: none !important;
    }
    header[data-testid="stHeader"] {
        background: transparent !important;
    }
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        max-width: 1280px !important;
    }

    /* Global Dark Theme Variables */
    :root {
        --bg-dark: #070d1a;
        --card-glass: rgba(10, 18, 36, 0.75);
        --border-glass: rgba(56, 189, 248, 0.22);
        --border-glass-hover: rgba(56, 189, 248, 0.55);
        --accent-cyan: #38bdf8;
        --accent-blue: #0284c7;
        --accent-emerald: #10b981;
        --accent-rose: #f43f5e;
        --accent-amber: #f59e0b;
    }

    body, .stApp {
        background-color: var(--bg-dark) !important;
        color: #f8fafc !important;
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
    }

    /* Fixed Background Canvas for 3D Cityscape */
    #cityscape-canvas {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        pointer-events: none;
        z-index: 0;
    }

    /* Hero Header Elements */
    .hero-badge {
        background: rgba(56, 189, 248, 0.12);
        border: 1px solid rgba(56, 189, 248, 0.35);
        color: #38bdf8;
        font-weight: 700;
        padding: 6px 18px;
        border-radius: 30px;
        font-size: 0.85rem;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 16px;
        backdrop-filter: blur(12px);
    }

    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        letter-spacing: -1.5px;
        line-height: 1.05;
        background: linear-gradient(135deg, #ffffff 0%, #38bdf8 45%, #0284c7 75%, #f43f5e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 6px;
        filter: drop-shadow(0 0 30px rgba(56, 189, 248, 0.3));
    }

    .hero-bengali {
        font-size: 2.6rem;
        font-weight: 700;
        background: linear-gradient(135deg, #f59e0b, #fb923c);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
        font-family: 'Hind Siliguri', sans-serif;
    }

    /* Subtext WITHOUT side border */
    .hero-subtext {
        font-size: 1.35rem;
        font-weight: 700;
        color: #94a3b8;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 24px;
        border-left: none !important;
        padding-left: 0 !important;
    }

    /* Navigation Chips */
    .connect-bar {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-bottom: 35px;
    }
    .connect-chip {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(10, 18, 36, 0.7);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 9999px;
        padding: 8px 20px;
        font-size: 0.9rem;
        font-weight: 600;
        color: #38bdf8;
        text-decoration: none !important;
        backdrop-filter: blur(12px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .connect-chip:hover {
        background: rgba(56, 189, 248, 0.2);
        border-color: #38bdf8;
        color: #ffffff;
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 10px 25px rgba(56, 189, 248, 0.3);
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: var(--card-glass);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid var(--border-glass);
        border-radius: 22px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    .glass-card:hover {
        transform: translateY(-6px);
        border-color: var(--border-glass-hover);
        box-shadow: 0 25px 50px rgba(56, 189, 248, 0.22);
    }

    /* Badges & Pills */
    .pill-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 12px;
        border-radius: 30px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-right: 6px;
        margin-bottom: 10px;
        text-transform: uppercase;
    }
    .pill-cyan { background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); }
    .pill-emerald { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }
    .pill-amber { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); }
    .pill-rose { background: rgba(244, 63, 94, 0.15); color: #fb7185; border: 1px solid rgba(244, 63, 94, 0.4); }

    /* Card Action Links */
    .repo-link {
        color: #38bdf8;
        font-weight: 700;
        text-decoration: none !important;
        transition: color 0.2s ease, text-shadow 0.2s ease;
    }
    .repo-link:hover {
        color: #34d399;
        text-shadow: 0 0 12px rgba(52, 211, 153, 0.5);
    }

    /* Streamlit Tab Customization */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background: rgba(10, 18, 36, 0.6);
        padding: 8px;
        border-radius: 16px;
        border: 1px solid var(--border-glass);
    }
    .stTabs [data-baseweb="tab"] {
        height: 48px;
        border-radius: 12px;
        color: #94a3b8;
        font-weight: 700;
        background: transparent;
        border: none;
        padding: 0 24px;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #0284c7, #06b6d4) !important;
        color: #ffffff !important;
        box-shadow: 0 4px 20px rgba(2, 132, 199, 0.4);
    }

    .section-title {
        font-size: 2rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 4px;
    }
    .section-desc {
        color: #94a3b8;
        font-size: 1rem;
        margin-bottom: 24px;
    }
</style>

<!-- 3D Cityscape & Vehicle Light Trails Canvas Script (Three.js) -->
<script>
    (function() {
        if (document.getElementById('cityscape-canvas')) return;
        
        const canvas = document.createElement('canvas');
        canvas.id = 'cityscape-canvas';
        document.body.prepend(canvas);

        function initThree() {
            if (typeof THREE === 'undefined') {
                setTimeout(initThree, 100);
                return;
            }

            const scene = new THREE.Scene();
            scene.fog = new THREE.FogExp2(0x070d1a, 0.0065);

            const camera = new THREE.PerspectiveCamera(55, window.innerWidth / window.innerHeight, 1, 1200);
            camera.position.set(0, 48, 145);
            camera.lookAt(0, 10, -60);

            const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

            // Lighting
            const ambientLight = new THREE.AmbientLight(0x0f172a, 2.2);
            scene.add(ambientLight);

            const dirLight = new THREE.DirectionalLight(0x38bdf8, 1.4);
            dirLight.position.set(60, 100, 50);
            scene.add(dirLight);

            // Ground Grid
            const groundGrid = new THREE.GridHelper(500, 50, 0x0284c7, 0x0f2942);
            groundGrid.position.y = -0.5;
            scene.add(groundGrid);

            // 1. Generate 3D Buildings
            const buildingGroup = new THREE.Group();
            const bldgMaterial = new THREE.MeshPhongMaterial({
                color: 0x0b192e,
                specular: 0x38bdf8,
                shininess: 30,
                flatShading: true
            });
            const edgeMaterial = new THREE.LineBasicMaterial({ color: 0x0ea5e9, transparent: true, opacity: 0.35 });

            const cityBounds = 160;
            const roadGap = 20;

            for (let x = -cityBounds; x <= cityBounds; x += 22) {
                for (let z = -cityBounds; z <= 60; z += 22) {
                    if (Math.abs(x) < roadGap || Math.abs(z + 40) < 14) continue;
                    if (Math.random() > 0.85) continue;

                    const height = THREE.MathUtils.randFloat(20, 85);
                    const width = THREE.MathUtils.randFloat(10, 16);
                    const depth = THREE.MathUtils.randFloat(10, 16);

                    const geometry = new THREE.BoxGeometry(width, height, depth);
                    const building = new THREE.Mesh(geometry, bldgMaterial);
                    building.position.set(x + THREE.MathUtils.randFloat(-2, 2), height / 2, z + THREE.MathUtils.randFloat(-2, 2));

                    const wireframe = new THREE.LineSegments(new THREE.EdgesGeometry(geometry), edgeMaterial);
                    building.add(wireframe);

                    if (height > 50) {
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

            // 2. Highway Vehicles (Animated Light Trails)
            const vehicleCount = 60;
            const vehicles = [];
            const carGeo = new THREE.BoxGeometry(1.2, 0.6, 2.8);
            const redCarMat = new THREE.MeshBasicMaterial({ color: 0xf43f5e });
            const blueCarMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });

            for (let i = 0; i < vehicleCount; i++) {
                const isNorthbound = Math.random() > 0.5;
                const laneX = isNorthbound ? THREE.MathUtils.randFloat(2.5, 7) : THREE.MathUtils.randFloat(-7, -2.5);
                const mat = isNorthbound ? blueCarMat : redCarMat;
                const car = new THREE.Mesh(carGeo, mat);

                car.position.set(laneX, 0.4, THREE.MathUtils.randFloat(-200, 120));
                car.userData = {
                    speed: (isNorthbound ? -1 : 1) * THREE.MathUtils.randFloat(0.4, 0.9),
                    minZ: -220,
                    maxZ: 130
                };
                scene.add(car);
                vehicles.push(car);
            }

            // Mouse movement parallax
            let mouseX = 0, mouseY = 0;
            let targetX = 0, targetY = 48;

            window.addEventListener("mousemove", (e) => {
                mouseX = (e.clientX / window.innerWidth - 0.5) * 18;
                mouseY = (e.clientY / window.innerHeight - 0.5) * 8;
            });

            window.addEventListener("resize", () => {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            });

            // Animation Loop
            let clock = new THREE.Clock();
            function animate() {
                requestAnimationFrame(animate);
                const delta = clock.getDelta();

                vehicles.forEach(car => {
                    car.position.z += car.userData.speed;
                    if (car.position.z < car.userData.minZ) car.position.z = car.userData.maxZ;
                    if (car.position.z > car.userData.maxZ) car.position.z = car.userData.minZ;
                });

                targetX += (mouseX - targetX) * 0.03;
                targetY += ((48 - mouseY) - targetY) * 0.03;
                camera.position.x = targetX;
                camera.position.y = targetY;
                camera.lookAt(0, 12, -40);

                renderer.render(scene, camera);
            }
            animate();
        }

        initThree();
    })();
</script>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. Hero Header Section
# -----------------------------------------------------------------------------
st.markdown("""
<div>
    <div class="hero-badge">
        <span>✨ Full-Stack Systems, AI/ML & CyberSec Engineer</span>
    </div>
    <div class="hero-title">RAMRUP SATPATI</div>
    <div class="hero-bengali">রামরূপ সাতপতি</div>
    <div class="hero-subtext">Jack of all Trades &bull; RSNPIIT</div>
</div>

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
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. Featured Works Section (Tabs for Python, Rust, Vue)
# -----------------------------------------------------------------------------
st.markdown('<div class="section-title">🚀 Portfolio Repositories & Systems</div>', unsafe_allow_html=True)
st.markdown('<div class="section-desc">Selected full-stack web applications, machine learning architectures, and systems projects</div>', unsafe_allow_html=True)

tab_python, tab_rust, tab_vue = st.tabs(["🐍 Python & AI/ML Projects", "🦀 Rust Systems Projects", "⚡ Vue.js Projects"])

# TAB 1: PYTHON & AI/ML
with tab_python:
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        # Monorepo
        st.markdown("""
        <div class="glass-card">
            <span class="pill-badge pill-cyan">Monorepo Collection</span>
            <span class="pill-badge pill-amber">GNU GPLv3</span>
            <h3 style="color: #ffffff; margin: 6px 0 10px 0; font-weight: 700;">🐍 Python Projects Monorepo</h3>
            <p style="color: #94a3b8; font-size: 0.92rem; margin-bottom: 16px; line-height: 1.5;">
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
            <p style="color: #94a3b8; font-size: 0.92rem; margin-bottom: 16px; line-height: 1.5;">
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
            <p style="color: #94a3b8; font-size: 0.92rem; margin-bottom: 16px; line-height: 1.5;">
                Clinical portal managing patient appointments, doctor schedules, administrative analytics, and automated clinical notes recording.
            </p>
            <div style="display: flex; gap: 14px;">
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
            <p style="color: #94a3b8; font-size: 0.92rem; margin-bottom: 16px; line-height: 1.5;">
                Deep Learning model using BiGRU with Multi-Head Self-Attention and 10-Seed Ensembling for context-augmented multiple choice question answering.
            </p>
            <div style="display: flex; gap: 14px;">
                <a href="https://24f3004027.github.io/Deep_Learning_Project/" target="_blank" class="repo-link">🌐 Live Documentation</a>
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
            <p style="color: #94a3b8; font-size: 0.92rem; margin-bottom: 16px; line-height: 1.5;">
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
            <p style="color: #94a3b8; font-size: 0.92rem; margin-bottom: 16px; line-height: 1.5;">
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
    <div class="glass-card" style="max-width: 800px;">
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
    """, unsafe_allow_html=True)

# TAB 3: VUE
with tab_vue:
    st.markdown("""
    <div class="glass-card" style="max-width: 800px;">
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
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. Future Horizons Notice & Footer
# -----------------------------------------------------------------------------
st.markdown("""
<div class="glass-card" style="margin-top: 35px; border-color: rgba(56, 189, 248, 0.4); text-align: center; padding: 35px;">
    <h3 style="color: #38bdf8; font-weight: 800; font-size: 1.8rem; margin-bottom: 8px;">
        Learning much more and <span style="color: #ffffff;">A lot more to come...</span>
    </h3>
    <p style="color: #94a3b8; font-weight: 700; font-size: 1.2rem; margin-bottom: 0;">
        stay tuned 🔥
    </p>
</div>

<div style="text-align: center; margin-top: 40px; padding-bottom: 20px; color: #64748b; font-size: 0.85rem;">
    RAMRUP SATPATI (রামরূপ সাতপতি) &bull; Released under GNU General Public License v3.0 (GNU GPLv3) &copy; 2026
</div>
""", unsafe_allow_html=True)