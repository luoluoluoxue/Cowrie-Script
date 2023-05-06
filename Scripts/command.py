import os
import json
import csv

import operator
# folder_path = 'E:\\0330\\json'
folder_path = 'E:\\桌面\\FYP\\logFile\\all\\json'
count = {}
count_busybox={};
count_src_ip= {}

total=0;
total_busy=0;

for file_name in os.listdir(folder_path):
    # if file_name.endswith('.json'):
    with open(os.path.join(folder_path, file_name)) as f:
        for line in f:
            try:
                data = json.loads(line)

            except json.decoder.JSONDecodeError:
                continue


            if data.get('eventid') == 'cowrie.command.input':
                inputs = data.get('input')



                for input1 in inputs.split(';'):
                    for input in input1.split('&&'):
                        input = input.strip()
                        if input:
                            count[input] = count.get(input, 0) + 1
                            if operator.contains(input,'busybox'):
                                total+=1;

                            if operator.contains(input, '/bin/busybox'):
                                total_busy += 1;


                count[inputs] = count.get(inputs, 0) + 1
                # count_src_ip[ip]=count.get(ip, 0) + 1




with open('0428//output_input_ip_nosplit_0428.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['input', 'count'])
    for input, cnt in count.items():
        writer.writerow([input, cnt])
    # for src_ip, cnt in count_src_ip.items():
    #     writer.writerow([src_ip, cnt])

print(total)
print(total_busy)