import bs4
import requests
import datetime

read_from = "./players.txt"
write_into = "./stats.csv"
start = datetime.datetime.now()     # keeping track of the starting time
rows = 0

print("Scraping started on: ")
print(start.strftime("%Y-%m-%d %H:%M:%S"))

isFirstRow = True

with open(read_from, 'r') as f:     # file with the players list
    with open(write_into, "a") as txt_file:     # file where the stats will be written into
        lines = f.readlines()
        for line in lines:
            player = ""
            cols = ""
            dati = ""
            if len(line) > 0:
                player = line.split(", ")[0]
                print("Scraping stats for " + player + "...")
                newline = line.split(", ")[1][:-1]
                response = requests.get(newline)
                response.raise_for_status()  # in case of errors, this row returns more details
                soup = bs4.BeautifulSoup(response.text, 'html.parser')  # parsing the result of the request (for me to check the HTML tags)
                table_players = soup.find('table', class_='stats_table')
                thead = table_players.find('thead')
                tbody = table_players.find('tbody')

                cols = "Player,"
                th = thead.find_all('th')
                for line in th:
                    cols += line.text + ", "

                cols = cols[:-2] + "\n"

                tr = tbody.find_all('tr')   # scraping the actual stats
                for line in tr:
                    dati = player + ","
                    th = line.find('th')
                    if th != None:
                        dati += th.text +","
                        td = line.find_all('td')
                        for text in td:
                            if text.text == "":  # trying to prevent inserting NULL data
                                dato = 0
                            else:
                                dato = text.text
                            if type(dato) != int:   # if not an int
                                dato = dato.replace(",", "-")   # double roles are reported as i.e. PF,C Replacing that column with an - in order to avoid messing up with the CSV formatting
                            dati += str(dato) + ","
                    if isFirstRow:  # if it's the first row, adding the columns list before it
                        dati = cols + dati
                        isFirstRow = False

                    dati = dati[:-1] + "\n"

                    txt_file.write(dati)
                    rows += 1

# closing both text files
txt_file.close()
f.close()
end = datetime.datetime.now()   # stopping the counting of time
print("Scraping completed on: ")
print(end.strftime("%Y-%m-%d %H:%M:%S, %f"))    # completing the stop warning on the screen
print("Scraping performed in: " + str(end - start) + " (" + str(rows) + " rows)\n")   # showing how long the scraping took