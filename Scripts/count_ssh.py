import os
import json
import csv

folder_path = 'E:\\桌面\\FYP\\logFile\\all\\json'

ssh_count = 0
telnet_count = 0

for file_name in os.listdir(folder_path):
    # if file_name.endswith('.json'):
    with open(os.path.join(folder_path, file_name)) as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get('eventid') == 'cowrie.session.connect':
                    protocol = data.get('protocol')
                    if protocol == 'ssh':
                        ssh_count += 1
                    elif protocol == 'telnet':
                        telnet_count += 1
            except json.decoder.JSONDecodeError:
                continue

with open('0428\\output_ssh_telnet_0428.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Protocol', 'Count'])
    writer.writerow(['SSH', ssh_count])
    writer.writerow(['Telnet', telnet_count])
