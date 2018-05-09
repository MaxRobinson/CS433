import csv
import matplotlib.pyplot as plt

def word_sets_over_time(inputFiles):
    topic_per_month = []
    for inputFile in inputFiles:
        inputRows = []
        with open(inputFile, 'r') as f:
            reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            next(reader)

            for row in reader:
                inputRows.append(row)

        word_set = set()
        for row in inputRows:
            for word in row:
                word_set.add(word)

        topic_per_month.append(word_set)

    print(topic_per_month)

    # Calculate word diff over time
    total_words_per_day = []
    word_deltas_per_day = [0]
    for i in range(len(topic_per_month)-1):
        dayi = topic_per_month[i]
        dayj = topic_per_month[i+1]
        # delta_set1 = dayi - dayj
        # delta_set2 = dayj - dayi
        #
        # delta_set = delta_set1.union(delta_set2)

        delta_set = dayi.intersection(dayj)

        word_deltas_per_day.append(len(delta_set))
        # lens = len(dayi) + len(dayj)
        # lens /= 2
        total_words_per_day.append(len(dayi))
        if i+1 >= len(topic_per_month)-1:
            total_words_per_day.append(len(dayj))

    plt.figure()

    plt.ylim(ymax=18, ymin=0)
    plt.xlim(xmax=31, xmin=0)

    plt.plot(range(1, len(total_words_per_day)+1), word_deltas_per_day, label='Words in Common From Previous Day')
    plt.plot(range(1, len(total_words_per_day)+1), total_words_per_day, label='Unique Words')

    plt.legend()
    plt.xlabel("Day Number in April")
    plt.ylabel("Number of Unique Words")

    title = "Change in Unique Words From Day to Day"
    # title_part2 = "with DistQL-{} tau {} in {}".format(DQL_type, tau, env_name)
    plt.title(title)

    plt.savefig("UniqueWordsOverTime.svg")
    plt.show()
    plt.close()


def topics_per_month(inputFiles):

    topic_per_month = []
    for inputFile in inputFiles:
        inputRows = []
        with open(inputFile, 'r') as f:
            reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            next(reader)

            for row in reader:
                inputRows.append(row)

        # print(inputRows)
        topic_per_month.append(inputRows[0])

    print(topic_per_month)


if __name__ == '__main__':
    data_files = ['data-2018-04-01.csv',
                  'data-2018-04-02.csv',
                  'data-2018-04-03.csv',
                  'data-2018-04-04.csv',
                  'data-2018-04-05.csv',
                  'data-2018-04-06.csv',
                  'data-2018-04-07.csv',
                  'data-2018-04-08.csv',
                  'data-2018-04-09.csv',
                  'data-2018-04-10.csv',
                  'data-2018-04-11.csv',
                  'data-2018-04-12.csv',
                  'data-2018-04-13.csv',
                  'data-2018-04-14.csv',
                  'data-2018-04-15.csv',
                  'data-2018-04-16.csv',
                  'data-2018-04-17.csv',
                  'data-2018-04-18.csv',
                  'data-2018-04-19.csv',
                  'data-2018-04-20.csv',
                  'data-2018-04-21.csv',
                  'data-2018-04-22.csv',
                  'data-2018-04-23.csv',
                  'data-2018-04-24.csv',
                  'data-2018-04-25.csv',
                  'data-2018-04-26.csv',
                  'data-2018-04-27.csv',
                  'data-2018-04-28.csv',
                  'data-2018-04-29.csv',
                  'data-2018-04-30.csv']
    # topics_per_month(data_files)
    word_sets_over_time(data_files)

