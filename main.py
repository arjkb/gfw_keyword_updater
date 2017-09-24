# read all urls
# read all words
# generate a query string with a word and url
# sent http get to that url 100 times
# if request gets blocked for over 70 % of the time,
# then it is a banned keyword

# add the word to the list of banned keywords

import argparse
import requests

def get_query_url(base_url, keyword):
    return base_url + "/?q=" + keyword

def read_lines(filename):
    contents = list()
    with open(filename, 'r') as f:
        for line in f:
            contents.append(line.strip())
    return contents

def is_blocked_keyword(keyword, urls):
    max_iterations = 1
    blocked_count = 0
    worked_count = 0
    for url in urls:
        query_url = get_query_url(url, keyword)
        # print(query_url)
        for i in range(max_iterations):
            try:
                r = requests.get(query_url)
                if r.status_code == requests.codes.ok:
                    worked_count += 1
            except requests.exceptions.ConnectionError:
                blocked_count += 1
            except:
                pass

    print(keyword, blocked_count, worked_count)
    if (blocked_count > worked_count):
        return True
    else:
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("words_file", help="file containing all the words", type=str)
    parser.add_argument("urls_file", help="file containing all the urls", type=str)
    args = parser.parse_args()

    urls = read_lines(args.urls_file)
    print(urls[0])

    keywords = read_lines(args.words_file)
    print(keywords[0])

    print(get_query_url(urls[0], keywords[0]))

    for keyword in keywords:
        blocked_keyword = is_blocked_keyword(keyword, urls)
        if blocked_keyword:
            print(keyword + " is blocked")

if __name__ == '__main__':
    main()
