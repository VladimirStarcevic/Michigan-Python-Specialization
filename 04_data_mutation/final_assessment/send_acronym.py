stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

sent_list = sent.split()
acro_parts = []

for word in sent_list:
    if word.lower() not in stopwords:
        acro_parts.append(word[:2].upper())

acro = ". ".join(acro_parts)

print(f"Acronym: {acro}")