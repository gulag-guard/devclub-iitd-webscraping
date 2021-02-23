from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image 
from io import BytesIO
import os
PATH1 = "C:\Program Files (x86)\chromedriver.exe"
driver  = webdriver.Chrome(PATH1)
base = "https://codeforces.com/contest/"
parent_dir = "./"
n = input()
path = os.path.join(parent_dir, n)
os.mkdir(path)
base = base +n+"/problems"
driver.get(base)
s1 = driver.find_elements_by_class_name("problem-statement")
parent_dir  = parent_dir+n+'/'
base = "https://codeforces.com/contest/problem/"
arr = [0]*len(s1)
for i in range(len(s1)):
	w = s1[i].text
	x = w.split('.')
	pid = x[0]
	arr[i] = x[0]
	path = os.path.join(parent_dir, pid)
	os.mkdir(path)
	tmp = parent_dir + pid+'/problem.png'
	img = s1[i].screenshot(tmp)
base = "https://codeforces.com/contest/"+n+'/problem/'
for i in range(len(arr)):
	driver.get(base+arr[i])
	s1 = driver.find_elements_by_class_name("input")
	s2 = driver.find_elements_by_class_name("output")
	for j in range(len(s1)):
		w1 = s1[j].text
		w1= w1[11:]
		w2 = s2[j].text
		w2 = w2[12:]
		if (len(s1)!=1):
			tmp1 = parent_dir + arr[i] + '/input' + str(j+1) +'.txt'
			tmp2 = parent_dir + arr[i] + '/output' + str(j+1) +'.txt'
		else:
			tmp1 = parent_dir + arr[i] + '/input.txt'
			tmp2 = parent_dir + arr[i] + '/output.txt'
		file1 = open(tmp1, "w")
		file2 = open(tmp2, "w")
		file1.write(w1)
		file2.write(w2)
		file1.close()
		file2.close()

		
	
	








 



