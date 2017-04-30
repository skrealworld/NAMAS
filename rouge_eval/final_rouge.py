
op_file=open('vist_abs_scores.txt').read()
op_lines=op_file.split('\n') 

count=0
rouge_sum=0

no_lines=len(op_lines)

for x in range(0,no_lines-1):
  rouge_sum=rouge_sum+float(op_lines[x].split()[1])
  count+=1

print('Final Rouge : ',rouge_sum/count)


