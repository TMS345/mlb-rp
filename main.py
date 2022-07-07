import http.client

conn = http.client.HTTPSConnection("mlb-data.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "SIGN-UP-FOR-KEY",
    'X-RapidAPI-Host': "mlb-data.p.rapidapi.com"
    }

conn.request("GET", "/json/named.roster_40.bam?team_id='121'", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))