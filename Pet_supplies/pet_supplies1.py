import json
import random
import contractions
import re
from string import punctuation

def clean_text(text):
    # remove contractions
    text=contractions.fix(text)

    # make lowercase
    text=text.lower()

    # remove punctuations
    text=re.sub('[%s]'%re.escape(punctuation),'',text)

    # remove numbers
    text = re.sub(r'\w*\d\w*', '', text)

    # remove stopwords
    stopword=[stopword.strip()for stopword in open('./data/stopword_en.txt','r')]

    # return string
    return ' '.join([word for word in text.split() if word not in stopword])

try:
    with open('./data/pet_supplies_new.json', 'r') as file:
        reviews = json.load(file)
except FileNotFoundError:
    print("The file selected_reviews.json was not found.")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    exit(1)

# Step 2: Clean the reviewText fields
'''for review in reviews:
    if 'reviewText' in review:
        review['reviewText'] = clean_text(review['reviewText'])'''
cleaned_reviews = []
for review in reviews:
    cleaned_review_text = clean_text(review['reviewText'])
    cleaned_reviews.append({
        'clean reviewText': cleaned_review_text,
        'Score': review['overall']
    })

# Step 3: Print the cleaned reviewText and the rating
'''for review in reviews:
    #print(f"Rating: {review['rating']}")
    print(f"Cleaned Review: {review['reviewText']}")
    print("-" * 50)'''

# Step 3: Save the cleaned reviews to a new JSON file
with open('./data/cleaned_reviews.json', 'w') as outfile:
    json.dump(cleaned_reviews, outfile, indent=4)

print(f'Successfully cleaned and saved {len(cleaned_reviews)} reviews to cleaned_reviews.json')



    