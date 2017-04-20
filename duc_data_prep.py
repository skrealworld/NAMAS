#Script to formant DUC dataset according to the NAMAS requirement. 

import sys
import glob
import nltk 
import re
import fnmatch 
from bs4 import BeautifulSoup 
import html2text
import pickle as pk

DUC_DIR=sys.argv[1] 
SUM_DIR=sys.argv[2]

def removeLines(_text):
	all_text=''
	lines=_text.splitlines() 
	for _line in lines:
		all_text=all_text+_line 
	return all_text

topics_dirs=glob.glob(DUC_DIR+'topics/*/')
pk.dump(topics_dirs,open('topics_list.pk','wb'))

train_file=open('train.data.txt','a')
for topic in topics_dirs:
	documents_in_topic=glob.glob(topic+'/*')
	all_doc_in_topic=''
	for document in documents_in_topic:
		_file=open(document)
		text_data=_file.read()
		text_data=html2text.html2text(text_data)
		text_data = re.sub(r"&nbsp;", " ", text_data)
		soup = BeautifulSoup(text_data)
		text_data=soup.get_text()
		text_data=text_data[30:]
		text_data=removeLines(text_data)
		all_doc_in_topic=all_doc_in_topic+text_data
	train_file.write(all_doc_in_topic+'\n')
train_file.close()
title_file=open('train.title.txt','a') 
summaries_files=glob.glob(SUM_DIR+"*")
for topic in topics_dirs: 
	doc_regex=topic.split('/')[-2][:-1] #for example 'D0634' 
	_summaries_by_doc=fnmatch.filter(summaries_files,'*'+doc_regex+'*')
	for _summary in _summaries_by_doc:
		_file=open(_summary,encoding="ISO-8859-1")
		text_data=_file.read()
		text_data=html2text.html2text(text_data)
		text_data = re.sub(r"&nbsp;", " ", text_data)
		soup = BeautifulSoup(text_data)
		text_data=soup.get_text()
		text_in_line=''
		text_data=text_data.split('\n')
		for _line in text_data:
			text_in_line=text_in_line+_line
		title_file.write(text_in_line+'\n')

title_file.close()

train_data=open('train.data.txt','r') 
train_data=train_data.read() 
train_data=train_data.split('\n') 

_train_file=open('train.article.txt','a') 
for article in train_data:
	if(len(article)!=0):
		_train_file.write(article+'\n')
		_train_file.write(article+'\n')
		_train_file.write(article+'\n')
		_train_file.write(article+'\n')

_train_file.close()
