import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
#import stopwords as stopwords

def summerfunc(text):
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    sent_tokens = nltk.sent_tokenize(text)
    word_tokens = nltk.word_tokenize(text)
    word_tokens_lower = [word.lower() for word in word_tokens]
    stopwords = list(set(stopwords.words('english')))
    word_tokens_refined = [word for word in word_tokens_lower if word not in stopwords]

    freqTable = dict()
    for word in word_tokens_refined:
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    sentenceValue = dict()
    for sentence in sent_tokens:
        sentenceValue[sentence] = 0
        for word, freq in freqTable.items():
            if word in sentence.lower():
                sentenceValue[sentence] += freq

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
    average = int(sumValues / len(sentenceValue))
    #print(average)
    # Storing sentences into our summary.
    summary = ''
    for sentence in sent_tokens:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.3 * average)):
            summary += " " + sentence

    return summary



