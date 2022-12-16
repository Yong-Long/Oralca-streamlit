/*
  VGG Image Annotator (via)
  www.robots.ox.ac.uk/~vgg/software/via/

  Copyright (c) 2016-2018, Abhishek Dutta.
  All rights reserved.

  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions are met:

  Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.
  Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
  POSSIBILITY OF SUCH DAMAGE.
*/

function _via_load_submodules() {
  _via_basic_demo_load_img();
  //_via_basic_demo_draw_default_regions();
  _via_basic_demo_define_attributes();
  _via_basic_demo_define_annotations();

  toggle_attributes_editor();
  update_attributes_update_panel();

  annotation_editor_show();
}

function _via_basic_demo_load_img() {
  // add files
  var i, n;
  var file_count = 0;
  n = _via_basic_demo_img.length;
  for ( i = 0; i < n; ++i ) {
    project_file_add_base64( _via_basic_demo_img_filename[i], _via_basic_demo_img[i] );
    file_count += 1;
  }

  _via_show_img(0);
  update_img_fn_list();
}

function _via_basic_demo_draw_default_regions() {
  var csv_annotations = 'filename,file_size,file_attributes,region_count,region_id,region_shape_attributes,region_attributes\nadutta_swan.jpg,-1,"{}",1,0,"{""name"":""polygon"",""all_points_x"":[116,94,176,343,383,385,369,406,398,364,310,297,304,244,158],""all_points_y"":[157,195,264,273,261,234,222,216,155,124,135,170,188,170,175]}","{}"\nwikimedia_death_of_socrates.jpg,-1,"{}",3,0,"{""name"":""rect"",""x"":174,""y"":139,""width"":108,""height"":227}","{}"\nwikimedia_death_of_socrates.jpg,-1,"{}",3,1,"{""name"":""rect"",""x"":347,""y"":114,""width"":91,""height"":209}","{}"\nwikimedia_death_of_socrates.jpg,-1,"{}",3,2,"{""name"":""ellipse"",""cx"":316,""cy"":180,""rx"":17,""ry"":12}","{}"';

  import_annotations_from_csv(csv_annotations);
}

function _via_basic_demo_define_attributes() {
  var attributes_json = '{"region":{"name":{"type":"text","description":"Name of the object","default_value":"not_defined"},"type":{"type":"dropdown","description":"Category of object","options":{"bird":"Bird","human":"Human","cup":"Cup (object)","unknown":"Unknown (object)"},"default_options":{"unknown":true}},"image_quality":{"type":"checkbox","description":"Quality of image region","options":{"blur":"Blurred region","good_illumination":"Good Illumination","frontal":"Object in Frontal View"},"default_options":{"good":true,"frontal":true,"good_illumination":true}}},"file":{"caption":{"type":"text","description":"","default_value":""},"public_domain":{"type":"radio","description":"","options":{"yes":"Yes","no":"No"},"default_options":{"no":true}},"image_url":{"type":"text","description":"","default_value":""}}}';

  project_import_attributes_from_json(attributes_json);
}

function _via_basic_demo_define_annotations() {
  var annotations_json = '{"adutta_swan.jpg-1":{"filename":"adutta_swan.jpg","size":-1,"regions":[{"shape_attributes":{"name":"polygon","all_points_x":[116,94,176,343,383,385,369,406,398,364,310,297,304,244,158],"all_points_y":[157,195,264,273,261,234,222,216,155,124,135,170,188,170,175]},"region_attributes":{"name":"Swan","type":"bird","image_quality":{"good_illumination":true}}}],"file_attributes":{"caption":"Swan in lake Geneve","public_domain":"no","image_url":"http://www.robots.ox.ac.uk/~vgg/software/via/images/swan.jpg"}},"wikimedia_death_of_socrates.jpg-1":{"filename":"wikimedia_death_of_socrates.jpg","size":-1,"regions":[{"shape_attributes":{"name":"rect","x":174,"y":139,"width":108,"height":227},"region_attributes":{"name":"Plato","type":"human","image_quality":{"good_illumination":true}}},{"shape_attributes":{"name":"rect","x":347,"y":114,"width":91,"height":209},"region_attributes":{"name":"Socrates","type":"human","image_quality":{"frontal":true,"good_illumination":true}}},{"shape_attributes":{"name":"ellipse","cx":316,"cy":180,"rx":17,"ry":12},"region_attributes":{"name":"Hemlock","type":"cup"}}],"file_attributes":{"caption":"The Death of Socrates by David","public_domain":"yes","image_url":"https://en.wikipedia.org/wiki/The_Death_of_Socrates#/media/File:David_-_The_Death_of_Socrates.jpg"}}}';

  import_annotations_from_json(annotations_json);
}

var _via_basic_demo_img = [];
