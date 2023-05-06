import os
import json
import pandas as pd

# 指定文件夹路径
#folder_path = 'E:\\0330\\json'
folder_path = 'E:\\桌面\\FYP\\logFile\\all\\json'



import os
import csv
import json

# 存储统计结果
count = {}

# 文件夹路径
# folder_path = 'path/to/folder'

# 遍历文件夹中所有的json文件
for filename in os.listdir(folder_path):
    print(filename)
    # if filename.endswith('.json'):
    with open(os.path.join(folder_path, filename), 'r') as f:
        print(os.path.join(folder_path, filename))
        for line in f:
            # 解析json字符串
            try:
                data = json.loads(line)
            except json.decoder.JSONDecodeError:
                continue

            # 查找特定的eventid
            if data.get('eventid') == 'cowrie.session.connect':
                src_ip = data.get('src_ip')
                # 统计src_ip数量
                count[src_ip] = count.get(src_ip, 0) + 1

# 将统计结果保存为CSV文件
with open('0428//output_0428.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['src_ip', 'count'])
    for src_ip, cnt in count.items():
        writer.writerow([src_ip, cnt])


