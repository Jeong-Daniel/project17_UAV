https://github.com/lhiday-purdue/Project17-UAV-Ground-Detection-and-Tracking-Systems

Often a forest of trees has many different kinds of trees. In this project, we want to design a novel way to fly over a tree and determine what kind if tree it is, using a visual or biological sensor. Then, record the GPS point on the tree. At the end of a flight a map will show all of the GPS points for the specific variety of tree.

## Team Members  
Christian Ekeigwe -Purdue University  
Daehyeon Jeong -Pusan National University  
Jaeyoung Shim -Pusan National University  
Jeonghwan Kang -Pusan National University  
Seoungheong Jeong -Pusan National University  
--
## Projet Goal
This project aims to build a environmental operation system that can be to detect trees using machine learning object detection algorithm.
* OpenCV - One of the open source computer vision libraries is cross-platform and real-time image processing.
* Haar Cascade - It is an Object Detection Algorithm used to identify faces in an image or a real time video  

## System overview
![image](https://user-images.githubusercontent.com/85277660/131251447-076249fb-1508-49d7-b9ad-d2c8fb78c464.png)

* Use the Haar Cascades built into OpenCV to detect trees.
* When the object is detected, the raspberry pi stores the number of trees and the latitude and longitude received from the module from the GPS in MariaDB.
* Connect to the DB with another computer connected to the internal network to visualize the data.
