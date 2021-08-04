# python-nlp-toolkit

split_to_kor_and_eng.py => pandas, numpy, hgtk required(pip install pandas, numpy hgtk) , you should give your csv name(not with extension only name) as argument.
And csv file should look like this
some.csv =
content
firstline
secondline
etc
...
So It means, the label of column should be content
After processing, this script gives you kor.csv and eng.csv(which kor.csv contains all entries if contains non-alphabet character, and eng.csv if contains alphabet only)

wordcloud.py => pandas, nltk, wordcloud required, you should give your csv name(not with extension only name) as argument.
And csv file should look same as above.
Then it will generate output.png(wordcloud image)
