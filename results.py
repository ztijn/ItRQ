import csv
import nltk

def average():
    total_val = 0
    total_sentlen = 0
    counter = 0

    with open('JEOPARDY.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            if row[2] == 'Jeopardy!':
                value = row[4][1:]
                for char in value:
                    if char in ".,":
                        value = value.replace(char, '')
                val = int(value)
                question = row[5]

                total_val += val
                total_sentlen += len(nltk.word_tokenize(question))
                counter += 1

                #print(val, question)
        avg_val = total_val / counter
        avg_len = total_sentlen / counter
        print(avg_val, avg_len)

def result_data():

    diff_long = 0
    diff_short = 0
    easy_long = 0
    easy_short = 0

    with open('JEOPARDY.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            if row[2] == 'Jeopardy!':
                value = row[4][1:]
                for char in value:
                    if char in ".,":
                        value = value.replace(char, '')
                val = int(value)
                question = row[5]
                que_len = len(nltk.word_tokenize(question))

                if val > 490:
                    if que_len > 16:
                        diff_long += 1
                    else:
                        diff_short += 1
                else:
                    if que_len > 16:
                        easy_long += 1
                    else:
                        easy_short += 1

    print("diff_long:", diff_long, "\ndiff_short:", diff_short, "\neasy_long:", easy_long, "\neasy_short:", easy_short)




def main():
    #average()
    result_data()


if __name__ == "__main__":
    main()	
