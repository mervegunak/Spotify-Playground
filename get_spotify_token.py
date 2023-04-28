import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

def get_token():
    try:
        # Spotify API client ID and secret
        client_id = os.getenv('SPOTIFY_CLIENT_ID')
        client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

        # Encode client ID and secret in Base64
        auth_header = base64.b64encode(bytes(client_id + ':' + client_secret, 'utf-8')).decode('utf-8')

        # Send authentication request to Spotify API
        auth_url = 'https://accounts.spotify.com/api/token'
        auth_data = {'grant_type': 'client_credentials'}
        auth_headers = {'Authorization': 'Basic ' + auth_header}
        auth_response = requests.post(auth_url, data=auth_data, headers=auth_headers)

        # Check if response is OK
        auth_response.raise_for_status()

        # Get access token from authentication response
        access_token = auth_response.json()['access_token']

        return access_token

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while sending the authentication request: {e}")
        return None

    except KeyError as e:
        print(f"The authentication response did not contain an access token: {e}")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
