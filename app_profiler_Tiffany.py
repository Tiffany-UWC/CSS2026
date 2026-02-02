import streamlit as st
import pandas as pd
import numpy as np


# Page Config/customizations
st.set_page_config(
    page_title=" 🔬Researcher Profile",
    layout="wide"  
)

st.markdown(
    """
    <style>
    /* Background colour */
    .stApp {
        background-color: #000000;
        color: #ffffff; 
    }
    
     /* Card styling */
    .card {
        background-color: rgba(255, 255, 255, 0.95);
        color: #000;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        margin-bottom: 20px;
        text-align: center;
    }

    /* Centre Streamlit headings */
    h1, h2, h3, h4, h5, h6 {
    text-align: center !important;
    }

    /* Centre ALL text */
    .stMarkdown * {
    text-align: center !important;
    }
 
    /* Centre bullet lists*/
    .stMarkdown ul,
    .stMarkdown ol {
    list-style-position: inside;
    padding-left: 0 !important;
    margin-left: 0 !important;
    }

    </style>
    """,
    unsafe_allow_html=True  
)

# My Basic Info 
name = "Tiffany Fredericks"
field = "Bioinformatics"
institution = "University of the Western Cape"

col1, col2, col3 = st.columns([2, 3, 2])

with col1:
    st.image(
        "https://cdn.pixabay.com/animation/2025/07/24/00/26/00-26-53-596_512.gif", width=500
    )

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🔬 Researcher Overview")
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.image(
        "https://cdn.pixabay.com/animation/2025/07/24/00/26/00-26-53-596_512.gif", width=500
    )

# Researcher Summary/Overview
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header(" 👤 Overview")
st.write("""MSc Bioinformatics Candidate (UWC). Focusing on a project which aims to develop a 
         bioinformatics pipeline to analyse genotyping microarray data for human leukocyte antigen 
         (HLA) genotype and pharmacogenetic (PGx) profiles in population cohorts from the Western Cape, South Africa. 
         This work addresses the underrepresentation of the genetically diverse African populations in 
         global genomic research, and aims to inform genotype-guided healthcare predictions in the Western Cape.""")
st.markdown('</div>', unsafe_allow_html=True)

# Education 
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("🎓 Education")
st.write("**MSc in Bioinformatics**  \nUniversity of the Western Cape (UWC)  \n2025–current")
st.write("**BSc (Hons) in Biotechnology**  \nUniversity of the Western Cape (UWC)  \n2024  \n*Dean's merit award; 80.41% aggregate*")
st.write("**BSc in Biotechnology**  \nUniversity of the Western Cape (UWC)  \n2021–2023  \n*Graduated Cum Laude, Dean's merit award, 75.51% aggregate*")
st.markdown('</div>', unsafe_allow_html=True)


# Technical Skills
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("💻 Technical Skills")
st.write("""
- Data quality control (QC) and analysis 
- Genomic data processing (Plink, GenomeStudio, Imputation)
- Statistical analysis and modelling (R)
- Data workflows and containerization
- MySQL database development
""")
st.markdown('</div>', unsafe_allow_html=True)

# Contact Info
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("Contact Information")

email = "tfredericks@myuwc.ac.za"
linkedin = "https://www.linkedin.com/in/my-profile"
cell = "+27 67 139 2877"

st.write(f"📧 **Email:** {email}")
st.write(f"🔗 **LinkedIn:** {linkedin}")
st.write(f"📱 **Cell:** {cell}")

st.markdown('</div>', unsafe_allow_html=True)
