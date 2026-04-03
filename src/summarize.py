from textblob import TextBlob

def summarize_text(text):
    sentences = text.split('.')
    if len(sentences) > 3:
        return sentences[0] + "." + sentences[1] + "." + sentences[2]
    return text
