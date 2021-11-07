# A-Two-stream-CNN-based-Visual-Quality-Assessment-Method-for-Light-Field-Images

Light Field (LF) cameras are able to capture both the intensity and the direction of light rays from the scene. Thisrich information demands a certain amount of memory and bandwidth for storage and transmission and, to alle-viate this requirement, LF content is processed and compressed. These operations often add degradations to theLF content that may affect their visual quality, requiring the use of methods that are able to measure the visualquality as perceived by the end consumer.  In this paper, we propose a no-reference LF image quality assessment(LF-IQA) method that is based on a two-stream CNN architecture. The two-stream CNN interprets and learnscomplex binocular characteristics in spatial and angular domains of distorted LF contents, and predicts qualityscores that are in correlation with subjective quality assessment. The first stream processes the angular infor-mation from canny maps of Epipolar Plane Images (EPIs) generated from the corresponding LF contents, whilethe second stream processes the spatial information from mean canny maps generated from canny maps of sub-aperture images (SAIs).  We also propose a novel approach to generate multiple epipolar-plane images, and we name this approach as MultiEPL. Results show that the proposed method outperforms state-of-the-art LF-IQAmethods.

# Paper: coming soon...

# Base Model:
StereoQA-Net: https://github.com/weizhou-geek/Stereoscopic-Image-Quality-Assessment-Network

# MultiEPL Approach
In this work, instead of using a single row as an epipolar plane or line, we process all rows of the grid. We name this approach MultiEPL. Generally, as shown in Figure (a) below, we fix t=359 and process all SAI rows. This way, we extract EPIs of size 10x960, as illustrated in Figure (b). But using the MultiEPL approach, we obtain one EPI of resolution 100x960 for each LFI.
