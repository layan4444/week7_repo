import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from embedding import get_embedding


def build_user_vector(skills):
   if not skills:
       return get_embedding("general")

   vectors = [get_embedding(skill) for skill in skills]
   return np.mean(vectors, axis=0)


def recommend_courses(user_skills, course_rows, top_n=3, min_score=0.45):
   user_vector = build_user_vector(user_skills)

   course_vectors = []
   course_list = []

   for row in course_rows:
       course = row._mapping

       title = course["title"]
       description = course["description"]

       text = f"{title} {description}"

       course_vectors.append(get_embedding(text))
       course_list.append({
           "title": title,
           "description": description
       })

   if not course_vectors:
       return []

   scores = cosine_similarity([user_vector], course_vectors)[0]

   ranked = sorted(
       zip(course_list, scores),
       key=lambda x: x[1],
       reverse=True
   )

   filtered = [
       course for course, score in ranked
       if score >= min_score
   ]

   return filtered[:top_n]