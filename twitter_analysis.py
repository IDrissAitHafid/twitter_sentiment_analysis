from textblob import TextBlob
import tweepy

consumerKey       = 'ppjgSjqrsbLhNAt03imfwFOCu'
consumerSecret    = '0iuW4QeNTXPlpkMhDRADT5mgOdC1k5X33ksSOX7UbWDfRoAu1H'

accessToken 	  = '908510687953080320-xErnPdMpDKCismryew4VatyGUfovGdF'
accessTokenSecret = 'xuTeteMmUzoitd5XPTmPKQgl7AzhQZvgZZ9OIdH9F1Yfb'

#Authentication
auth = tweepy.OAuthHandler(consumerKey, consumerSecret )
auth.set_access_token(accessToken,accessTokenSecret)

#Get the twitter API
api = tweepy.API(auth)

public_tweets = api.search('trump')
polarityScore = 0
i=0
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	polarityScore+= analysis.sentiment.polarity
	i+=1


print("the average polarity of trump: ")
print(polarityScore/i)