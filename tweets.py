import tweepy
import csv
import pandas as pd
import sys
import configparser

config = configparser.ConfigParser()
config.sections()
config.read('tweets.conf')
print ('API KEY: '+config ['API']['consumer_key']+'\n'
       +'API secret: '+config ['API']['consumer_secret']+'\n'
       +'Access token: '+config ['API']['access_token']+'\n'
       +'Access secret: '+config ['API']['access_token_secret'])


auth = tweepy.OAuthHandler(config ['API']['consumer_key'], config ['API']['consumer_secret'])
auth.set_access_token(config ['API']['access_token'], config ['API']['access_token_secret'])
api = tweepy.API(auth,wait_on_rate_limit=True)


#####buscar por hashtag
# Open/Create a file to append data
def TweetSearch( string ):
    csvFile = open(string+'.csv', 'w+')
    
    #Use csv Writer
    csvWriter = csv.writer(csvFile)

    #Precisa regular os contadores e os itens em conjunto
    for tweet in tweepy.Cursor(api.search,q=string,result_type="mixed",count=100).items(100):
        #print (tweet.geo, tweet.created_at, tweet.text, tweet.user.screen_name)
        #print (tweet)
    
        csvWriter.writerow(["@"+tweet.user.screen_name,tweet.user.followers_count,tweet.geo,tweet.created_at,tweet.text.encode('utf-8')])
    #break
    return;

#print (sys.argv[1])
#TweetSearch (sys.argv[1])

#webserver

from bottle import route, run, template
@route('/')
@route('/a/<name>')
def index(name):
    return template('<b>Retorno de todos os tweets com a referencia {{name}}</b>!', name=name)

run(host='localhost', port=8080)
