import streamlit as st

# -----------------------------------------------------------------------------
# 1. Page Configuration & Knight Red Flame CSS Injection
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Ramrup Satpati | রামরূপ সাতপতি",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Knight Red / Fiery Obsidian Visual Styling & Animated Flame Canvas Component
st.markdown("""
<style>
    /* Global Page Styling — Knight Crimson & Obsidian Background */
    .stApp {
        background: linear-gradient(135deg, #180305 0%, #2b060a 40%, #450a10 75%, #110203 100%) !important;
        color: #fef2f2 !important;
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: rgba(24, 3, 5, 0.85) !important;
        border-right: 1px solid rgba(239, 68, 68, 0.25) !important;
        backdrop-filter: blur(16px);
    }

    /* Fiery Glowing Banner & Text Headers */
    .hero-title {
        font-size: 3.8rem;
        font-weight: 900;
        letter-spacing: -1px;
        line-height: 1.1;
        background: linear-gradient(135deg, #f87171 0%, #ef4444 40%, #f59e0b 80%, #fbbf24 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 35px rgba(239, 68, 68, 0.4);
        margin-bottom: 4px;
    }

    .hero-bengali {
        font-size: 2.8rem;
        font-weight: 800;
        color: #fb923c;
        text-shadow: 0 0 25px rgba(249, 115, 22, 0.5);
        margin-bottom: 12px;
        font-family: 'Hind Siliguri', 'Noto Sans Bengali', sans-serif;
    }

    .hero-subtext {
        font-size: 1.6rem;
        font-weight: 700;
        color: #fca5a5;
        letter-spacing: 1px;
        text-transform: uppercase;
        border-left: 4px solid #ef4444;
        padding-left: 14px;
        margin-bottom: 28px;
    }

    /* Glassmorphism Cards with Glowing Ember Borders */
    .knight-card {
        background: rgba(30, 7, 10, 0.75);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        border: 1px solid rgba(239, 68, 68, 0.28);
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.45);
        transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .knight-card:hover {
        transform: translateY(-5px);
        border-color: rgba(248, 113, 113, 0.6);
        box-shadow: 0 18px 45px rgba(239, 68, 68, 0.25);
    }

    /* Badge Pills */
    .pill-badge {
        display: inline-block;
        padding: 5px 14px;
        border-radius: 50rem;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-right: 8px;
        margin-bottom: 10px;
        text-transform: uppercase;
    }
    .pill-python { background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.4); }
    .pill-rust { background: rgba(249, 115, 22, 0.2); color: #fb923c; border: 1px solid rgba(249, 115, 22, 0.4); }
    .pill-vue { background: rgba(34, 197, 94, 0.2); color: #4ade80; border: 1px solid rgba(34, 197, 94, 0.4); }
    .pill-gpl { background: rgba(234, 179, 8, 0.2); color: #facc15; border: 1px solid rgba(234, 179, 8, 0.4); }

    /* Action Links */
    .repo-link {
        color: #f87171;
        font-weight: 700;
        text-decoration: none;
        transition: color 0.2s ease;
    }
    .repo-link:hover {
        color: #fbbf24;
        text-decoration: underline;
    }

    /* Custom Streamlit Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        border-bottom: 1px solid rgba(239, 68, 68, 0.25);
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: rgba(30, 7, 10, 0.6);
        border-radius: 12px 12px 0 0;
        gap: 8px;
        padding: 10px 24px;
        color: #fca5a5;
        font-weight: 700;
        border: 1px solid rgba(239, 68, 68, 0.2);
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(239, 68, 68, 0.25) !important;
        color: #ffffff !important;
        border-color: #ef4444 !important;
    }
</style>

<!-- HTML5 Animated Rising Ember Flame Canvas Component -->
<script>
    (function() {
        if (document.getElementById('flame-canvas')) return;
        const canvas = document.createElement('canvas');
        canvas.id = 'flame-canvas';
        canvas.style.position = 'fixed';
        canvas.style.top = '0';
        canvas.style.left = '0';
        canvas.style.width = '100vw';
        canvas.style.height = '100vh';
        canvas.style.pointerEvents = 'none';
        canvas.style.zIndex = '0';
        document.body.prepend(canvas);

        const ctx = canvas.getContext('2d');
        let width = canvas.width = window.innerWidth;
        let height = canvas.height = window.innerHeight;

        window.addEventListener('resize', () => {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        });

        class Ember {
            constructor() {
                this.reset();
            }

            reset() {
                this.x = Math.random() * width;
                this.y = height + Math.random() * 100;
                this.vy = -(Math.random() * 1.8 + 0.8);
                this.vx = (Math.random() - 0.5) * 0.8;
                this.size = Math.random() * 3.5 + 1;
                this.alpha = Math.random() * 0.7 + 0.3;
                this.hue = Math.random() * 35; // Red to Orange-Yellow sparks
            }

            update() {
                this.y += this.vy;
                this.x += this.vx + Math.sin(this.y * 0.02) * 0.4;
                this.alpha -= 0.003;
                if (this.y < -20 || this.alpha <= 0) {
                    this.reset();
                }
            }

            draw() {
                ctx.save();
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fillStyle = `hsla(${this.hue}, 100%, 60%, ${this.alpha})`;
                ctx.shadowBlur = 10;
                ctx.shadowColor = `hsla(${this.hue}, 100%, 50%, 0.8)`;
                ctx.fill();
                ctx.restore();
            }
        }

        const embers = Array.from({ length: 55 }, () => new Ember());

        function animate() {
            ctx.clearRect(0, 0, width, height);
            for (let ember of embers) {
                ember.update();
                ember.draw();
            }
            requestAnimationFrame(animate);
        }
        animate();
    })();
</script>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. Sidebar Profile & Developer Links
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 12px 0;">
        <h2 style="color: #f87171; font-weight: 800; margin-bottom: 2px;">Ramrup Satpati</h2>
        <p style="color: #fb923c; font-weight: 700; font-size: 1.2rem; margin: 0;">রামরূপ সাতপতি</p>
        <p style="color: #fca5a5; font-size: 0.85rem; margin-top: 4px;">RSNPIIT &bull; he/him</p>
    </div>
    """, unsafe_allow_html=True)

    st.caption("🔥 Tech Generalist | Full Stack • AI/ML • Cybersecurity • UI/UX | Student @ IIT Madras")

    st.markdown("---")

    st.markdown("### 📊 Metrics & Activity")
    st.metric(label="GitHub Contributions (Past Year)", value="773+")
    st.metric(label="IIT Madras CGPA", value="10.0 (Grade S)")

    st.markdown("---")

    st.markdown("### 🌐 Profiles & Connect")
    st.markdown("• **Personal GitHub**: [RSNPIIT](https://github.com/RSNPIIT)")
    st.markdown("• **Institute GitHub**: [24f3004027](https://github.com/24f3004027)")
    st.markdown("• **LinkedIn**: [Ramrup Satpati](https://www.linkedin.com/in/ramrup-satpati-683970341)")
    st.markdown("• **Email**: [ramrupsatpati@gmail.com](mailto:ramrupsatpati@gmail.com)")
    st.markdown("• **Location**: Jamshedpur, Jharkhand")

