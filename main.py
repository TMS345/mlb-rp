import requests

url = "https://mlb-data.p.rapidapi.com/json/named.player_info.bam"

def __get_input ():
    exit = False

    while (not exit):
        i = str (input ("1 - Search for a player\n2 - Search for a team\n3 - Exit the program" 
               + "\n\nEnter your selection: "))

        print_format ()
    
        if (i == "1"): 
            __get_player ()
        elif (i == "2"):
            __get_roster ()
        elif (i == "3"):
            exit = True
        else:    
            print ("Ensure that your input is correct")

        print_format ()


def __get_player ():

    querystring = {"sport_code":"'mlb'","player_id":"'493316'"}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def __get_roster ():

    querystring = {"team_id":"'121'"}

    headers = {
        "X-RapidAPI-Key": "8b77dd76e4msh15e560cc36053d2p1146c5jsnf90895c51573",
        "X-RapidAPI-Host": "mlb-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return (response.text)


def print_format ():
    print ("")
    print ('*' * 164)
    print ("")


if __name__ == '__main__':
    __get_input ()