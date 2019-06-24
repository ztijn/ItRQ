import csv
import nltk
import matplotlib.pyplot as plt

def average():
    total_val = 0
    total_sentlen = 0
    counter = 0

    with open('JEOPARDY.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:

            # only questions in the round Jeopardy!
            if row[2] == 'Jeopardy!':

                # get a value as integer corresponding with the diffuculty of the question
                value = row[4][1:]
                for char in value:
                    if char in ".,":
                        value = value.replace(char, '')
                val = int(value)

                # get the question
                question = row[5]

                # add all values to a total and keep track of counter
                total_val += val
                total_sentlen += len(nltk.word_tokenize(question))
                counter += 1

        # print average money value and average question length
        avg_val = total_val / counter
        avg_len = total_sentlen / counter
        print(avg_val, avg_len)

def result_data():

    diff_long = 0
    diff_short = 0
    easy_long = 0
    easy_short = 0

    data_val = []
    data_que = []

    total_long = 0
    total_short = 0
    long_counter = 0
    short_counter = 0

    with open('JEOPARDY.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:

            # only questions in the round Jeopardy!
            if row[2] == 'Jeopardy!':

                # get a value as integer corresponding with the difficulty of the question
                value = row[4][1:]
                for char in value:
                    if char in ".,":
                        value = value.replace(char, '')
                val = int(value)

                # get value for amount of tokens in a question
                question = row[5]
                que_len = len(nltk.word_tokenize(question))

                # add datapoint for graph
                data_val += [val]
                data_que += [que_len]

                # checks if question is long/short and difficult/easy
                if val > 490:
                    if que_len > 16:
                        diff_long += 1
                        total_long += val
                        long_counter += 1
                    else:
                        diff_short += 1
                        total_short += val
                        short_counter += 1
                else:
                    if que_len > 16:
                        easy_long += 1
                        total_long += val
                        long_counter += 1
                    else:
                        easy_short += 1
                        total_short += val
                        short_counter += 1

    #make a graph
    makeplot(data_que, data_val)

    #print values for the confusion matrix
    print("diff_long:", diff_long, "\ndiff_short:", diff_short, "\neasy_long:", easy_long, "\neasy_short:", easy_short)

    print("avg val long:", (total_long/long_counter), "\navg val short:", (total_short/short_counter))



def makeplot(x, y):
    # plotting the points
    plt.scatter(x, y, label= "stars", color= "blue", marker= ".", s=30)
    # naming the x axis
    plt.xlabel('tokens in question')
    # naming the y axis
    plt.ylabel('money value of question')
    # giving a title to my graph
    plt.title('question difficulty vs question length')
    # function to show the plot
    plt.savefig("temp.png")
    plt.show()


def main():
    average()
    result_data()


if __name__ == "__main__":
    main()	
