stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

og_list = org.split()
acro = ""

for element in og_list:
    if element.lower() not in stopwords:
        acro += element[0].upper()
print(f"Acro of original string: {acro}")

