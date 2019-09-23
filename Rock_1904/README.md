# Geographic Slice Segmentation: Segment the Geographic Images via Deeplab Algorithm


This repository contains my TensorFlow segmentation implementation, which is highly referenced from [the deeplab github](https://github.com/tensorflow/models/tree/master/research/deeplab). The procedure I provided here allows others to quickly prepare the data, train the model, evaluate results in terms of mIOU (mean intersection-over-union), and visualize segmentation results, especially on our ROCK segmentation project.

## setup tensorflow deeplab and labelme
Install deeplab via running:
* <a href='../g3doc/installation.md'>Deeplab Installation. </a><br>

Since we annotated the rock images via the [Labelme annotation tool](https://github.com/wkentaro/labelme), it is necessary to install the Labelme accordingly:
* <a href='https://github.com/wkentaro/labelme'>Labelme setting up. </a><br>  

## preprocess of images
What we need are original jpg image files and the corresponding json files from the labelme annotaion tool. 

Deeplab actually supports several commonly used dataset format, such as Pascal VOC, Cityscapes and ADE20K. The code for data generation is provided in <a href='../datasets/'>Generate Data </a>. I here used the Pascal VOC data format. The original rock images in jpg reside in <a href='../Rock_1904/JPEGImages'>JPEGImages/</a>, and the json files from Labelme resdie in <a href='../Rock_1904/Org_Json'>Org_Json/</a>, whose labels needs to be converted according to the task. 

### statistics on images and labels
The original annotation of rock images includes 30+ kinds of minerals, like "q","qtz","mag","holes" as shown in <a href='../Rock_1904/preprocess/Org_Label.md'>Original Label</a>. However, availabe sample size is relatively small (aournd 300 images). Hence, I have to focus on few commonly seen minerals at this moment. 

The following code calculate the statistics of the annoatated rock images and generate barplots:

```python
## under the research/deeplab
LABEL_NAME_MAP = {
   ## if we only segment the "qtz" class for this time
   "_background_": 0,
   "qtz": 1,
}
```

The following code is used to 1) limit the labels for segmentation, and 2) generate PNG files as labels following the Pascal VOC format. 

 * <a href='preprocess/Org_json_to_newPNG.py'>Org_json_to_newPNG.</a><br> 
 
 Assume I only focus on the "qtz" mineral, which is actually the consumer's target at this stage, then the LABEL_NAME_MAP can be defined as:

```python
LABEL_NAME_MAP = {
   ## if we only segment the "qtz" class for this time
   "_background_": 0,
   "qtz": 1,
}
```

 

Preprocess procedure can be found in:
* <a href='preprocess/Preprocess.md'>Preprocess.</a><br>

## Training

## Evaluation 

### Visualize on single image

Firstly, export the model to a .pb file:

```bash
# From the tensorflow/models/research/deeplab directory.
sh myexport.sh
```

Then, use the "myeval.py" function to generate a segmented image:

```bash
# From the tensorflow/models/research/deeplab/ directory.
python myeval.py \
--image_dir=

```

