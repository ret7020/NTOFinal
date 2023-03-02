import argostranslate.package
import argostranslate.translate
import pandas as pd
import json
import os
from tqdm import tqdm

#argostranslate.package.install_from_path("/home/stephan/Downloads/ru_en.argosmodel")
#argostranslate.package.install_from_path("~/Downloads/en_ru.argosmodel")

with open("dwnld_2.txt") as fd:
    ready = eval(fd.read())


sets = ["val", "test"]
videos = []

res = []
for subset in sets:
    counter = 0
    # questions
    with open(f"{subset}_q.json") as fd:
        cont = json.load(fd)
    with open(f"{subset}_a.json") as fd:
        answers = json.load(fd)
    #print(answers)

    for q in tqdm(cont):
        #print(f'{q["video_name"]}.mp4')
        if f'{q["video_name"]}.mp4' in ready:
            question_ru = argostranslate.translate.translate(q["question"], "en", "ru").lower()
            res.append({"video_name": q["video_name"], "question": question_ru, "answer": argostranslate.translate.translate(next(item for item in answers if item["question_id"] == q["question_id"])["answer"], "en", "ru").lower()})
            

df = pd.DataFrame(res)
df.to_csv("russian.csv")
