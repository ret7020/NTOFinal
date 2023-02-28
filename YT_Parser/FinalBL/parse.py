#from pytube import YouTube
import os
import json
import time

with open("train_q.json") as fd:
    dataset = json.load(fd)

counter = 0
res = []
for q in dataset:
    res.append(q["video_name"])

with open("test_q.json") as fd:
    dataset = json.load(fd)
for q in dataset:
    res.append(q["video_name"])

with open("val_q.json") as fd:
    dataset = json.load(fd)
for q in dataset:
    res.append(q["video_name"])
import pandas as pd

df = pd.read_csv("updatedtrain.csv")
alr_down = list(df["video_name"].unique())

task = list(set(res) - set(alr_down))


counter = 0

for q in task:
  os.system(f'yt-dlp https://youtube.com/watch?v={q} -o "./parsed/%(id)s.%(ext)s" -f "mp4"')
  os.system(f'ffmpeg -y -i ./parsed/{q}.mp4 -vf "scale=trunc(iw/6)*2:trunc(ih/6)*2" -c:v libx265 -crf 20 -t 00:01:00.0 ./final/{q}.mp4')
  os.system(f"rm ./parsed/{q}.mp4")
  print("OK")
  #time.sleep(5)

