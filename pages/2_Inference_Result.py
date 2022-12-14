# ====== ====== [ Phase 2. Show inference result ] ====== ======


# ====== ====== ====== [   LIB    ] ====== ====== ======

import streamlit as st
import os
import time
import numpy as np


# ====== ====== ====== [  CONFIG  ] ====== ====== ======
DIST_PACK_DIR = os.path.dirname(os.path.realpath(__file__))
VIA_SRC_DIR = os.path.join(DIST_PACK_DIR, '../..')

# ====== ====== ====== [ FUNCTION ] ====== ====== ======

def progressBar():
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    # chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        # chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()


# ====== ====== ====== [   MAIN   ] ====== ====== ======

def inference_result():

    st.set_page_config(page_title="Inference result", page_icon="📈")

    st.markdown("# Inference result")
    st.sidebar.header("Inference result")
    st.write(
        """This demo illustrates a combination of plotting and animation with
        Streamlit. We're generating a bunch of random numbers in a loop for around
        5 seconds. Enjoy!"""
    )
    
    st.image(os.path.join(VIA_SRC_DIR,"dist/data/000015_00.png"))
    
    st.button("Open VIA")

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    # st.button("Re-run")
    
inference_result()