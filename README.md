# MLB STATS PROGRAM
# **viewMLB**
#_Getting Team and Player Data using a simple MLB API_
#Marlon Dominguez
#Gershom Gbadebo

---

- API: https://rapidapi.com/theapiguy/api/mlb-data/
- API Documentation: https://appac.github.io/mlb-data-api-docs/

---

- Modules To Import
'''
import requests (used to connect to service using api), import sqlite3 (used to create and manage database), import json (used to decode in python)
'''
-Please make sure Python is installed. If not already installed, use: https://www.python.org/downloads/
---
_Database_

'''

Install(not necessary on python):
https://www.sqlite.org/index.html

More sqlite Documentation:
https://docs.python.org/3/library/sqlite3.html

More:
-No pip install
-import sqlite and you are ready to connect/create a database


_Create an sqlite object using cursor() to execute commands in SQL_

'''
try:
        connection = sqlite3.connect(database_file)
        print(sqlite3.version)
    
        #check if database is empty
        cur = connection.cursor()
        
        cur.execute("SELECT name FROM sqlite_master")
        
        #fetchall() iterator to get all rows in database
        list = cur.fetchall()
                .
                .
                .
                .
'''
---
_Primary Menu_

'''
Functions include: 
- Get player information
- Get team information 
- Update database history as user interacts


def __menu ():
    exit = False
    
    while (not exit):
        i = str (input ("1 - Search for a player\n2 - Search for a team\n3 - Exit the program" 
               + "\n\nEnter your selection: "))

        print_format_one ()
    
        if (i == "1"): 
            print("Please enter the Player name: ")
            
            name = input()

            print("Printing name: "+name)

            __get_player_info(name)

        elif (i == "2"):
            print_format_three ()

            __get_roster ()

            print_format_three ()

        elif (i == "3"):
            exit = True

            print_format_two ()

        else:    
            print ("Ensure that your input is correct")

        print_format_one ()

---
-def get_from_name (name, item):
'''
 url = "https://mlb-data.p.rapidapi.com/json/named.search_player_all.bam"
 
    querystring = {"sport_code":"'mlb'","active_sw": "'Y'", "name_part": "'{}'".format(name)}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request ("GET", url, headers=headers, params=querystring)

    response.raise_for_status ()

    response_json = response.json ()

    json_dump = json.dumps (response_json, indent=2)

    for i in response_json['search_player_all']['queryResults']['row']: 
        if i == item: 
            return response_json['search_player_all']['queryResults']['row'][i]
'''
###### v1 build