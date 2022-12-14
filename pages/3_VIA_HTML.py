# ====== ====== [ Phase 3. Modify annotation by VIA ] ====== ======


# ====== ====== ====== [   LIB    ] ====== ====== ======

import streamlit as st
import streamlit.components.v1 as components

import os
import sys
import json
import string
import base64


# ====== ====== ====== [  CONFIG  ] ====== ====== ======

DIST_PACK_DIR = os.path.dirname(os.path.realpath(__file__))
VIA_SRC_DIR = os.path.join(DIST_PACK_DIR, '../')

SOURCE_HTML = os.path.join(VIA_SRC_DIR,'src','index.html')

if len(sys.argv) == 1:
  TARGET = 'basic'
  OUT_HTML = os.path.join(VIA_SRC_DIR,'via_demo.html')
  print("Usage: python3 pack_demo.py [face|wikimedia|face_track_annotation]")
else:
  TARGET = sys.argv[1]
  OUT_HTML = os.path.join(VIA_SRC_DIR,'via_'+TARGET +'_demo.html')
# print("[Test] sys.argv => {}".format(sys.argv))

# - Fetch demo data and demo scripts -
TARGET_DEMO_JS_FILENAME = os.path.join(VIA_SRC_DIR,'src','demo','_via_'+TARGET+'_demo.js')
TARGET_OUT_JS_FILENAME = os.path.join(VIA_SRC_DIR,'_via_'+TARGET+'_demo.js')

# - Fetch COCO anno JSON -
TARGET_COCO_JSON_FILENAME = os.path.join(VIA_SRC_DIR,'data','test_coco_ann.json')

# - Fetch COCO anno JSON -
TARGET_ATTR_JSON_FILENAME = os.path.join(VIA_SRC_DIR,'data','via_project_attributes.json')


# ====== ====== ====== [ FUNCTION ] ====== ====== ======

def get_file_contents(filename): #[not used]
  with open(filename) as f:
    return f.read()

def get_src_file_contents(filename):
    # full_filename = os.path.join(VIA_SRC_DIR, 'src', filename)
    with open(filename) as f:
        return f.read()

def Base64_Encode(img_path):
    with open(img_path, "rb") as img_f:
        base64_img = base64.b64encode(img_f.read())
    return "data:image/jpeg;base64,"+base64_img.decode("utf-8")


# ====== ====== ====== [   MAIN   ] ====== ====== ======

def VIA_html():
    st.set_page_config(page_title="VIA HTML", page_icon="📈", layout="wide", initial_sidebar_state="collapsed")

    # ------ ------ Load source files ------ ------
    TARGET_DEMO_JS = get_src_file_contents(TARGET_DEMO_JS_FILENAME)
    TARGET_COCO_JSON = get_src_file_contents(TARGET_COCO_JSON_FILENAME)
    TARGET_ATTR_JSON = get_src_file_contents(TARGET_ATTR_JSON_FILENAME)

    # ------ ------ Compile images in Base64 ------ ------
    # - List image file path in DIR -
    all_img_list = os.listdir(os.path.join(VIA_SRC_DIR,"data")) #dist/
    all_img_list = [imgf for imgf in all_img_list if not imgf.endswith('.json')]
    # - Base64 encoding -
    base64_imgs = [Base64_Encode(os.path.join(VIA_SRC_DIR,'data',img_path)) for img_path in all_img_list]

    # ------ ------ Compile VIA JS ------ ------
    with open(TARGET_OUT_JS_FILENAME, 'w') as outf:
        with open(TARGET_DEMO_JS_FILENAME, 'r') as inf:
            for line in inf:
                parsedline = line
                if 'var attributes_json = ' in line:
                    parsedline  = "var attributes_json = '"+TARGET_ATTR_JSON+"';\n"
                elif 'var annotations_json = ' in line:
                    parsedline  = "var annotations_json = '"+TARGET_COCO_JSON+"';\n"
                elif 'import_annotations_from_json(annotations_json);' in line:
                    parsedline  = "import_coco_annotations_from_json(annotations_json);\n"
                elif 'var _via_basic_demo_img_filename = [' in line:
                    parsedline  = "var _via_basic_demo_img_filename = "+str(all_img_list)+";\n"
                    for b64 in base64_imgs:
                        parsedline += "_via_basic_demo_img.push('"+b64+"');\n"
                outf.write(parsedline)

    # ------ ------ Compile VIA HTML ------ ------
    with open(OUT_HTML, 'w') as outf:
        with open(SOURCE_HTML, 'r') as inf:
            for line in inf:
                if '<script src="' in line:
                    tok = line.split('"')
                    filename = tok[1] # via.js
                    outf.write('<!-- START: Contents of file (PACK @41): ' + filename + '-->\n')
                    outf.write('<script>\n')
                    outf.write( get_src_file_contents(os.path.join(VIA_SRC_DIR, 'src', filename)) )
                    outf.write('</script>\n')
                    outf.write('<!-- END: Contents of file: ' + filename + '-->\n')
                else:
                    if '<link rel="stylesheet" type="text/css"' in line:
                        tok = line.split('"')
                        filename = tok[5] # via.css
                        outf.write('<!-- START: Contents of file (PACK @50): ' + filename + '-->\n')
                        outf.write('<style>\n')
                        outf.write( get_src_file_contents(os.path.join(VIA_SRC_DIR, 'src', filename)) )
                        outf.write('</style>\n')
                        outf.write('<!-- END: Contents of file: ' + filename + '-->\n')
                    else:
                        parsedline = line
                        if  "<!-- DEMO SCRIPT AUTOMATICALLY INSERTED BY VIA PACKER SCRIPT -->" in line:
                            parsedline += '' # src/demo/_via_basic_demo.js
                            parsedline += '<!-- START: Contents of file (PACK @63): ' + TARGET_OUT_JS_FILENAME + '-->\n'
                            parsedline += '<script>\n'
                            parsedline += get_src_file_contents(TARGET_OUT_JS_FILENAME)
                            # parsedline += "\nfunction _via_basic_demo_define_annotations() {\n"
                            # parsedline += "var annotations_json = '"+TARGET_COCO_JSON+"';\n"
                            # parsedline += "import_coco_annotations_from_json(annotations_json);\n}\n"
                            # parsedline += "var _via_basic_demo_img = [];\n"
                            # parsedline += "var _via_basic_demo_img_filename = ['"+all_img_list[0]+"'];\n"
                            # parsedline += "_via_basic_demo_img.push('"+base64_imgs[0]+"');\n" #data:image/jpeg;base64,
                            parsedline += '</script>\n'
                            parsedline += '<!-- END: Contents of file: ' + TARGET_OUT_JS_FILENAME + '-->\n'
                        outf.write(parsedline)
    print("Written packed file to: " + OUT_HTML)

    # ------ ------ Render VIA HTML ------ ------
    # embed streamlit docs in a streamlit app
    # components.iframe("https://docs.streamlit.io/en/latest")

    # - Get output VIA HTML source -
    with open(os.path.join(VIA_SRC_DIR,"via_demo.html")) as html_file:
        via_demo_html = '{}'.format(html_file.read())

    # - Embed & Render VIA UI on Streamlit -
    components.html(
        via_demo_html,
        height=900,
        width=1450
    )

VIA_html()
