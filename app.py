import streamlit as st


about_page = st.Page(

    page = "views/about.py",
    title = "About Me",
    icon =":material/account_circle:",
    default= True,
)
project_1 = st.Page(

    page = "views/projects.py",
    title = "Projects",
    icon =":material/bar_chart:",
)
project_2 = st.Page(

    page = "views/Chat.py",
    title = "Chat With me",
    icon =":material/smart_toy:",
)
pg = st.navigation(
    {
        "info": [about_page],
        "Project":[project_1],
        "Chat":[project_2],
    }
)
st.logo("assets/logo.png")
st.sidebar.text("Made with ❤ with Qasim")
pg.run()