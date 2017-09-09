import bleach

def linkify(text):
    text = bleach.clean(text, tags=[], attributes={}, styles=[], strip=True)
    return bleach.linkify(text)



