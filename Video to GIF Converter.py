from moviepy.editor import VideoFileClip
from tkinter.filedialog import *

video = askopenfilename()
clip = VideoFileClip(video)
clip.write_gif("Converted GIF.gif",fps = 12)
print("Conversion Complete!!!")