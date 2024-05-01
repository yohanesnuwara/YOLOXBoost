# YOLOXBoost
POC improvement of YOLO model with histogram equalization and model post processing stacking

## The problem
We use a use case in oil palm industry where photos are collected onsite and computer vision model is required to detect oil palm fresh fruit bunches (FFB) on the ground and classify the fruit based on its ripeness. The problem is the photos can have abnormalities such as over-exposure (photo taken during broad day light), yellowish, and bright flash. 

## YOLOXBoost

|Model|Description|Average F1|
|:--:|:--:|:--:|
|Model 1|Colour augmentation + CutMix + Ray Tuned|0.799|
|Model 2|Histogram equalization matched to test data|0.729|
|Model 3|Stacking of Model 1 and 2 + NMS|0.844|

In Figure 1, Model 1 gives a correct detection of Abnormal class while cannot detect 

![image](https://github.com/yohanesnuwara/YOLOXBoost/assets/51282928/fc7d3788-b3c1-4ca7-8085-22e037e8364d)

Figure 1. Detection result of (a) Model 1, (b) Model 2, and (c) Stack of Model 1 and 2

![image](https://github.com/yohanesnuwara/YOLOXBoost/assets/51282928/1e08f30f-fc5c-4ca2-b242-258442ed83d7)

Figure 2. Detection result of (a) Model 1, (b) Model 2, and (c) Stack of Model 1 and 2
