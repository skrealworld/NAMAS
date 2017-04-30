from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals


from sumy.evaluation import rouge_2, rouge_l_sentence_level, rouge_l_summary_level
from sumy.evaluation.rouge import _get_ngrams, _split_into_words, _get_word_ngrams, _len_lcs, _recon_lcs, _union_lcs
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser


_input_file=open('/home/sk1846/namas/working_dir/test.article.txt').read()
_input_articles=_input_file.split('\n') 

_summ_file=open('/home/sk1846/namas/NAMAS/abs_model_10.txt').read()
_summ_file=_summ_file.split('\n') 

sum_rouge_2=0
count=0
for x in range(0,len(_input_articles)-1):
	count+=1
#	if(count==480):
#		break
	_input_text=_input_articles[x]
	_input_text=PlaintextParser(_input_text,Tokenizer("english")).document.sentences
	
	_output_story=_summ_file[x] 
	_output_story=PlaintextParser(_output_story,Tokenizer("english")).document.sentences
	sum_rouge_2=sum_rouge_2+rouge_2(_input_text,_output_story)

print('Final Rouge-2 : ',sum_rouge_2/count)
