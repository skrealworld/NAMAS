#Script to formant DUC dataset according to the NAMAS requirement. 

import sys
import glob
import nltk 
import re
import fnmatch 
#from bs4 import BeautifulSoup 
#import html2text
import pickle as pk
import numpy as np 
working_dir="/home/sk1846/namas/working_dir/"

"""
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

train_file=open('article.txt','a')
for topic in topics_dirs:
	documents_in_topic=glob.glob(topic+'/*')
	for x in range(0,4):
		for document in documents_in_topic:
			_file=open(document)
			text_data=_file.read()
			text_data=html2text.html2text(text_data)
			text_data = re.sub(r"&nbsp;", " ", text_data)
			soup = BeautifulSoup(text_data)
			text_data=soup.get_text()
			text_data=text_data[30:]
			text_data=removeLines(text_data)
			train_file.write(text_data+'\n')

train_file.close()


title_file=open('title.txt','a') 
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
		for x in range(0,25):
			title_file.write(text_in_line+'\n')

title_file.close()

train_articles=open('article.txt','r')
train_articles=train_articles.read()
train_articles=train_articles.split('\n')

train_titles=open('title.txt','r')
train_titles=train_titles.read()
train_titles=train_titles.split('\n')

random_idx=np.random.permutation(5000)
train_articles=np.take(train_articles,random_idx,axis=0)
train_titles=np.take(train_titles,random_idx,axis=0)

split_idx=int(5000*.75)

train_article_txt=train_articles[:split_idx]
valid_article_txt=train_articles[split_idx+1:]
train_title_txt=train_titles[:split_idx]
valid_title_txt=train_titles[split_idx+1:]


_train_article_txt=open('train.article.txt','a')
for _train_article in train_article_txt:
        _train_article_txt.write(_train_article+'\n')
_train_article_txt.close()


_valid_article_txt=open('valid.article.txt','a')
for _valid_article in valid_article_txt:
        _valid_article_txt.write(_valid_article+'\n')
_valid_article_txt.close()


_train_title_txt=open('train.title.txt','a')
for _train_title in train_title_txt:
        _train_title_txt.write(_train_title+'\n')
_train_title_txt.close()


_valid_title_txt=open('valid.title.txt','a')
for _valid_title in valid_title_txt:
        _valid_title_txt.write(_valid_title+'\n')
_valid_title_txt.close()
_train_file.close()
"""
train_articles=open(working_dir+'train.article_old.txt','r')
train_articles=train_articles.read() 
train_articles=train_articles.split('\n')
train_titles=open(working_dir+'train.title_old.txt','r') 
train_titles=train_titles.read()
train_titles=train_titles.split('\n') 

random_idx=np.random.permutation(200)
train_articles=np.take(train_articles,random_idx,axis=0)  
train_titles=np.take(train_titles,random_idx,axis=0)

split_idx=int(200*.75)

train_article_txt=train_articles[:split_idx]
valid_article_txt=train_articles[split_idx+1:]
train_title_txt=train_titles[:split_idx]
valid_title_txt=train_titles[split_idx+1:]


_train_article_txt=open(working_dir+'train.article.txt','a')
for _train_article in train_article_txt:
	_train_article_txt.write(_train_article+'\n')	
_train_article_txt.close()


_valid_article_txt=open(working_dir+'valid.article.txt','a')
for _valid_article in valid_article_txt:
        _valid_article_txt.write(_valid_article+'\n')   
_valid_article_txt.close()


_train_title_txt=open(working_dir+'train.title.txt','a')
for _train_title in train_title_txt:
        _train_title_txt.write(_train_title+'\n')   
_train_title_txt.close()


_valid_title_txt=open(working_dir+'valid.title.txt','a')
for _valid_title in valid_title_txt:
        _valid_title_txt.write(_valid_title+'\n')
_valid_title_txt.close()



