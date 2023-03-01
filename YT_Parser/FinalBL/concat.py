import json
import pandas as pd
from translate import Translator

translator = Translator(to_lang="ru", from_lang="en")
res = []
#paths = [("train_q.json", "train_a.json"), ("test_q.json", "test_a.json"), ("val_q.json", "val_a.json")]

paths = [("test_q.json", "test_a.json")]
for pl in paths:
    questions = pl[0]
    answers = pl[1]

    with open(questions) as fd:
        train = json.load(fd)

    with open(answers) as fd:
        answ = json.load(fd)

    ans = {}
    print(len(answ))
    for i in answ:
        ans[i["question_id"]] = i["answer"]
    counter = 0
    for q in train:
        try: # translate to russian
            question_trans = translator.translate(q["question"])
            answ_trans = translator.translate(ans[q['question_id']])
            res.append({"video_name": q["video_name"], "question": question_trans, "answer": answ_trans})
        except: # fallback to english
            res.append({"video_name": q["video_name"], "question": q["question"], "answer": ans[q["question_id"]]})
        counter += 1
        print(counter)
    print("Counted:", counter)
    
    # Check point
    q = pd.DataFrame.from_dict(res)
    q.to_csv("translated.csv")

q = pd.DataFrame.from_dict(res)
q.to_csv("translated.csv")
