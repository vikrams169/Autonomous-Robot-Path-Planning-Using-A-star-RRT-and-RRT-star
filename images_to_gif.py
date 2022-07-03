# Code to convert the series of saved frames into a video for animation purposes

# Importing the Required Libraries
import imageio
import os

# Naming the image directory we wish to make an animation from 
'''image_directory = "a_star_frames"
image_directory = "rrt_frames"'''
image_directory = "rrt_star_frames"

# Extracting the frames into a video
num_frames = len(os.listdir(image_directory))
with imageio.get_writer('animations/rrt_star.mp4',mode='I',fps=100) as writer:   # Otherwise "animations/a_star.mp4" or "animations/rrt.mp4"
    for i in range(num_frames):
        image = imageio.imread(image_directory+"/frame"+str(i)+".jpg")
        writer.append_data(image)