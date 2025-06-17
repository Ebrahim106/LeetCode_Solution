import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['viewer_id']==views['author_id']].sort_values('author_id',ascending=True)
    df = df['author_id'].unique()
    result = pd.DataFrame({'id':df})
    return result