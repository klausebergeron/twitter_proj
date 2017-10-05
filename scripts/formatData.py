import os
import time
import re

trueInfile = open("//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//data//rawData//trueRT.txt", 'r')
falseInfile = open("//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//data//rawData//falseRT.txt", 'r')
tDataPath = "//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//data//tData//"

track_false = open("//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//data//track_false.txt", 'r+')
track_true = open("//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//data//track_true.txt", 'r+')
tsi = int(track_true.readline())
fsi = int(track_false.readline())


def newFileName(classif, ind):
	if classif == 'f':
		return tDataPath+"fLearnWord//no."+str(ind)+".txt"
	elif classif == 't':
		return tDataPath+"tLearnWord//no."+str(ind)+".txt"


for line in trueInfile:
	text = re.sub(r'[^a-zA-Z ,\']+', " ", (re.sub(r'\bhttp\S+', '', (line.split('\t',2)[1]))))
	output_filename = newFileName('t', tsi)
	out = open(output_filename, 'w+')
	out.write(text)
	out.close()
	tsi+=1

track_true.write(str(tsi))
track_true.close()
trueInfile.close()

for line in falseInfile:
	text = re.sub(r'[^a-zA-Z ,\']+', " ", (re.sub(r'\bhttp\S+', '', (line.split('\t',2)[1]))))
	output_filename = newFileName('f', fsi)
	out = open(output_filename, 'w+')
	out.write(text)
	out.close()
	fsi+=1

track_false.write(str(fsi))
track_false.close()
falseInfile.close()