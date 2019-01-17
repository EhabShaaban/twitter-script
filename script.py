import tweepy
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener

consumer_key="MOx8bFSO4gQe5GW5TpW6YaikA"
consumer_secret="8UZruw1DC0FymDescsunsy3JR4un3399EgQgPwc1YSSq2dp3ZP"
access_token="901277118654500869-0snVPTIoOWxET9ozBo8ukHNW7hCGyiq"
access_token_secret="Gyb5ie2D2B2dlQx0yK7keR45KiiDeWP7bpNq6PeoG6Bl5"

class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token , access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,
wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60)

twitterstream = Stream(auth, StdOutListener())
#twitterstream.filter(track=["car"])
#827002120373207040
user = api.get_user(827002120373207040)
print(user.screen_name)