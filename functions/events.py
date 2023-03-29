import discord
import requests
from decouple import config

api_url = config('API_URL')
apikey = config('API_KEY')

def daily_update(date):
    taday_events = []
    countryCode = 'MX'
    cityCode = '404'
    endDateTime=date+'T00:00:00Z'
    
    url = f'{api_url}countryCode={countryCode}&cityCode={cityCode}&preSaleDateTime={endDateTime}&sort=relevance,desc&apikey={apikey}'
    print(url)
    response = requests.get(url)
    json_response = response.json()
    
    for id, event in enumerate(json_response['_embedded']['events']):
        try:
            eventDescription = event['info']
        except:
            eventDescription = 'Sin descripcion'

        taday_events.append(
            make_event_embed(
                eventTitle = event['name'], 
                eventDescription = eventDescription, 
                eventPic = event['images'][0]['url'],
                eventLink = event ['url']
            )
        )
    
    return taday_events

def make_event_embed(eventTitle = None, eventDescription = None, eventPic = None, eventLink = None):
  embed = discord.Embed(
    title = eventTitle,
    description = eventDescription,
    color=discord.Color.gold()
  )
  embed.set_thumbnail(url=eventPic)
  embed.add_field(name = 'Event link', value = eventLink)

  return embed