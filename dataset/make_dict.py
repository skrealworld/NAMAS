#
#  Copyright (c) 2015, Facebook, Inc.
#  All rights reserved.
#
#  This source code is licensed under the BSD-style license found in the
#  LICENSE file in the root directory of this source tree. An additional grant
#  of patent rights can be found in the PATENTS file in the same directory.
#
#  Author: Alexander M Rush <srush@seas.harvard.edu>
#          Sumit Chopra <spchopra@fb.com>
#          Jason Weston <jase@fb.com>

import sys
from collections import Counter
from itertools import izip
import ipdb
#@lint-avoid-python-3-compatibility-imports

title_words = Counter()
article_words = Counter()
limit = 3


_article_file=open('/home/sk1846/namas/working_dir/train.article.txt') 
_title_file=open('/home/sk1846/namas/working_dir/train.title.txt')


for _article,_title in izip(_article_file,_title_file):
	#article_words=_article.split()
	article_words.update(_article.lower().split())
	article_words.update(_title.lower().split())
	#title_words.update(_title.lower().split())
#ipdb.set_trace()
#for l in open(sys.argv[1]):
#    splits = l.strip().split("\t")
#    if len(splits) != 4:
#        continue
#    title_parse, article_parse, title, article = l.strip().split("\t")
#    title_words.update(title.lower().split())
#    article_words.update(article.lower().split())

with open("/home/sk1846/namas/working_dir/train.article.dict", "w") as f:
    print >>f, "<unk>", 1e5
    print >>f, "<s>", 1e5
    print >>f, "</s>", 1e5
    for word, count in article_words.most_common():
        if count < limit:
            break
        print >>f, word, count

with open("/home/sk1846/namas/working_dir/train.title.dict", "w") as f:
    print >>f, "<unk>", 1e5
    print >>f, "<s>", 1e5
    print >>f, "</s>", 1e5
    #for word, count in title_words.most_common():
    for word,count in article_words.most_common():
        if count < limit:
            break
        print >>f, word, count
