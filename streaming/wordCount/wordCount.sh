#!/bin/bash

# 指定hadoop-stream的jar包位置
# input hdfs的输入位置
# output 结果写入hdfs的位置
# file 加载辞典，其实就是在运行的时候会将这些file拷贝到每个tasktracker的机器上
# mapper map的代码
# reducer reduce的代码
# jobconf mapred.reduce.tasks 设置reduce的个数
# jobconf mapred.job.name 设置job的名字

# /opt/hadoop-2.2.0/share/hadoop/tools/lib/hadoop-streaming-2.2.0.jar
hadoop jar /opt/hadoop-2.5.2/share/hadoop/tools/lib/hadoop-streaming-2.5.2.jar \
        -input //m20p13/user/playground/whm/streaming/test.txt \
        -output //m20p13/user/playground/whm/streaming/ \
        -file mapper1.py \
        -file reducer1.py \
        -mapper "python mapper1.py" \
        -reducer "python reducer1.py" \
        -jobconf mapred.reduce.tasks=1 \
        -jobconf mapred.job.name="whm_wordCount_streaming_test"
