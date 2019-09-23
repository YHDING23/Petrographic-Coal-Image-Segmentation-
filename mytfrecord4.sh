python datasets/build_voc2012_data.py \
--image_folder="Rock_1904/pascal_voc_seg/JPEGImages/" \
--semantic_segmentation_folder="Rock_1904/4classes/SegmentationClassRaw/" \
--list_folder="Rock_1904/4classes/index/" \
--image_format="jpg" \
--output_dir="Rock_1904/4classes/tfrecord/"
