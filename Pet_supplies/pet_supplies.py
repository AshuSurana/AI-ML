import json
import random

# Step 1: Load the JSON file line by line
reviews = []
try:
    with open('./data/Pet_Supplies.json', 'r') as file:
        for line in file:
            try:
                review = json.loads(line.strip())
                reviews.append(review)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON on line: {line.strip()} - {e}")
except FileNotFoundError:
    print("The file pet_supplies.json was not found.")
    exit(1)

# Step 2: Select the specified number of reviews (between 100 and 1000)
num_reviews = random.randint(100, min(1000, len(reviews)))

# Step 3: Extract the reviewText and rating fields
selected_reviews = []
for item in reviews[:num_reviews]:
    if 'reviewText' in item and 'overall' in item:
        selected_reviews.append({
            'reviewText': item['reviewText'],
            'overall': item['overall']
        })

# Step 4: Save the extracted reviews to a new JSON file
with open('./data/pet_supplies_new.json', 'w') as outfile:
    json.dump(selected_reviews, outfile, indent=4)

print(f'Successfully extracted {len(selected_reviews)} reviews to pet_supplies_new.json')
