import string
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

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

# macierz term-dokument C

C = np.zeros((len(vocabulary), len(docs_tokens)), dtype=int)

for doc_idx, tokens in enumerate(docs_tokens):
    for token in tokens:
        if token in vocabulary:
            token_idx = vocabulary.index(token)
            C[token_idx, doc_idx] = 1

# dekompozycja macierzy C wg SVD

U, s, Vt = np.linalg.svd(C, full_matrices=False)

# aproksymacja rzędu k

Uk = U[:, :k]
Sk = np.diag(s[:k])
VkT = Vt[:k, :]

# macierz której kolumny są wektorami dokumentów w zredukowanej przestrzeni

Ck = Sk.dot(VkT)

# wektor zapytania

q = np.zeros(len(vocabulary), dtype=int)

for token in zap_tokens:
    if token in vocabulary:
        token_idx = vocabulary.index(token)
        q[token_idx] = 1

# wektor zapytania w zredukowanej przestrzeni

Sk1 = np.linalg.inv(Sk)
qk = Sk1.dot(Uk.T.dot(q))

# podobieństwo zapytania do każdego z dokumentów wg miary cosinusa

similarities = cosine_similarity(qk.reshape(1, -1), Ck.T)
rounded = np.round(similarities, decimals=2)
result = rounded.tolist()[0]
print(result)