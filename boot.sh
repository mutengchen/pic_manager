#!/bin/bash
cd $(dirname $0)
for id in `ps -ef|grep "pedstron_main" | grep -v "grep" |awk '{print $2}'`
do
kill -9 $id
echo "kill $id"
done
source ~/anaconda3/etc/profile.d/conda.sh
conda activate cuda10
echo "save log to ~/pedestron/recogizeLog.out"
nohup python pedstron_main.py $1 > recogizeLog.out 2>&1 &
nohup python test_html.py >/dev/null 2>&1 &
