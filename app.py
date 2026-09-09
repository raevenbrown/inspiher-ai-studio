import os
import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(
    page_title="The Brown Girls Creative Studio | AI Growth Assistant",
    page_icon="🤎",
    layout="wide"
)

# 2. Studio Brand Styling
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400;1,9..144,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stAppDeployButton {display: none;}
    a.anchorjs-link, [data-testid="stHeaderActionElements"] {display: none !important;}
    
    .stApp {
        background-color: #1A120B !important;
        background-image: 
            linear-gradient(to right, rgba(197, 155, 88, 0.08) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(197, 155, 88, 0.08) 1px, transparent 1px) !important;
        background-size: 44px 44px !important;
        color: #EADBC8 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    .studio-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0px 24px 0px;
        border-bottom: 1px solid rgba(197, 155, 88, 0.18);
        margin-bottom: 30px;
    }

    .brand-logo {
        font-family: 'Fraunces', serif !important;
        font-size: 24px !important;
        font-weight: 700 !important;
        color: #FAF5E9 !important;
        text-decoration: none !important;
        letter-spacing: -0.3px !important;
        display: inline-flex !important;
        align-items: baseline !important;
        gap: 6px !important;
    }
    .brand-logo:hover, .brand-logo:visited, .brand-logo:active {
        color: #FAF5E9 !important;
        text-decoration: none !important;
    }
    .brand-logo .accent-gold {
        color: #C59B58 !important;
    }

    .nav-links {
        display: flex;
        gap: 24px;
        align-items: center;
        font-size: 13.5px;
        font-weight: 500;
        color: #D4C3B3;
    }
    
    .nav-audit-btn {
        background: #C59B58 !important;
        color: #1A120B !important;
        font-weight: 700 !important;
        font-size: 13px !important;
        padding: 9px 18px !important;
        border-radius: 6px !important;
        text-decoration: none !important;
        box-shadow: 0 4px 12px rgba(197, 155, 88, 0.25) !important;
    }

    .section-eyebrow {
        color: #C59B58;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }

    .hero-title {
        font-family: 'Fraunces', serif;
        font-size: 46px;
        font-weight: 700;
        line-height: 1.15;
        color: #FAF5E9;
        letter-spacing: -0.8px;
        margin-bottom: 16px;
    }
    .hero-title em {
        font-family: 'Fraunces', serif;
        font-style: italic;
        color: #C59B58;
        font-weight: 400;
    }

    .hero-sub {
        font-size: 15px;
        line-height: 1.65;
        color: #C4B5A5;
        max-width: 680px;
        margin-bottom: 32px;
    }

    label {
        color: #FAF5E9 !important;
        font-size: 13px !important;
        font-weight: 600 !important;
    }
    
    div[data-baseweb="select"] {
        background-color: #140D07 !important;
        border: 1px solid rgba(197, 155, 88, 0.3) !important;
        border-radius: 6px !important;
        color: #FAF5E9 !important;
    }

    .stTextInput input {
        background-color: #140D07 !important;
        color: #FAF5E9 !important;
        border: 1px solid rgba(197, 155, 88, 0.3) !important;
        border-radius: 6px !important;
        padding: 10px 14px !important;
    }
    .stTextInput input:focus {
        border-color: #C59B58 !important;
        box-shadow: 0 0 0 1px #C59B58 !important;
    }

    .stButton button {
        background-color: #C59B58 !important;
        color: #1A120B !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 12px 24px !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 12px rgba(197, 155, 88, 0.25) !important;
    }
    .stButton button:hover {
        background-color: #D6AA66 !important;
        transform: translateY(-1px);
    }
    
    .status-badge {
        display: inline-block;
        font-size: 11px;
        padding: 4px 10px;
        border-radius: 12px;
        margin-bottom: 14px;
        font-weight: 600;
        background: rgba(16, 185, 129, 0.2);
        color: #10B981;
        border: 1px solid rgba(16, 185, 129, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# 3. Navigation Bar
st.markdown("""
<div class="studio-nav">
    <a href="https://raevenbrown.github.io/thebrowngirlsstudio/index.html#education" class="brand-logo" target="_blank">
        <span>the brown girls</span><span class="accent-gold">creative studio</span>
    </a>
    <div class="nav-links">
        <span>Studio Services</span>
        <span>Creative Metrix</span>
        <span>School Labs</span>
        <span>Apprenticeships</span>
        <a href="https://raevenbrown.github.io/thebrowngirlsstudio/index.html#education" target="_blank" class="nav-audit-btn">Run Free Audit</a>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Hero Section
st.markdown("""
<div class="section-eyebrow">— DATA ARCHITECTURE · AI INNOVATION · WORKFORCE IMPACT</div>
<div class="hero-title">Building the front end, back end, <em>and future</em> of local business.</div>
<div class="hero-sub">
    We turn disconnected operations into streamlined, data-driven growth machines with Creative Metrix — 
    while training the next generation of AI and tech talent right here in our community.
</div>
""", unsafe_allow_html=True)

st.markdown('<span class="status-badge">🟢 HIGH-SPEED AI ENGINE ACTIVE</span>', unsafe_allow_html=True)

# 5. Groq Setup
raw_key = st.secrets.get("GROQ_API_KEY", os.environ.get("GROQ_API_KEY", ""))
groq_key = str(raw_key).strip() if raw_key else ""
client = Groq(api_key=groq_key) if groq_key else None

STUDIO_SYSTEM_INSTRUCTION = """
You are the Principal Growth Architect for "The Brown Girls Creative Studio".
Deliver clear, highly tactical, revenue-grounded, and actionable strategic blueprints.

Structure every strategy into:
1. 🎯 The Revenue Math & Target Blueprint (Breakdown of prices, package units, and monthly trajectory)
2. ⚡ Phase 1: High-Conversion Offer Setup (Days 1–30)
3. 📈 Phase 2: Pipeline & Systems Engine (Days 31–60)
4. 💼 Phase 3: High-Ticket Close & Retainer Scaling (Days 61–90)
5. 🤎 Executive Standard (1 non-negotiable operational standard)
"""

# 6. Interactive Studio AI Assistant Panel
st.markdown('<div class="section-eyebrow">— INTERACTIVE AI STRATEGY ENGINE</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    persona_options = [
        "Creative Entrepreneur",
        "Content & Brand Strategy",
        "Operations & Automation",
        "Brand Identity & Design",
        "Client Acquisition"
    ]
    selected_persona = st.selectbox("Select Advisory Lens:", persona_options)
    placeholder_map = {
        "Creative Entrepreneur": "How to get $7k in 3 months with a marketing business",
        "Content & Brand Strategy": "How do I create short-form hooks that convert viewers into paying clients?",
        "Operations & Automation": "How do I automate client onboarding without writing complex code?",
        "Brand Identity & Design": "How do I position my business as an executive, high-ticket brand?",
        "Client Acquisition": "How do I pitch corporate clients and close bigger ongoing retainers?"
    }

with col2:
    user_input = st.text_input("Ask a Growth or Systems Question:", placeholder=placeholder_map[selected_persona])
    generate_btn = st.button("Generate Strategic Blueprint ✨")

# 7. Streaming Response Generation
if generate_btn:
    query = user_input.strip() if user_input.strip() else placeholder_map[selected_persona]
    st.markdown(f"### Strategic Output: *{selected_persona}*")
    message_placeholder = st.empty()

    if client:
        try:
            # Auto-detect the best active text model on your account
            all_models = [m.id for m in client.models.list().data if "whisper" not in m.id and "embed" not in m.id]
            selected_model = next((m for m in all_models if "llama" in m.lower()), all_models[0])

            stream = client.chat.completions.create(
                model=selected_model,
                messages=[
                    {"role": "system", "content": STUDIO_SYSTEM_INSTRUCTION},
                    {"role": "user", "content": f"Advisory Lens: {selected_persona}\nGoal: {query}"}
                ],
                temperature=0.7,
                stream=True
            )
            
            full_response = ""
            for chunk in stream:
                content = chunk.choices[0].delta.content or ""
                full_response += content
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)

        except Exception as e:
            st.error(f"Engine Error: {e}")
    else:
        st.warning("Please add `GROQ_API_KEY` under Streamlit Settings > Secrets.")
