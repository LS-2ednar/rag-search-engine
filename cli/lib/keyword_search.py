from .search_utils import DEFAULT_SEARCH_LIMIT, load_movies, load_stopwords, text_preprocessing
from nltk.stem import PorterStemmer
from .invertedindex import InvertedIndex

def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    stopwords = load_stopwords()
    results = []
    stemmer = PorterStemmer()
    for movie in movies:
        if len(results) >= limit:
            break
        movie_token = [stemmer.stem(token) for token in text_preprocessing(movie["title"]) if token not in stopwords]
        for q_token in [stemmer.stem(token) for token in text_preprocessing(query) if token not in stopwords]:
            for m_token in movie_token:
                if q_token in m_token:
                    if movie not in results:
                        results.append(movie)

    return results