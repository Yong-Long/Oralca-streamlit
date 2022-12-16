# ====== ====== [ Phase 1. Select inference material ] ====== ======


# ====== ====== ====== [   LIB    ] ====== ====== ======

import streamlit as st
import os
import time
import numpy as np


# ====== ====== ====== [  CONFIG  ] ====== ====== ======
DIST_PACK_DIR = os.path.dirname(os.path.realpath(__file__))
VIA_SRC_DIR = os.path.join(DIST_PACK_DIR, '../')

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
    st.image(os.path.join(VIA_SRC_DIR,"data/000015_00.png"))
    # inference_result()

def upload_image_files(inImgsName,inImgsDict,inImgsData):
    upload_files = st.file_uploader("Please choose image files",accept_multiple_files=True)
    for idx, inFile in enumerate(upload_files):
        inImgsName.append(inFile.name)
        inImgsDict[inFile.name] = idx
        inImgsData.append(inFile.read())
    return inImgsName,inImgsDict,inImgsData

# ====== ====== ====== [   MAIN   ] ====== ====== ======

def select_inference_material():
    st.set_page_config(page_title="Select inference material", page_icon="📈")
    
    st.markdown("# Select inference material")
    st.sidebar.header("Select inference material")
    st.write(
        """This demo illustrates a combination of plotting and animation with
        Streamlit. We're generating a bunch of random numbers in a loop for around
        5 seconds. Enjoy!"""
    )
    
    #if st.button("Load data"):
    inImgsName = []
    inImgsDict = {}
    inImgsData = []
        
    #if st.button("Upload images"):
    inImgsName,inImgsDict,inImgsData = upload_image_files(inImgsName,inImgsDict,inImgsData)
    
    #st.image(os.path.join(VIA_SRC_DIR,"data/000015_00.png"))
    # col1, col2 = st.columns(2)
    if inImgsData != []:
        selImg = st.radio(
            "Select a image to view",
            inImgsName
        )
        st.image(inImgsData[inImgsDict[selImg]])
    
    if st.button("Inference"):
        progressBar()
    
    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    # st.button("Re-run")
    
select_inference_material()
