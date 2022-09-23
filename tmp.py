import PyPDF2
import os

path = "I:/LARC park/Permits/Spring 2022/Requests/"
fp = os.listdir(path)
reader = PyPDF2.PdfReader(path+fp[0])

file = open(path+fp[0], rb)
