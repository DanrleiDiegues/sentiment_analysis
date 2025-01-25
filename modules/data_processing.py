# Module: data_processing.py
from sklearn.preprocessing import MinMaxScaler

def process_entity_sentiment(entity_data, positive_threshold=0.2, negative_threshold=-0.2, magnitude_threshold=0.5, salience_threshold=0.1):
    """
    Process entity sentiment data to categorize sentiment scores.

    Args:
        entity_data (list): List of entities from the Google NLP API response.
        positive_threshold (float): Threshold above which the sentiment is categorized as Positive.
        negative_threshold (float): Threshold below which the sentiment is categorized as Negative.

    Returns:
        list: A list of dictionaries containing entity name, sentiment score, magnitude, and category.
    """
    processed_data = []

    for entity in entity_data:
        name = entity.get("name", "Unknown")
        type_ = entity.get("type", "Unknown")
        score = entity.get("sentiment_score", 0)
        magnitude = entity.get("sentiment_magnitude", 0)
        salience = entity.get("salience", 0)

        # Categorize the sentiment
        if score > positive_threshold:
            category = "Positive"
        elif score < negative_threshold:
            category = "Negative"
        else:
            category = "Neutral"

        # Scaler
        # scaler = MinMaxScaler()
        # normalized_data = scaler.fit_transform([[magnitude, salience]])
        
        # Create each entity's caracteristic with a indice in from of the carecteristics for example: entity_1, entity_2, entity_3
            
        # Append processed data
        processed_data.append({
            "entity": name,
            "sentiment_score": score,
            "sentiment_magnitude": magnitude,
            "salience": salience,
            "category": category
        })

    return processed_data

# Example Usage
if __name__ == "__main__": # The code below will only run if this script is executed directly
                           # The if __name__ == "__main__": block is used to 
                           # prevent the code inside it from running when the script is 
                           # imported as a module.
                           
    # Example JSON data from Google NLP API
    example_data = [
        {
            "name": "sushi",
            "type": "Food",
            "sentiment_score": 0.8,
            "sentiment_magnitude": 0.5,
            "salience": 0.7
        },
        {
            "name": "service",
            "type": "Service",
            "sentiment_score": -0.6,
            "sentiment_magnitude": 0.4,
            "salience": 0.5
        },
        {  
            "name": "ambiance",
            "type": "Ambiance",
            "sentiment_score": 0.4,
            "sentiment_magnitude": 0.3,
            "salience": 0.3
        }
    ]

    processed = process_entity_sentiment(example_data)
    for item in processed:
        print(f"Entity: {item['entity']}, Sentiment Score: {item['sentiment_score']}, Sentiment Magnitude: {item['sentiment_magnitude']}, Salience: {item['salience']}, Category: {item['category']}")
