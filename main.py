import requests #used to connect to service using api
import sqlite3 #used to create and manage database
import json #used to decode in python

#initial prompt menu
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

#User selected to see player information
def __get_player_info(name):
    exit = False

    while (not exit):
        i = str (input("1 - General player info\n2 - Projected Stats\n3 - Season Stats" + 
            "\n4 - Career Stats\n5 - League Stats\n6 - Return\n\nEnter your selection: "))
        
        if (i == "1"): 
            print_format_three ()

            __get_player (name)

            print_format_three ()
        elif (i == "2"):
            print_format_two ()

            __print_proj(name)

        elif (i == "3"):
            print_format_two ()

            __print_sn (name)

        elif (i == "4"):
            print_format_two ()

            __print_career (name)

        elif (i == "5"):
            print_format_two (name)

            __print_league (name)

        elif (i == "6"): 
            exit = True
        else:    
            print ("Ensure that your input is correct")




#proj options
#need name parameter to calculate player id for query
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

            __get_proj_pitch (name)

            print_format_three ()

        elif (i == "3"):
            exit = True
            print_format_two ()




#Seasonal options
#need name parameter to calculate player id for query
def __print_sn (name, exit = False):
    while (not exit):
        i = str (input ("1 - Season Hitting Stats\n2 - Season Pitching Stats\n3 - Return" + 
                    "\n\nEnter your selection: ")) 
                
        if (i == "1"):
            print_format_three ()

            __get_season_hit (name)

            print_format_three ()

        elif (i == "2"):

            print_format_three ()

            __get_season_pitch (name)

            print_format_three ()

        elif (i == "3"):

            exit = True

            print_format_two ()




#Career options
#need name parameter to calculate player id for query
def __print_career (name, exit = False):
     while (not exit):
        i = str (input ("1 - Career Hitting Stats\n2 - Career Pitching Stats\n3 - Return" + 
                    "\n\nEnter your selection: ")) 
                
        if (i == "1"):
            print_format_three ()
            __get_career_hit (name)
            print_format_three ()
        elif (i == "2"):
            print_format_three ()
            __get_career_pitch (name)
            print_format_three ()
        elif (i == "3"):
            exit = True
            print_format_two ()




#League Options
def __print_league (name, exit = False):
    while (not exit):
        i = str (input ("1 - League Hitting Stats\n2 - League Pitching Stats\n3 - Return" + 
                    "\n\nEnter your selection: ")) 
                        
        if (i == "1"):
            print_format_three ()

            __get_league_hit (name)

            print_format_three ()
        
        elif (i == "2"):
            print_format_three ()

            __get_league_pitch (name)

            print_format_three ()

        elif (i == "3"):
            exit = True
            print_format_two () 
        



def __get_season_hit (name):

    url = "https://mlb-data.p.rapidapi.com/json/named.sport_hitting_tm.bam"

    value = get_from_name(name, 'player_id')

    querystring = {"league_list_id":"'mlb'","game_type":"'R'","season":"'2017'","player_id":"'{}'".format(value)}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response.raise_for_status()

    response_json = response.json()
  
    json_dump = json.dumps(response_json, indent=2)
    
    try:
        for i in response_json['sport_pitching_tm']['queryResults']['row']:
         print(i," = ", response_json['sport_pitching_tm']['queryResults']['row'][i])
    except:
        print("Player does not having hitting stats for the season.")
    




#Retrieves career hitting stats
def __get_career_hit (name):

    url = "https://mlb-data.p.rapidapi.com/json/named.sport_career_hitting.bam"

    value = get_from_name(name, 'player_id')

    querystring = {"league_list_id":"'mlb'", "game_type":"'R'","player_id":"'{}'".format(value)}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response.raise_for_status()

    response_json = response.json()

    json_dump = json.dumps(response_json, indent=2)

    #Use try/except to handle edge case concerning pitching stats for non-pitching players
    try:
        for i in response_json['sport_career_hitting']['queryResults']['row']:
            print(i," = ", response_json['sport_career_hitting']['queryResults']['row'][i])
    except:
        print("{} does not have any career pitching stats.".format(name))

