import streamlit as st

class Home:
    def __int__(self):
        pass
    def app(self):
        st.write("##")
        st.subheader("Hi, I am Zhanibek")
        st.title("I am student of double degree program Arizona University")
        st.write('I am passionate about learning IT. In my logo imaged team from anime called "Haikuuy" that translated as volleyball. :)  ')

        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I do")
            st.write("##")
            st.write(
                """
                - I read books
                - Play volleyball
                - Study and develop
                """
            )



