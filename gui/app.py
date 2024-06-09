import sys
import os
import streamlit as st

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(src_path)

from gen.main import PandasToPolarsCrew


class PandasToPolarsGUI:

    def apply_css(self, file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    @st.cache
    def convert_pandas_to_polars(self, pandas_code):

        pandas_code = {
            'pandas_code': pandas_code
        }

        crew = PandasToPolarsCrew()
        result = crew.run(pandas_code)
        return result

    def main_page(self):
        # Text area for code input with a unique key
        st.session_state.pandas_code = st.text_area("Enter your Pandas code here:",
                                                    height=300,
                                                    key="pandas_code_input",
                                                    value=st.session_state.pandas_code)

        # Apply custom CSS for dark mode
        self.apply_css("style.css")

        # Convert button
        convert_button_disabled = st.session_state.get('button_clicked', False)
        if st.button("Convert to Polars", key="convert_button", disabled=convert_button_disabled):
            st.session_state.button_clicked = True
            if st.session_state.pandas_code:
                st.session_state.polars_code = self.convert_pandas_to_polars(st.session_state.pandas_code)
            else:
                st.warning("Please enter some Pandas code to convert.")
            st.session_state.button_clicked = False

        # Text area for code output with a unique key
        if st.session_state.get('polars_code', ''):
            st.text_area("Polars code output:", value=st.session_state.polars_code, height=300,
                         key="polars_code_output")

    def render(self):
            st.set_page_config(page_title="Pandas To Polars Converter", page_icon=":snake:")
            st.title("Pandas To Polars Converter")

            # Initialize session state
            if 'pandas_code' not in st.session_state:
                st.session_state.pandas_code = ""
            if 'polars_code' not in st.session_state:
                st.session_state.polars_code = ""
            if 'button_clicked' not in st.session_state:
                st.session_state.button_clicked = False

            self.main_page()


if __name__ == "__main__":
    PandasToPolarsGUI().render()
