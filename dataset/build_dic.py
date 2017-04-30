
import re 
from collections import Counter
article_file=open('/home/sk1846/namas/NAMAS_OLD/working_dir/train.article.txt')
article_text=article_file.read()
word_counter=Counter()
word_counter.update(article_text.lower().split())
print(len(word_counter))
