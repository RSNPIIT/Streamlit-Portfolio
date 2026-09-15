import streamlit as st
from PIL import Image

# -----------------------------------------------------------------------------
# 1. Page Configuration & Custom CSS Injection
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Ramrup Satpati | Developer Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Glassmorphism & Cyberpunk-Modern Styling
st.markdown("""
<style>
    /* Global Page Styling */
    .main {
        background: linear-gradient(135deg, #090d16 0%, #0f172a 50%, #1e1b4b 100%);
        color: #f8fafc;
    }
    
    /* Glassmorphism Card Style */
    .glass-card {
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-4px);
        border-color: rgba(56, 189, 248, 0.5);
    }

    /* Badge & Tag Styling */
    .badge-tag {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-right: 6px;
        margin-bottom: 8px;
    }
    .tag-python { background: rgba(56, 189, 248, 0.2); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); }
    .tag-rust { background: rgba(249, 115, 22, 0.2); color: #f97316; border: 1px solid rgba(249, 115, 22, 0.4); }
    .tag-vue { background: rgba(65, 184, 131, 0.2); color: #41b883; border: 1px solid rgba(65, 184, 131, 0.4); }
    .tag-ai { background: rgba(168, 85, 247, 0.2); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.4); }
    .tag-cyber { background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.4); }
    .tag-gpl { background: rgba(34, 197, 94, 0.2); color: #4ade80; border: 1px solid rgba(34, 197, 94, 0.4); }

    /* Text Gradients */
    .gradient-text {
        background: linear-gradient(135deg, #38bdf8 0%, #2dd4bf 50%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    /* Button Styling */
    .stButton>button {
        background: linear-gradient(135deg, #0284c7 0%, #0d9488 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px 24px;
        font-weight: 700;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        opacity: 0.92;
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. Sidebar Profile & Navigation
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 10px 0;">
        <h2 class="gradient-text" style="margin-bottom: 0;">Ramrup Satpati</h2>
        <p style="color: #94a3b8; font-size: 0.9rem; margin-top: 4px;">RSNPIIT &bull; he/him</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.caption("🚀 Tech Generalist | Full Stack • AI/ML • Cybersecurity • UI/UX | Student @ IIT Madras")
    
    st.markdown("---")
    
    # Navigation Selector
    nav_choice = st.radio(
        "Navigation",
        [
            "🏠 Overview & Bio",
            "🐍 Python Dev (AI/ML/DL/CyberSec)",
            "🦀 Rust Dev (Systems)",
            "⚡ Vue.js Dev (Reactive Web)",
            "🎓 IIT Madras Academic S-Grade Showcase",
            "🚀 Learning Roadmap & Future Horizons",
            "📬 Contact & Connect"
        ]
    )
    
    st.markdown("---")
    
    # Key Stats Metrics
    st.markdown("### 📊 Quick Metrics")
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label="Contributions", value="773+")
    with col_b:
        st.metric(label="IIT CGPA", value="10.0 (S)")
        
    st.markdown("---")
    st.markdown("### 🌐 Profiles")
    st.markdown("• **Personal GitHub**: [RSNPIIT](https://github.com/RSNPIIT)")
    st.markdown("• **Institute GitHub**: [24f3004027](https://github.com/24f3004027)")
    st.markdown("• **LinkedIn**: [Ramrup Satpati](https://www.linkedin.com/in/ramrup-satpati-683970341)")

# -----------------------------------------------------------------------------
# 3. Main Section Router
# -----------------------------------------------------------------------------

# TAB 1: OVERVIEW & BIO
if nav_choice == "🏠 Overview & Bio":
    st.markdown("<h1 class='gradient-text'>Ramrup Satpati — Developer Portfolio</h1>", unsafe_allow_html=True)
    st.markdown("##### *Always learning, always building. Bridging high-level AI/ML frameworks with systems-level performance.*")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        <div class="glass-card">
            <h3>👤 About Me</h3>
            <p style="line-height: 1.7; color: #cbd5e1;">
                Welcome! I am a <b>Tech Generalist</b> and Student at <b>IIT Madras</b> passionate about building software across the entire computing stack.
                My work spans deep learning & generative AI, systems programming in <b>Rust</b>, reactive frontend design in <b>Vue.js</b>, and cybersecurity exploit analysis.
            </p>
            <br>
            <h4>🏛️ The Bazaar Philosophy of Open Source</h4>
            <p style="line-height: 1.7; color: #cbd5e1;">
                I adhere to the <b>Bazaar Philosophy of Open Source</b> (as articulated by Eric S. Raymond). Rather than keeping ideas isolated in single monolithic projects, 
                my personal repositories act as living, evolving collections of experiments, mini-apps, and architectural patterns.
            </p>
            <div>
                <span class="badge-tag tag-python">Python (AI/ML/Cyber)</span>
                <span class="badge-tag tag-rust">Rust Systems</span>
                <span class="badge-tag tag-vue">Vue.js Frontend</span>
                <span class="badge-tag tag-ai">Deep Learning</span>
                <span class="badge-tag tag-gpl">GNU GPLv3 Open Source</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="glass-card">
            <h3>⚡ Core Skill Domains</h3>
            <ul style="line-height: 2; color: #cbd5e1;">
                <li><b>Artificial Intelligence & ML</b>: PyTorch, Scikit-Learn, BiGRU, Multi-Head Self-Attention, Context-Augmented QA.</li>
                <li><b>Systems Programming</b>: Rust, Cargo, Memory Safety, Low-Level Concurrency, Zero-Cost Abstractions.</li>
                <li><b>Frontend Engineering</b>: Vue.js 3, Composition API, Glassmorphism UI 2.0, HTML5 3D Canvas Engines.</li>
                <li><b>Cybersecurity</b>: Exploit Scripting, Network Traffic Analysis, Web Vulnerability Auditing.</li>
                <li><b>Backend Systems</b>: Flask, SQLAlchemy, RESTful APIs, SQLite/MySQL Engine Optimization.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# TAB 2: PYTHON DEV
elif nav_choice == "🐍 Python Dev (AI/ML/DL/CyberSec)":
    st.markdown("<h1 class='gradient-text'>🐍 Python Development & Intelligence Systems</h1>", unsafe_allow_html=True)
    st.markdown("##### *Artificial Intelligence, Machine Learning, Deep Learning, Natural Language Processing & Cybersecurity Scripting.*")
    
    st.markdown("""
    <div class="glass-card">
        <h3>📦 Personal Monorepo Collection</h3>
        <p>A culmination of Python scripts, deep learning models, security toolkits, and NLP pipelines built under the Bazaar philosophy.</p>
        <p>🔗 <b>GitHub Collection Repo</b>: <a href="https://github.com/RSNPIIT/Python-Projects" target="_blank" style="color: #38bdf8;">https://github.com/RSNPIIT/Python-Projects</a> <span class="badge-tag tag-gpl">GNU GPLv3</span></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 💡 Core Focus Areas")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="glass-card">
            <h4>🧠 Deep Learning & NLP</h4>
            <p style="color: #94a3b8; font-size: 0.9rem;">
                PyTorch BiGRU architectures, Multi-Head Self-Attention layers, 10-Seed ensembling, and context-augmented Question Answering systems.
            </p>
            <span class="badge-tag tag-python">PyTorch</span>
            <span class="badge-tag tag-ai">NLP / Transformers</span>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="glass-card">
            <h4>📊 Machine Learning & Analytics</h4>
            <p style="color: #94a3b8; font-size: 0.9rem;">
                Gradient boosting regression, advanced feature engineering pipelines, RMSLE benchmarking, and automated model cross-validation.
            </p>
            <span class="badge-tag tag-python">Scikit-Learn</span>
            <span class="badge-tag tag-python">Pandas / NumPy</span>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="glass-card">
            <h4>🛡️ Cybersecurity & Scripting</h4>
            <p style="color: #94a3b8; font-size: 0.9rem;">
                Network packet inspection, automated security scanning, payload generation, and vulnerability auditing tools.
            </p>
            <span class="badge-tag tag-cyber">CyberSec</span>
            <span class="badge-tag tag-python">Socket & Scapy</span>
        </div>
        """, unsafe_allow_html=True)

# TAB 3: RUST DEV
elif nav_choice == "🦀 Rust Dev (Systems)":
    st.markdown("<h1 class='gradient-text'>🦀 Rust Systems Programming</h1>", unsafe_allow_html=True)
    st.markdown("##### *Explorations in memory safety, concurrency without data races, zero-cost abstractions, and blazing-fast execution.*")
    
    st.markdown("""
    <div class="glass-card">
        <h3>📦 Personal Rust Collection Repository</h3>
        <p>My ongoing journey mastering Rust ownership, lifetimes, trait systems, concurrency patterns, and CLI tools.</p>
        <p>🔗 <b>GitHub Collection Repo</b>: <a href="https://github.com/RSNPIIT/Rust-Projects" target="_blank" style="color: #f97316;">https://github.com/RSNPIIT/Rust-Projects</a></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### ⚙️ Why Rust?")
    
    r1, r2 = st.columns(2)
    with r1:
        st.markdown("""
        <div class="glass-card">
            <h4>🛡️ Memory Safety Without Garbage Collection</h4>
            <p style="color: #cbd5e1;">
                Rust's compile-time ownership model eliminates null pointer dereferences, dangling pointers, and data races before code ever reaches production.
            </p>
            <span class="badge-tag tag-rust">Ownership & Lifetimes</span>
            <span class="badge-tag tag-rust">Safe Concurrency</span>
        </div>
        """, unsafe_allow_html=True)
        
    with r2:
        st.markdown("""
        <div class="glass-card">
            <h4>⚡ Zero-Cost Abstractions & Systems Performance</h4>
            <p style="color: #cbd5e1;">
                High-level functional abstractions (iterators, closures, pattern matching) compile down to bare-metal machine code with zero runtime overhead.
            </p>
            <span class="badge-tag tag-rust">Bare-Metal Speed</span>
            <span class="badge-tag tag-rust">Cargo / Crates.io</span>
        </div>
        """, unsafe_allow_html=True)

# TAB 4: VUE.JS DEV
elif nav_choice == "⚡ Vue.js Dev (Reactive Web)":
    st.markdown("<h1 class='gradient-text'>⚡ Vue.js Modern Frontend Engineering</h1>", unsafe_allow_html=True)
    st.markdown("##### *Crafting responsive, reactive, glassmorphic user interfaces with modular component architectures.*")
    
    st.markdown("""
    <div class="glass-card">
        <h3>📦 Personal Vue.js Collection Repository</h3>
        <p>Experiments and web applications built with Vue.js, single-file components, dynamic state management, and modern CSS animation.</p>
        <p>🔗 <b>GitHub Collection Repo</b>: <a href="https://github.com/RSNPIIT/Vue-Projects" target="_blank" style="color: #41b883;">https://github.com/RSNPIIT/Vue-Projects</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    v1, v2 = st.columns(2)
    with v1:
        st.markdown("""
        <div class="glass-card">
            <h4>🎨 Composition API & Single File Components</h4>
            <p style="color: #cbd5e1;">
                Building scalable, maintainable UI logic with reactive refs, computed properties, and lifecycle hooks inside Vue 3 Single File Components (.vue).
            </p>
            <span class="badge-tag tag-vue">Vue 3</span>
            <span class="badge-tag tag-vue">Composition API</span>
        </div>
        """, unsafe_allow_html=True)
        
    with v2:
        st.markdown("""
        <div class="glass-card">
            <h4>💎 Glassmorphism UI 2.0 Aesthetics</h4>
            <p style="color: #cbd5e1;">
                Merging backdrop blur effects, vibrant gradient borders, smooth CSS transitions, and dark/light mode switches into seamless user experiences.
            </p>
            <span class="badge-tag tag-vue">UI/UX Design</span>
            <span class="badge-tag tag-vue">CSS / Backdrop Blur</span>
        </div>
        """, unsafe_allow_html=True)

# TAB 5: IIT MADRAS ACADEMIC PROJECTS
elif nav_choice == "🎓 IIT Madras Academic S-Grade Showcase":
    st.markdown("<h1 class='gradient-text'>🎓 IIT Madras Academic S-Grade Showcase</h1>", unsafe_allow_html=True)
    st.markdown("##### *Bridging Personal Open Source Repositories with Rigorous Academic Milestone Term Projects (10.0 CGPA / Grade S).*")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Project 1
    st.markdown("""
    <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h3 style="margin:0;">🧠 Deep Learning & GenAI — Smart MCQ Solver</h3>
            <span class="badge-tag tag-ai" style="font-size: 0.9rem;">GRADE S (10.0 CGPA) | SCORE: 91.00/100</span>
        </div>
        <p style="color: #38bdf8; font-weight: 600; margin-top: 6px;">Rank 60 (+264 Jump on Private Leaderboard)</p>
        <p style="color: #cbd5e1; line-height: 1.6;">
            <b>Architecture</b>: PyTorch BiGRU with Multi-Head Self-Attention & 10-Seed Ensembling for Context-Augmented QA.
            Trained and benchmarked on complex multiple-choice question datasets.
        </p>
        <p>
            🔗 <a href="https://24f3004027.github.io/Deep_Learning_Project/" target="_blank" style="color: #38bdf8;">Live Interactive Site</a> &bull; 
            💻 <a href="https://github.com/24f3004027/Deep_Learning_Project" target="_blank" style="color: #38bdf8;">GitHub Repository</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Project 2
    st.markdown("""
    <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h3 style="margin:0;">🚜 Machine Learning Practice — Heavy Equipment Price Prediction</h3>
            <span class="badge-tag tag-python" style="font-size: 0.9rem;">GRADE S (10.0 CGPA) | SCORE: 90.00/100</span>
        </div>
        <p style="color: #2dd4bf; font-weight: 600; margin-top: 6px;">Validation RMSLE: 0.18663</p>
        <p style="color: #cbd5e1; line-height: 1.6;">
            <b>Architecture</b>: End-to-end 5-Seed Gradient Boosting regression pipeline with automated feature engineering, outlier detection, and hyperparameter tuning.
        </p>
        <p>
            💻 <a href="https://github.com/24f3004027/MLP_Project" target="_blank" style="color: #2dd4bf;">GitHub Repository</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Project 3
    st.markdown("""
    <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h3 style="margin:0;">🏥 PulseCare HMS — Hospital Management System v2.0</h3>
            <span class="badge-tag tag-vue" style="font-size: 0.9rem;">FULL-STACK FLASK & 3D CANVAS</span>
        </div>
        <p style="color: #4ade80; font-weight: 600; margin-top: 6px;">Multi-Role Healthcare Management Platform</p>
        <p style="color: #cbd5e1; line-height: 1.6;">
            Full-stack Flask, SQLAlchemy, and Flask-Login app featuring Admin governance, Specialist Doctor clinical notes & prescription workflows, Patient booking, and a 3D Medical Plus rotating canvas visual engine.
        </p>
        <p>
            🌐 <a href="https://24f3004027.github.io/HMS-MAD-Projectv1/" target="_blank" style="color: #4ade80;">Live Showcase Landing Page</a> &bull; 
            💻 <a href="https://github.com/24f3004027/HMS-MAD-Projectv1" target="_blank" style="color: #4ade80;">GitHub Repository</a> <span class="badge-tag tag-gpl">GNU GPLv3</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

# TAB 6: LEARNING ROADMAP
elif nav_choice == "🚀 Learning Roadmap & Future Horizons":
    st.markdown("<h1 class='gradient-text'>🚀 Learning Roadmap & Future Horizons</h1>", unsafe_allow_html=True)
    st.markdown("##### *Learning more to come... Continually pushing boundaries across systems, AI models, and web technologies.*")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    l1, l2 = st.columns(2)
    with l1:
        st.markdown("""
        <div class="glass-card">
            <h4>🔮 Upcoming Technical Frontiers</h4>
            <ul style="line-height: 2; color: #cbd5e1;">
                <li><b>Generative AI & LLM Fine-Tuning</b>: Deep diving into LoRA, QLoRA parameter-efficient fine-tuning, and Retrieval-Augmented Generation (RAG).</li>
                <li><b>WebAssembly (Wasm) + Rust</b>: Compiling high-performance Rust modules directly into the browser for near-native web execution.</li>
                <li><b>Distributed Systems & Concurrency</b>: Building fault-tolerant distributed services with Tokio, gRPC, and message brokers.</li>
                <li><b>Advanced CyberSec Auditing</b>: Memory corruption analysis, reverse engineering binaries, and kernel-level security primitives.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with l2:
        st.markdown("""
        <div class="glass-card">
            <h4>🎯 Growth Mindset & Philosophy</h4>
            <blockquote style="border-left: 3px solid #38bdf8; padding-left: 12px; color: #94a3b8; font-style: italic;">
                "My imperfections are a part of me — growth comes from building, failing fast, iterating, and sharing openly with the world."
            </blockquote>
            <p style="color: #cbd5e1; margin-top: 15px;">
                Every repository, commit, and project is a building block in an endless journey of mastering technology and solving real-world challenges.
            </p>
        </div>
        """, unsafe_allow_html=True)

# TAB 7: CONTACT
elif nav_choice == "📬 Contact & Connect":
    st.markdown("<h1 class='gradient-text'>📬 Let's Connect</h1>", unsafe_allow_html=True)
    st.markdown("##### *Open for collaboration, open source contributions, research discussions, and engineering opportunities.*")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="glass-card">
        <h3>📍 Location & Contact Information</h3>
        <p style="font-size: 1.1rem; line-height: 2;">
            <b>Name</b>: Ramrup Satpati<br>
            <b>Personal GitHub</b>: <a href="https://github.com/RSNPIIT" target="_blank" style="color: #38bdf8;">github.com/RSNPIIT</a><br>
            <b>Institute GitHub</b>: <a href="https://github.com/24f3004027" target="_blank" style="color: #38bdf8;">github.com/24f3004027</a><br>
            <b>LinkedIn</b>: <a href="https://www.linkedin.com/in/ramrup-satpati-683970341" target="_blank" style="color: #38bdf8;">linkedin.com/in/ramrup-satpati-683970341</a><br>
            <b>Email</b>: <a href="mailto:ramrupsatpati@gmail.com" style="color: #38bdf8;">ramrupsatpati@gmail.com</a><br>
            <b>Location</b>: Jamshedpur, Jharkhand, India
        </p>
    </div>
    """, unsafe_allow_html=True)

# Footer Notice
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.85rem;'>Crafted with Streamlit &bull; Released under GNU General Public License v3.0 (GNU GPLv3) &copy; 2026 Ramrup Satpati.</p>", unsafe_allow_html=True)
