import streamlit as st
import streamlit.components.v1 as components
import base64

# ---------------------------
# Router state
# ---------------------------

# Default page
if "page" not in st.session_state:
    st.session_state.page = "home"

# Read URL query parameters
query_params = st.query_params

if "page" in query_params:
    page_value = query_params.get("page")

    # Handle list case (new Streamlit behavior)
    if isinstance(page_value, list):
        st.session_state.page = page_value[0]
    else:
        st.session_state.page = page_value

# ---------------------------
# Helper to load images
# ---------------------------
def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Images
HEADER_B64 = image_to_base64("header.jpg")
THYROID_B64 = image_to_base64("thyroid.jpeg")     
GOITRE_B64 = image_to_base64("goitre.jpeg")
BENIGN_B64 = image_to_base64("benign.jpeg")
MALIGNANT_B64 = image_to_base64("malignant.jpeg")
RIBBON_B64 = image_to_base64("ribbon.jpeg")

st.set_page_config(
    page_title="Multimodal Thyroid Abnormality Detection",
    layout="wide"
)

# ---------------------------
# Background + Button Styles
# ---------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #dbeafe 0%, #ffffff 65%);
    color: #0f172a;
}

section.main > div {
    background: transparent;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #c7ddff 0%, #eef5ff 100%);
}

