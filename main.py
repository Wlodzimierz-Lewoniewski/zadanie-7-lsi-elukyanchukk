import string

n_docs = int(input("Liczba dokumentów do przetworzenia: "))

docs_tokens = []

for n in range(n_docs): 
    doc = input(f"Dokument {n+1}: ").strip().lower()
    doc = doc.translate(str.maketrans('', '', string.punctuation))
    doc_tokens = doc.split()
    docs_tokens.append(doc_tokens)

zapytanie = input("Zapytanie: ").strip().lower()
zap_tokens = zapytanie.split()

k = int(input("Liczba wymiarów po zredukowaniu: "))

vocabulary = sorted(set(word for doc_tokens in docs_tokens for word in doc_tokens))

print(vocabulary)
