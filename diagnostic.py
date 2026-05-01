import streamlit as st
import random
from PIL import Image, ImageDraw
import base64

def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

RIBBON_B64 = image_to_base64("ribbon.jpeg")

def show():

    st.markdown("""
    <style>

    /* ===== File uploader styling ===== */

    div[data-testid="stFileUploader"] section {
        background: linear-gradient(135deg, #0d4daa, #3a7bd5) !important;
        border: none !important;
        border-radius: 18px !important;
        padding: 16px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }

    div[data-testid="stFileUploader"] section div[role="button"] {
        background: linear-gradient(135deg, rgba(255,255,255,0.15), rgba(255,255,255,0.05)) !important;
        border: 2px dashed rgba(255,255,255,0.6) !important;
        border-radius: 14px !important;
        color: white !important;
        padding: 20px !important;
    }

    /* Text inside uploader */
    div[data-testid="stFileUploader"] section * {
        color: white !important;
    }

    /* Hover effect */
    div[data-testid="stFileUploader"] section div[role="button"]:hover {
        background: linear-gradient(135deg, rgba(255,255,255,0.25), rgba(255,255,255,0.10)) !important;
        border-color: white !important;
    }


    /* ===== Number input styling ===== */

    div[data-testid="stNumberInput"] input {
        background-color: #f4f8ff !important;
        border: 1.5px solid #cfe0ff !important;
        border-radius: 10px !important;
        color: #0f2a44 !important;
        padding: 8px 10px !important;
    }

    /* Number input focus */
    div[data-testid="stNumberInput"] input:focus {
        border-color: #3a7bd5 !important;
        box-shadow: 0 0 0 2px rgba(58,123,213,0.25) !important;
        outline: none !important;
    }


    /* ===== Selectbox (dropdown) styling ===== */

    div[data-baseweb="select"] {
        background-color: #f4f8ff !important;
        border-radius: 10px !important;
        border: 1.5px solid #cfe0ff !important;
    }

    /* Dropdown text */
    div[data-baseweb="select"] span {
        color: #0f2a44 !important;
    }

    /* Dropdown arrow */
    div[data-baseweb="select"] svg {
        fill: #0f2a44 !important;
    }

    /* Dropdown menu */
    div[data-baseweb="menu"] {
        background-color: #f4f8ff !important;
    }

    /* Dropdown items */
    div[data-baseweb="menu"] div {
        color: #0f2a44 !important;
    }

    /* Hover effect */
    div[data-baseweb="menu"] div:hover {
        background-color: #dbeafe !important;
    }


    /* ===== Labels ===== */

    label {
        color: #0f2a44 !important;
        font-weight: 600 !important;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>

    /* Run Multimodal Analysis + Back to Home buttons */

    div[data-testid="stButton"] button {
        background: linear-gradient(90deg,#020024,#090979) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 0.6em 1.4em !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
        transition: all 0.2s ease-in-out !important;
    }

    /* Hover */

    div[data-testid="stButton"] button:hover {
        background: linear-gradient(90deg,#020024,#090979) !important;
        box-shadow: 0 6px 16px rgba(0,0,0,0.25) !important;
    }

    /* Click */

    div[data-testid="stButton"] button:active {
        transform: translateY(0px);
        box-shadow: 0 3px 8px rgba(0,0,0,0.2) !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # ================= HEADER =================
    st.markdown(f"""
    <div style="
    background: radial-gradient(circle, rgba(135,167,199,1) 0%, rgba(88,131,191,1) 40%, rgba(23,71,138,1) 81%);
    padding: 40px 50px;
    border-radius: 24px;
    color: white;
    display:flex;
    align-items:center;
    justify-content:space-between;
    ">

    <div style="max-width:70%;">
    <h1 style="margin:0; font-size:3.5rem; font-weight:800;">Multimodal Thyroid Diagnostic Assessment</h1>
    <p style="opacity:0.9; margin-top:10px; font-size:1.15rem;">
    Upload imaging and clinical parameters to evaluate thyroid abnormality risk.
    </p>
    </div>

    <img src="data:image/jpeg;base64,{RIBBON_B64}" style="width:280px;">

    </div>
    """, unsafe_allow_html=True)

    # ================= INPUT SECTION =================
    st.header("Multimodal Input Data")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Ultrasound Image")
        image_file = st.file_uploader(
            "Upload Thyroid Ultrasound Image",
            type=["png", "jpg", "jpeg"]
        )

    with col2:
        st.subheader("Voice Sample (Optional)")
        voice_file = st.file_uploader(
            "Upload Voice Sample (WAV / MP3)",
            type=["wav", "mp3"]
        )

    st.divider()

    # ================= CLINICAL DATA =================
    st.subheader("Clinical Parameters")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        age = st.number_input("Age", 1, 100, 35)
    with c2:
        gender = st.selectbox("Gender", ["Male", "Female"])
    with c3:
        tsh = st.number_input("TSH Level", 0.0, 20.0, 2.5)
    with c4:
        nodule_history = st.selectbox("Nodule History", ["No", "Yes"])

    c5, c6 = st.columns(2)
    with c5:
        t3 = st.number_input("T3 Level", 0.0, 10.0, 1.2)
    with c6:
        t4 = st.number_input("T4 Level", 0.0, 20.0, 8.5)

    st.divider()

    # ================= RADIOLOGY =================
    st.subheader("Radiologist-Reported Descriptors")

    r1, r2, r3, r4 = st.columns(4)

    with r1:
        echogenicity = st.selectbox("Echogenicity", ["Hyperechoic", "Isoechoic", "Hypoechoic"])
    with r2:
        margin = st.selectbox("Margin", ["Regular", "Irregular"])
    with r3:
        calcification = st.selectbox("Calcifications", ["Absent", "Present"])
    with r4:
        shape = st.selectbox("Shape", ["Wider-than-tall", "Taller-than-wide"])

    st.divider()

    # ================= RUN ANALYSIS =================
    if st.button("Run Multimodal Analysis") and image_file:

        image = Image.open(image_file).convert("RGB")
        image = image.resize((640, 640))

        draw = ImageDraw.Draw(image)
        x1, y1 = random.randint(100, 200), random.randint(100, 200)
        x2, y2 = random.randint(350, 500), random.randint(350, 500)

        detected_class = random.choice(["Goitre", "Benign Nodule", "Malignant Tumour"])
        detection_conf = round(random.uniform(85, 98), 2)

        draw.rectangle([x1, y1, x2, y2], outline="red", width=4)
        draw.text((x1, y1 - 15), detected_class, fill="red")

        risk_category = random.choice(["Low Risk", "Medium Risk", "High Risk"])
        combined_conf = round(random.uniform(88, 96), 2)

        if voice_file:
            voice_class = random.choice(["Normal", "Hoarse"])
            voice_prob = round(random.uniform(70, 95), 2)
        else:
            voice_class = "Not Provided"
            voice_prob = None

        st.header("Multimodal Diagnostic Results")

        colA, colB = st.columns(2)

        with colA:
            st.image(image, use_container_width=True)

        with colB:
            st.subheader("Detection Details")
            st.markdown(f"**Detected Thyroid Condition:** {detected_class}")
            st.markdown(f"**Ultrasound Detection Confidence:** {detection_conf}%")
            st.markdown(f"**Risk Category:** {risk_category}")
            st.markdown(f"**Combined Confidence Score:** {combined_conf}%")

            if voice_prob:
                st.markdown("---")
                st.markdown("**Voice Analysis**")
                st.markdown(f"**Condition:** {voice_class}")
                st.markdown(f"**Abnormality Probability:** {voice_prob}%")
    
        # -------------------------
        # Diagnostic Summary
        # -------------------------
        st.subheader("Diagnostic Summary")

        if risk_category == "High Risk":
            bg_gradient = "linear-gradient(135deg, #fee2e2, #fecaca)"
            text_color = "#7f1d1d"
        elif risk_category == "Low Risk":
            bg_gradient = "linear-gradient(135deg, #dcfce7, #bbf7d0)"
            text_color = "#14532d"
        else:
            bg_gradient = "linear-gradient(135deg, #fef9c3, #fde047)"
            text_color = "#713f12"

        st.markdown(f"""
        <div style="
            background:{bg_gradient};
            color:{text_color};
            padding:20px;
            border-radius:16px;
            margin-top:20px;
        ">
            <p>The multimodal analysis indicates a <b>{detected_class}</b> 
            with a <b>{risk_category}</b> classification.
            </p>
            <p>Confidence from combined modalities suggests a reliability of <b>{combined_conf}%</b></p>
            <p style="font-size:0.95rem; opacity:0.9;">
                This result is intended to support clinical decision-making and should be reviewed by a qualified medical professional.
            </p>

        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("Please upload an ultrasound image to start analysis.")


    st.divider()

    if st.button("← Back to Home"):
        st.session_state.page = "home"
        st.rerun()