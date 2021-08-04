import pandas as pd
import nltk
from nltk.corpus import stopwords
import sys
from wordcloud import WordCloud

try:
  file_name = sys.argv[1]
except IndexError:
  print("Please give your csv file name as argument(except extension[.csv]")
  exit()
if(type(file_name) != str):
  file_name = str(file_name)

data = pd.read_csv(file_name)
content_text = ""

for line in data.content.items():
  if(type(line[1])==float):
      continue
  content_text += line[1] + "\n"

tokens = nltk.word_tokenize(content_text)
stop_words = set(stopwords.words('english'))

tokens = [word for word in tokens if word not in stop_words]
en = nltk.Text(tokens)

wordcloud = WordCloud(relative_scaling=0.2,background_color='white').generate_from_frequencies(en.vocab())
wordcloud.to_file('output.png')
