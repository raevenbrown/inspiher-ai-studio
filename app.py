import time
import re
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="The Brown Girls Creative Studio | AI Growth Assistant",
    page_icon="🤎",
    layout="wide"
)

# 2. Complete CSS Customization matching raevenbrown.github.io/thebrowngirlsstudio
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400;1,9..144,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>
    /* Hide Streamlit default header decorations & stray anchor badges */
    #MainMenu, footer, header {visibility: hidden;}
    .stAppDeployButton {display: none;}
    a.anchorjs-link, [data-testid="stHeaderActionElements"] {display: none !important;}
    
    /* Global Canvas Background & Architectural Grid */
    .stApp {
        background-color: #1A120B !important;
        background-image: 
            linear-gradient(to right, rgba(197, 155, 88, 0.08) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(197, 155, 88, 0.08) 1px, transparent 1px) !important;
        background-size: 44px 44px !important;
        color: #EADBC8 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Top Studio Header Navbar */
    .studio-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0px 24px 0px;
        border-bottom: 1px solid rgba(197, 155, 88, 0.18);
        margin-bottom: 30px;
    }

    /* Logo - Removes blue hyperlink & underline completely */
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

    /* Subtitle Tag */
    .section-eyebrow {
        color: #C59B58;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }

    /* Headline Editorial Serif */
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

    /* Form Fields Styling */
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

    /* Studio Mustard/Gold Primary Button */
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
</style>
""", unsafe_allow_html=True)

# 3. Top Navigation Header (Pure Cream + Gold, Zero Blue Links)
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

# 5. Rule-Based AI Knowledge Engine
def search_knowledge_base(raw_prompt: str, persona: str) -> str:
    p = raw_prompt.lower().strip()
    clean = re.sub(r"[?!.]", "", raw_prompt).strip()

    subject = re.sub(r"[?!.]", "", p)
    subject = re.sub(r"^(how (do|can|to|should) (i|we|you) |how (to|do|can) |what (is|are|does) |why (is|are|do|does) |can (i|you) )", "", subject).strip()
    topic = subject.capitalize() if subject else clean

    # 1. Monetization & $10k Packages
    if persona == "Creative Entrepreneur" or any(k in p for k in ["10k", "money", "price", "package", "sell"]):
        return (
            "💼 **[The Brown Girls Studio • Business Strategy]**\n\n"
            f"**Monetization Roadmap for \"{clean}\":**\n\n"
            "• **Step 1 (Value Over Hours):** Package high-touch deliverables into fixed monthly retainers. Stop trading hours for dollars.\n"
            "• **Step 2 (Unit Economics):** Reverse-engineer your $10k milestone: four $2,500 clients or five $2,000 active retainers.\n"
            "• **Step 3 (The Soft Launch):** Pre-sell to 3 pilot clients using personalized discovery calls before building complex landing pages!"
        )

    # 2. Content & Brand Strategy
    if persona == "Content & Brand Strategy" or any(k in p for k in ["video", "post", "hook", "content", "tiktok", "views"]):
        return (
            "🎬 **[The Brown Girls Studio • Content Lab]**\n\n"
            f"**Growth Strategy for \"{clean}\":**\n\n"
            "• **Step 1 (The Visual Hook):** Stop the scroll in the first 1.5 seconds by showcasing the end transformation or challenging an industry myth.\n"
            "• **Step 2 (High-Utility Breakdown):** Deliver 1 actionable SOP, template, or insight rather than vague tips.\n"
            "• **Step 3 (Conversion Call to Action):** Ask viewers to comment a specific keyword (e.g., 'SYSTEMS') to trigger an automated direct message!"
        )

    # 3. Operations & Workflow Automation
    if persona == "Operations & Automation" or any(k in p for k in ["automate", "system", "workflow", "crm", "scale"]):
        return (
            "⚙️ **[The Brown Girls Studio • Systems & Automation]**\n\n"
            f"**Operational Blueprint for \"{clean}\":**\n\n"
            "• **Step 1 (Audit Client Journey):** Map every touchpoint from intake form submission to onboarding and invoice generation.\n"
            "• **Step 2 (No-Code Bridges):** Connect your web forms directly to your CRM and project management board via Zapier or Make.\n"
            "• **Step 3 (Automated Delivery):** Instantly trigger welcome kits, calendar links, and agreements the second payment processes!"
        )

    # 4. Brand Identity & Design
    if persona == "Brand Identity & Design" or any(k in p for k in ["brand", "design", "logo", "aesthetic", "premium"]):
        return (
            "✨ **[The Brown Girls Studio • Brand Aesthetics]**\n\n"
            f"**Positioning Guide for \"{clean}\":**\n\n"
            "• **Step 1 (Warm Architectural Palette):** Anchor your brand in deep rich tones, warm neutrals, and ochre gold accents for an editorial look.\n"
            "• **Step 2 (Editorial Font Pairing):** Pair a classic serif header with a modern sans-serif body for immediate visual authority.\n"
            "• **Step 3 (Metric-Driven Proof):** Feature real case-study metrics, client dashboards, and workflow screenshots!"
        )

    # 5. Client Acquisition & Contracts
    if persona == "Client Acquisition" or any(k in p for k in ["client", "pitch", "contract", "lead"]):
        return (
            "📈 **[The Brown Girls Studio • Client Acquisition]**\n\n"
            f"**Pipeline Strategy for \"{clean}\":**\n\n"
            "• **Step 1 (Warm Pipeline Outreach):** Reach out to past partners and network contacts with your new service offerings and case studies.\n"
            "• **Step 2 (Value-First Video Audits):** Send 10 targeted 2-minute Loom teardowns identifying 2 immediate operational bottlenecks.\n"
            "• **Step 3 (24-Hour Proposals):** Present concise, 3-tiered proposals within 24 hours of every discovery session!"
        )

    # Fallback Advisory
    return (
        f"🤎 **[The Brown Girls Studio • Executive Advisory]**\n\n"
        f"**Strategic Focus for \"{clean}\":**\n\n"
        f"• **Identify the Highest-Leverage Task:** Zero in on the single action that moves the needle on {topic.lower()} this week.\n"
        "• **Sprint Execution:** Execute in two 45-minute distraction-free work blocks.\n"
        "• **Weekly Review:** Track results, refine your client messaging, and eliminate friction points every Friday!"
    )

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
        "Creative Entrepreneur": "How do I package my services to hit $10k/month?",
        "Content & Brand Strategy": "How do I create videos that convert viewers into paying clients?",
        "Operations & Automation": "How do I automate client onboarding without writing code?",
        "Brand Identity & Design": "How do I position my business as a luxury, high-ticket brand?",
        "Client Acquisition": "How do I pitch corporate clients and close bigger contracts?"
    }

with col2:
    user_input = st.text_input("Ask a Growth or Systems Question:", placeholder=placeholder_map[selected_persona])
    generate_btn = st.button("Generate Strategic Blueprint ✨")

# 7. Output Streaming
if generate_btn:
    if not user_input.strip():
        st.warning("⚠️ Please enter a strategic question or goal above.")
    else:
        with st.status("Analyzing Strategic Blueprint...", expanded=False):
            st.write(f'🔍 Query: "{user_input}"')
            time.sleep(0.3)
            st.write("Cross-referencing The Brown Girls Studio growth systems...")
            time.sleep(0.3)

        response = search_knowledge_base(user_input, selected_persona)

        message_placeholder = st.empty()
        full_text = ""
        for char in response:
            full_text += char
            message_placeholder.markdown(full_text + "▌")
            time.sleep(0.007)
        message_placeholder.markdown(full_text)
