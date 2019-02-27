#!/usr/bin/env python
# -*- coding: utf-8 -*-


import hdfs
from hdfs.client import Client



client = Client('spark://10.0.120.105:7077')
dir(client)

# 拷贝几个文件到单独一个文件夹进行测试
hadoop fs -cp hdfs://bcg/opt/int_group/tri_element/optimize/month45/part-00674-e28f5a23-1aa8-472f-b1c9-83bb7a9caec1-c000.csv hdfs://bcg/opt/int_group/tri_element/optimize/month45/test/

hdfs_path = 'hdfs://bcg/opt/int_group/tri_element/optimize/month45'

hdfs_path = 'hdfs://bcg/opt/int_group/tri_element/optimize/month45/test/'
file_names = client.list(hdfs_path)
