# importing the module
import tweepy
 
# personal details
consumer_key ="zsf1BdhbkeZNjGxfmJz1yjB5w"
consumer_secret ="ytMoDAIEDSMEysbmfNxbbGLwG3G0TfCTdAqGokzSdqLQR4MmeI"
access_token ="963448461436665856-YzSaFCzyVG1fkyBvj9ik07WClEU1E3Y"
access_token_secret ="iJsFS6ybcggWkvj4oBqjJ9OEOeYKFM9kZCX8GspKaR02w"

 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="Hello Everyone !")
