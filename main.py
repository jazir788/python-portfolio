import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/me2.jpg")
with col2:
    st.title("Jazir Shine")
    content = """ 
    Junior developer with two years of software developer consultancy experience,
    bringing a strong foundation in front-end development, backed by a year of hands-on experience. 
    I have actively contributed to four diverse projects, encompassing consulting and full-stack development, 
    where I've played a pivotal role in creating essential functionalities. 
    My passion for coding and problem-solving, combined with a commitment to staying updated on industry trends, 
    allows me to deliver high-quality results and continuously improve my skills. 
    I am excited to leverage my expertise in software development to drive innovation 
    and make a positive impact on future projects.
    """
    st.info(content)