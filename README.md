# AutoLabelImg
Automatically annotate images using your own pre-trained yolo models.

# What is does?
The tool will wait for you to click on enter.</br>
Then it will give you a delay of 1 second (You can increase in code). And then it will</br>
detect using your model the object. And using pyautogui draw a rectangle and save it.</br>
If it did right you can just go to the next image. If not fix it and move on to the next image.

# What it good for?
Well if you ever tried to train a custom yolo model you understand. It takes a lot of time</br>
creating a decent dataset for training. I literally swapped hands from time to time to avoid the pain.</br>
Using this method you can create a really small dataset manually (150-300 images). Train your model</br>
on this small dataset and then use this tool to make annotating faster.</br>
The tool is meant to help you to do the hard work. You still need to supervise it.

# Compatibility
This tool is designed to work only with yolo models. And won't work with another type of a model.
Tested only on windows.
