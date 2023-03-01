import pandas as pd
import nltk
import numpy as np

path_gt = 'private_test_gt.csv'
path_pred = 'answer.csv'
df_eval = pd.read_csv(path_gt)
df_pred = pd.read_csv(path_pred)
scores = []
for pred, gt in zip(df_eval.answer, df_pred.answer):
    if type(pred)==str and type(gt)==str:
        score = nltk.translate.bleu_score.sentence_bleu([gt.lower().split()], pred.lower().replace('<|endoftext|>','').split(), weights = (0.5, 0.5))
    scores+=[score]
ans = np.array(scores).mean()*100
df = pd.DataFrame({'ans':[ans]})
df.to_csv('score.csv')
print(round(ans, 5))
