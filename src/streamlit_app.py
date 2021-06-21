import streamlit as st
import pages
import sys
import inspect
import os

st.set_page_config(layout="centered", page_title="Alexander Black", page_icon='🎓')
st.markdown(
    f"""
<style>
    .reportview-container .main .block-container{{
        max-width: {954}px;
    }}
</style>
""", unsafe_allow_html=True)

container_buttons = st.beta_container()
container_header = st.beta_container()

with container_header:
    cols = st.beta_columns(2)

    with cols[0]:
        st.markdown("# Alexander Black")
        st.markdown(
            "[![](https://shields.io/badge/@AlexBlackAI--grey?logo=twitter&style=flat)](https://twitter.com/AlexBlackAI) "
            "[![](https://shields.io/badge/AlexBlck--grey?logo=github&style=flat)](https://github.com/alexblck/) "
            "[![](https://shields.io/badge/Scholar--grey?logo=googlescholar&style=flat)](https://scholar.google.com/citations?user=Xzt0ib0AAAAJ) "
            "[![](https://shields.io/badge/AlexBlck--grey?logo=linkedin&style=flat)](https://www.linkedin.com/in/alexblck/) "
        )
        # st.image(os.path.join(os.path.dirname(__file__), '../imgs/me.jpeg'), width=200)
    st.markdown('---')

pages = {obj.name: obj for name, obj in inspect.getmembers(sys.modules[pages.__name__]) if inspect.isclass(obj)}
page_buttons = dict()
with container_buttons:
    cols = st.beta_columns(6)
    for i, button_name in enumerate(pages.keys()):
        with cols[i + 2]:
            page_buttons[button_name] = st.button(button_name)
    st.markdown('---')

if not any(page_buttons.values()):
    page_buttons['Projects'] = True
for name, pressed in zip(page_buttons.keys(), page_buttons.values()):
    if pressed:
        pages[name].display()
