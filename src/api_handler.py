import os
import json
import requests
from src.utils.logging import configure_logging

logger = configure_logging()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")

if not API_KEY:
    logger.error("Environment variable API_KEY is not set.")
    exit(1)

def call_api(input_data):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        "inputs": {},
        "query": input_data,
        "response_mode": "streaming",
        "user": "admin"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        if not response.content:
            logger.error("API response is empty.")
            return "Error: The API response is empty."

        if 'application/json' in response.headers.get('Content-Type', ''):
            return response.json()

    except requests.exceptions.Timeout:
        logger.error("API request timed out.")
        return "Error: The request to the API timed out."
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - {response.text}")
        return f"Error: {response.status_code} - {response.text}"
    except requests.exceptions.RequestException as err:
        logger.error(f"Request exception: {err}")
        return f"Error: {err}"
    except json.JSONDecodeError:
        logger.error("Failed to decode JSON from API response.")
        return "Error: Received invalid JSON from the API."