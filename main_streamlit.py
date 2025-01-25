# Main app: Streamlit app for the project
import streamlit as st

# Importing the function from the model_api_call.py
from modules.model_api_call import get_entity_sentiment
from modules.data_processing import process_entity_sentiment
from modules.get_reviews_to_csv import save_reviews_to_csv
# from modules.data_storage import append_to_google_sheets

# Title of the app
st.title('Give the review of about the service you received')

# Text area for the user to input the review
commentary = st.text_area('Enter your review here')

# Button to submit the review
if st.button('Submit'):
    # Call the API function
    entities = get_entity_sentiment(commentary)
    
    # Preprocess the data
    sentiments = process_entity_sentiment(entities)
    
    # Sentiment response in a better way:
    st.write(f'You submitted: {commentary}')
    
    # Display and analyze the sentiment
    st.subheader('Sentiment analysis result:')
    
    for sentiment in sentiments:
        # Color red for negative, green for positive, and white for neutral:
        color = 'red' if sentiment['category'] == 'Negative' else 'green' if sentiment['category'] == 'Positive' else 'white'
        
        # Display the sentiment information and use the color variable to set the text color
        st.markdown(f'<p style="color: {color};">Entity: {sentiment["entity"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color: {color};">Sentiment Category: {sentiment["category"]}</p>', unsafe_allow_html=True)
        st.write(f"Sentiment Score: {sentiment['sentiment_score']} | Sentiment Magnitude: {sentiment['sentiment_magnitude']} | Salience: {sentiment['salience']}")
        st.write('---')
    
    
    # JSON response
    st.write('JSON format: Entities Sentiment analysis')
    st.write(entities)
    
    # Display the processed data
    st.write('Processed Sentiment Information:')
    st.write(sentiments)
    
    # Save the review to a CSV file
    save_reviews_to_csv(commentary, sentiments, "data_reviews/reviews.csv")
    