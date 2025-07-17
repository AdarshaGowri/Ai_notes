##Classification problem , Comments on product is a positive ot negative product
from nltk.stem import PorterStemmer
stemming = PorterStemmer()
words = words = [
    # Positive stems
    "taste", "tasteless" , "delic", "delicious","flavor", "amaz", "excell", "love", "enjoy", "perfect",
    "crisp", "fresh", "juici", "yum", "satisfi", "great", "sweet", "rich",
    "mouthwater", "aromat", "tender", "beauti", "pleas", "favourit",

    # Negative stems
    "bland", "bad", "horribl", "disappoint", "unpleas", "stale", "worst",
    "overcook", "undercook", "greasi", "soggi", "hard", "cold", "tasteless",
    "burn", "raw", "unhappi", "salt", "too", "unflavor", "distast"
]

for word in words:
    print(word + "---->"+stemming.stem(word))

from nltk.stem import SnowballStemmer