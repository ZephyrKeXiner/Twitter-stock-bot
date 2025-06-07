import tweepy
from utils.config import Config

class TwitterService:
    def __init__(self):
        config = Config()
        self.client = tweepy.Client(
            consumer_key=config.API_KEY,
            consumer_secret=config.API_SECRET,
            access_token=config.ACCESS_TOKEN,
            access_token_secret=config.ACCESS_TOKEN_SECRET
        )

    def post_tweet(self, text, in_reply_to_tweet_id=None):
        try:
            return self.client.create_tweet(text=text, in_reply_to_tweet_id=in_reply_to_tweet_id)
        except tweepy.TweepyException as e:
            raise Exception(f"❗ 推文失败: {e}")

    def verify_credentials(self):
        try:
            user = self.client.get_me()
            return f"✅ API 凭据有效，当前用户: {user.data['username']}"
        except tweepy.TweepyException as e:
            raise Exception(f"❗ API 凭据验证失败: {e}")
