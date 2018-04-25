##youtube-dl --skip-download --write-auto-sub --convert-subs srt https://www.youtube.com/watch?v=V9A4m5isNJI
##youtube-dl --skip-download --sub-lang pt --write-auto-sub --convert-subs srt https://www.youtube.com/watch?v=V9A4m5isNJIwatch?v=V9A4m5isNJI


##youtube-dl --write-auto-sub --convert-subs srt https://www.youtube.com/watch?v=t6rHHnABoT8



import re
from collections import Counter
from moviepy.editor import VideoFileClip, concatenate

def convert_time(timestring):
    """string para segundos"""
    nums = map(float, re.findall(r'\d+', timestring))
    return 3600*nums[0] + 60*nums[1] + nums[2] + nums[3]/1000

with open("video.srt") as f:
    lines = f.readlines()

times_texts = []
current_times , current_text = None, ""
for line in lines:
    times = re.findall("[0-9]*:[0-9]*:[0-9]*,[0-9]*", line)
    if times != []:
        current_times = map(convert_time, times)
    elif line == '\n':
        times_texts.append((current_times, current_text))
        current_times, current_text = None, ""
    elif current_times is not None:
        current_text = current_text + line.replace("\n"," ")

#print (times_texts)

whole_text = " ".join([text for (time, text) in times_texts])
all_words = re.findall("\w+", whole_text)

counter = Counter([w.lower() for w in all_words if len(w)>5])
print (counter.most_common(10))
