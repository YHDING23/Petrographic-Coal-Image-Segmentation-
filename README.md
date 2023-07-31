# PetroGraphic Coal Segmentation via DeepLab v3

This project aims to segment 10+ kinds of minerals (such as Quartz, Pyrite, Mica and interstitial) in microscope images under varied conditions. As shown in the Figure, the inputs are two geographic or petrographic chip images collected under plane-polarized light and cross-polarized light, respectively. The chip shows variant resolutions, edges and textures under these conditions. With our proposed model, mIoU achieves ~78%, overcoming the deeplabv3 (61%) and PSPnet (69%). 



The model can only be downloaded and tested after applying for a permit from the repository author[dingyaohui2016@gmail.com]. 

DeepLab is a state-of-art deep learning model for semantic image segmentation,
where the goal is to assign semantic labels (e.g., person, dog, cat and so on)
to every pixel in the input image. In deeplab v3+, the decoder module to refine the segmentation results especially along object
boundaries. Furthermore, in this encoder-decoder structure one can
arbitrarily control the resolution of extracted encoder features by atrous convolution to trade-off precision and runtime.

*   Proposed Method
```
@inproceedings{deeplabv3plus2019,
  title={Petrographic Coal Images Segmentation Based on an Enhanced Deeplabv3 Model},
  author={Yaohui Ding, Changzheng Zan, Ye Zhou},
  booktitle={Computers & Geosciences},
  year={2019}
}
```

*   DeepLabv3+:

```
@inproceedings{deeplabv3plus2018,
  title={Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation},
  author={Liang-Chieh Chen and Yukun Zhu and George Papandreou and Florian Schroff and Hartwig Adam},
  booktitle={ECCV},
  year={2018}
}
```




# PetroGraphic Coal Segmentation via DeepLab v3
