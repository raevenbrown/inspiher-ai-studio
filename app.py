import time
import re
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="The Brown Girls Creative Studio | AI Growth Assistant",
    page_icon="🤎",
    layout="centered"
)

# 2. Custom Brand Styling (The Brown Girls Creative Studio)
st.markdown("""
<style>
    /* Global Canvas Background */
    .stApp {
        background-color: #1C1614;
        color: #FDF8F5;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    /* Studio Header Styling */
    .brand-tag {
        display: inline-block;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #D4AF37;
        background: rgba(212, 175, 55, 0.12);
        border: 1px solid rgba(212, 175, 55, 0.3);
        padding: 4px 12px;
        border-radius: 20px;
        margin-bottom: 8px;
    }
    
    .studio-title {
        font-size: 28px;
        font-weight: 800;
        color: #FDF8F5;
        margin-bottom: 4px;
        letter-spacing: -0.5px;
    }
    
    .studio-sub {
        font-size: 14px;
        color: #BDB2AA;
        margin-bottom: 24px;
    }

    /* Form & Input Adjustments */
    label {
        color: #FDF8F5 !important;
        font-weight: 600 !important;
    }
    
    div[data-baseweb="select"] {
        background-color: #261F1D !important;
        border: 1px solid #453935 !important;
        border-radius: 8px !important;
        color: #FDF8F5 !important;
    }

    .stTextInput input {
        background-color: #261F1D !important;
        color: #FDF8F5 !important;
        border: 1px solid #453935 !important;
        border-radius: 8px !important;
    }
    .stTextInput input:focus {
        border-color: #D4AF37 !important;
        box-shadow: 0 0 0 1px #D4AF37 !important;
    }

    /* Button Styling */
    .stButton button {
        width: 100%;
        background: linear-gradient(135deg, #C86D51 0%, #B25A3F 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 20px !important;
        box-shadow: 0 4px 14px rgba(200, 109, 81, 0.3) !important;
        transition: transform 0.1s ease;
    }
    .stButton button:hover {
        filter: brightness(1.08);
        transform: translateY(-1px);
    }
</style>
""", unsafe_allow_html=True)

