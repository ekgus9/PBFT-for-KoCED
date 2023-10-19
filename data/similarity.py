from pororo import Pororo
from sentence_transformers import SentenceTransformer, util
from setproctitle import *
from tqdm import tqdm
import csv

gec = Pororo(task="gec", lang="en")
gec_ko = Pororo(task="gec", lang="ko")

model = SentenceTransformer('distiluse-base-multilingual-cased-v1')

data_list = ['dev','test'] # ['train','dev','test']
n = 0 #
for data_name in data_list:
    with open('./data/koced_gec/'+data_name+'.tsv', 'a', encoding='utf-8', newline='') as f:
        tw = csv.writer(f, delimiter='\t')
        tw.writerow(['s1','s2','gec_en','gec_ko','similarity','label'])
    
    with open('./data/koced/'+data_name+'.tsv', 'r', encoding='utf-8') as f:
        for line in tqdm(f.readlines()):
            n += 1
            if 's1\t' in line: continue
            line = line.split('\t')
            line[2] = int(line[2])
            
            sentences1 = [line[0]]

            sentences2 = [line[1]]

            # Compute embedding for both lists
            embeddings1 = model.encode(sentences1, convert_to_tensor=True)
            embeddings2 = model.encode(sentences2, convert_to_tensor=True)

            # Compute cosine-similarities
            cosine_scores = util.cos_sim(embeddings1, embeddings2)

            similarity = round(float(cosine_scores[0]),4)

            # result = {'s1':line[0],'s2':line[1],'gec_en':gec(line[0],correct_spell=True),'gec_ko':gec_ko(line[1],correct_spell=True),'similarity':similarity,'label':line[2]}

            with open('./data/koced_gec/'+data_name+'.tsv', 'a', encoding='utf-8', newline='') as f:
                tw = csv.writer(f, delimiter='\t')
                try:
                    tw.writerow([line[0],line[1],gec(line[0],correct_spell=True),gec_ko(line[1],correct_spell=True),similarity,line[2]])
                except:
                    # print('**error**')
                    tw.writerow([line[0],line[1],gec(line[0],correct_spell=True),gec_ko(line[1]),similarity,line[2]])
