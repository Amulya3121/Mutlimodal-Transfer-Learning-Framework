import streamlit as st
import streamlit.components.v1 as components
import base64

def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Replace with your malignant tumor image
MALIGNANT_B64 = image_to_base64("malignant.jpeg")

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
            margin: 0 auto 40px auto;
            padding: 0;
            max-width: 900px;
        }}

        /* Main section titles */
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
            <h1>Malignant Thyroid Nodules</h1>
            <div class="thy-nav">
                <span class="tab">Overview</span>
                <span class="tab">Types</span>
                <span class="tab">Symptoms</span>
                <span class="tab">Diagnosis</span>
                <span class="tab">Treatment</span>
            </div>
        </div>

        <div class="thy-img">
            <img src="data:image/jpeg;base64,{MALIGNANT_B64}">
        </div>

        <!-- Overview -->
        <div class="thy-section">
            <h1>Overview</h1>
            <p>
                A malignant thyroid nodule is a tumor that occurs in the thyroid gland and is cancerous in nature. The thyroid gland is an 
                endocrine gland located at the front of the neck, shaped like a butterfly, and controls the production of hormones that regulate 
                metabolism, heart rate, body temperature, and levels of energy.
            </p>
            <p>
                Thyroid nodules are very common, but only a small percentage of them may be malignant or cancerous in nature. 
                Malignant thyroid nodules occur when abnormal cells grow uncontrollably due to genetic mutations, leading to the formation of a tumor. 
                The tumor may be localized to the thyroid gland or may metastasize to the surrounding lymph nodes and other parts of the body, like the lungs or bones.
            </p>
            <p>
            Thyroid cancer is considered to be one of the most treatable and curable forms of cancer. The nature of the malignant thyroid nodule depends on the size of the 
            tumor, the rate of growth, and the extent of metastasis to the surrounding tissues.
            </p>
            <p>
            Physical examination, ultrasound imaging, blood tests, and fine needle aspiration biopsy of the tumor have significantly improved the outcome of thyroid cancer.
            </p>
        </div>

        <!-- Types -->
        <div class="thy-section">
            <h1>Types of Thyroid Cancer</h1>
            <p>
            There are three main types of cancer, and the look of the cancer cells classifies them as:</p>
            <ul>
            <li>differentiated, with cells appearing similar to the regular thyroid cells</li>
            <li>medullary, with cells developing from our C cells, which are the cells that produce the hormone that regulates calcium and phosphate in your blood</li>
            <li>anaplastic, with cells appearing different from regular thyroid cells</li>
            </ul>
            <p>
            Types of thyroid cancer can include:
            </p>

            <h3>Papillary Thyroid Carcinoma</h3>
            <p>
                Papillary thyroid cancer is a well-differentiated form of thyroid cancer. It’s the most common type of thyroid cancer. This type of cancer cell grows slowly. However, when they do grow, they can spread to lymph nodes.
                Papillary cancer is often treated successfully and has a low rate of mortality.
            </p>

            <h3>Follicular Thyroid Carcinoma</h3>
            <p>
                Follicular thyroid cancer (FTC) is the second most common type of differentiated thyroid cancer. There tends 
                to be a higher rate of FTC in places where people eat a diet deficient in iodine. A lack of iodine may be related to certain types of thyroid cancer, including FTC, but more research is needed to confirm this. Like papillary cancer, 
                FTC has a good outlook, even though it can spread to other parts of the body when untreated.
            </p>

            <h3>Hurthle Cell Cancer</h3>
            <p>
            Hurthle cell thyroid carcinoma accounts for 5 percent of all thyroid cancer diagnoses. It is a type of follicular thyroid cancer and can be more aggressive than other types. It also has a greater chance of metastasizing or spreading to other parts of the body.</p>
            <p>Factors like age, tumor size at diagnosis, cancer stage at diagnosis, and sex may affect the outlook for people with Hurthle cell cancer.</p>

            <h3>Sporadic Medullary Thyroid Carcinoma</h3>
            <p>
                Sporadic medullary thyroid cancer (MTC) comes from the C cells of your thyroid gland. These cells make a hormone that controls the amount of calcium in your blood. Between 75 and 85 percent of 
                medullary thyroid cancers are sporadic, meaning they aren’t hereditary. Sporadic medullary thyroid cancer occurs mainly in older adults. If diagnosed in stages I through III, MTC can have a good outlook.
            </p>

            <h3>Anaplastic Thyroid Carcinoma</h3>
            <p>
                Anaplastic thyroid cancer is the most aggressive form of thyroid cancer. It is undifferentiated, 
                which means that the cells do not look like normal thyroid gland cells. While rare, this type of cancer can also 
                metastasize to distant locations in the body. Because it spreads fast, it may not be diagnosed until it has already spread. 
                This can make treating it more difficult. All anaplastic thyroid cancers are considered stage IV.
            </p>

            <h3>Thyroid Lymphoma</h3>
            <p>
            This is a rare type of thyroid cancer. It begins in the white blood cells located within the thyroid gland.
            Thyroid lymphoma can occur frequently in people with Hashimoto’s thyroiditis, a chronic autoimmune disease that damages the thyroid.</p>
            <p>
            In general, thyroid lymphoma may have a good outlook. Factors that can influence outlook may include age, tumor size at diagnosis, stage, and treatment type.
            </p>
        </div>

        <!-- Symptoms -->
        <div class="thy-section">
            <h1>Symptoms</h1>
            <ul>
                <li>A lump or nodule that can be felt in front of the neck.</li>
                <li>Hoarse voice</li>
                <li>Difficult to swallow</li>
                <li>Difficulty breathing</li>
                <li>Persistent cough</li>
                <li>Swollen lymph nodes in the neck</li>
                <li>Pain sensation in the neck and throat.</li>
            </ul>
            <p>
                In many cases, early thyroid cancer may not cause noticeable symptoms.
            </p>
        </div>

        <!-- Diagnosis -->
        <div class="thy-section">
            <h1>Diagnosis</h1>
            <ul>
                <li>Physical examination The thyroid doctor will perform a physical examination of the neck to detect growths or changes in 
                the thyroid gland, such as a lump or nodes on the thyroid. The doctor will record the medical history such as any radiation exposure or a family hereditary.</li>
                <li>Thyroid profile test There are many blood tests to detect thyroid problems. One of the tests is known as tumour marker tests or cancer markers, 
                in the blood, urine, or body tissues.</li>
                <li>Blood tests include-</li>
                <p>
                Thyroid hormone levels, Thyroid-stimulating hormone (TSH),Thyroglobulin (Tg) and thyroglobulin antibodies (TgAb), Medullary type-specific tests.
                </p>
                <li>Ultrasound scan High-frequency sound waves of ultrasound is used to find out thyroid disorders.</li>
                <li>Biopsy test A biopsy test can make a definite diagnosis. To determine whether a nodule is malignant or benign is done through a biopsy.</li>
                <li>Molecular testing of the nodule sample Genetic testing of the thyroid nodule may help to know the risk of the thyroid nodule being cancerous.</li>
                <li>Radionuclide scanning It involves a whole-body scan. It can be done with a very less quantity and harmless amount of radioactive iodine I-131 or I-123, 
                called a tracer. This test is mostly done to examine a thyroid nodule.</li>
                <li>X-ray A chest X-ray test is done to check if cancer has spread to the lungs.</li>
                <li>Computed tomography (CT or CAT) scan CT scans are used to inspect thyroid cancer to examine parts of the neck that cannot be done with ultrasound.</li>
                <li>Positron emission tomography (PET) or PET-CT scan The PET scan is performed to check whether cancer has metastasized.</li>
            </ul>
        </div>

        <!-- Treatment -->
        <div class="thy-section">
            <h1>Treatment</h1>
            <p>
            The treatment for thyroid cancer depends upon the type, stage of the cancer and the overall health of the person. Most thyroid cancer 
            patients show an excellent prognosis, as most of the cases can be cured with timely treatment. The treatment methods include:
            </p>
            <ul>
                <li>Surgery
                <ol type="1">
                <li><b>Thyroidectomy:</b> It involves removing all or most of the thyroid gland.</li>
                <li><b>Thyroid lobectomy:</b> Removing a part of the thyroid gland.</li>
                <li><b>Lymph node dissection:</b> Taking out lymph nodes in the neck.</li>
                </ol></li>
                <li><b>Thyroid hormone therapy:</b> It is a treatment to replace or supplement the thyroid hormones. This therapy medication is usually taken in pill form.</li>
                <li>Radioactive iodine This treatment uses a form of radioactive iodine to destroy thyroid cells and thyroid cancer cells remaining after the surgery.</li>
                <li>Alcohol ablation or ethanol ablation It uses a needle to inject alcohol into small areas of cancerous thyroid tissues. The alcohol ablation therapy causes the thyroid cancer cells to shrink.</li>
                <li>Advanced thyroid cancer treatment involves:
                <ol type="1">
                <li>Targeted drug therapy</li>
                <li>Radiation therapy</li>
                <li>Chemotherapy</li>
                <li>Killing cancer cells with heat and cold therapy</li>
                </ol></li>
            </ul>
        </div>

        """,
        height=3900,
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