# ==============================
# ZOMATO / SWIGGY REVIEW ANALYZER
# ==============================

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob

print("======================================")
print("   ZOMATO / SWIGGY REVIEW ANALYZER")
print("======================================\n")

# ---------------------------------
# SAMPLE REVIEW
# ---------------------------------
review = "The biryani was amazing and arrived hot. Service was quick. But packaging could be better. Will definitely order again!"

# ---------------------------------
# STEP 1: TOKENIZATION
# ---------------------------------
print("1. TOKENIZATION")
print("------------------------------")

words = word_tokenize(review)
sentences = sent_tokenize(review)

print("Original Review:")
print(review)
print()

print("Total Words:", len(words))
print("Total Sentences:", len(sentences))
print()

print("Words:", words)
print()

print("Sentences:")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}. {sentence}")

print("\n")

# ---------------------------------
# STEP 2: STOP WORD REMOVAL
# ---------------------------------
print("2. STOP WORD REMOVAL")
print("------------------------------")

stop_words = set(stopwords.words("english"))

tokens = word_tokenize(review.lower())
cleaned = [word for word in tokens if word.isalpha() and word not in stop_words]

print("Original Tokens:")
print(tokens)
print()

print("Cleaned Tokens:")
print(cleaned)

print("\n")

# ---------------------------------
# STEP 3: SENTIMENT ANALYSIS
# ---------------------------------
print("3. SENTIMENT ANALYSIS")
print("------------------------------")

reviews = [
    "Paneer butter masala was outstanding! Hot food, fast delivery. 5 stars!",
    "Ordered biryani but got fried rice. Very disappointing. Cold food.",
    "Food was okay. Delivery took usual time. Nothing special.",
    "Best chole bhature in Bengaluru! Packaging excellent, quantity good."
]

for i, text in enumerate(reviews, 1):
    score = TextBlob(text).sentiment.polarity

    if score > 0.2:
        mood = "POSITIVE 😊"
    elif score < -0.1:
        mood = "NEGATIVE 😡"
    else:
        mood = "NEUTRAL 😐"

    print(f"Review {i}: {mood}")
    print(f"Score: {score:.2f}")
    print(f"Text: {text}")
    print("-" * 50)