/* Nav buttons */
div[data-testid="stHorizontalBlock"] button {
    background: linear-gradient(135deg, #020024, #090979) !important;
    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 0.42em 0.85em !important;
    font-weight: 600 !important;
    font-size: 1.02rem !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
    transition: all 0.2s ease-in-out !important;
}

div[data-testid="stHorizontalBlock"] button:hover {
    background: linear-gradient(135deg, #1e40af, #2563eb) !important;
    transform: translateY(-1px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.25) !important;
}

div[data-testid="stHorizontalBlock"] button:active {
    transform: translateY(0px);
    box-shadow: 0 3px 8px rgba(0,0,0,0.2) !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# HOME PAGE
# ---------------------------
def show_home():

    # -------- HEADER --------
    components.html(
        f"""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

        <div style="background-color: #eaf0fb; padding: 16px; border-radius: 24px;">
            <div style="
                position: relative;
                width: 100%;
                height: 230px;
                border-radius: 32px;
                overflow: hidden;
                font-family: Segoe UI, sans-serif;
                box-shadow: 0 6px 16px rgba(0,0,0,0.12);
            ">

                <div style="
                    position: absolute;
                    inset: 0;
                    background-image:
                        linear-gradient(to right, rgba(248,251,255,0.0) 0%, rgba(13,77,170,0.85) 60%, rgba(58,123,213,0.95) 100%),
                        url('data:image/jpeg;base64,{HEADER_B64}');
                    background-repeat: no-repeat;
                    background-size: contain;
                    background-position: left center;
                "></div>

                <div style="
                    position: relative;
                    height: 100%;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    padding-left: 45%;
                    padding-right: 40px;
                    color: white;
                ">
                    <h1 style="margin: 0 0 10px 0; font-size: 2rem;">
                        Multimodal Thyroid Abnormality Detection
                    </h1>

                    <p style="margin: 0; font-size: 1.05rem;">
                        <i class="fa-regular fa-image"></i> Ultrasound &nbsp; • &nbsp;
                        <i class="fa-regular fa-microphone"></i> Voice &nbsp; • &nbsp;
                        <i class="fa-regular fa-flask"></i> Clinical &nbsp; • &nbsp;
                        <i class="fa-regular fa-file-lines"></i> Radiology
                    </p>
                </div>
            </div>
        </div>
        """,
        height=260,
    )

    # -------- INTRO --------
    st.markdown(
        """
        <div style="text-align: center; margin: 12px 0 10px 0;">
            <h3 style="
                background: radial-gradient(circle,rgba(2, 0, 36, 1) 0%, rgba(9, 9, 121, 1) 40%, rgba(9, 71, 121, 1) 81%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: 800;
                margin-bottom: 6px;
            ">
                Reference Imaging for Multimodal Thyroid Assessment
            </h3>
            <p style="font-size: 1.05rem; color: #444; max-width: 900px; margin: 0 auto;">
                The following reference images illustrate typical appearances of different thyroid conditions used in this system.
                These examples support visual interpretation and demonstrate how imaging features complement clinical, and laboratory inputs in the proposed multimodal diagnostic framework.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -------- CAROUSEL --------
    components.html(
        f"""
        <style>
        .centai-wrap {{
          width: 100%;
          max-width: 1100px;
          margin: 10px auto 0 auto;
          overflow: hidden;
        }}

        .centai-track {{
          display: flex;
          gap: 24px;
          scroll-snap-type: x mandatory;
          overflow-x: auto;
          padding: 20px 40px;
          scroll-behavior: smooth;
        }}

        .centai-item {{
          flex: 0 0 auto;
          width: 622px;
          height: 450px;
          scroll-snap-align: center;
          transition: transform 0.4s ease, opacity 0.4s ease;
        }}

        .centai-item img {{
          width: 100%;
          height: 100%;
          object-fit: cover;
          border-radius: 22px;
          box-shadow: 0 10px 24px rgba(0,0,0,0.25);
        }}

        .centai-track:hover .centai-item {{
          opacity: 0.4;
          transform: scale(0.9);
        }}

        .centai-track .centai-item:hover {{
          opacity: 1;
          transform: scale(1.0);
        }}

        .centai-track::-webkit-scrollbar {{ display: none; }}
        .centai-track {{ -ms-overflow-style: none; scrollbar-width: none; }}
        </style>

        <div class="centai-wrap">
          <div class="centai-track" id="track">
            <div class="centai-item"><img src="data:image/jpeg;base64,{THYROID_B64}"></div>
            <div class="centai-item"><img src="data:image/jpeg;base64,{GOITRE_B64}"></div>
            <div class="centai-item"><img src="data:image/jpeg;base64,{BENIGN_B64}"></div>
            <div class="centai-item"><img src="data:image/png;base64,{MALIGNANT_B64}"></div>
          </div>
        </div>

        <script>
        const titles = ["Thyroid Tumor","Thyroid Goitre","Benign Nodule","Malignant Tumor"];
        const descs = [
          "General thyroid lesion appearance used as a reference for multimodal assessment.",
          "Enlargement of the thyroid gland, often linked to iodine deficiency or hormonal imbalance.",
          "Non-cancerous thyroid nodule with smooth margins and low clinical risk.",
          "Suspicious thyroid lesion with irregular features and higher risk of malignancy."
        ];

        function updateDescription(index) {{
          const t = parent.document.getElementById("carousel-title");
          const d = parent.document.getElementById("carousel-desc");
          if (t && d) {{
            t.innerText = titles[index];
            d.innerText = descs[index];
          }}
        }}

        const track = document.getElementById("track");
        track.addEventListener("scroll", () => {{
          const items = document.querySelectorAll(".centai-item");
          let closest = 0;
          let minDist = Infinity;
          items.forEach((item, i) => {{
            const rect = item.getBoundingClientRect();
            const center = rect.left + rect.width / 2;
            const screenCenter = window.innerWidth / 2;
            const dist = Math.abs(center - screenCenter);
            if (dist < minDist) {{
              minDist = dist;
              closest = i;
            }}
          }});
          updateDescription(closest);
        }});
        </script>
        """,
        height=520
    )

    # -------- BUTTONS (RIGHT UNDER CAROUSEL) --------
    st.markdown("<div style='margin-top:-10px'></div>", unsafe_allow_html=True)

    _, c1, c2, c3, c4, _ = st.columns([2, 1, 1, 1, 1, 2], gap="xxsmall")

    with c1:
        if st.button("Thyroid Tumor"):
            st.session_state.page = "thyroid"
            st.rerun()

    with c2:
        if st.button("Thyroid Goitre"):
            st.session_state.page = "goitre"
            st.rerun()

    with c3:
        if st.button("Benign Nodule"):
            st.session_state.page = "benign"
            st.rerun()

    with c4:
        if st.button("Malignant Nodule"):
            st.session_state.page = "malignant"
            st.rerun()

    # -------- TITLE + DESCRIPTION (UNDER BUTTONS) --------
    st.markdown("""
    <div style="text-align:center; margin-top:10px; font-family: Segoe UI, sans-serif;">
        <div id="carousel-title" style="font-size:1.3rem; font-weight:700; color:#1e3a8a;">
          Thyroid Tumor
        </div>
        <div id="carousel-desc" style="font-size:0.95rem; color:#444; max-width:800px; margin:6px auto 0 auto;">
          General thyroid lesion appearance used as a reference for multimodal assessment.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("""
    <style>

    .risk-title{
        font-size:2.4rem;
        font-weight:700;
        color:#0f172a;
    }

    .risk-text{
        font-size:1.1rem;
        line-height:1.7;
        color:#444;
        max-width:520px;
    }

    .image-card{
        padding:35px;
        border-radius:40px;
        background: radial-gradient(circle,
            rgba(23,71,138,1) 0%,
            rgba(18,53,110,1) 45%,
            rgba(10,33,80,1) 100%);
        box-shadow: 0 20px 40px rgba(0,0,0,0.35);
    }

    .image-card img{
        border-radius:20px;
    }

    div[data-testid="stButton"] button{
        background: linear-gradient(90deg,#020024,#090979);
        color:white;
        border-radius:16px;
        padding:14px 28px;
        font-weight:700;
        border:none;
    }

    div[data-testid="stButton"] button:hover{
        transform:translateY(-2px);
    }

    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.3,1])

    # LEFT SIDE
    with col1:

        st.markdown('<div class="risk-title">WHAT’S MY RISK?</div>', unsafe_allow_html=True)

        st.markdown(
            '<div class="risk-text">Our multimodal diagnostic system evaluates thyroid abnormalities using ultrasound imaging and clinical indicators, helping support early detection and informed medical assessment.<br><br>When it comes to avoiding cancer, prevention and early detection are essential. That’s why knowing your risk is so important.</div>',
            unsafe_allow_html=True
        )

        st.write("")

        if st.button("Run Diagnostic Test"):
            st.session_state.page = "diagnostic"
            st.rerun()

    # RIGHT SIDE
    with col2:

        components.html(f"""
        <style>

        @keyframes pulseGlow {{
            0% {{
                filter: drop-shadow(0px 0px 25px rgba(23,71,138,0.6))
                        drop-shadow(0px 0px 40px rgba(18,53,110,0.5));
            }}

            50% {{
                filter: drop-shadow(0px 0px 45px rgba(23,71,138,0.9))
                        drop-shadow(0px 0px 75px rgba(18,53,110,0.8));
            }}

            100% {{
                filter: drop-shadow(0px 0px 25px rgba(23,71,138,0.6))
                        drop-shadow(0px 0px 40px rgba(18,53,110,0.5));
            }}
        }}

        .image-wrap {{
            display:flex;
            justify-content:center;
            align-items:center;
            height:320px;
            position:relative;
        }}

        .image-wrap::before {{
            content:"";
            position:absolute;
            width:480px;
            height:320px;
            background: radial-gradient(circle,
                rgba(23,71,138,0.25) 0%,
                rgba(23,71,138,0.15) 40%,
                rgba(23,71,138,0) 75%);
            filter: blur(40px);
            border-radius:50%;
        }}

        .glow-image {{
            width:460px;
            height:300px;
            border-radius:20px;
            position:relative;
            animation: pulseGlow 4s ease-in-out infinite;
        }}

        </style>

        <div class="image-wrap">

            <img src="data:image/jpeg;base64,{RIBBON_B64}"
                class="glow-image">

        </div>

        """, height=340)

# ---------------------------
# ROUTER
# ---------------------------
page = st.session_state.page

if page == "home":
    show_home()
elif page == "diagnostic":
    import diagnostic
    diagnostic.show()
elif page == "thyroid":
    import thyroid
    thyroid.show()
elif page == "goitre":
    import goitre
    goitre.show()
elif page == "benign":
    import benign
    benign.show()
elif page == "malignant":
    import malignant
    malignant.show()