import streamlit as st
import streamlit.components.v1 as components
import base64

def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

THYROID_B64 = image_to_base64("thyroid.jpeg")

def show():
    st.set_page_config(layout="wide")

    # ---------- HEADER WITH GRADIENT + JS NAV LINKS ----------
    components.html(f"""
    <style>
    .thy-header {{
        background: radial-gradient(circle,rgba(135, 167, 199, 1) 0%, rgba(88, 131, 191, 1) 40%, rgba(23, 71, 138, 1) 81%);
        padding: 40px 50px 30px 50px;
        border-radius: 24px;
        color: white;
        font-family: Segoe UI, sans-serif;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        margin-bottom: 30px;
    }}

    .thy-header h1 {{
        margin: 0 0 12px 0;
        font-size: 2.6rem;
        font-weight: 800;
    }}

    .thy-nav span {{
        margin-right: 18px;
        font-weight: 600;
        opacity: 0.95;
    }}

    .thy-section {{
        background: transparent;
        padding: 4px 0;
        border-radius: 0;
        box-shadow: none;
        margin: 0 auto 40px auto;
        max-width: 900px;
        font-family: Segoe UI, sans-serif;
    }}

    .thy-section h1 {{
        margin-top: 0;
        margin-bottom: 16px;
        border-bottom: 1.5px solid #B2BEB5;
        padding-bottom: 6px;
    }}

    .thy-section h3 {{
        margin-top: 28px;   
        margin-bottom: 10px;
    }}
                    
    .thy-section p {{
    margin-top: 0;
    margin-bottom: 10px;
    line-height: 1.7;
    }}
                    
    .thy-section ul {{
        margin-top: 6px;
        margin-bottom: 12px;
        padding-left: 18px;
        line-height: 1.7;
    }}
                
    .thy-section ul {{
        list-style-position: inside;
        margin-top: 6px;
        margin-bottom: 6px;
    }}

    .thy-img {{
        text-align: center;
        margin-bottom: 30px;
    }}
                    
    .thy-nav .tab {{
        display: inline-block;
        margin-right: 12px;
        font-weight: 600;
        opacity: 0.95;
        padding: 6px 12px;
        border-radius: 12px;
        background: rgba(255,255,255,0.15);
    }}

    .thy-img img {{
        max-width: 520px;
        width: 100%;
        border-radius: 18px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }}
    </style>

    <div class="thy-header">
        <h1>Thyroid Tumor</h1>
        <div class="thy-nav">
            <span class="tab">Overview</span>
            <span class="tab">Symptoms</span>
            <span class="tab">Causes</span>
            <span class="tab">Risk Factors</span>
        </div>
    </div>
    <div class="thy-img">
        <img src="data:image/jpeg;base64,{THYROID_B64}">
    </div>

    <div id="overview" class="thy-section">
        <h1>Overview</h1>

        <h3>What is the thyroid?</h3>
        <p>
            Your thyroid is a small, butterfly-shaped gland located at the front of your neck under your skin. It’s a part
            of your endocrine system and controls many of your body’s important functions by producing and releasing
            (secreting) certain hormones. Your thyroid’s main job is to control the speed of your metabolism (metabolic rate),
            which is the process of how your body transforms the food you consume into energy. All of the cells in your body
            need energy to function. When your thyroid isn’t working properly, it can impact your entire body.
        </p>

        <h3>What does my thyroid do?</h3>
        <p>
            As an endocrine gland, your thyroid makes and secretes hormones. Your thyroid produces and releases the following hormones:
        </p>
        <ul>
            <li>
                <b>Thyroxine (T4):</b> This is the primary hormone your thyroid makes and releases. Although your thyroid produces the
                most of this hormone, it doesn’t have much direct effect on your metabolism. Once your thyroid releases T4 into your
                bloodstream, it can convert to T3 through a process called deiodination.
            </li>
            <li>
                <b>Triiodothyronine (T3):</b> Your thyroid produces smaller amounts of T3 than T4, but T3 has a much greater effect
                on your metabolism.
            </li>
            <li>
                <b>Reverse triiodothyronine (RT3):</b> Your thyroid makes very small amounts of RT3, which can reverse the effects of T3.
            </li>
            <li>
                <b>Calcitonin:</b> This hormone helps regulate the amount of calcium in your blood.
            </li>
        </ul>
        <h3>What is a thyroid tumor?</h3>
        <p>Thyroid tumors are abnormal growths, or neoplasms, that develop in the thyroid gland at the base of the neck, ranging from common benign (noncancerous) 
        adenomas to rare, often treatable malignant (cancerous) carcinomas. They frequently present as painless nodules or lumps, sometimes causing hoarseness, 
        swallowing difficulties, or thyroid hormone imbalances. Several types of thyroid cancer exist. Most types grow slowly, though some types can be very aggressive. 
        Most thyroid cancers can be cured with treatment.
        </p>
        </ul>
    </div>

    <div id="symptoms" class="thy-section">
        <h1>Symptoms</h1>
        <ul>
            <li>A lump (nodule) that can be felt through the skin on your neck</li>
            <li>A feeling that close-fitting shirt collars are becoming too tight</li>
            <li>Changes to your voice, including increasing hoarseness</li>
            <li>Difficulty swallowing</li>
            <li>Swollen lymph nodes in your neck</li>
            <li>Pain in your neck and throat</li>
        </ul>
    </div>

    <div id="causes" class="thy-section">
        <h1>Causes</h1>
        <p>
            Thyroid cancer happens when cells in the thyroid develop changes in their DNA. A cell's DNA contains the 
            instructions that tell the cell what to do. The changes, which doctors call mutations, tell the cells to
            grow and multiply rapidly. The cells go on living when healthy cells would naturally die. The accumulating cells form a mass called a tumor.
        </p>
        <p>The tumor can grow to invade nearby tissue and can spread (metastasize) to the lymph nodes in the neck. 
        Sometimes the cancer cells can spread beyond the neck to the lungs, bones and other parts of the body.
        For most thyroid cancers, it's not clear what causes the DNA changes that cause the cancer.
        </p>
    </div>

    <div id="risk" class="thy-section">
        <h1>Risk Factors</h1>
        <p>Factors that may increase the risk of thyroid cancer include:</p>
        <ul>
            <li>
             <b>Female sex:</b> Thyroid cancer occurs more often in women than in men. Experts think it may be related to the hormone estrogen. 
             People who are assigned female sex at birth generally have higher levels of estrogen in their bodies.</li>
            <li>
            <b>Exposure to high levels of radiation:</b> Radiation therapy treatments to the head and neck 
            increase the risk of thyroid cancer.</li>
            <li>
            <b>Certain inherited genetic syndromes:</b> Genetic syndromes that increase the risk of thyroid cancer 
            include familial medullary thyroid cancer, multiple endocrine neoplasia, Cowden syndrome and familial 
            adenomatous polyposis. Types of thyroid cancer that sometimes run in families include medullary thyroid cancer and papillary thyroid cancer.
            </li>
            </ul>
    </div>
    """, height=2300, scrolling=False)

    st.markdown("""
    <style>

    /* Back to Home button styling */

    div[data-testid="stButton"] button {
        background: linear-gradient(90deg,#020024,#090979) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 0.6em 1.4em !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
    }

    /* Hover */

    div[data-testid="stButton"] button:hover {
        background: linear-gradient(135deg, #1e40af, #2563eb) !important;
        transform: translateY(-1px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.25) !important;
    }

    </style>
    """, unsafe_allow_html=True)

    st.divider()

    # ---------- BACK BUTTON ----------
    if st.button("← Back to Home"):
        st.session_state.page = "home"
        st.rerun()