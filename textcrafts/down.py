import nltk
import ssl

def ensure_nlk_downloads() :
  try:
    _create_unverified_https_context = ssl._create_unverified_context
  except AttributeError:
    pass
  else:
    ssl._create_default_https_context = _create_unverified_https_context

  nltk.download('words')
  nltk.download('wordnet')
  nltk.download('stopwords')

ensure_nlk_downloads()
