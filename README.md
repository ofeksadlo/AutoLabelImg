# AutoLabelImg
Automatically annotate images using your own pre-trained yolo models.

![showcase](showcase%20(2).gif)

# Update
Added train.py edit the path to the folder with your images and run the script. It</br>
will loop through all the image and annotate all the images for you.

# What is does?
Open up the tool and go to LabelImg.</br>
When you need to use the auto detection press Q.</br>

# What it's good for?
Well if you ever tried to train a custom yolo model you understand. It takes a lot of time</br>
creating a decent dataset for training. I literally swapped hands from time to time to avoid the pain.</br>
Using this method you can create a really small dataset manually (150-300 images). Train your model</br>
on this small dataset and then use this tool to make annotating faster.</br>
The tool is meant to help you to do the hard work. You still need to supervise it.

# Compatibility
* This tool is designed to work only with yolo models.</br>
* Don't use this tool with tiny yolo. It won't work very well</br>
  train another model in order to use this tool.
* Tested only on windows 10 using python 3.7.7</br>
**<ins>Bonus Tip:<ins>**</br>
Depending on the image you're detecting you should zoom in and out in order to help</br>
your model to detect the desired object more accurately. </br>
A specially when it's trained on a small dataset (150-300).

# Future plans
1) ~~Detecting more than 1 class and more than 1 object.~~ (Added)
2) ~~Detecting click on Next image or 'D' on the keyboard and annotating the objects, without the need to press enter.~~</br>
   ~~Letting you focus entirely on fixing defects in the model detections.~~ (Added keyboard shortcut)

