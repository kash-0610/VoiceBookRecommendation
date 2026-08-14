import re
from database import BOOK_DATABASE


def get_genre_keywords():
    return {
        "mystery": [
            "mystery", "detective", "crime", "murder", "spy",
            "suspense", "secret", "thriller", "twist"
        ],
        "romance": [
            "romance", "love story", "romantic", "love",
            "chemistry", "slow burn", "happy ending", "heartbreak"
        ],
        "fantasy": [
            "fantasy", "magic", "dragons", "wizard", "mythical",
            "kingdom", "quest", "journey"
        ],
        "sci-fi": [
            "sci-fi", "science fiction", "space", "future", "alien",
            "technology", "robot", "galaxy", "planet", "cyberpunk"
        ],
        "horror": [
            "horror", "scary", "ghost", "haunted", "creepy",
            "terror", "fear", "curse", "demon", "vampire"
        ],
    }


def detect_genre(text: str):
    text = text.lower()
    genre_keywords = get_genre_keywords()

    for genre, keywords in genre_keywords.items():
        if any(keyword in text for keyword in keywords):
            return genre

    return None


def detect_author(text: str):
    pattern = r"(?:by|written by)\s+([A-Z][a-zA-Z.\s]+)"
    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        name = match.group(1).strip()

        # Remove common words that may accidentally be captured
        name = re.split(
            r"\s+(?:please|book|novel|recommend|recommendation)\b",
            name,
            flags=re.IGNORECASE
        )[0]

        return name.strip().lower()

    return None


def get_recommendation(user_query: str) -> dict:
    """
    Analyzes the user query and matches it with books from BOOK_DATABASE.
    """

    if not user_query:
        return {
            "title": "N/A",
            "author": "N/A",
            "genre": "N/A",
            "reason": "No query provided."
        }

    genre = detect_genre(user_query)
    author = detect_author(user_query)

    # 1. Search database for a match by author
    if author:
        for book in BOOK_DATABASE:
            if author in book["author"].lower():
                return book

    # 2. Search database for a match by genre
    if genre:
        for book in BOOK_DATABASE:
            if book["genre"] == genre:
                return book

    # 3. Default fallback recommendation if no direct match is found
    return {
        "title": "Project Hail Mary",
        "author": "Andy Weir",
        "genre": "sci-fi",
        "reason": (
            "No direct match was found for your specific keywords, "
            "but this is a top-rated general recommendation!"
        )
    }