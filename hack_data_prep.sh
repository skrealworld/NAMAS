#/bin/bash`

python dataset/make_dict.py /home/sk1846/namas/working_dir/train.data.filter.txt  /home/sk1846/namas/working_dir/train 5
bash ./prep_torch_data.sh /home/sk1846/namas/working_dir/
