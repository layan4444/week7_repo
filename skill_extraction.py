from embedding import get_embedding

import numpy as np

 


SKILL_BANK = [

    "python", "machine learning", "deep learning",

    "data analysis", "sql", "web development",

    "backend development", "ai", "nlp"

]
                                 
 

 

def extract_skills(text):

    text_vector = get_embedding(text)

 

    extracted = []

 

    for skill in SKILL_BANK:

        skill_vector = get_embedding(skill)

 

        similarity = np.dot(text_vector, skill_vector) / (

            np.linalg.norm(text_vector) * np.linalg.norm(skill_vector)

        )

 

        if similarity > 0.4:  
            extracted.append(skill)

 

    return extracted