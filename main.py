import requests

def __menu ():
    exit = False

    while (not exit):
        i = str (input ("1 - Search for a player\n2 - Search for a team\n3 - Exit the program" 
               + "\n\nEnter your selection: "))

        print_format_one ()
    
        if (i == "1"): 
            __get_player_info ()
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


def __print_proj (exit = False):
    while (not exit):
        i = str (input ("1 - Projected Hitting Stats\n2 - Projected Pitching Stats\n3 - Return" +
            "\n\nEnter your selection: ")) 
                    
        if (i == "1"):
            print_format_three ()
            __get_proj_hit ()
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
        

def __get_player_info():
    exit = False

    while (not exit):
        i = str (input ("1 - General player info\n2 - Projected Stats\n3 - Season Stats" + 
            "\n4 - Career Stats\n5 - League Stats\n6 - Return\n\nEnter your selection: "))
        
        if (i == "1"): 
            print_format_three ()
            __get_player ()
            print_format_three ()
        elif (i == "2"):
            print_format_two ()
            __print_proj ()
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


def __get_proj_pitch ():

    url = "https://mlb-data.p.rapidapi.com/json/named.proj_pecota_pitching.bam"

    querystring = {"player_id":"'592789'","league_list_id":"'mlb'","season":"'2017'"}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def __get_proj_hit ():

    url = "https://mlb-data.p.rapidapi.com/json/named.proj_pecota_batting.bam"

    querystring = {"player_id":"'592789'","league_list_id":"'mlb'","season":"'2017'"}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def __get_player ():

    url = "https://mlb-data.p.rapidapi.com/json/named.player_info.bam"
 
    querystring = {"sport_code":"'mlb'","player_id":"'493316'"}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


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


if __name__ == '__main__':
    __menu ()