
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json 
import twitter_credentials
 

class TwitterStream():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(languages=["en"], track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tweet = json.dumps(data, ensure_ascii=False)
		tf.write(data)
#		tweet = json.loads(data)
#      	    with open('your_data.json', 'a') as my_file:
#                json.dump(tweet, my_file)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)

 
if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ["Soccer","us","politics","WWE","."]
    fetched_tweets_filename = "harsha_tweets.json"

    twitter_streamer = TwitterStream()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
