# BasketballReference.com Test Scraper


An exercise to test the very basic features of <a href="https://pypi.org/project/beautifulsoup4/" target="_blank">Beautiful Soup</a>.

## Description

As a long time basketball enthusiast, my interest into the numbers of basketball has grown with time, especially thanks to the increasing number of sources where taking info from.

One of my favourites is <a href="https://www.basketball-reference.com/" target="_blank">BasketballReference.com</a>, among the most popular ones.
This script is intended as an exercise and as a token of appreciation for their work. I hope they won't get mad at me!

The script is very simple for the moment.
It involves:

```
BeautifulSoup
Python Requests 
Python 
```

The highlights of the script are:

* `requests.get()`: importing the [Requests](https://docs.python-requests.org/en/latest/) library, to make a _request_ and obtain a _response_ object in return with the data about the website page
* `response.raise_for_request()`: a [method](https://docs.python-requests.org/en/latest/user/quickstart/#response-status-codes) to check the actual status of the request. It returns something different from _None_ in case anything unwanted happens
* BeautifulSoup <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/#calling-a-tag-is-like-calling-find-all)" target="_blank">`find()`</a> and <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/#calling-a-tag-is-like-calling-find-all" target="_blank">`find_all()`</a> returning, in order, just one or all the tags we want them to search for
* Handling <a href="https://www.w3schools.com/python/python_file_handling.asp">`files`</a> to read from and write into

The data is stored in .txt or .csv files for simplicity