# 3. Universal Rule-Based Knowledge Engine
def search_knowledge_base(raw_prompt: str, persona: str) -> str:
    p = raw_prompt.lower().strip()
    clean = re.sub(r"[?!.]", "", raw_prompt).strip()

    subject = re.sub(r"[?!.]", "", p)
    subject = re.sub(r"^(how (do|can|to|should) (i|we|you) |how (to|do|can) |what (is|are|does) |why (is|are|do|does) |can (i|you) )", "", subject).strip()
    topic = subject.capitalize() if subject else clean

    # 1. BUSINESS & $10k MONETIZATION
    if persona == "Creative Entrepreneur" or any(k in p for k in ["10k", "money", "price", "package", "sell"]):
        return (
            "💼 **[The Brown Girls Studio • Business Strategy]**\n\n"
            f"**Monetization Roadmap for \"{clean}\":**\n\n"
            "• **Step 1 (Offer Clarification):** Move from hourly billing to value-based retainers. Structure one flagship offer that solves an expensive bottleneck for your client.\n"
            "• **Step 2 (Unit Economics):** Reverse-engineer your target (e.g., $10,000/month = four $2,500 clients or five $2,000 ongoing retainers).\n"
            "• **Step 3 (The Soft Launch):** Pre-sell to 3 pilot clients using personalized discovery calls before building complex landing pages!"
        )

    # 2. CONTENT CREATION & VIRAL HOOKS
    if persona == "Content & Brand Strategy" or any(k in p for k in ["video", "post", "hook", "content", "tiktok", "views"]):
        return (
            "🎬 **[The Brown Girls Studio • Content Lab]**\n\n"
            f"**Growth Strategy for \"{clean}\":**\n\n"
            "• **Step 1 (The Visual Hook):** Stop the scroll in the first 1.5 seconds by showing the finished result or debunking a common industry myth.\n"
            "• **Step 2 (Educational Core):** Share 1 specific insight, template, or breakdown rather than generic advice.\n"
            "• **Step 3 (Frictionless Conversion):** Give one direct call-to-action (e.g., 'Comment BLUEPRINT and I will send the exact workflow')!"
        )

    # 3. WORKFLOW AUTOMATION & SYSTEMS
    if persona == "Operations & Automation" or any(k in p for k in ["automate", "system", "workflow", "crm", "scale"]):
        return (
            "⚙️ **[The Brown Girls Studio • Systems & Automation]**\n\n"
            f"**Operational Blueprint for \"{clean}\":**\n\n"
            "• **Step 1 (Audit & Map):** Map out your customer journey on paper—from first inquiry to onboarding and invoice payment.\n"
            "• **Step 2 (Connect Tools):** Use Zapier or Make to connect your intake forms directly to your project tracker and CRM without manual data entry.\n"
            "• **Step 3 (Client Experience):** Trigger automated welcome emails, booking links, and agreements the second an invoice is approved!"
        )

    # 4. BRAND POSITIONING & LUXURY AESTHETICS
    if persona == "Brand Identity & Design" or any(k in p for k in ["brand", "design", "logo", "aesthetic", "premium"]):
        return (
            "✨ **[The Brown Girls Studio • Brand Aesthetics]**\n\n"
            f"**Positioning Guide for \"{clean}\":**\n\n"
            "• **Step 1 (Curated Palette):** Stick to 3 cohesive tones (a signature dark neutral, warm mid-tone, and metallic/terracotta accent) for instant luxury recognition.\n"
            "• **Step 2 (Editorial Typography):** Pair a classic serif header with a clean, modern sans-serif body font to command executive authority.\n"
            "• **Step 3 (Case Study Proof):** Showcase transformations and metrics rather than just deliverables!"
        )

    # 5. CLIENT ACQUISITION & PITCHING
    if persona == "Client Acquisition" or any(k in p for k in ["client", "pitch", "contract", "lead"]):
        return (
            "📈 **[The Brown Girls Studio • Client Acquisition]**\n\n"
            f"**Pipeline Strategy for \"{clean}\":**\n\n"
            "• **Step 1 (Warm Referral Engine):** Re-engage past clients and contacts with an updated portfolio showcase and exclusive booking availability.\n"
            "• **Step 2 (Targeted Pitching):** Identify 20 ideal business partners and send hyper-tailored video teardowns highlighting 2 immediate fixes.\n"
            "• **Step 3 (Proposal Precision):** Send proposals within 24 hours of discovery calls with 3-tier pricing options!"
        )

    # 6. UNIVERSAL FALLBACK
    return (
        f"🤎 **[The Brown Girls Studio • Executive Advisory]**\n\n"
        f"**Strategic Focus for \"{clean}\":**\n\n"
        f"• **Clarify the Revenue Driver:** Identify the single most profitable action for {topic.lower()} this week.\n"
        "• **Simplify the Execution:** Remove friction by breaking this goal into two 45-minute focus sprints today.\n"
        "• **Measure the Output:** Track your conversion metrics weekly—consistent iteration builds sustainable brands!"
    )

# 4. App UI Layout
st.markdown('<span class="brand-tag">The Brown Girls Creative Studio</span>', unsafe_allow_html=True)
st.markdown('<div class="studio-title">AI Growth Strategist</div>', unsafe_allow_html=True)
st.markdown('<div class="studio-sub">Ask questions on monetization, client acquisition, automated systems, or content scaling.</div>', unsafe_allow_html=True)

persona_options = [
    "Creative Entrepreneur",
    "Content & Brand Strategy",
    "Operations & Automation",
    "Brand Identity & Design",
    "Client Acquisition"
]
selected_persona = st.selectbox("Select Advisory Lens:", persona_options)

placeholder_map = {
    "Creative Entrepreneur": "e.g., How do I package my services to make $10k/month?",
    "Content & Brand Strategy": "e.g., How do I make videos that convert viewers to clients?",
    "Operations & Automation": "e.g., How do I automate client onboarding with no code?",
    "Brand Identity & Design": "e.g., How do I build a luxury brand aesthetic?",
    "Client Acquisition": "e.g., How do I pitch corporate clients or government contracts?"
}

user_input = st.text_input("Your Question or Strategic Goal:", placeholder=placeholder_map[selected_persona])

if st.button("Generate Strategic Blueprint ✨"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a question or business goal above!")
    else:
        with st.status("Synthesizing Strategic Blueprint...", expanded=False):
            st.write(f'🔍 Analyzing: "{user_input}"...')
            time.sleep(0.4)
            st.write("Consulting The Brown Girls Studio playbook...")
            time.sleep(0.3)

        response = search_knowledge_base(user_input, selected_persona)

        message_placeholder = st.empty()
        full_text = ""
        for char in response:
            full_text += char
            message_placeholder.markdown(full_text + "▌")
            time.sleep(0.008)
        message_placeholder.markdown(full_text)
