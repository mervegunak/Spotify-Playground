import requests
import get_spotify_token

def get_tracks_in_playlist(playlist_id):
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
    track_unique_ids = []

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
            album_name = track['track']['album']['name']
            tracks.append({
                'ID': track_ids,
                'Track': track_name,
                'Artist': artist_name,
                'Album' : album_name
            })
            track_unique_ids.append(track_ids)

        # Increment the offset by the limit for the next request
        offset += limit

    return track_unique_ids

def track_features(track_id):
    # Spotify API endpoint for audio-features
    url = f'https://api.spotify.com/v1/audio-features/{track_id}'
        
    access_token = get_spotify_token.get_token()

    # Set headers with the access token
    headers = {'Authorization': 'Bearer ' + access_token}

    # Send GET request to Spotify API
    response = requests.get(url, headers=headers)

    # Get audio features of track from response
    audio_features = response.json()

    return audio_features


print(get_tracks_in_playlist('7CSf1UnUFwuz7jRVGmCiaQ'))

for x in get_tracks_in_playlist('7CSf1UnUFwuz7jRVGmCiaQ'):
    print(track_features(x))