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
    tracks_unique_ids = []

    # Create Playlists folder if it does not exist
    directory = "./Spotify_Playground/Playlists/"
    if not os.path.exists(directory):
        os.makedirs(directory)

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
            artist_id = track['track']['artists'][0]['id']
            artist_name = track['track']['artists'][0]['name']
            album_name = track['track']['album']['name']
            album_id = track['track']['album']['id']
            artist_genre = get_artist_genre(artist_id)
            tracks.append({
                'Track_Id': track_ids,
                'Track': track_name,
                'Artist_Id': artist_id,
                'Artist': artist_name,
                'Album_Id': album_id,
                'Album' : album_name,
                'Artist Genre' : artist_genre
            })
            tracks_unique_ids.append(track_ids)

        # Increment the offset by the limit for the next request
        offset += limit

    # Create DataFrame from list of tracks
    df = pd.DataFrame(tracks)

    filename = f"{directory}tracks_in_playlist_{playlist_name}.csv"
    
    # Save DataFrame to CSV file
    df.to_csv(filename, index=True)

    return df

def get_artist_genre(artist_id):
    # Spotify API endpoint
    url_artists = f'https://api.spotify.com/v1/artists/{artist_id}'

    # Get access token from authentication response
    access_token = get_spotify_token.get_token()

    # Set headers with the access token
    headers = {'Authorization': 'Bearer ' + access_token}

    # Send GET request to Spotify API
    response = requests.get(url_artists, headers=headers)

    # get artist genre
    genre_response = response.json()
    artist_genre = genre_response['genres']

    return artist_genre