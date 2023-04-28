import os
import requests
import get_spotify_token
import pandas as pd

def get_tracks_in_playlist(playlist_id, playlist_name):
    # Spotify API endpoint
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

    # Get access token from authentication response
    access_token = get_spotify_token.get_token()

    # Set headers with the access token
    headers = {'Authorization': 'Bearer ' + access_token}

    # Initialize variables for pagination
    limit = 100
    offset = 0
    total_number_of_tracks = None
    tracks = []
    track_ids = []

    directory = "./Spotify_Playground/Playlists/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = f"{directory}tracks_in_playlist_{playlist_name}.csv"


    # Make requests until all tracks have been fetched to the csv
    while total_number_of_tracks is None or offset < total_number_of_tracks:
        # Set query parameters for pagination
        params = {
            'offset': offset,
            'limit': limit
        }

        # Send GET request to Spotify API
        response = requests.get(url, headers=headers, params=params)

        # Get tracks in playlist details from response
        tracks_response = response.json()["items"]
        total_number_of_tracks = response.json()["total"]

        # get track details
        for track in tracks_response:
            track_ids = track['track']['id']
            track_name = track['track']['name']
            artist_name = track['track']['artists'][0]['name']
            artist_id = ", ".join(
                [artist["id"] for artist in track["track"]["artists"]]
            )
            album_name = track['track']['album']['name']
            tracks.append({
                'ID': track_ids,
                'Track': track_name,
                'Artist': artist_name,
                'Album' : album_name
            })

        # Increment the offset by the limit for the next request
        offset += limit
    
    def get_artist(artist_id):
        url_arists = f'https://api.spotify.com/v1/artists/{artist_id}'

        access_token = get_spotify_token.get_token()
        headers = {'Authorization': 'Bearer ' + access_token}
        response_artists = requests.get(url_arists, headers=headers)

        artists_json = response_artists.json()
        genres = artists_json['genres'][0]

        genres.append({
        'Genres': genres
        })       

    # Create DataFrame from list of tracks
    df = pd.DataFrame(tracks)
    
    filename = f"{directory}tracks_in_playlist_{playlist_name}.csv"

    # Save DataFrame to CSV file
    df.to_csv(filename, index=True)

    return df
