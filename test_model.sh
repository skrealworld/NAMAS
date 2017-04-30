export LUA_PATH="$LUA_PATH;?.lua"

th summary/run.lua \
 -modelFilename $1 \
 -inputf /home/sk1846/namas/working_dir/test.article.txt \
 -length 30 \
 -blockRepeatWords 