#Retrieves league hitting stats... mimics seasonal data
def __get_league_hit (name):

    url = "https://mlb-data.p.rapidapi.com/json/named.sport_career_hitting_lg.bam"

    value = get_from_name(name, 'player_id')

    querystring = {"league_list_id":"'mlb'", "game_type":"'R'","player_id":"{}".format(value)}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    #check to see if request was successful
    response.raise_for_status()

    response_json = response.json()

   
    json_dump = json.dumps(response_json, indent=2)
   
    #try/except to handle player with no stats
    try:
        for i in response_json['sport_career_hitting_lg']['queryResults']['row']:
           print(i," = ", response_json['sport_career_hitting_lg']['queryResults']['row'][i])
    except:
        print("{} does not have any league hits.".format(name))
    

#Retrieves career pitching stats 
def __get_career_pitch (name):

    url = "https://mlb-data.p.rapidapi.com/json/named.sport_career_pitching.bam"

    value = get_from_name(name, 'player_id')

    querystring = {"league_list_id":"'mlb'", "game_type":"'R'","player_id":"'{}'".format(value)}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response.raise_for_status()

    response_json = response.json()

    json_dump = json.dumps(response_json, indent=2)
    
    #Use try/except to handle edge case concerning pitching stats for non-pitching players
    try:
        for i in response_json['sport_career_pitching']['queryResults']['row']:
            print(i," = ", response_json['sport_career_pitching']['queryResults']['row'][i])
    except:
        print("{} does not have any career pitching stats.".format(name))
    

#Retrieves and prints seasonal pitching stats
def __get_season_pitch (name):

    url = "https://mlb-data.p.rapidapi.com/json/named.sport_pitching_tm.bam"

    value = get_from_name(name, 'player_id')

    querystring = {"league_list_id":"'mlb'", "game_type":"'R'", "season": "'2017'","player_id":"'{}'".format(value)}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)

    response.raise_for_status()

    response_json = response.json()

    json_dump = json.dumps(response_json, indent=2)
    
    #Use try/except to handle edge case concerning pitching stats for non-pitching players
    try:
        for i in response_json['sport_pitching_tm']['queryResults']['row']:
            print(i," = ", response_json['sport_pitching_tm']['queryResults']['row'][i])
    except:
        print("{} does not have pitching stats for the season.".format(name))
    



#Retrieves leage pitching stats. Stats mimic seasonal data.
def __get_league_pitch (name):

    url = "https://mlb-data.p.rapidapi.com/json/named.sport_career_pitching_lg.bam"

    value = get_from_name(name, 'player_id')

    querystring = {"league_list_id":"'mlb'", "game_type":"'R'","player_id":"{}".format(value)}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response.raise_for_status()

    response_json = response.json()
    #json_object = json.loads(response_json)

    json_dump = json.dumps(response_json, indent=2)

    
    #Use try/except to handle edge case concerning pitching stats for non-pitching players
    try:
        for i in response_json['sport_career_pitching_lg']['queryResults']['row']:
    
            print(i," = ", response_json['sport_career_pitching_lg']['queryResults']['row'][i])

    except:
        print("{} does not have any league pitches.".format(name))




def __get_proj_pitch (name):
    
    url = "https://mlb-data.p.rapidapi.com/json/named.proj_pecota_pitching.bam"

    value = get_from_name(name, 'player_id')

    querystring = {"season":"'2017'", "player_id":"'{}'".format(value)}
    
    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response.raise_for_status()

    response_json = response.json()

    #json_object = json.loads(response_json)

    json_dump = json.dumps(response_json, indent=2)
    
    #Use try/except to handle edge case concerning pitching stats for non-pitching players
    try:
        for i in response_json['proj_pecota_pitching']['queryResults']['row']:
            print(i," = ", response_json['proj_pecota_pitching']['queryResults']['row'][i])
    except:
        print("Player is not a pitcher!")




