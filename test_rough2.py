
import sys 
import os

test_file=open('/home/sk1846/namas/working_dir/_test_stories_Enc.txt').read()

test_lines=test_file.split('\n')
count=1
for x in range(0,len(test_lines)):
  if(count==10):
    break
  count+=1
  os.system('./test_model.sh '+ x + ' /home/sk1846/namas/trained_mode/model.th 50')
