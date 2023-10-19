import jsonlines
import csv
import random

koced_train = []
koced_dev = []
koced_test = []

with open('train.tsv', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if 's1\t' in line: continue
        line = line.split('\t')
        line[2] = int(line[2])
        if line[2] == 1:
            koced_train.append({'s1':line[0],'s2':line[1],'label':line[2]})
        elif line[2] == 0:
            num = random.random()
            if num > 0.3:
                koced_train.append({'s1':line[0],'s2':line[1],'label':line[2]})

with open('dev.tsv', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if 's1\t' in line: continue
        line = line.split('\t')
        line[2] = int(line[2])
        if line[2] == 1:
            koced_dev.append({'s1':line[0],'s2':line[1],'label':line[2]})
        elif line[2] == 0:
            num = random.random()
            if num > 0.3:
                koced_dev.append({'s1':line[0],'s2':line[1],'label':line[2]})

with open('test.tsv', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if 's1\t' in line: continue
        line = line.split('\t')
        line[2] = int(line[2])
        koced_test.append({'s1':line[0],'s2':line[1],'label':line[2]})


with open('../train.tsv', 'w', encoding='utf-8', newline='') as f:
    tw = csv.writer(f, delimiter='\t')
    tw.writerow(['s1','s2', 'label'])
    for t in koced_train:
        tw.writerow([t['s1'],t['s2'], t['label']])

with open('../dev.tsv', 'w', encoding='utf-8', newline='') as f:
    tw = csv.writer(f, delimiter='\t')
    tw.writerow(['s1','s2', 'label'])
    for t in koced_dev:
        tw.writerow([t['s1'],t['s2'], t['label']])

with open('../test.tsv', 'w', encoding='utf-8', newline='') as f:
    tw = csv.writer(f, delimiter='\t')
    tw.writerow(['s1','s2', 'label'])
    for t in koced_test:
        tw.writerow([t['s1'],t['s2'], t['label']])
