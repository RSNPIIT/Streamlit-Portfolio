import streamlit as st

# -----------------------------------------------------------------------------
# 1. Page Configuration & Knight Red Flame CSS Injection
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Ramrup Satpati | রামরূপ সাতপতি",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Knight Red / Fiery Obsidian Visual Styling & Animated Flame Canvas Component
st.markdown("""
<style>
    /* Completely hide Streamlit Sidebar */
    [data-testid="stSidebar"], section[data-testid="stSidebar"] {
        display: none !important;
    }
    [data-testid="collapsedControl"] {
        display: none !important;
    }

    /* Global Page Styling — Knight with Crimson Flame Ambience */
    .stApp {
        background: 
            radial-gradient(circle at 50% 15%, rgba(239, 68, 68, 0.22) 0%, transparent 60%),
            linear-gradient(180deg, rgba(17, 2, 3, 0.88) 0%, rgba(30, 6, 10, 0.94) 50%, rgba(10, 1, 2, 0.98) 100%),
            url('https://images.unsplash.com/photo-1579783902614-a3fb3927b675?auto=format&fit=crop&w=1920&q=80') center center / cover no-repeat fixed !important;
        color: #fef2f2 !important;
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
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
        font-size: 1.5rem;
        font-weight: 700;
        color: #fca5a5;
        letter-spacing: 1px;
        text-transform: uppercase;
        border-left: 4px solid #ef4444;
        padding-left: 14px;
        margin-bottom: 24px;
    }

    /* Top Social Connect Bar */
    .connect-bar {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-bottom: 35px;
    }
    .connect-chip {
        display: inline-flex;
        align-items: center;
        background: rgba(30, 7, 10, 0.7);
        border: 1px solid rgba(239, 68, 68, 0.35);
        border-radius: 9999px;
        padding: 6px 16px;
        font-size: 0.88rem;
        color: #fca5a5;
        text-decoration: none;
        transition: all 0.25s ease;
    }
    .connect-chip:hover {
        background: rgba(239, 68, 68, 0.25);
        border-color: #f87171;
        color: #ffffff;
        transform: translateY(-2px);
    }

    /* Glassmorphism Cards with Glowing Ember Borders */
    .knight-card {
        background: rgba(26, 5, 8, 0.82);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        border: 1px solid rgba(239, 68, 68, 0.3);
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
        transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .knight-card:hover {
        transform: translateY(-4px);
        border-color: rgba(248, 113, 113, 0.65);
        box-shadow: 0 14px 40px rgba(239, 68, 68, 0.25);
    }

    /* Badge Pills */
    .pill-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 50rem;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-right: 8px;
        margin-bottom: 8px;
        text-transform: uppercase;
    }
    .pill-python { background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.4); }
    .pill-rust { background: rgba(249, 115, 22, 0.2); color: #fb923c; border: 1px solid rgba(249, 115, 22, 0.4); }
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

    /* Section Header */
    .section-header {
        font-size: 2.1rem;
        font-weight: 800;
        color: #fef2f2;
        letter-spacing: -0.5px;
        margin-top: 10px;
        margin-bottom: 6px;
    }
    .section-sub {
        color: #fca5a5;
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 24px;
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
                this.y = height + Math.random() * 80;
                this.vy = -(Math.random() * 1.9 + 0.8);
                this.vx = (Math.random() - 0.5) * 0.8;
                this.size = Math.random() * 3.5 + 1;
                this.alpha = Math.random() * 0.7 + 0.3;
                this.hue = Math.random() * 38; // Deep Red to Fiery Yellow-Amber
            }

            update() {
                this.y += this.vy;
                this.x += this.vx + Math.sin(this.y * 0.02) * 0.4;
                this.alpha -= 0.0032;
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
                ctx.shadowColor = `hsla(${this.hue}, 100%, 50%, 0.85)`;
                ctx.fill();
                ctx.restore();
            }
        }

        const embers = Array.from({ length: 65 }, () => new Ember());

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
# 2. Hero Section & Quick Links (Integrated Top Bar)
# -----------------------------------------------------------------------------
st.markdown("""
<div>
    <div class="hero-title">RAMRUP SATPATI</div>
    <div class="hero-bengali">রামরূপ সাতপতি</div>
    <div class="hero-subtext">Jack of all Trades &bull; RSNPIIT</div>
</div>

<div class="connect-bar">
    <a href="https://github.com/RSNPIIT" target="_blank" class="connect-chip">🐙 GitHub: RSNPIIT</a>
    <a href="https://github.com/24f3004027" target="_blank" class="connect-chip">💻 Work Repos: 24f3004027</a>
    <a href="https://www.linkedin.com/in/ramrup-satpati-683970341" target="_blank" class="connect-chip">💼 LinkedIn</a>
    <a href="mailto:ramrupsatpati@gmail.com" class="connect-chip">✉️ Contact Email</a>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. My Works Section
# -----------------------------------------------------------------------------
st.markdown('<div class="section-header">⚔️ My Works</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">_< Exploring systems, automation, distributed architectures, and machine learning</div>', unsafe_allow_html=True)

col_python, col_rust = st.columns([1.1, 0.9], gap="large")

# LEFT COLUMN: PYTHON PROJECTS
with col_python:
    st.markdown("""
    <h3 style="color: #f87171; border-bottom: 2px solid rgba(239, 68, 68, 0.4); padding-bottom: 8px; margin-bottom: 18px;">
        🐍 Python Projects
    </h3>
    """, unsafe_allow_html=True)

    # 1. Python Projects Repo
    st.markdown("""
    <div class="knight-card">
        <span class="pill-badge pill-python">Monorepo Collection</span>
        <span class="pill-badge pill-gpl">GNU GPLv3</span>
        <h4 style="margin: 6px 0 8px 0; color: #f87171;">🐍 Python Projects Repo</h4>
        <p style="color: #fca5a5; font-size: 0.9rem; margin-bottom: 10px;">
            A centralized monorepo of Python systems and mini-projects spanning Artificial Intelligence, Machine Learning, Deep Learning, NLP, and Cybersecurity.
        </p>
        <p style="margin-bottom: 0;">
            🔗 <a href="https://github.com/RSNPIIT/Python-Projects" target="_blank" class="repo-link">github.com/RSNPIIT/Python-Projects</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 2. HMS Repo
    st.markdown("""
    <div class="knight-card">
        <span class="pill-badge pill-python">Healthcare Architecture</span>
        <span class="pill-badge pill-gpl">GNU GPLv3</span>
        <h4 style="margin: 6px 0 8px 0; color: #f87171;">🏥 HMS Repo (PulseCare HMS v2.0)</h4>
        <p style="color: #fca5a5; font-size: 0.9rem; margin-bottom: 10px;">
            Full-stack Flask, SQLAlchemy & Flask-Login healthcare platform featuring Admin panels, Doctor clinical care notes, and Patient appointments.
        </p>
        <p style="margin-bottom: 0;">
            🌐 <a href="https://24f3004027.github.io/HMS-MAD-Projectv1/" target="_blank" class="repo-link">Live Showcase</a> &bull; 
            💻 <a href="https://github.com/24f3004027/HMS-MAD-Projectv1" target="_blank" class="repo-link">HMS Repo</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 3. Placement Portal Repo
    st.markdown("""
    <div class="knight-card">
        <span class="pill-badge pill-python">Full-Stack Application</span>
        <h4 style="margin: 6px 0 8px 0; color: #f87171;">📋 Placement Portal Repo</h4>
        <p style="color: #fca5a5; font-size: 0.9rem; margin-bottom: 10px;">
            Comprehensive placement automation application managing student applications, recruiter drives, interview scheduling, and offer status pipelines.
        </p>
        <p style="margin-bottom: 0;">
            💻 <a href="https://github.com/24f3004027/Placement_Portal_Application_V2" target="_blank" class="repo-link">Placement Portal Repo</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 4. Vehicle Parking Repo
    st.markdown("""
    <div class="knight-card">
        <span class="pill-badge pill-python">Smart Management</span>
        <h4 style="margin: 6px 0 8px 0; color: #f87171;">🚗 Vehicle Parking Repo</h4>
        <p style="color: #fca5a5; font-size: 0.9rem; margin-bottom: 10px;">
            ParkSmart vehicle parking reservation system featuring automated parking slot allocations, availability tracking, and admin dashboard metrics.
        </p>
        <p style="margin-bottom: 0;">
            💻 <a href="https://github.com/24f3004027/vehicle-parking-appv1" target="_blank" class="repo-link">Vehicle Parking Repo</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 5. DL GenAI Project Repo
    st.markdown("""
    <div class="knight-card">
        <span class="pill-badge pill-python">PyTorch &bull; GenAI</span>
        <h4 style="margin: 6px 0 8px 0; color: #f87171;">🧠 DL GenAI Project Repo (Smart MCQ Solver)</h4>
        <p style="color: #fca5a5; font-size: 0.9rem; margin-bottom: 10px;">
            PyTorch BiGRU with Multi-Head Self-Attention and 10-Seed Ensembling designed for context-augmented multiple choice question-answering.
        </p>
        <p style="margin-bottom: 0;">
            🌐 <a href="https://24f3004027.github.io/Deep_Learning_Project/" target="_blank" class="repo-link">Live Site</a> &bull; 
            💻 <a href="https://github.com/24f3004027/Deep_Learning_Project" target="_blank" class="repo-link">DL GenAI Repo</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 6. MLP Project Repo
    st.markdown("""
    <div class="knight-card">
        <span class="pill-badge pill-python">Gradient Boosting</span>
        <h4 style="margin: 6px 0 8px 0; color: #f87171;">🚜 MLP Project Repo (Price Prediction)</h4>
        <p style="color: #fca5a5; font-size: 0.9rem; margin-bottom: 10px;">
            End-to-end 5-Seed Gradient Boosting regression pipeline with extensive feature engineering for heavy equipment price estimation (RMSLE 0.1866).
        </p>
        <p style="margin-bottom: 0;">
            💻 <a href="https://github.com/24f3004027/MLP_Project" target="_blank" class="repo-link">MLP Project Repo</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

# RIGHT COLUMN: RUST PROJECTS
with col_rust:
    st.markdown("""
    <h3 style="color: #fb923c; border-bottom: 2px solid rgba(249, 115, 22, 0.4); padding-bottom: 8px; margin-bottom: 18px;">
        🦀 Rust Projects
    </h3>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="knight-card">
        <span class="pill-badge pill-rust">Systems Programming</span>
        <h4 style="margin: 6px 0 8px 0; color: #fb923c;">🦀 Rust-Projects</h4>
        <p style="color: #fca5a5; font-size: 0.9rem; margin-bottom: 12px;">
            Explorations in low-level systems programming, memory safety without garbage collection, zero-cost abstractions, lifetimes, CLI utilities, and high-concurrency tooling.
        </p>
        <p style="margin-bottom: 0;">
            🔗 <b>Repository</b>: <a href="https://github.com/RSNPIIT/Rust-Projects" target="_blank" class="repo-link" style="color: #fb923c;">github.com/RSNPIIT/Rust-Projects</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Growth & Horizons Card
    st.markdown("""
    <div class="knight-card" style="border-color: rgba(245, 158, 11, 0.4); background: rgba(45, 10, 14, 0.85); margin-top: 24px;">
        <h4 style="color: #fbbf24; margin-top: 0;">🚀 Future Horizons</h4>
        <blockquote style="border-left: 3px solid #ef4444; padding-left: 12px; color: #fca5a5; font-style: italic; margin: 12px 0;">
            "Growth comes from building, iterating, and sharing openly with the world."
        </blockquote>
        <p style="font-size: 1.25rem; font-weight: 800; color: #fef2f2; margin-bottom: 4px;">
            Learning much more and <br><span style="color: #fbbf24;">A lot more to come...</span>
        </p>
        <p style="color: #fca5a5; font-weight: 700; font-style: italic; margin: 0;">
            .. stay tuned 🔥
        </p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. Footer Notice
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.85rem;'>RAMRUP SATPATI (রামরূপ সাতপতি) &bull; Released under GNU General Public License v3.0 (GNU GPLv3) &copy; 2026.</p>", unsafe_allow_html=True)