import pandas as pd
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # Filter tweets where content length > 15 and select tweet_id and content
    df = tweets[tweets['content'].str.len() > 15][['tweet_id']]
    return df