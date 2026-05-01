import streamlit as st
import streamlit.components.v1 as components
import base64

def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

GOITRE_B64 = image_to_base64("goitre.jpeg")
STAGES_GOITRE_B64 = image_to_base64("stages_goiter.png")
SYMPTOMS_B64 = image_to_base64("enlarge.jpg")

def show():
    st.set_page_config(layout="wide")

    components.html(
        f"""
        <style>
        body {{
            margin: 0;
            font-family: Segoe UI, sans-serif;
        }}

        .thy-header {{
            background: radial-gradient(circle,rgba(135, 167, 199, 1) 0%, rgba(88, 131, 191, 1) 40%, rgba(23, 71, 138, 1) 81%);
            padding: 40px 50px 30px 50px;
            border-radius: 24px;
            color: white;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
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

        .thy-header h1 {{
            margin: 0 0 12px 0;
            font-size: 2.6rem;
            font-weight: 800;
        }}

        .thy-nav a {{
            color: white;
            text-decoration: none;
            margin-right: 18px;
            font-weight: 600;
            opacity: 0.9;
        }}

        .thy-section h4,
        .thy-section p,
        .thy-section ul {{
            margin-top: 4px;
            margin-bottom: 4px;
            margin-left: 0;
            padding-left: 0;
        }}

        .thy-section ul {{
            list-style-position: inside;
            line-height: 1.7;
            margin-top: 6px;
            margin-bottom: 14px;
            padding-left: 18px;
        }}

        .thy-section p {{
            margin-top: 0;
            margin-bottom: 12px;
            line-height: 1.7;
        }}

        .thy-nav a:hover {{
            text-decoration: underline;
            opacity: 1;
        }}

        .thy-img {{
            text-align: center;
            margin-bottom: 20px;
        }}

        .thy-img img {{
            max-width: 520px;
            max-height: 360px;
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 18px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }}

        .thy-section {{
            padding: 0;
            margin-top: 40px;
            padding-top: 0;
            margin: 0 auto 2px auto;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
        }}

        .thy-section h1 {{
            margin-top: 0px;
            margin-bottom: 16px;
            border-bottom: 1.5px solid #B2BEB5;
            padding-bottom: 6px;
        }}

        .thy-section h3 {{
            margin-top: 28px;       
            margin-bottom: 10px;
        }}

        .thy-section h4 {{
            margin-top: 20px;
            margin-bottom: 8px;
            }}
        </style>

        <div class="thy-header">
            <h1>Goitre</h1>
            <div class="thy-nav">
                <span class="tab">Overview</span>
                <span class="tab">Symptoms</span>
                <span class="tab">Causes</span>
                <span class="tab">Risk Factors</span>
            </div>
        </div>

        <div class="thy-img">
            <img src="data:image/jpeg;base64,{GOITRE_B64}">
        </div>

        <div id="overview" class="thy-section">
            <h1>Overview</h1>
            <p>
                A goitre (GOI-tur) is the irregular growth of the thyroid gland.
                The thyroid is a butterfly-shaped gland located at the base of the neck just below the Adam's apple.
                A goitre may be an overall enlargement of the thyroid, or it may be the result of irregular cell growth that forms one or more lumps (nodules) in the thyroid. 
                A goitre may be associated with no change in thyroid function or with an increase or decrease in thyroid hormones.
            </p>
            <h3>Enlarged thyroid</h3>
            <p>
                Widespread enlargement of the thyroid can expand the gland well beyond its typical size (left) and cause a noticeable bulge in the neck (right).
            </p>
            <p>
                The most common cause of goitres worldwide is a lack of iodine in the diet. In the United States, where the use of iodized salt is common, 
                goitres are caused by conditions that change thyroid function or factors that affect thyroid growth. Treatment depends on the cause of the goitre, 
                symptoms, and complications resulting from the goitre. Small goitres that aren't noticeable and don't cause problems usually don't need treatment.
                </p>
            
            <h3>What are the stages of goitre swelling?</h3>
            <div style="text-align:center;">
            <img src="data:image/png;base64,{STAGES_GOITRE_B64}" 
                style="max-width: 520px; width: 100%; border-radius: 16px; box-shadow: 0 8px 20px rgba(0,0,0,0.15);">
            <div style="text-align: left;">
            <div class="thy-section">

            <h3>Classification Systems for Goitre</h3>

            <h4>By Morphology</h4>
            <p>Goitre is classified into two main morphological categories:</p>
            <ul style="list-style-type: disc; padding-left: 18px; margin-left: 0;">
                <li><b>Diffuse goitre:</b> Uniform enlargement of the entire thyroid gland without discrete nodules.</li>
                <li><b>Nodular goitre:</b> Presence of single (solitary nodule) or multiple nodules (multinodular goitre) within the thyroid gland.</li>
            </ul>

            <h4>By Functional Status</h4>
            <p>Goitres are further subdivided based on thyroid function:</p>
            <ul style="list-style-type: disc; padding-left: 18px; margin-left: 0;">
                <li><b>Toxic goitre:</b> Associated with hyperthyroidism symptoms and/or suppressed TSH levels.</li>
                <li><b>Nontoxic goitre:</b> Associated with normal TSH levels and euthyroid state.</li>
            </ul>

            <h4>By Clinical Severity (Not "Stages")</h4>
            <p>Rather than stages, goitres are characterized by their clinical presentation:</p>
            <ul style="list-style-type: disc; padding-left: 18px; margin-left: 0;">
                <li><b>Asymptomatic goitre:</b> Incidentally discovered, no symptoms, normal thyroid function.</li>
                <li><b>Symptomatic goitre with local compression:</b> Presenting with dysphagia, cough, dyspnea, orthopnea, obstructive sleep apnea, or stridor due to tracheal compression.</li>
                <li><b>Goitre with systemic symptoms:</b> Associated with hypothyroidism or hyperthyroidism.</li>
            </ul>
            <h3> Single Nodule Goitre</h3>
            <p>
            A single, palpable, or imaging-detected lump within an otherwise normal thyroid gland. While most (approx. 90-95%) are benign, such as follicular adenomas, cysts, or dominant nodules 
            in multinodular goitre, they require evaluation to rule out malignancy, which occurs in 4-6.5% of cases.
            </p>
            
            <h3>Multi-Nodular Goitre</h3>
            <p>
            Multinodular goitre is the presence of multiple nodules or bumps on an abnormally enlarged thyroid gland. 
            These thyroid nodules are common, harmless, and mostly noncancerous. However, sometimes, these nodules can 
            cause the thyroid gland to produce excessive thyroid hormone resulting in a condition called hyperthyroidism. 
            Multinodular goitres like solitary thyroid nodule are also linked with small (less than 5%) risk of thyroid cancer.
            </p>
            </div>
            </div>
        </div>
        </div>
            </ul>
            </div>

        <div id="symptoms" class="thy-section">

    <h1>Symptoms</h1>

    <div style="display: flex; gap: 24px; align-items: flex-start;">

        <!-- Left: text -->
        <div style="flex: 1; text-align: left;">

            <p style="line-height:1.7; margin-top: 0;">
                You can have a goitre but have no symptoms at all, other than 
                having some swelling at the lower part of your neck. Due to the swelling, some people also may have:
            </p>

            <ul style="list-style-type: disc; padding-left: 18px; margin-top: 6px; line-height: 1.7;">
                <li>A lump or swelling in the neck</li>
                <li>Difficulty swallowing or breathing</li>
                <li>Hoarseness or voice changes</li>
                <li>Neck discomfort or pain</li>
                <li>Symptoms of hyperthyroidism or hypothyroidism (in some cases)</li>
            </ul>

        </div>

    <!-- Right: image -->
    <div style="flex: 1; text-align: center;">
        <img src="data:image/png;base64,{SYMPTOMS_B64}"
             style="max-width: 360px; width: 100%; height: 250px; border-radius: 16px; box-shadow: 0 8px 20px rgba(0,0,0,0.15);">
    </div>
</div>
<p style="line-height:1.7; margin-top: 8px;">
                If your goitre is making your thyroid underactive or overactive, you may also have a wide range of 
                symptoms, from fatigue and weight gain to involuntary weight loss, irritability, and sleep disorders.
            </p>

        <div id="causes" class="thy-section">
            <h1>Causes</h1>
            <ul style="list-style-type: disc; padding-left: 18px; margin-left: 0;, line-height: 1.7;">
                <li><b>Iodine deficiency:</b> Iodine is essential for the production of thyroid hormones. If a person does not get enough dietary iodine, 
                hormone production drops and the pituitary gland signals the thyroid to make more. This increased signal results in thyroid growth. 
                In the United States, this cause is uncommon because of iodine added to table salt.</li>
                <li><b>Hashimoto's disease:</b> Hashimoto's disease is an autoimmune disorder, an illness caused by the immune system attacking healthy tissues. 
                The damaged and inflamed tissues of the thyroid don't produce enough hormones (hypothyroidism). When the pituitary gland detects the decline 
                and prompts the thyroid to create more hormones, the thyroid can become enlarged.</li>
                <li><b>Graves' disease:</b> Another autoimmune disorder called Graves' disease occurs when the immune system produces a protein that mimics TSH. 
                This rogue protein prompts the thyroid to overproduce hormones (hyperthyroidism) and can result in thyroid growth.</li>
                <li><b>Thyroid nodules:</b> A nodule is the irregular growth of thyroid cells that form a lump. A person may have one nodule 
                or several nodules (multinodular goitre). The cause of nodules is not clear, but there may be multiple factors — genetics, 
                diet, lifestyle and environment. Most thyroid nodules are noncancerous (benign).</li>
                <li><b>Pregnancy:</b> A hormone produced during pregnancy, human chorionic gonadotropin (HCG), may cause the thyroid gland to be overactive and enlarge slightly.</li>
                <li><b>Inflammation:</b> Thyroiditis is inflammation of the thyroid caused by an autoimmune disorder, bacterial or viral infection, or medication. The inflammation may cause hyperthyroidism or hypothyroidism.</li>
            </ul>
        </div>

        <div id="risk" class="thy-section">
            <h1>Risk Factors</h1>
            <ul>
                <li>Being a woman (four times more often in women than in men)</li>
                <li>Being over 40 years old  </li>
                <li>Being pregnant or in menopause </li>
                <li>Having a family history of autoimmune disease or goitre </li>
                <li>Having been exposed to radiation as a child or having had radiation treatment to your neck or chest</li>
                <li>Having a diet low in iodine</li>
                <li>Some medical treatments, including the heart drug amiodarone (Pacerone) and the psychiatric drug lithium (Lithobid), increase your risk.</li>
            </ul>
        </div>
        """,
        height=3500,
        scrolling=False
    )

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

    if st.button("← Back to Home"):
        st.session_state.page = "home"
        st.rerun()