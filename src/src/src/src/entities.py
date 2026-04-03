import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)

    names = []
    dates = []
    orgs = []
    amounts = []

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            names.append(ent.text)
        elif ent.label_ == "DATE":
            dates.append(ent.text)
        elif ent.label_ == "ORG":
            orgs.append(ent.text)
        elif ent.label_ == "GPE":
            orgs.append(ent.text)

    # Money regex
    amounts += re.findall(r'₹\s?\d+(?:,\d+)*(?:\.\d+)?', text)
    amounts += re.findall(r'\$\s?\d+(?:,\d+)*(?:\.\d+)?', text)

    return {
        "names": list(set(names)),
        "dates": list(set(dates)),
        "organizations": list(set(orgs)),
        "amounts": list(set(amounts))
    }
