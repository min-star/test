#! /bin/bash

find $1 -name '*_gt.json*' | wc -l

# 在命令行窗口输入：bash count_file.sh dirname(需要查找的文件夹的名字)
# 若显示权限不够，则先执行chmod a+x count_file.sh