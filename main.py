import http.client

conn = http.client.HTTPSConnection("mlb-data.p.rapidapi.com")

<<<<<<< HEAD
headers = 
{
    'X-RapidAPI-Key': "SIGN-UP-FOR-KEY",
=======
headers = {
    'X-RapidAPI-Key': "d2e36dc2aemsh56d545e7ce2aba1p144f27jsn7ac9a581efba",
>>>>>>> abd3ef4bfabaf2708e62d8d6549878ae0e4eebad
    'X-RapidAPI-Host': "mlb-data.p.rapidapi.com"
}

conn.request("GET", "/json/named.roster_40.bam?team_id='121'", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

print("API KEY AND HOST HAS BEEN UPDATED")