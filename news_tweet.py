from newsapi import NewsApiClient
import time
import tweepy as tw
from datetime import datetime, timedelta
import pyshorteners

consumer_key= ''
consumer_secret= ''
access_token= ''
access_token_secret= ''

t_now = datetime.now()
to_time =t_now
from_time  = t_now-timedelta(hours=10, minutes=0)
to_time = to_time.strftime("%Y")+"-"+to_time.strftime("%m")+'-'+to_time.strftime("%d")+"T"+to_time.strftime("%X")
from_time = from_time.strftime("%Y")+"-"+from_time.strftime("%m")+'-'+from_time.strftime("%d")+"T"+from_time.strftime("%X")
newsapi = NewsApiClient(api_key='')
type_tiny = pyshorteners.Shortener()
while True:
    top_headlines = newsapi.get_everything(q='artificial intelligence',from_param=from_time,to=to_time,language='en')
    print(top_headlines['totalResults'])
    art = top_headlines['articles']   
    print(len(art)) 
    for i in range(len(art)):        
        img_url = art[i]['urlToImage']       
        short_url = type_tiny.tinyurl.short((art[i]['url'])) 
        text = (art[i]['title'])+"     "+(art[i]['source']['name'])+"      Link: "+short_url+" #artificialintelligence #technology #technews"
        print(text)     
        if (len(text)<275):
            auth = tw.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tw.API(auth, wait_on_rate_limit=True)
            api.update_status(text)   
        time_sleep = int(36000 / len(art))+1
        time.sleep(1)