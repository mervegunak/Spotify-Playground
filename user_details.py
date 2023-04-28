import requests
import get_spotify_token
import re

class SpotifyUser:
    def __init__(self, spotify_user_link):
        self.spotify_user_link = spotify_user_link
        self.user_id = self.extract_spotify_user_id()
        self.display_name = self.get_details()
        self.playlists_id = self.get_playlists_id()
        self.playlists_name = self.get_playlists_name()

    def extract_spotify_user_id(self):
        # Define the regular expression pattern to match Spotify user links
        pattern = r"^(?:https:\/\/|http:\/\/|www\.)?(?:open\.)?spotify\.com\/user\/([a-zA-Z0-9]+)(?:\?.*)?$"
        
        # Match the pattern against the Spotify user link
        match = re.match(pattern, self.spotify_user_link)
        
        # If the match is found, return the user id. Otherwise, return None.
        if match:
            return match.group(1)
        else:
            return None

    def get_details(self):
        # Spotify API endpoint for playlists
        url = f'https://api.spotify.com/v1/users/{self.user_id}'
        
        access_token = get_spotify_token.get_token()

        # Set headers with the access token
        headers = {'Authorization': 'Bearer ' + access_token}

        # Send GET request to Spotify API
        response = requests.get(url, headers=headers)

        # Get user details from response
        user_response = response.json()["display_name"]

        return user_response
    
    def get_playlists_id(self):
        # Spotify API endpoint for playlists
        url = f'https://api.spotify.com/v1/users/{self.user_id}/playlists'

        access_token = get_spotify_token.get_token()

        # Set headers with the access token
        headers = {'Authorization': 'Bearer ' + access_token}

        # Send GET request to Spotify API
        response = requests.get(url, headers=headers)

        # Get playlist details from response
        playlists_response = response.json()["items"]
        playlists_id = []

        # Iterate over each playlist
        for playlist in playlists_response:
            # Retrieve playlist ID
            playlists_id.append(playlist["id"])

        return playlists_id

    def get_playlists_name(self):
        # Spotify API endpoint for playlists
        url = f'https://api.spotify.com/v1/users/{self.user_id}/playlists'

        access_token = get_spotify_token.get_token()

        # Set headers with the access token
        headers = {'Authorization': 'Bearer ' + access_token}

        # Send GET request to Spotify API
        response = requests.get(url, headers=headers)

        # Get playlist details from response
        playlists_response = response.json()["items"]
        playlists_name = []

        # Iterate over each playlist
        for playlist in playlists_response:
            # Retrieve playlist ID
            playlists_name.append(playlist["name"])

        return playlists_name