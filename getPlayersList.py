import string
import bs4
import requests
import datetime

alphabet_string = string.ascii_lowercase    # all the letters
alphabet_list = list(alphabet_string)    # making a list of all the letters
start = datetime.datetime.now()     # keeping track of the starting time

print("Scraping started on: ")
print(start.strftime("%Y-%m-%d %H:%M:%S, %f"))

rows = 0

with open("players.txt", "a") as txt_file:
    for letter in alphabet_list:
        LINK = f'https://www.basketball-reference.com/players/{letter}'
        response = requests.get(LINK)
        response.raise_for_status()     # in case of errors, this row returns more details

        soup = bs4.BeautifulSoup(response.text, 'html.parser')  # parsing the result of the request (for me to check the HTML tags)

        table_players = soup.find('table', class_='sortable')   # the table containing the players list
        a_players = table_players.find_all('a')
        toFind = ".html"
        for a in a_players:
            names = ""
            names += a.text + ", "
            href = a.get('href')
            if(href.find(toFind) != -1):    # I want to be sure that's an href pointing to a player's page
                names += "https://www.basketball-reference.com" + href + "\n"
                txt_file.write(names)
                rows += 1


txt_file.close()    # closing the file where the list of players was stored
end = datetime.datetime.now()   # stopping the counting of time
print("Scraping completed on: ")
print(end.strftime("%Y-%m-%d %H:%M:%S, %f"))    # completing the stop warning on the screen
print("Scraping performed in: " + str(end - start) + " (" + str(rows) + " rows)")   # showing how long the scraping took