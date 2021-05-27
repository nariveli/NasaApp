import os
import json
import sqlite3
import requests
from datetime import date, timedelta
from database import create_table, insert, view

today = date.today()
next_monday = today + timedelta(days=-today.weekday(), weeks=1)
end = next_monday + timedelta(days=6)

dir = os.path.dirname(__file__)

api_key = os.environ['API_KEY']

with open(os.path.join(dir, "conf.json")) as json_conf : 
    CONF = json.load(json_conf)

url_this_week = CONF["urls"]["this_week"].format(today,next_monday,api_key)
url_next_week = CONF["urls"]["next_week"].format(next_monday,end,api_key)

urls = [url_this_week,url_next_week]

create_table()

for url in urls:
    response = requests.get(url)
    for approach_date, neo_details in response.json()["near_earth_objects"].items():
        for i in range(len(neo_details)):
            id = neo_details[i]['id']
            name = neo_details[i]['name']
            jpl_url = neo_details[i]['nasa_jpl_url']
            is_hazardous = neo_details[i]['is_potentially_hazardous_asteroid']
            next_approach = neo_details[i]['close_approach_data'][0]['close_approach_date_full']
                    
            try:
                insert(id, name, jpl_url, is_hazardous, next_approach)
                
            except sqlite3.IntegrityError:
                pass