import streamlit as st
import streamlit.components.v1 as components
import base64

def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Change this image to any benign nodule / thyroid image you have
BENIGN_B64 = image_to_base64("benign.jpeg")
BENIGN_CANCER_B64 = image_to_base64("ben.png")

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
            background: radial-gradient(circle, rgba(135,167,199,1) 0%, rgba(88,131,191,1) 40%, rgba(23,71,138,1) 81%);
            padding: 40px 50px 30px 50px;
            border-radius: 24px;
            color: white;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            margin-bottom: 30px;
        }}

        .thy-header h1 {{
            margin: 0 0 12px 0;
            font-size: 2.6rem;
            font-weight: 800;
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

        .thy-img {{
            text-align: center;
            margin-bottom: 30px;
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

        /* Section container */
        .thy-section {{
            margin: 0 auto 40px auto;   /* consistent gap between sections */
            padding: 0;
            max-width: 900px;
        }}

        /* Main headings */
        .thy-section h1 {{
            margin-top: 0;
            margin-bottom: 16px;
            border-bottom: 1.5px solid #B2BEB5;
            padding-bottom: 6px;
        }}

        /* Subheadings */
        .thy-section h3 {{
            margin-top: 28px;
            margin-bottom: 10px;
        }}

        .thy-section h4 {{
            margin-top: 20px;
            margin-bottom: 8px;
        }}

        /* Text */
        .thy-section p {{
            margin-top: 0;
            margin-bottom: 12px;
            line-height: 1.7;
        }}

        /* Lists */
        .thy-section ul {{
            margin-top: 6px;
            margin-bottom: 14px;
            padding-left: 18px;
            line-height: 1.7;
        }}
        </style>

        <div class="thy-header">
            <h1>Benign Thyroid Nodule</h1>
            <div class="thy-nav">
                <span class="tab">Overview</span>
                <span class="tab">Types</span>
                <span class="tab">Symptoms</span>
                <span class="tab">Diagnosis</span>
            </div>
        </div>

        <div class="thy-img">
            <img src="data:image/jpeg;base64,{BENIGN_B64}">
        </div>

        <!-- Overview -->
        <div class="thy-section">
            <h1>Overview</h1>
            <p>
                Benign thyroid tumours are neoplasms of the thyroid gland that are not malignant. They develop as a result of abnormal growth and division of cells of this organ.  
                Thyroid nodules are very common, especially in adults, and most of them are harmless. Many people 
                may have thyroid nodules without noticing any symptoms.
            </p>
            <p>
                Benign neoplasms of the thyroid gland occur in 30% of the adult population of the planet. In many people, these tumours do not manifest themselves in any way and do not require intervention. 
                In such cases, constant monitoring is indicated. If symptoms appear and the tumour grows, conservative or surgical treatment may be needed.
            </p>
            <p>
            Thyroid function tests help assess whether the thyroid gland is producing hormones normally, indicating if the nodule is affecting overall thyroid function. An ultrasound scan of 
            the thyroid gland provides detailed images, allowing doctors to examine the size, shape, and characteristics of the nodule, helping to distinguish benign nodules from those that may 
            require further investigation or treatment. Together, these tests form the foundation for effective diagnosis and management of thyroid nodules. The majority of benign thyroid nodules can 
            continue to grow and multiple nodules in both lobes are common, which can cause pressure symptoms.
            </p>
        </div>

        <!-- Types -->
        <div class="thy-section">
            <h1>What are benign tumours of the thyroid gland?</h1>

            <h3>Thyroid Adenoma</h3>
            <p>
                More than 90% of benign thyroid tumours are adenomas. They develop from thyroid tissue cells. Such neoplasms are conditionally benign. Some of them can develop into cancerous ones. 
                Oxyphilic adenomas are the most dangerous, and the most common are follicular and toxic thyroid adenomas. Such tumours are treated surgically.
            </p>

            <h3>Thyroid Cysts</h3>
            <p>
                Thyroid cysts are benign nodular neoplasms that are filled with fluid. In 90% of cases, they have no pronounced symptoms. Cysts become dangerous with inflammation. Also, 
                these neoplasms can grow rapidly in size and compress the trachea or blood vessels. Nodules up to 1 cm in size should be observed. Large cysts are surgically removed.
            </p>

            <h3>Colloid Cyst Nodule</h3>
            <p>
                A colloid cyst nodule is a common type of benign thyroid nodule that contains fluid. Nodules develop when thyroid tissue grows abnormally. With a colloid cyst nodule, 
                the overgrowth can be extensive. Fortunately, colloid thyroid nodules don’t spread outside the thyroid.
            </p>

            <h3>Inflammatory Nodules</h3>
            <p>
            Inflammatory thyroid nodules are typically benign, often developing from chronic inflammation like Hashimoto’s thyroiditis, rather than cancer. They are frequently found during 
            routine exams or imaging (ultrasound) and, while usually painless, can cause tenderness, neck discomfort, and swallowing issues. Most are benign, and treatment usually focuses on 
            monitoring or managing underlying thyroiditis.           
            </p>
        </div>

        <div class="thy-section">
            <h1>Can a Benign Thyroid Nodule Become Malignant?</h1>
            <p>
            One of the key concerns in thyroid nodule management is determining which nodules may harbor cancer. While the majority of thyroid nodules are benign, there is ongoing research into 
            the potential for transformation from benign thyroid nodule to malignant over time. This transformation, if it occurs, is generally thought to be a rare event.
            </p>
            <div class="thy-img">
            <img src="data:image/png;base64,{BENIGN_CANCER_B64}"       
                style="max-width: 520px; width: 100%; border-radius: 16px; box-shadow: 0 8px 20px rgba(0,0,0,0.15);">
            </div>
            <p>
            While benign thyroid nodules are generally stable and do not commonly transform into malignant nodules, there is a small but real potential for changes that warrant careful monitoring. 
            The majority of benign nodules remain benign, but vigilant follow-up is crucial for early detection of any possible malignant transformation. Advances in diagnostic techniques and ongoing research 
            continue to improve our understanding of thyroid nodule behavior and management, helping to ensure that patients receive the most appropriate and effective care. Staying informed and proactive is the best 
            way to manage thyroid health and address any potential issues before they become serious.
            </p>
        </div>
        <!-- Symptoms -->
        <div class="thy-section">
            <h1>Symptoms</h1>
            <p>
            In the early stage of the disease, symptoms of a benign thyroid tumour do not manifest themselves. As the tumour grows, patients feel lumps in the neck and develop the following symptoms:
            </p>
            <ul>
                <li>Fatigue</li>
                <li>Pain in the area of the neoplasm</li>
                <li>Difficulty swallowing</li>
                <li>Hoarseness of voice and coughing</li>
                <li>Weight loss, headaches</li>
                <li>Insomnia</li>
                <li>Palpitations</li>
                <li>Mood swings</li>
                <li>Excessive sweating</li>
            </ul>
            <p>
                In some cases, nodules can produce excess thyroid hormones and lead to symptoms of hyperthyroidism.
            </p>
        </div>

        <!-- Diagnosis -->
        <div class="thy-section">
            <h1>Diagnosis</h1>
            <p>
                In more than 70% of cases, patients discover benign thyroid tumours by themselves during palpation of the neck, or by the doctors during diagnostics for another disease.
            </p>
            <ul>
                <li>If the neoplasm is small, it is treated with drug therapy. Patients take prescribed medications to normalize the level of thyroid hormones.</li>
                <li>Tumours that are large and produce symptoms need to be removed by surgery or radiofrequency ablation.</li>
                <li><b>Physical examination:</b> A doctor may feel a lump in the neck during a routine check-up or after a patient reports symptoms.</li>
                <li><b>Imaging tests:</b> An ultrasound is commonly used to get a detailed image of the thyroid and assess the size, shape, and appearance of the nodule.</li>
                <li><b>Fine-needle aspiration biopsy (FNAB):</b> This is the most important test for determining whether a thyroid nodule is benign or suspicious. A thin needle 
                is used to collect a small sample of cells from the nodule, usually under ultrasound guidance. The sample is then examined under a microscope by a pathologist.</li>
            </ul>
        </div>
        """,
        height=3200,
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