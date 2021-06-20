import streamlit as st


class About:
    name = "About Me"

    @staticmethod
    def display():
        st.markdown(
            "Hi! My name is Alex, I'm a PhD Student at CVSSP, University of Surrey"
        )


class Projects:
    name = "Projects"

    @staticmethod
    def display():
        st.markdown("# Projects")
        cols = st.beta_columns(2)
        with cols[0]:
            st.markdown('### Compositional Sketch Search')
            st.markdown(
                "[![](https://shields.io/badge/github--green?logo=github&style=social)](https://github.com/alexblck/compsketch) "
                "[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/alexblck/compsketch/share/src/) "
                "[![arXiv](https://img.shields.io/badge/arXiv-2106.08009-b31b1b.svg?style=flat)](https://arxiv.org/abs/2106.08009) "
            )
            st.markdown('#### ICIP 2021')
            st.markdown(
                'Compositional Sketch Search started as my MSc dissertation project. '
                'It has won The MSc Advisory Board Prize which is awarded to the best project on any MSc full time '
                'programme in Electronic Engineering. '
                'It was then published at International Conference on Image Processing (ICIP) 2021.')
        with cols[1]:
            st.image('https://github.com/AlexBlck/compsketch/raw/main/examples/header.png')

        st.markdown('---')

        cols = st.beta_columns(2)
        with cols[0]:
            st.markdown('### Deep Image Comparator')
            st.markdown(
                "[![](https://shields.io/badge/wandb-psbattles-green?logo=weightsandbiases&style=flat)](https://wandb.ai/alex-flox/psbattles) "
                "[![](https://shields.io/badge/pdf-CVF-blue?logo=adobeacrobatreader&style=flat)](https://openaccess.thecvf.com/content/CVPR2021W/WMF/html/Black_Deep_Image_Comparator_Learning_To_Visualize_Editorial_Change_CVPRW_2021_paper.html) ")
            st.markdown('#### CVPR WMF 2021')
            st.markdown('Provided a query image, retrieves the original from a trusted database and highlights any editorial changes.')
        with cols[1]:
            st.video('https://youtu.be/5dIaM2-Zq3I')
