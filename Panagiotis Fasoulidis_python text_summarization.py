Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Your text
text = """[Your text here]"""

# Tokenize text into sentences
sentences = sent_tokenize(text)

# Tokenize words and remove stopwords
words = word_tokenize(text)
stopwords = set(stopwords.words("english"))
filtered_words = [word for word in words if word not in stopwords and word.isalpha()]

# Frequency distribution of words
freq = FreqDist(filtered_words)

# Scoring sentences based on frequency of words
sentence_scores = {}
for sentence in sentences:
    word_count_in_sentence = (word for word in word_tokenize(sentence) if word in freq)
    for word in word_count_in_sentence:
        if sentence not in sentence_scores:
            sentence_scores[sentence] = freq[word]
        else:
            sentence_scores[sentence] += freq[word]

# Get the summary (top N sentences)
summary_length = int(len(sentences) * 0.3)  # Summarize to 30% of the original text
summary = nlargest(summary_length, sentence_scores, key=sentence_scores.get)

print(' '.join(summary))
