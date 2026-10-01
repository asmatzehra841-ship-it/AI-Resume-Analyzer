import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Resume Analyzer")
st.write("Analyze your skills and compare them with job requirements.")

st.header("Upload Your Resume")

resume = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

st.header("Job Description")

job = st.text_area(
    "Enter required job skills",
    placeholder="Example: Python, Java, SQL, HTML, CSS"
)

if st.button("Analyze Resume"):

    if resume is not None and job.strip():

        resume_text = resume.getvalue().decode(
            "latin-1", errors="ignore"
        ).lower()

        job_text = job.lower()

        skills = [
            "python", "java", "html", "css",
            "sql", "c++", "javascript",
            "machine learning", "communication"
        ]

        found_skills = [
            skill for skill in skills
            if skill in resume_text
        ]

        required_skills = [
            skill for skill in skills
            if skill in job_text
        ]

        matched_skills = [
            skill for skill in required_skills
            if skill in found_skills
        ]

        missing_skills = [
            skill for skill in required_skills
            if skill not in found_skills
        ]

        percentage = (
            len(matched_skills) / len(required_skills) * 100
            if required_skills else 0
        )

        st.success("Analysis Completed!")

        st.subheader("Your Results")

        st.metric("Skill Match", f"{percentage:.1f}%")

        st.write("### Skills Found")
        st.write(found_skills or "No listed skills detected")

        st.write("### Matched Skills")
        st.write(matched_skills or "No matching skills")

        st.write("### Missing Skills")
        st.write(missing_skills or "No missing skills detected")

        st.info("Keep learning and improving your skills!")

    else:
        st.warning("Please upload a PDF and enter job skills.")