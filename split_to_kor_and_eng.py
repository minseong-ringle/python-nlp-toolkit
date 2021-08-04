import sys
import pandas as pd
import numpy as np
import hgtk

try:
  file_name = sys.argv[1]
except IndexError:
  print("Please give your csv file name as argument")
  exit()
if(type(file_name) == str):
  file_name = str(file_name)

eng = []
kor = []
data = pd.read_csv(file_name+".csv")
for line in data.content.items():
  if(type(line[1]) == float):
    continue
  sentence = line[1]
  if(hgtk.checker.is_latin1(sentence)):
    eng.append(sentence)
  else:
    kor.append(sentence)

eng_np = np.array(eng,dtype=str)
kor_np = np.array(kor,dtype=str)

eng_df = pd.DataFrame(eng)
kor_df = pd.DataFrame(kor)

eng_df.to_csv("eng.csv",index=False)
kor_df.to_csv("kor.csv",index=False)