#Display projected hitting stats
def __get_proj_hit (name):

    url = "https://mlb-data.p.rapidapi.com/json/named.proj_pecota_batting.bam"

    value = get_from_name(name, 'player_id')
    
    #Query String
    querystring = {"season":"'2017'", "player_id":"'{}'".format(value)}
    
    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response.raise_for_status()

    response_json = response.json()
    
    json_dump = json.dumps(response_json, indent=2)

    for i in response_json['proj_pecota_batting']['queryResults']['row']:
        print(i," = ", response_json['proj_pecota_batting']['queryResults']['row'][i])
    



def __get_player(name):

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

    try:

        connection = sqlite3.connect("database.db")

        cur = connection.cursor()
        
        #Calculate the number of rows present in History Table
        cur.execute("SELECT * FROM History")
        
        #New ID value 
        index = len(cur.fetchall())
        
        #Confirm changes to database
        connection.commit()
        
        #Update Database
        cur.execute ("INSERT INTO History VALUES ({},'{}','{}','{}','{}');".format(index,
                      response_json['search_player_all']['queryResults']['row']['name_display_first_last'],
                      response_json['search_player_all']['queryResults']['row']['team_full'],
                      response_json['search_player_all']['queryResults']['row']['position'],
                      response_json['search_player_all']['queryResults']['row']['birth_country']) )
        
        #close connection to database
        connection.commit()
            
    except:
        print("Error updating history.")
    
    finally: 
        connection.close()

    #Print Player information after updating history
    for i in response_json['search_player_all']['queryResults']['row']:               
        print(i," = ", response_json['search_player_all']['queryResults']['row'][i])




#gets all teams to print and update database
def __get_all_teams(season):
    url = "https://mlb-data.p.rapidapi.com/json/named.team_all_season.bam"
 
    querystring = {"sport_code":"'mlb'","all-star":"'N'", "sort_order": "name_asc", "season" : "'{}'".format(season)}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response.raise_for_status ()

    response_json = response.json ()

    json_dump = json.dumps (response_json, indent=2)

    list_count = len ( response_json['team_all_season']['queryResults']['row'] ) - 1
    try:
     connection = sqlite3.connect("database.db")

     cur = connection.cursor()

     cur.execute("CREATE TABLE Teams(ID INT PRIMARY KEY NOT NULL, TEAM TEXT NOT NULL);")

     index = 0
     
     for lists in range ( 0, list_count):

        if response_json['team_all_season']['queryResults']['row'][lists]['mlb_org'] != "":

            print(response_json['team_all_season']['queryResults']['row'][lists]['mlb_org'])

            cur.execute ( "INSERT INTO Teams VALUES({},'{}');".format(index, response_json['team_all_season']['queryResults']['row'][lists]['mlb_org']) )
           
            index+=1
     
     #Save changes to database
     connection.commit()
            
    except:
        print("error")
    
    finally: 
        connection.close()



#gets team id #needed for queries
def get_team_id ( team, season ):
    url = "http://lookup-service-prod.mlb.com/json/named.team_all_season.bam"
 
    querystring = {"sport_code":"'mlb'","all-star_sw":"'N'", "sort_order": "name_asc", "season" : "'{}'".format(season)}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response.raise_for_status ()

    response_json = response.json ()

    json_dump = json.dumps (response_json, indent=2)

    list_count = len ( response_json['team_all_season']['queryResults']['row'] ) - 1

    for lists in range ( 0, list_count):
        if response_json['team_all_season']['queryResults']['row'][lists]['mlb_org'] == "{}".format(team):
            return response_json['team_all_season']['queryResults']['row'][lists]['team_id'] 
    
    




