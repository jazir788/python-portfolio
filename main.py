import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, emptycol1, col2 = st.columns([1.5,0.5,1.5])

with col1:
    st.image("images/me_2.jpg")
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

content2 = """Below you can find some of the apps I have built in Python. Feel free to contact me! """
st.write(content2)

col3, emptycol2, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv", sep=";")
with (col3):
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write("[Source Code](Link)")





