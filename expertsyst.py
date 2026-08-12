import re
def get_genre_keywords():
    return{
    "mystery":["mystery","detective","crime","murder","spy","suspense","secret","unknown","tension","thriller","conspiracy","twist"],
    "romance":["romance","love story","romantic","love","chemistry","friends-to-lover","slow burn","opposite attract","yearn","yearning","joy","happiness","happy ending","hope","peace"],
    "fantasy":["fantasy","magic","dragons","wizard","mythical","kingdom","unicorn","queen","king","prince","princess","knight","quest","journey"],
    "sci-fi":["sci-fi","science","fiction","space","future","alien","technology","innovation","innovative","planet","galaxy","universe","asteriod","robot","spaceship","dimension","hacker","AI"],
    "horror":["horror","scary","ghost","haunted","creepy","terror","fear","curse","nightmare","demon","haunting","devil","vampire","zombie","phantom"],
}
def detect_genre(text:str):
    text=text.lower()
    genre_keywords=get_genre_keywords()
    for genre, keywords in genre_keywords.items():
        if any(kw in text for kw in keywords):
            return genre
    return None
def detect_author(text:str):
    pattern=r"(?:by|written by)\s+([A-Z][a-zA-Z.\s]+)"
    match=re.search(pattern,text)
    if match:
        name=match.group(1).strip()
        name=re.split(r"\s+(?:please|book|novel)\b",name, flags=re.IGNORECASE)[0]
        return name.strip()
    return None
def extract_conditions(text:str)->dict:
    return{
        "genre":detect_genre(text),
        "author":detect_author(text),
        "raw_text":text,
    }
if __name__=="__main__":
    test_inputs=[
        "I want a mystery book",
        "Give me something by Stephen King",
        "I feel like reading a scary horror story",
        "Recommend a sci-fi book by Isaac Asimov please",
        "Just give me any book",
    ]
    for t in test_inputs:
        print("INPUT:",t)
        print("OUTPUT:",extract_conditions(t))
        print()