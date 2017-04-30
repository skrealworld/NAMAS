
import sumy.summarizers.lsa as lsa_module
from sumy.summarizers.lsa import LsaSummarizer

from sumy.models.dom import ObjectDocumentModel

_input_file=open('/home/sk1846/namas/working_dir/test.article.txt').read()
_input_articles=_input_file.split('\n')

_summ_file=open('/home/sk1846/EMNLP/Summarize/ABS/abs_model_6.txt').read()
_summ_file=_summ_file.split('\n')

summarizer = LsaSummarizer()
_summ_doc=ObjectDocumentModel(_summ_file)
print(summarizer(_summ_doc,30))


