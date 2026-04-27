import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from embedding import get_embedding

 

 

def build_user_vector(skills):

    if not skills:

        return get_embedding("general")

 

    vectors = [get_embedding(skill) for skill in skills]

    return np.mean(vectors, axis=0)

 

 

def recommend_courses(user_skills, course_rows, top_n=3):

 

    user_vector = build_user_vector(user_skills)

 

    course_vectors = []

    course_titles = []

 

    for row in course_rows:

        text = f"{row.title} {row.description}"

        course_titles.append(row.title)

        course_vectors.append(get_embedding(text))

 

    scores = cosine_similarity([user_vector], course_vectors)[0]

 

    ranked = np.argsort(scores)[::-1]

 

    results = []

 

    for i in ranked[:top_n]:

        results.append({

            "course": course_titles[i],

            "score": float(scores[i]),

            "explanation": "Matched using semantic similarity between user skills and course content"

        })

 

    return results