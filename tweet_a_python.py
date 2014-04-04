'''
Created on Apr 4, 2014

@author: bonino
'''

import twitter, tts, urllib

def getTweets():
    tweets = {}
    # get access to apis
    api = twitter.Api(consumer_key='wIDHvofdfV2QO94s1bjebQ', 
                      consumer_secret='nO0q0Ko8EBQ6Lb8FNLwEsT3r2QLkjWsO02dr9uegU', 
                      access_token_key='2408639030-691GXH8B4aQt2JgXN05uSkWAJyywmds6OeLCaI4', 
                      access_token_secret='I7lxOY8wSBf0bKlWKJ5UlI3tVRoSaYUeiUseRLo9VBoky')
    #get the user followers
    users = api.GetFollowers()
    #iterate over followers
    for user in users:
        #prepare an array of statuses for each follower
        tweets[user.name] = []
        i=1
        #fill statuses
        for status in api.GetUserTimeline(user.id):
            tweets[user.name].append(status.text)
            i+=1
            if(i>2):
                break
    return tweets

def sayTweets(tweets = None):
    '''Says tweets
    Args:
        tweets: the dictionary containing the tweets to read, keys represent the follower name, values are arrays of statuses
    '''
    if(tweets!=None):
        #iterate over the dictionary keys
        for key in tweets.keys():
            #say the tweet author at first
            tts.say('Tweet from %s'%key, 'en')
            #iterate over tweets
            for tweet in tweets[key]:
                #encode the tweet text to be suitable for urls
                tweet_text =  urllib.urlencode({'text':tweet})
                #cut-off "text:"
                tweet_text = tweet_text[5:]
                #read the status text
                tts.say(tweet_text,'it')
            

if __name__ == '__main__':
    #fetch tweets
    tweets = getTweets()
    #read tweets
    sayTweets(tweets)
