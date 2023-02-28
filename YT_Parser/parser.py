from pytube import YouTube
import json
import pandas as pd
import pytube

#already_downloaded = list()
df = pd.read_csv("ods.csv")
alr_down = list(df["video_name"].unique())
#print(alr_down)

with open("train_q.json") as fd:
    dataset = json.load(fd)

counter = 0
#print(dataset)
res = []
for q in dataset:
    res.append(q["video_name"])
task = list(set(res) - set(alr_down)))

for q in task:
        try:
            yt = YouTube(f"https://youtube.com/watch?v={task}")
            yt.streams.filter(file_extension='mp4').order_by('resolution').first()#.download(output_path="./videos", filename=f"{q['video_name']}.mp4")
            counter += 1
        except:
            pass
            
print(counter)
