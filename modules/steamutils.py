import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .decorators import cache

# https://www.kaggle.com/code/fetenbasak/content-based-recommendation-game-recommender

def get_recommendations(appName):
    df = pd.read_csv('steam_games_dataset_kaggle.csv')
    df1 = df[['name', 'desc_snippet', 'popular_tags', 'genre', 'original_price']]
    df2 = pd.DataFrame(df1.dropna())

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df2['desc_snippet'])
    tfidf_matrix.toarray()

    cosine_sim = cosine_similarity(tfidf_matrix,
                                   tfidf_matrix)

    indices = pd.Series(df2.index, index=df2['name'])
    indices.index.value_counts()
    indices = indices[~indices.index.duplicated(keep='last')]
    
    indices = pd.Series(df2.index, index=df2['name'])
    indices = indices[~indices.index.duplicated(keep='last')]
    game_index = indices[appName]
    similarity_scores = pd.DataFrame(cosine_sim[game_index], columns=['score'])
    game_indices = similarity_scores.sort_values("score", ascending=False)[1:11].index
    return df2['name'].iloc[game_indices].tolist()