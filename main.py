# read all urls
# read all words
# generate a query string with a word and url
# sent http get to that url 100 times
# if request gets blocked for over 70 % of the time,
# then it is a banned keyword

# add the word to the list of banned keywords

import argparse

def read_lines(filename):
    contents = list()
    with open(filename, 'r') as f:
        for line in f:
            contents.append(line.strip())
    return contents

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("words_file", help="file containing all the words", type=str)
    parser.add_argument("urls_file", help="file containing all the urls", type=str)
    args = parser.parse_args()

    urls = read_lines(args.urls_file)
    print(urls)

    print(args.words_file, args.urls_file)

if __name__ == '__main__':
    main()
