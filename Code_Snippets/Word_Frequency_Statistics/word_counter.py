import os
from collections import Counter
import nltk
from nltk.corpus import stopwords
import string

# 下载必要的 NLTK 数据
nltk.download('punkt')
nltk.download('stopwords')

def count_words_in_files(directory):
    word_counts = Counter()
    stop_words = set(stopwords.words('english'))
    punctuation = set(string.punctuation)

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                text = file.read()
                words = nltk.word_tokenize(text)
                filtered_words = [word for word in words if word.lower() not in stop_words and word not in punctuation]
                word_counts.update(filtered_words)

    return word_counts
