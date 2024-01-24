# Toxicity Classifier

Toxicity Classifier is a project that aims to detect toxicity in text using a machine learning model. It includes a toxicity classification model trained on textual data and a FastAPI-based API for integrating the model into applications.

## Project Structure

The project is organized as follows:

- `app.py`: Main script for the Streamlit web application.
- `toxicity_model.pkl`: Pickled file containing the trained toxicity classification model.
- `tf_idf.pkl`: Pickled file containing the TF-IDF vectorizer used for text preprocessing.
- `requirements.txt`: Dependencies for the API.
- `api/`: Folder containing the FastAPI-based API.
  - `main.py`: FastAPI application script.
  
  

## Setup

1. Install the required Python packages:
```
  pip install -r requirements.txt
   ```
2.Run the Streamlit web application:
   ```
  streamlit run app.py
  ```
3.Access the web application by visiting http://localhost:8501 in your browser.

# API Usage
The FastAPI-based API allows you to programmatically interact with the toxicity classification model. Here's how you can use it:

1.Navigate to the api/ folder:
```
cd api
```
2.Run the FastAPI application:
```
uvicorn main:app --reload
```
3.Access the API documentation at http://localhost:8000/docs to explore and test the API.

# API Endpoints
` /predict: Endpoint for making toxicity predictions. Send a POST request with the text to classify. `

# Dependencies
- Streamlit
- Scikit-learn
- FastAPI
- fastapi
- uvicorn
- numpy

# Acknowledgments
The toxicity classification model is trained using labeled data from [Kaggle](https://www.kaggle.com/datasets/ashwiniyer176/toxic-tweets-dataset?resource=download)

# License
This project is licensed under the MIT License

# Contributing
Before contributing, please take a moment to read the guidelines outlined below.

## How to Contribute

1. Fork the repository to your GitHub account.

2. Clone the forked repository to your local machine:
```
   git clone https://github.com/Prureddy/Toxicity_classifier.git
```

3.Create a new branch for your contribution:
```
    git checkout -b feature/your-feature-name
```

4.Make your changes and commit them with descriptive commit messages:
```
    git commit -m "Add your descriptive commit message"
```

5.Push your changes to your forked repository:
```
 git push origin feature/your-feature-name
 ```
