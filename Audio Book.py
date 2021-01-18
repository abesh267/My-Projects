import  pyttsx3
import PyPDF2
from tkinter.filedialog import *

doc = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(doc)
pages = pdfreader.numPages

for i in range(1,pages+2):
    page = pdfreader.getPage(i)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()