# -----------------------------------------------------------------------------
# 3. Main Hero Banner
# -----------------------------------------------------------------------------
st.markdown("""
<div>
    <div class="hero-title">RAMRUP SATPATI</div>
    <div class="hero-bengali">রামরূপ সাতপতি</div>
    <div class="hero-subtext">Jack of all Trades</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. Project Showcase Cards (Python, Rust, Vue.js)
# -----------------------------------------------------------------------------
st.markdown("## ⚔️ Code Repositories & Collections")
st.caption("Embracing Eric S. Raymond's **Bazaar Philosophy of Open Source** — living collections of ideas, tools, and platforms.")

tab_python, tab_rust, tab_vue = st.tabs([
    "🐍 Python Projects",
    "🦀 Rust Projects",
    "⚡ Vue Projects"
])

# TAB 1: PYTHON PROJECTS
with tab_python:
    st.markdown("""
    <div class="knight-card">
        <span class="pill-badge pill-python">Personal Monorepo Collection</span>
        <span class="pill-badge pill-gpl">GNU GPLv3</span>
        <h3 style="color: #f87171; margin-top: 6px;">🐍 Python-Projects</h3>
        <p style="color: #fca5a5;">
            A culmination of Python projects and mini-projects built over time across Artificial Intelligence, Machine Learning, Deep Learning, NLP, and Cybersecurity.
        </p>
        <p>🔗 <b>Repository</b>: <a href="https://github.com/RSNPIIT/Python-Projects" target="_blank" class="repo-link">https://github.com/RSNPIIT/Python-Projects</a></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 🎓 Featured Python Systems & IIT Madras Academic Repositories")

    col_p1, col_p2 = st.columns(2)

    with col_p1:
        st.markdown("""
        <div class="knight-card">
            <span class="pill-badge pill-python">Full-Stack Web App</span>
            <span class="pill-badge pill-gpl">GNU GPLv3</span>
            <h4>🏥 PulseCare HMS (Hospital Management System v2.0)</h4>
            <p style="color: #fca5a5; font-size: 0.9rem;">
                Full-stack Flask, SQLAlchemy & Flask-Login healthcare platform featuring Admin controls, Doctor clinical care notes, Patient booking, and 3D Medical Plus canvas effects.
            </p>
            <p>
                🌐 <a href="https://24f3004027.github.io/HMS-MAD-Projectv1/" target="_blank" class="repo-link">Live Showcase</a> &bull; 
                💻 <a href="https://github.com/24f3004027/HMS-MAD-Projectv1" target="_blank" class="repo-link">HMS Repo</a>
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="knight-card">
            <span class="pill-badge pill-python">Vehicle Parking Platform</span>
            <h4>🚗 ParkSmart Vehicle Parking App</h4>
            <p style="color: #fca5a5; font-size: 0.9rem;">
                Smart parking space management web application with automated slot reservation, real-time availability tracking, and admin controls.
            </p>
            <p>
                💻 <a href="https://github.com/24f3004027/vehicle-parking-appv1" target="_blank" class="repo-link">Vehicle Parking App Repo</a>
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="knight-card">
            <span class="pill-badge pill-python">Full-Stack Portal</span>
            <h4>📋 Placement Portal Application V2</h4>
            <p style="color: #fca5a5; font-size: 0.9rem;">
                Full-stack academic placement portal application automating student job applications, recruiter drives, interview scheduling, and offer tracking.
            </p>
            <p>
                💻 <a href="https://github.com/24f3004027/Placement_Portal_Application_V2" target="_blank" class="repo-link">Placement Portal Repo</a>
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_p2:
        st.markdown("""
        <div class="knight-card">
            <span class="pill-badge pill-python">Grade S &bull; 10.0 CGPA</span>
            <span class="pill-badge pill-python">Rank 60 (+264 Jump)</span>
            <h4>🧠 Deep Learning & GenAI — Smart MCQ Solver</h4>
            <p style="color: #fca5a5; font-size: 0.9rem;">
                PyTorch BiGRU with Multi-Head Self-Attention & 10-Seed Ensembling for Context-Augmented QA. Score: 91.00/100.
            </p>
            <p>
                🌐 <a href="https://24f3004027.github.io/Deep_Learning_Project/" target="_blank" class="repo-link">Live Site</a> &bull; 
                💻 <a href="https://github.com/24f3004027/Deep_Learning_Project" target="_blank" class="repo-link">DL Repo</a>
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="knight-card">
            <span class="pill-badge pill-python">Grade S &bull; 10.0 CGPA</span>
            <span class="pill-badge pill-python">RMSLE 0.1866</span>
            <h4>🚜 Machine Learning Practice — Price Prediction</h4>
            <p style="color: #fca5a5; font-size: 0.9rem;">
                End-to-end 5-Seed Gradient Boosting regression pipeline with automated feature engineering for heavy equipment price estimation. Score: 90.00/100.
            </p>
            <p>
                💻 <a href="https://github.com/24f3004027/MLP_Project" target="_blank" class="repo-link">MLP Repo</a>
            </p>
        </div>
        """, unsafe_allow_html=True)

# TAB 2: RUST PROJECTS
with tab_rust:
    st.markdown("""
    <div class="knight-card">
        <span class="pill-badge pill-rust">Systems Programming</span>
        <h3 style="color: #fb923c; margin-top: 6px;">🦀 Rust-Projects</h3>
        <p style="color: #fca5a5;">
            My Rust learning journey and experiments in memory safety, zero-cost abstractions, lifetimes, cargo tools, and low-level system performance.
        </p>
        <p>🔗 <b>Repository</b>: <a href="https://github.com/RSNPIIT/Rust-Projects" target="_blank" class="repo-link" style="color: #fb923c;">https://github.com/RSNPIIT/Rust-Projects</a></p>
    </div>
    """, unsafe_allow_html=True)

# TAB 3: VUE PROJECTS
with tab_vue:
    st.markdown("""
    <div class="knight-card">
        <span class="pill-badge pill-vue">Frontend Engineering</span>
        <h3 style="color: #4ade80; margin-top: 6px;">⚡ Vue-Projects</h3>
        <p style="color: #fca5a5;">
            This repository is about my work in Vue.js as I continue to build reactive web applications, single-file components, and modern glassmorphic user interfaces.
        </p>
        <p>🔗 <b>Repository</b>: <a href="https://github.com/RSNPIIT/Vue-Projects" target="_blank" class="repo-link" style="color: #4ade80;">https://github.com/RSNPIIT/Vue-Projects</a></p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. Future Horizons & Down-Right Section
# -----------------------------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)

col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown("""
    <div class="knight-card">
        <h4>🔥 Growth Mindset & Philosophy</h4>
        <blockquote style="border-left: 3px solid #ef4444; padding-left: 12px; color: #fca5a5; font-style: italic;">
            "My imperfections are a part of me — growth comes from building, failing fast, iterating, and sharing openly with the world."
        </blockquote>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
    <div class="knight-card" style="border-color: rgba(245, 158, 11, 0.4); background: rgba(45, 10, 14, 0.85);">
        <h4 style="color: #fbbf24;">🚀 Future Horizons</h4>
        <p style="font-size: 1.35rem; font-weight: 800; color: #fef2f2; margin-bottom: 8px;">
            Learning much more and <br><span style="color: #fbbf24;">A lot more to come...</span>
        </p>
        <p style="color: #fca5a5; font-weight: 700; font-style: italic;">
            .. stay tuned 🔥
        </p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. Footer Notice
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.85rem;'>RAMRUP SATPATI (রামরূপ সাতপতি) &bull; Released under GNU General Public License v3.0 (GNU GPLv3) &copy; 2026.</p>", unsafe_allow_html=True)
