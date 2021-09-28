from math import radians, sin, cos, asin, sqrt
import matplotlib.pyplot as plt
import seaborn as sns

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import unidecode


def haversine_distance(lon1, lat1, lon2, lat2):
    """
    Compute distance between two pairs of (lat, lng)
    See - (https://en.wikipedia.org/wiki/Haversine_formula)
    """
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return 2 * 6371 * asin(sqrt(a))


def return_significative_coef(model):
    """
    Returns p_value, lower and upper bound coefficients
    from a statsmodels object.
    """
    # Extract p_values
    p_values = model.pvalues.reset_index()
    p_values.columns = ['variable', 'p_value']

    # Extract coef_int
    coef = model.params.reset_index()
    coef.columns = ['variable', 'coef']
    return p_values.merge(coef,
                          on='variable')\
                   .query("p_value<0.05").sort_values(by='coef',
                                                      ascending=False)

def plot_kde_plot(df, variable, dimension):
    """
    Plot a side by side kdeplot for `variable`, split
    by `dimension`.
    """
    g = sns.FacetGrid(df,
                      hue=dimension,
                      col=dimension)
    g.map(sns.kdeplot, variable)


def clean(text):

    for punctuation in string.punctuation:
        text = text.replace(punctuation, ' ')  # Remove Punctuation

    lowercased = text.lower()  # Lower Case

    unaccented_string = unidecode.unidecode(lowercased)  # remove accents

    tokenized = word_tokenize(unaccented_string)  # Tokenize

    words_only = [word for word in tokenized
                  if word.isalpha()]  # Remove numbers

    stop_words = set(stopwords.words('portuguese'))  # Make stopword list

    without_stopwords = [
        word for word in words_only if not word in stop_words
    ]  # Remove Stop Words

    return " ".join(without_stopwords)
