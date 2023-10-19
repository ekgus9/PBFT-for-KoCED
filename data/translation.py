# pip install googletrans==3.1.0a0 

from googletrans import Translator

import jsonlines
import csv
import random

translator = Translator()

print('**train**')

with open('../train.tsv', 'a', encoding='utf-8', newline='') as f:
    tw = csv.writer(f, delimiter='\t')
    tw.writerow(['s1','s2', 'label'])

num = 1

with open('train.tsv', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if 's1\t' in line: continue
        line = line.split('\t')
        result = translator.translate(line[0], src="en", dest="ko")
        t = {'s1':line[0],'s2':result.text,'label':line[2]}
        
        with open('../train.tsv', 'a', encoding='utf-8', newline='') as f:
            tw = csv.writer(f, delimiter='\t')
            tw.writerow([t['s1'], t['s2'], int(t['label'])])
            
        if num % 100 == 0 : print(num)
        num += 1

print('**dev**')

with open('../dev.tsv', 'a', encoding='utf-8', newline='') as f:
    tw = csv.writer(f, delimiter='\t')
    tw.writerow(['s1','s2', 'label'])

num = 1

with open('dev.tsv', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if 's1\t' in line: continue
        line = line.split('\t')
        result = translator.translate(line[0], dest="ko")
        t = {'s1':line[0],'s2':result.text,'label':line[2]}
        
        with open('../dev.tsv', 'a', encoding='utf-8', newline='') as f:
            tw = csv.writer(f, delimiter='\t')
            tw.writerow([t['s1'], t['s2'], int(t['label'])])
            
        if num % 100 == 0 : print(num)
        num += 1
        
print('**test**')

with open('../test.tsv', 'a', encoding='utf-8', newline='') as f:
    tw = csv.writer(f, delimiter='\t')
    tw.writerow(['s1','s2','google', 'label'])

num = 1

with open('test.tsv', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if 's1\t' in line: continue
        line = line.split('\t')
        result = translator.translate(line[0], dest="ko")
        t = {'s1':line[0],'s2':line[1], 'google':result.text,'label':line[2]}
        
        with open('../test.tsv', 'a', encoding='utf-8', newline='') as f:
            tw = csv.writer(f, delimiter='\t')
            tw.writerow([t['s1'], t['s2'],t['google'], int(t['label'])])
            
        if num % 100 == 0 : print(num)
        num += 1
        
print('**end**')

