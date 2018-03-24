from textblob import TextBlob
import tweepy
import csv


consumerKey       = 'ppjgSjqrsbLhNAt03imfwFOCu'
consumerSecret    = '0iuW4QeNTXPlpkMhDRADT5mgOdC1k5X33ksSOX7UbWDfRoAu1H'

accessToken 	  = '908510687953080320-xErnPdMpDKCismryew4VatyGUfovGdF'
accessTokenSecret = 'xuTeteMmUzoitd5XPTmPKQgl7AzhQZvgZZ9OIdH9F1Yfb'

#Authentication
auth = tweepy.OAuthHandler(consumerKey, consumerSecret )
auth.set_access_token(accessToken,accessTokenSecret)

#Get the twitter API
api = tweepy.API(auth)

#Searching for tweets that contains 'trump' on it
public_tweets = api.search('trump')

#"w" indicates that you're writing strings to the file
csv = open('twitterSentimentAnalysisResult.csv', "w") 

columnTitleRow = "tweet, sentiment\n"
csv.write(columnTitleRow)

for tweet in public_tweets:
	tweetAnalysis = TextBlob(tweet.text)#converting the tweet to a textblob for analyzing it
	polarity = tweetAnalysis.sentiment.polarity#returns sentiment value between -1 and 1
	if(polarity<0):#Negatif sentiment on the tweet
		row=tweet.text + " , Negatif\n"
		csv.write(row)
	elif(polarity==0):
		row= tweet.text + " , Neutral\n"
		csv.write(row)
	else:#Positif sentiment on the tweet 
		row=tweet.text + " , Positif\n"
		csv.write(row)
	