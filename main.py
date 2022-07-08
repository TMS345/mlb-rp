import requests
import sqlite3
import json

def __menu (connection):
    exit = False
    
    while (not exit):
        i = str (input ("1 - Search for a player\n2 - Search for a team\n3 - Exit the program" 
               + "\n\nEnter your selection: "))

        print_format_one ()
    
        if (i == "1"): 
            print("Please enter the Player name: ")
            name = input()
            print("Printing name: "+name)
            __get_player_info(name, connection)
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


def __print_proj (name, exit = False):
    while (not exit):
        i = str (input ("1 - Projected Hitting Stats\n2 - Projected Pitching Stats\n3 - Return" +
            "\n\nEnter your selection: ")) 
                    
        if (i == "1"):
            print_format_three ()
            __get_proj_hit (name)
            print_format_three ()
        elif (i == "2"):
            print_format_three ()
            __get_proj_pitch ()
            print_format_three ()
        elif (i == "3"):
            exit = True
            print_format_two ()


def __print_sn (exit = False):
    while (not exit):
        i = str (input ("1 - Season Hitting Stats\n2 - Season Pitching Stats\n3 - Return" + 
                    "\n\nEnter your selection: ")) 
                
        if (i == "1"):
            print_format_three ()
            __get_season_hit ()
            print_format_three ()
        elif (i == "2"):
            print_format_three ()
            __get_season_pitch ()
            print_format_three ()
        elif (i == "3"):
            exit = True
            print_format_two ()


def __print_career (exit = False):
    while (not exit):
        i = str (input ("1 - Career Hitting Stats\n2 - Career Pitching Stats\n3 - Return" + 
                    "\n\nEnter your selection: ")) 
                
        if (i == "1"):
            print_format_three ()
            __get_career_hit ()
            print_format_three ()
        elif (i == "2"):
            print_format_three ()
            __get_career_pitch ()
            print_format_three ()
        elif (i == "3"):
            exit = True 
            print_format_two ()


def __print_league (exit = False):
    while (not exit):
        i = str (input ("1 - League Hitting Stats\n2 - League Pitching Stats\n3 - Return" + 
                    "\n\nEnter your selection: ")) 
                        
        if (i == "1"):
            print_format_three ()
            __get_league_hit ()
            print_format_three ()
        elif (i == "2"):
            print_format_three ()
            __get_league_pitch ()
            print_format_three ()
        elif (i == "3"):
            exit = True
            print_format_two () 
        

def __get_player_info(name, connection):
    exit = False

    while (not exit):
        i = str (input("1 - General player info\n2 - Projected Stats\n3 - Season Stats" + 
            "\n4 - Career Stats\n5 - League Stats\n6 - Return\n\nEnter your selection: "))
        
        if (i == "1"): 
            print_format_three ()
            __get_player (name, connection)
            print_format_three ()
        elif (i == "2"):
            print_format_two ()
            __print_proj(name)
        elif (i == "3"):
            print_format_two ()
            __print_sn ()
        elif (i == "4"):
            print_format_two ()
            __print_career ()
        elif (i == "5"):
            print_format_two ()
            __print_league ()
        elif (i == "6"):        
            exit = True
        else:    
            print ("Ensure that your input is correct")


def __get_season_hit ():

    url = "https://mlb-data.p.rapidapi.com/json/named.sport_hitting_tm.bam"

    querystring = {"league_list_id":"'mlb'","game_type":"'R'","season":"'2017'","player_id":"'493316'"}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def __get_career_hit ():

    url = "https://mlb-data.p.rapidapi.com/json/named.sport_career_hitting.bam"

    querystring = {"player_id":"'592789'","game_type":"'R'","league_list_id":"'mlb'"}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def __get_league_hit ():

    url = "https://mlb-data.p.rapidapi.com/json/named.sport_career_hitting_lg.bam"

    querystring = {"game_type":"'R'","player_id":"'592789'","league_list_id":"'mlb'"}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def __get_career_pitch ():

    url = "https://mlb-data.p.rapidapi.com/json/named.sport_career_pitching.bam"

    querystring = {"player_id":"'592789'","league_list_id":"'mlb'","game_type":"'R'"}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def __get_season_pitch ():

    url = "https://mlb-data.p.rapidapi.com/json/named.sport_pitching_tm.bam"

    querystring = {"season":"'2017'","player_id":"'592789'","league_list_id":"'mlb'","game_type":"'R'"}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def __get_league_pitch ():

    url = "https://mlb-data.p.rapidapi.com/json/named.sport_career_pitching_lg.bam"

    querystring = {"league_list_id":"'mlb'","game_type":"'R'","player_id":"'592789'"}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def __get_proj_pitch (name):
    
    url = "https://mlb-data.p.rapidapi.com/json/named.proj_pecota_pitching.bam"
    
    querystring = {"player_id":"'592789'","league_list_id":"'mlb'","season":"'2017'"}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response.raise_for_status()
    response_json = response.json()
    #json_object = json.loads(response_json)
    json_dump = json.dumps(response_json, indent=2)
    print (json_dump)
    for i in response_json ['search_player_all']['queryResults']['row']:
         print (i , " = ", response_json ['search_player_all']['queryResults']['row'][i])
    #print(response_json)
    #print("Name:", response_json['search_player_all']['queryResults']['row']['name_display_first_last'] )
    #print("Player ID: ", response_json['search_player_all']['queryResults']['row']['player_id'])
    #print("Player")
    #print(response.text)


