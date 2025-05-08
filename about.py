import streamlit as st
from form.conatct  import conatct_form

@st.dialog("Conatact Me" )
def show_conatct_form():
     conatct_form()




col1, col2 = st.columns(2, gap="small",vertical_alignment="center")

with col1:
    st.image("./assets/profile.png" , width=230)

with col2:
    st.title("QASIM ALI",anchor=False)
    st.write(
        "E-commerce  website Developer or Python Developer "
    )
    if st.button("Conatct Me"):
         show_conatct_form()


st.write("\n")

st.subheader("Experience / Qualification", anchor=False)

st.write(
     
     """
     - Advance diploma in Software Engineering
     - CMA(Chartered Management Accountants) Ongoing
     - 1.5  year experience in E-commerce
     - Strongs hands-on knowledge in python with its frameworks
     """
)

st.write("\n")
st.subheader("Hard Skills",anchor=False)
st.write(
    
     """
      - Python (Streanlit , django , pandas , Sql)
     - Web Desging (Html , css , Bootsrap , Raactjs)
      - web development ( Express , Php )
      - E-commerce ( Wordpress , Spoify )
     - Database ( mysql , SqlServer , monogodb)

     """
)