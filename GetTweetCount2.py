__author__ = 'Judah'

import tweepy, sys
from tweepy import OAuthHandler
from TwitterScraper import TwitterSearchImpl

def isToday(inString):
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
    liveTwitterSearch = twit.search(name + ' near:Atlanta')
    tweets = twit.getTweets()
    seenHashTags = set()
    seenTweetIds = set()
    #######
    print "Tweet Length", len(tweets)

    layorOneIterator = 0
    while layorOneIterator < len(tweets):
        print "Loop ", layorOneIterator
        tweetLayorOne = tweets[layorOneIterator]
        layorOneIterator += 1

        if (tweetLayorOne['tweet_id'] not in seenTweetIds) and isToday(tweetLayorOne['created_at']):
             print "Checking Tweet with ID: " + str(tweetLayorOne['tweet_id'])
             seenTweetIds.add(tweetLayorOne['tweet_id'])
        else:
             print "Continued/Skipped Tweet with ID: " + str(tweetLayorOne['tweet_id'])
             continue



    #print "Tweets: " + str(tweets)

    # for tweet in tweets:

    #     ###### Adds tweet id if not already seen else continues to next tweet
    #     if (tweet['tweet_id'] not in seenTweetIds) and isToday(tweet['created_at']):
    #         print "TweetChecked"
    #         seenTweetIds.add(tweet['tweet_id'])
    #     else:
    #         print "Continued"
    #         continue
    #     ######


    #     for hashtag in tweet['hashtags']:
    #         print "\nOn hashtag: " + hashtagToCheck + "\n"
    #         if (hashtag not in seenHashTags) and shouldHashTagBeUsed(hashtag, nameArray):
    #             ###### Adds hashtags if not in seenHas Tags else continues
    #             seenHashTags.add(hashtag)
    #             ######
    #             ###### If hashtag not seen searches it and gets 20 tweets
    #             liveTwitterSearch = twit.search('#'+ hashtag.encode('utf-8') + ' near:Atlanta')
    #             tweets2 = twit.getTweets()
    #             ######
    #             for tweet2 in tweets2:
    #                 if (tweet2['tweet_id'] not in seenTweetIds) and isToday(tweet2['created_at']):
    #                     ##### Adds tweet if not added
    #                     seenTweetIds.add(tweet2['tweet_id'])
    #                     #####
    #                     ##### Traverse hashtags in tweets from hashtags
    #                     for hashtag2 in tweet2['hashtags']:
    #                         if (hashtag2 not in seenHashTags) and shouldHashTagBeUsed(hashtag2, nameArray):
    #                             ###### Get 2nd round of tweets from hash tags
    #                             seenHashTags.add(hashtag2)
    #                             liveTwitterSearch = twit.search('#'+ hashtag2.encode('utf-8') + ' near:Atlanta')
    #                             tweets3 = twit.getTweets()
    #                             ######
    #                             for tweet3 in tweets3:
    #                                 if (tweet3['tweet_id'] not in seenTweetIds) and isToday(tweet3['created_at']):
    #                                     seenTweetIds.add(tweet3['tweet_id'])
    #                     #####
    #                 else:
    #                     continue
    #         else:
    #             continue #Next hashtag

    #print len(seenTweetIds)
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
        if nameToCheck.lower() in hashtagToCheck.lower():
            return True
        else:
            print "hashtag " + hashtagToCheck + " not found"
    return False


# def trace(frame, event, arg):
#     print "%s, %s:%d" % (event, frame.f_code.co_filename, frame.f_lineno)
#     return trace

# sys.settrace(trace)
getTweetCount('Imagine Music Festival')
#getTweetCount('Beyonce Georgia Dome')
#getTweetCount('Cirque du Soleil')






