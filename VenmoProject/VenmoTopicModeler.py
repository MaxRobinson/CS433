import csv

import praw
import json
import gensim

# setup for tokenization and stopwords
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
from gensim import corpora, models, similarities

def get_message(filename:str) -> list:
    values = {}
    with open(filename, 'r') as f:
        values = json.load(f)

    messages = []
    for key, value in values.items():
        for transaction in value:
            messages.append(transaction.get('message'))

    return messages


def write_results(outputFile:str, data) -> None:
    f = open(outputFile, 'w')
    writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    # write information into CSVs
    header = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10']
    writer.writerow(header)

    for datum in data:
        writer.writerow(datum)

    return


def model_topics(filename:str, outputFile:str):
    #from collections import defaultdict
    stop_words = set(stopwords.words('english'))
    stop_words.update(['.',  ',', '"', "'", '’', '&', '/', '\\', '-', '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']) # remove it if you need punctuation

    messages = get_message(filename)

    all_tokens = ''
    all_words = []

    for message in messages:

        words = [i.lower() for i in wordpunct_tokenize(message) if i.lower() not in stop_words]
        all_words += words
        all_tokens = ' '.join(words)


    # Remove words that appear only once
    texts = all_words
    # remove words that appear only once
    tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)

    texts = [[words for words in texts if words not in tokens_once] for words in all_tokens]


    # Setup for Document Matrix

    #Setup gensim dictionary
    dictionary = corpora.Dictionary(texts)

    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('reddit.mm', corpus)
    #print(corpus)

    print("Start Topics")

    lda = gensim.models.LdaModel(corpus, id2word=dictionary, alpha='auto', num_topics=5)
    words_in_all_topics = []
    for topic in lda.show_topics():
        words_in_topic = topic[1]
        words_in_topic = words_in_topic.replace('"', "")
        words_in_topic = words_in_topic.replace('+', "")
        words_in_topic = words_in_topic.replace('.', "")
        words_in_topic = words_in_topic.replace('*', "")
        words_in_topic = ''.join([i for i in words_in_topic if not i.isdigit()])
        words_in_topic = words_in_topic.split("  ")
        print(words_in_topic)

        words_in_all_topics.append(words_in_topic)

    write_results(outputFile, words_in_all_topics)



    #convert to BOW vectors

    # import pyLDAvis.gensim
    #
    # topic_vis = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
    # pyLDAvis.display(topic_vis)


if __name__ == '__main__':
    model_topics("data-2018-04-01T17:00:00.json", "data-2018-04-01.csv")
    model_topics("data-2018-04-02T19:00:00.json", "data-2018-04-02.csv")
    model_topics("data-2018-04-03T16:00:00.json", "data-2018-04-03.csv")
    model_topics("data-2018-04-04T14:00:00.json", "data-2018-04-04.csv")
    model_topics("data-2018-04-05T11:00:00.json", "data-2018-04-05.csv")
    model_topics("data-2018-04-06T09:00:00.json", "data-2018-04-06.csv")
    model_topics("data-2018-04-07T13:00:00.json", "data-2018-04-07.csv")
    model_topics("data-2018-04-08T11:00:00.json", "data-2018-04-08.csv")
    model_topics("data-2018-04-09T08:00:00.json", "data-2018-04-09.csv")
    model_topics("data-2018-04-10T08:00:00.json", "data-2018-04-10.csv")

    model_topics("data-2018-04-11T13:00:00.json", "data-2018-04-11.csv")
    model_topics("data-2018-04-12T23:00:00.json", "data-2018-04-12.csv")
    model_topics("data-2018-04-13T09:00:00.json", "data-2018-04-13.csv")
    model_topics("data-2018-04-14T13:00:00.json", "data-2018-04-14.csv")
    model_topics("data-2018-04-15T17:00:00.json", "data-2018-04-15.csv")
    model_topics("data-2018-04-16T20:00:00.json", "data-2018-04-16.csv")
    model_topics("data-2018-04-17T09:00:00.json", "data-2018-04-17.csv")
    model_topics("data-2018-04-18T11:00:00.json", "data-2018-04-18.csv")
    model_topics("data-2018-04-19T13:00:00.json", "data-2018-04-19.csv")
    model_topics("data-2018-04-20T20:00:00.json", "data-2018-04-20.csv")

    model_topics("data-2018-04-21T08:00:00.json", "data-2018-04-21.csv")
    model_topics("data-2018-04-22T17:00:00.json", "data-2018-04-22.csv")
    model_topics("data-2018-04-23T19:00:00.json", "data-2018-04-23.csv")
    model_topics("data-2018-04-24T13:00:00.json", "data-2018-04-24.csv")
    model_topics("data-2018-04-25T11:00:00.json", "data-2018-04-25.csv")
    model_topics("data-2018-04-26T10:00:00.json", "data-2018-04-26.csv")
    model_topics("data-2018-04-27T20:00:00.json", "data-2018-04-27.csv")
    model_topics("data-2018-04-28T11:00:00.json", "data-2018-04-28.csv")
    model_topics("data-2018-04-29T22:00:00.json", "data-2018-04-29.csv")
    model_topics("data-2018-04-30T09:00:00.json", "data-2018-04-30.csv")



