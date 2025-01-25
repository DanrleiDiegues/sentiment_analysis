import requests

API_KEY = "API_KEY" # API key from Google Cloud Platform
URL = f"https://language.googleapis.com/v1/documents:analyzeEntitySentiment?key={API_KEY}"

# Example: "I liked the sushi but the service was terrible."
# COMMENTARY = "I liked the sushi but the service was terrible."

# Creating the function to call the API to use in the main.py:

def get_entity_sentiment(commentary):
    data = {
        "document": {
            "type": "PLAIN_TEXT",
            "content": commentary
        },
        "encodingType": "UTF8"
    }

    response = requests.post(URL, json=data)

    if response.status_code == 200:
        # Extracting the entities from the response
        result = response.json() # Parsing the JSON response. 
                                 # The response is a dictionary with the entities and their sentiment.
                                                          
        # Extracting the entities from the response
        entities = []
        
        # Looping through the entities in the response
        for entity in result.get("entities", []):
            
            # Extracting the name, type, sentiment, score, magnitude, and salience of the entity
            name = entity.get("name")
            type_ = entity.get("type")
            sentiment = entity.get("sentiment", {})
            score = sentiment.get("score", 0)
            magnitude = sentiment.get("magnitude", 0)
            
            # Appending the entity to the list
            entities.append({
                "name": name,
                "type": type_,
                "sentiment_score": score,
                "sentiment_magnitude": magnitude,
                "salience": entity.get("salience", 0)
            })
        return entities
    else:
        return None
    
    
# Example Usage
if __name__ == "__main__":
    commentary = "I liked the sushi but the service was terrible. The ambiance was great though!"
    sentiment = get_entity_sentiment(commentary)
    print(sentiment)