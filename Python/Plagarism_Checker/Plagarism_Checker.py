from numpy import vectorize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os # ===== all the libraries =======

# ======= defining two files for checking =======
student_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
student_notes = [open(File).read() for File in student_files]
# === getting values for texts============
vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

vectors = vectorize(student_notes)
s_vectors = list(zip(student_files, vectors))

# ======-function for checking two text files ======
def check_plagarism():
    plagarism_results = set()
    global s_vectors
    for student_a, text_vector_a in s_vectors:
        # ====== copying the texts =====
        new_vectors = s_vectors.copy()
        # === indexes for vectors_a and students =====
        curr_index = new_vectors.index((student_a, text_vector_a))
        del new_vectors[curr_index]
        for student_b, text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((student_a, student_b))
            score = (student_pair[0], student_pair[1], sim_score)
            plagarism_results.add(score)
    return plagarism_results

# === checking the data ===========
for data in check_plagarism():
    print(data)