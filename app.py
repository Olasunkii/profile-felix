from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Felix_CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Felix"
PAGE_ICON = ":wave:"
NAME = "Olasunkanmi Felix Oyadokun"
DESCRIPTION = """
Data Scientist and Researcher, assisting enterprises by transforming raw data into insightful information that is needed in order to advance and compete .
"""
EMAIL = "olasunkanmifelix@yahoo.com"
SOCIAL_MEDIA = {
    #"YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "www.linkedin.com/in/olasunkanmi-oyadokun-28b24aa7",
    "GitHub": "https://github.com/Olasunkii",
    "Twitter": "https://twitter.com/ytppk",
}
PROJECTS = {
    "🏆 Multi Disease Prediction - Pridect two different diseases given required features": "https://olasunkii-multiple-disease-app-v8khw5.streamlit.app/",
    "🏆 Automated EDA - Load your csv files and get EDAs": "https://olasunkii-auto-eda-app-ckehcv.streamlit.app/",
    "🏆 Heart Disease Prediction - Given some fearture, predict if a patient has heart disease or not": "https://github.com/Olasunkii/heart-disease",
    "🏆 Bulldozer Price Prediction - Given some fearture, predict price of bulldozers": "https://github.com/Olasunkii/Bulldozer_Price_Predition",
    "🏆 Lanaguage Identification - Predict a language given a set of parameters": "https://github.com/Olasunkii/language_identification/blob/main/Language_Classification.ipynb",
    "🏆 Wine Classification - Pridect wine type given various features": "https://github.com/Olasunkii/wine-clasification",
}

RESEARCH = {
    "🏆 Design and Implementation of Secured Communication in A Wireless Network Using Modifies Advanced Encryption Standard Algorithm": " http://dx.doi.org/10.13140/RG.2.2.29678.84804",
    "🏆 Decomposition of Advanced Encryption Standard (AES) Algorithm": "http://dx.doi.org/10.13140/RG.2.2.12455.98723",
    "🏆 Advanced Encryption Standard Algorithm for File Security": "https://www.irejournals.com/formatedpaper/17038321.pdf",
    "🏆 Essential Building Blocks of Convolutional Neural Network for Deep Learning": "https://www.irejournals.com/formatedpaper/1703854.pdf",
    "🏆 Curbing the Waste of Electrical Energy in Nigeria-A Case Study of Federal University of Technology, Minna": "https://www.academia.edu/41771948/CURBING_THE_WASTE_OF_ELECTRICAL_ENERGY_IN_NIGERIA-A_CASE_STUDY_OF_FEDERAL_UNIVERSITY_OF_TECHNOLOGY_MINNA?auto=download",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 7 Years expereince in research and teaching
- ✔️ Strong practical expertise in Python, SQL, and Excel 
- ✔️ A solid grasp of statistical concepts and the applications that they have 
- ✔️ Excellent team player who takes the initiative to complete assignments 
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas)
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Machine Learning: Logistic, Classification and Unsuppervised ML
- 🗄️ Databases: Postgres, and SQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Scientist/Analyst (Intern) | Explore AI Academy**")
st.write("07/2022 - Present")
st.write(
    """
- ► Used PowerBI to design and present various dashboards
- ► Data Engineer in a team of four in building and deploying a movies recommender system
- ► Prformed data cleaning, feature engineering, EDAs and predictions on different datasets
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Analyst | Natview Foundation for Technlogy**")
st.write("06/2022 - 01/2023")
st.write(
    """
- ► Scripted survey forms for Covid 19 and Sustainable Development Goals and uploaded them on ODK collect
- ► Processed several health related data and analyzed them using MS Excel, Power bi and Python and provided insight to  help NFT lab make informed decisions
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Teacher | NISMES**")
st.write("09/2015 - 01/2022")
st.write(
    """
- ► Planning teaching, including lectures, seminars/tutorials and learning materials
- ► Meeting students individually to discuss progress
- ► Meeting students individually to discuss progress
- ► Pursuing research
- ► Interviewing potential students
- ► Carrying out administration, such as attending faculty meetings and writing reports
- ► Planning teaching, including lectures, seminars/tutorials and learning materials
- ► Writing research proposals, papers and other publications
- ► Supervising National Diploma students
- ► Managing research budgets
- ► Preparing bids for funding for departmental research projects.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Research")
st.write("---")
for research, link in RESEARCH.items():
    st.write(f"[{research}]({link})")

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
