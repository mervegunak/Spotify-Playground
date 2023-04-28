import user_details
import user_playlists_track as user_playlists_track

# https://developer.spotify.com/documentation/web-api/reference/#/operations/save-tracks-user

user_link = input("Please Enter the Spotify User Link: ")

spotify_user = user_details.SpotifyUser(user_link)

print("User:",spotify_user.display_name)
print("User_ID:", spotify_user.user_id)
print("Playlist_Names:",spotify_user.playlists_name)
print("Playlist_IDs:",spotify_user.playlists_id)

# This for loop generates all of the user playlists tracks with different csv's.
for id, playlist_id in enumerate(spotify_user.playlists_id):
    playlist_name = spotify_user.playlists_name[id]
    user_playlists_track.get_tracks_in_playlist(playlist_id, playlist_name)
