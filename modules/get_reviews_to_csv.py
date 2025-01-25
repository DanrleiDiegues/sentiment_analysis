import os
import csv

file_path = "data_reviews/reviews.csv"

def save_reviews_to_csv(commentary, review_data, file_path=file_path):
    # Check if the file exists
    file_exists = os.path.isfile(file_path)

    # Open the file in append mode
    with open(file_path, mode="a", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["commentary", "entity", "sentiment_score", "sentiment_magnitude", "salience", "category"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write headers if the file is new
        if not file_exists:
            writer.writeheader()

        # Write review data
        for review in review_data:
            review_with_commentary = {"commentary": commentary}
            review_with_commentary.update(review)
            writer.writerow(review_with_commentary)

# Example Usage
if __name__ == "__main__":
    
    commentary = "The food and music were great!"
    
    review_data = [
        {
            "entity": "food",
            "sentiment_score": 0.9,
            "sentiment_magnitude": 0.9,
            "salience": 0.9426807,
            "category": "Positive"
        },
        {
            "entity": "music",
            "sentiment_score": 0.7,
            "sentiment_magnitude": 0.7,
            "salience": 0.05731931,
            "category": "Positive"
        }
    ]

    save_reviews_to_csv(commentary, review_data, file_path)