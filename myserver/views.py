from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Question
# from .models import ExampleModel
import cv2
import numpy as np
import urllib
import png
import subprocess
import time




def sathar(request):
	

	aa=urllib.urlretrieve("http://192.168.43.156:81/uploads/yup.png")


	img = cv2.imread(aa[0])
	                

	                
	                

	retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

	grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	retval2, threshold2 = cv2.threshold(grayscaled,12, 255, cv2.THRESH_BINARY)
	#gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
	retval,otsu = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	png.from_array(otsu, 'L').save("myserver/templates/aar.png")

	#cv2.imshow('original',img)
	#cv2.imshow('threshold',threshold)
	#cv2.imshow('threshold2',threshold2)
	#cv2.imshow('gaus',gaus)
	
	return HttpResponse("success")
	

def call(request):
	subprocess.call(['C:\\Users\\SATHU\\Desktop\\coderunnercs8a2\\Tesseract-OCR\\tesseract.exe','C:\\Users\\SATHU\\Desktop\\coderunnercs8a2\\myserver\\templates\\aar.png','C:\\Users\\SATHU\\Desktop\\coderunnercs8a2\\myserver\\templates\\sathu'])
	content="C:\\Users\\SATHU\\Desktop\\coderunnercs8a2\\myserver\\templates\\sathu.txt"

	fsock=open(content,"r")
	return HttpResponse(fsock,".txt")



def compile(request):
	p = subprocess.Popen(['C:\\Users\\SATHU\\Downloads\\MinGW\\bin\\g++.exe','C:\\xampp\\htdocs\\sathar\\uploads\\ztr.cpp','-o','C:\\Users\\SATHU\\Downloads\\MinGW\\bin\\program'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	if p[1]=='':
		p = subprocess.Popen(['C:\\Users\\SATHU\\Downloads\\MinGW\\bin\\program.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
		if p[1]=='':
			print p[0]
			return HttpResponse(p[0])
		return HttpResponse(p[1])
	return HttpResponse(p[1])

def recall(request):
	content="C:\\Users\\SATHU\\Desktop\\coderunnercs8a2\\myserver\\templates\\sathu.txt"

	fsock=open(content,"r")
	return HttpResponse(fsock,".txt")


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('myserver/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))





    #TESSDATA_PREFIX
    #C:\Users\SATHU\Desktop\Tesseract-OCR\tessdata