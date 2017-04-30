# -*- coding: utf-8 -*-
#run this python summy_test.py |grep Rouge-2 >vist_<method_name>_scores.txt 
import sys
import os
from itertools import izip

_input_file=open('/home/sk1846/namas/NAMAS_OLD/working_dir/test.article.txt')
_input_text=_input_file.read()
_input_articles=_input_text.split('\n') 

_ref_file=open('/home/sk1846/namas/NAMAS_OLD/working_dir/test.title.txt')
_ref_text=_ref_file.read()
_ref_stories=_ref_text.split('\n')

count=0
for _input,_ref in izip(_input_articles,_ref_stories):
	count+=1
	#if(count<2000):
	#	continue
	if(count==10):
		break
	with open("input_summary.txt",'w') as _file:
		_file.write(_input) 
		_file.close()
	with open("ref_summary.txt",'w') as _summ_file:
		_summ_file.write(_ref)
		_summ_file.close()
	os.system('./makeSummaries.sh input_summary.txt 5 ref_summary.txt')