def __get_proj_hit (name):

    url = "https://mlb-data.p.rapidapi.com/json/named.proj_pecota_batting.bam"
    value = get_from_name(name, 'player_id')
    print(value)
    querystring = {"season":"'2017'", "player_id":"'{}'".format(value)}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def __get_all_teams ():
    url = "https://mlb-data.p.rapidapi.com/json/named.team_all_season.bam"
 
    querystring = {"sport_code":"'mlb'","all-star":"'N'", "sort_order": ""}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def __get_player (name, connection):

    url = "https://mlb-data.p.rapidapi.com/json/named.search_player_all.bam"
 
    querystring = {"sport_code":"'mlb'","active_sw": "'Y'", "name_part": "'{}'".format(name)}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response.raise_for_status()
    response_json = response.json()
    #json_object = json.loads(response_json)
    json_dump = json.dumps(response_json, indent=2)
    print (json_dump)
    for i in response_json ['search_player_all']['queryResults']['row']:
         print (i , " = ", response_json ['search_player_all']['queryResults']['row'][i])
    #print(response_json)
    #print("Name:", response_json['search_player_all']['queryResults']['row']['name_display_first_last'] )
    #print("Player ID: ", response_json['search_player_all']['queryResults']['row']['player_id'])
    #print("Player")
    #print(response.text)


def __get_roster ():

    url = "https://mlb-data.p.rapidapi.com/json/named.roster_40.bam"
    
    querystring = {"team_id":"'121'"}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return (response.text)


def print_format_one ():
    print ("")
    print ('*' * 24)
    print ("")


def print_format_two ():
    print ("")
    print ('~' * 24)
    print ("")


def print_format_three ():
    print ("")
    print ('!' * 180)
    print ("")

<<<<<<< HEAD
=======
def get_from_name(name, item):
    url = "https://mlb-data.p.rapidapi.com/json/named.search_player_all.bam"
 
    querystring = {"sport_code":"'mlb'","active_sw": "'Y'", "name_part": "'{}'".format(name)}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response.raise_for_status()
    response_json = response.json()
    #json_object = json.loads(response_json)
    json_dump = json.dumps(response_json, indent=2)
    print(json_dump)
    for i in response_json['search_player_all']['queryResults']['row']: 
         if i == item:
            return response_json['search_player_all']['queryResults']['row'][i]
         

>>>>>>> 36651d8f1be584d7ab86198deb78417449699973

def close_connection(connection): 
    connection.close()


def connect_to_database (database_file):
    try:
        connection = sqlite3.connect(database_file)
        print(sqlite3.version)
        cur = connection.cursor()
        #check if database is empty
        connection.execute("SELECT name FROM sqlite_master")
        list = cur.fetchall()
        if len (list) > 0:
            return connection

        print('List is empty, creating and updating database')
        connection.execute('''CREATE TABLE Data(
                            ID INT PRIMARY KEY NOT NULL,
                            PLAYER TEXT NOT NULL,
                            TEAM TEXT NOT NULL,
                            POSITION TEXT NOT NULL,
                            COUNTRY TEXT NOT NULL);'''
                            )
        cur.execute("INSERT INTO Data(ID,PLAYER, TEAM, POSITION, COUNTRY) VALUES(CESPEDES)")
        cur.execute("SELECT * FROM PLAYER")
        
        print(cur.fetchall())
        
    except:
        print("Error")
     
    finally:
        close_connection(connection)
    
    return connection


if __name__ == '__main__':
    database_connection = connect_to_database('MLB.db')  #Connect to SQLITE Database
    __menu (database_connection)
    




