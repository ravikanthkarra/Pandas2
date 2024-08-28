import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]
    df = sorted(df['author_id'].unique())
    return pd.DataFrame(df, columns = ['id'])

