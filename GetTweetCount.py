__author__ = 'Judah'

import tweepy, sys
from tweepy import OAuthHandler
from TwitterScraper import TwitterSearchImpl

returnsOnlyCurrentTweets = True;

def isToday(inString):
    if not returnsOnlyCurrentTweets:
        return True
    timePeriodString = filter(lambda x: x.isalpha(), inString)
    if ('ago' in timePeriodString) or 'min' == timePeriodString or ('s'  == timePeriodString) or ('hr' == timePeriodString):
        return True
    else:
        return False


consumer_key = 'sG80wN7mOwn8UD9d1sTNVQK21'
consumer_secret = 'TkIFgdvvgQm3slBCJ0C8GmexPTj33BjVprGRxdz4M9eEy7Hecd'
ACCESS_TOKEN = '2328132828-Iq2HAjtq4xAChtkfjrU7wPj5Yeb5uR7OFZRfjru'
ACCESS_TOKEN_SECRET = '6rNv9zzq6XW383IXe3XqZkqdajgfFjKKDtQ4v0THZgN7v'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitterAPI = tweepy.API(auth)

twit = TwitterSearchImpl(0, 5, 20)


def getTweetCount(name):

    genericListOfWords = getListOfGenericWords()
    nameArray = getNameArray(name, genericListOfWords)

    #print genericListOfWords
    print nameArray

    ####### Gets 20 tweets from name
    tweets = findInitialTweets(nameArray)
    seenHashTags = set()
    seenTweetIds = set()
    #######

    print "\n\n\nTweet Count: " + str(len(tweets)) + "\n\n\n"

    print "\n\n\nTweets: " + str(tweets) + "\n\n\n"

    # print "\n\n\nTweets: "
    # for tweet in tweets:
    #     print str(tweet['text'])
    # print "\n\n\n"

    for tweet in tweets:

        ###### Adds tweet id if not already seen else continues to next tweet
        if (tweet['tweet_id'] not in seenTweetIds) and isToday(tweet['created_at']):
            print "Tweet Checked with ID " + str(tweet['tweet_id'])
            seenTweetIds.add(tweet['tweet_id'])
        else:
            print "Tweet Continued with ID " + str(tweet['tweet_id']) + " is today = " + str(isToday(tweet['created_at']))
            continue
        ######


        for hashtag in tweet['hashtags']:
            print "\nOn hashtag: " + hashtag + "\n"
            if (hashtag not in seenHashTags) and shouldHashTagBeUsed(hashtag, nameArray):
                ###### Adds hashtags if not in seenHas Tags else continues
                seenHashTags.add(hashtag)
                ######
                ###### If hashtag not seen searches it and gets 20 tweets
                liveTwitterSearch = twit.search('#'+ hashtag.encode('utf-8') + ' near:Atlanta')
                tweets2 = twit.getTweets()
                ######
                for tweet2 in tweets2:
                    if (tweet2['tweet_id'] not in seenTweetIds) and isToday(tweet2['created_at']):
                        ##### Adds tweet if not added
                        seenTweetIds.add(tweet2['tweet_id'])
                        #####
                        ##### Traverse hashtags in tweets from hashtags
                        for hashtag2 in tweet2['hashtags']:
                            if (hashtag2 not in seenHashTags) and shouldHashTagBeUsed(hashtag2, nameArray):
                                ###### Get 2nd round of tweets from hash tags
                                seenHashTags.add(hashtag2)
                                liveTwitterSearch = twit.search('#'+ hashtag2.encode('utf-8') + ' near:Atlanta')
                                tweets3 = twit.getTweets()
                                ######
                                for tweet3 in tweets3:
                                    if (tweet3['tweet_id'] not in seenTweetIds) and isToday(tweet3['created_at']):
                                        seenTweetIds.add(tweet3['tweet_id'])
                        #####
                    else:
                        continue
            else:
                continue #Next hashtag

    print seenHashTags
    #print "Has Tags Seen: " + str(seenHashTags)
    return len(seenTweetIds)



def getListOfGenericWords():
    genericListToReturn = []
    with open('words10k.txt', 'r') as f:
        while True:
            line = f.readline()  # Or any other reasonable-sized chunk
            if not line:
                break
            else:
                genericListToReturn.append(line.split("\n")[0])
    return genericListToReturn


def getNameArray(nameString, genericListOfWords):
    nameArrayToReturn = nameString.split(" ")
    for wordOfName in nameArrayToReturn:
        if wordOfName in genericListOfWords:
            nameArrayToReturn.remove(wordOfName)
    return nameArrayToReturn



def shouldHashTagBeUsed(hashtagToCheck, nameArray):
    print "\nChecking hashtag: " + hashtagToCheck + "\n"
    for nameToCheck in nameArray:
        if nameToCheck in hashtagToCheck:
            return True
        else:
            print "hashtag " + hashtagToCheck + " not found"
    return False



def findInitialTweets(nameArray):
    currentNameToQuery = ""
    tweetsToAdd = []
    tweetsToReturn = []

    currentNameToQuery = nameArrayToString(nameArray)
    tweetsToAdd = getArrayOfTweets(currentNameToQuery)
    tweetsToReturn = {key: value for (key, value) in (tweetsToReturn.items() + tweetsToAdd.items())}

    if len(tweetsToReturn) < 20 and len(nameArray) > 3:
        indexOfWordsToSearch = 0
        while len(tweetsToReturn) < 20 and indexOfWordsToSearch < (len(nameArray) - 1):
            newNameArray = []
            newNameArray.append(nameArray[indexOfWordsToSearch])
            newNameArray.append(nameArray[indexOfWordsToSearch+1])
            currentNameToQuery = nameArrayToString(newNameArray)
            tweetsToAdd = getArrayOfTweets(currentNameToQuery)
            tweetsToReturn = {key: value for (key, value) in (tweetsToReturn.items() + tweetsToAdd.items())}
            indexOfWordsToSearch += 2

    return tweetsToReturn


def nameArrayToString(nameArray):
    toReturn = ""
    for nameToAppend in nameArray:
        toReturn = toReturn + nameToAppend + " "
    toReturn = toReturn[:-1]
    return toReturn


def getArrayOfTweets(nameToQuery):
    liveTwitterSearch = twit.search(nameToQuery + ' near:Atlanta')
    tweetsToReturn = twit.getTweets()
    return tweetsToReturn



#getTweetCount('Imagine Music Festival')
#getTweetCount('Growing your Reputation through Social Media')
#getTweetCount('Atlanta Career Fair - April 15, 2016 On-The-Spot Hiring Job Fair')
#print "Twitter Count Returned: " + str(getTweetCount('Delaware North Sportservice- Employee Processing'))
#getTweetCount('Beyonce Georgia Dome')
#getTweetCount('Cirque du Soleil')

#print "Twitter Count Returned: " + str(getTweetCount('Drake'))
#print "Twitter Count Returned: " + str(getTweetCount('Imagine Music Festival'))
print "Twitter Count Returned: " + str(getTweetCount('Beyonce - The Formation World Tour'))