def __get_roster ():

    print("What season would you like to analyze?")

    #Save season in variable
    season = input()
    
    #print all teams
    print(__get_all_teams(season))
    
    #prompt user to select team of choice
    print("Here are all of the teams from the '{}' season. Please pick one.".format(season))
    
    #save user command in variable
    team = input()
    
    #get and save id in variable
    id = get_team_id ( team, season )
    
    url = "http://lookup-service-prod.mlb.com/json/named.roster_40.bam"

    #Roster Query String
    querystring = {"team_id":"'{}'".format(id)}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }
    
    #API Response
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    #Check for Exceptions
    response.raise_for_status ()
    
    #Save file as json
    response_json = response.json ()
    
    #Dump the database to convert objet 
    json_dump = json.dumps (response_json, indent=2)
    
    #The number of lists containing data we need 
    list_count = len ( response_json['roster_40']['queryResults']['row'] ) - 1
    
    #Use a try/except/finally to catch errors if database connection is unsuccessful
    try:

        connection = sqlite3.connect("database.db")

        cur = connection.cursor()

        cur.execute("CREATE TABLE Roster(ID INT PRIMARY KEY NOT NULL, TEAM TEXT NOT NULL, POSITION TEXT NOT NULL);")
       
        index = 0
     
        for lists in range (0, list_count):

            cur.execute ( "INSERT INTO Roster VALUES( {}, '{}', '{}');".format(index, response_json['roster_40']['queryResults']['row'][lists]['name_display_first_last'], response_json['roster_40']['queryResults']['row'][lists]['position_txt'] ) )
            
            index+=1

            connection.commit()
            
    except:
            print("Error updating roster to database")
    
    #close connection to database
    finally: 
            connection.close()
    
    #Print out roster after updating database
    for lists in range ( 0, list_count):
        print ( response_json['roster_40']['queryResults']['row'][lists]['name_display_first_last'], " ( Position:", 
                response_json['roster_40']['queryResults']['row'][lists]['position_txt'],")" )
    



#Print Formats
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




#method to retrieve Player Information using a name
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
    for i in response_json['search_player_all']['queryResults']['row']: 
         if i == item:
            return response_json['search_player_all']['queryResults']['row'][i]
    
    

        




def __get_proj_hit (name):

    url = "https://mlb-data.p.rapidapi.com/json/named.proj_pecota_batting.bam"

    value = get_from_name(name, 'player_id')
    
    querystring = {"season":"'2017'", "player_id":"'{}'".format(value)}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request ("GET", url, headers=headers, params=querystring)

    response.raise_for_status ()

    response_json = response.json ()

    json_dump = json.dumps (response_json, indent=2)
    
    print (json_dump)
    
    #Updates and prints name information
    for i in response_json['proj_pecota_pitching']['queryResults']['row']:
        print(i," = ", response_json['proj_pecota_pitching']['queryResults']['row'][i])



def get_from_name (name, item):
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
         
#Create or use database specified by user and establish a connection, 
#initially creating our history table
def connect_to_database(database_file):

    #Use a try/except/finally to catch errors if database connection is unsuccessful
    try:
        connection = sqlite3.connect(database_file)
        print(sqlite3.version)
    
        #check if database is empty
        cur = connection.cursor()
        
        cur.execute("SELECT name FROM sqlite_master")
        
        #fetchall() iterator to get all rows in database
        list = cur.fetchall()

        #If not empty, do not create a table and continue
        if len(list) > 0:
            return

        else:
            print('List is empty, creating database with an initial history table now.')
        
            #Create history table in database
            cur.execute('''CREATE TABLE History(
                          ID INT PRIMARY KEY NOT NULL,
                          PLAYER TEXT NOT NULL,
                          TEAM TEXT NOT NULL,
                          POSITION TEXT NOT NULL,
                          COUNTRY TEXT NOT NULL);''')
                          
            #Save changes to database
            connection.commit()
      
       
    except:
        print ("Error making initial history table.")
     
    finally:    
        #close connection to database
        connection.close()
    
    


if __name__ == '__main__':
    print("Please name your database: ")
    database_name = input()

    connect_to_database('database_name')  #Connect to SQLITE Database
    __menu () #Prompt user with menu 

