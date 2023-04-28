# Spotify-Auto-Playlistify-Sculptor

This project is a collection of Python scripts that interact with the Spotify Web API to extract information related to user and playlist details, as well as to retrieve tracks and associated details of a users public playlists.

**Prerequisites:**

Before using these scripts, there are a few prerequisites that need to be set up:

**1)** A Spotify account

**2)** Spotify API client ID and secret. To obtain these, create a Spotify Developer account, create a new application, and retrieve the client ID and secret from the application dashboard.

**3)** The following packages need to be installed:

    requests 
    base64 
    os 
    dotenv 
    re pandas
    
   **Example**: 
   
    pip install -r requirements.txt

**File structure:**

This project contains the following files:

* **get_spotify_token.py:** This script contains a function to retrieve an access token for the Spotify Web API, using the Spotify API client ID and secret.

* **get_user_details.py:** This script contains a SpotifyUser class, which takes a Spotify user link as input and extracts the user's display name, ID, as well as the names and IDs of their playlists.

* **get_playlist_tracks.py:** This script contains a function to retrieve tracks and associated details from a given playlist. The function outputs a CSV file that contains the following information: Track Id, Track Name, Artist Id, Artist Name, Album Id, Album Name, and Artist Genre.

* **.env:** This file contains environment variables for the Spotify API client ID and secret.

**How to use:**

- Clone the project repository and navigate to the project directory.
- Set the Spotify API client ID and secret in the .env file.
- In the command line, run python main.py . After running the main.py, user's profile link will be requested as an input from the terminal so please provide spotify profile link as an input for the program. This will output the user's display name, ID, as well as the names and IDs of their playlists and fetches them in a csv file generated under Playlists folder.

Note: Ensure that the necessary packages have been installed before running the scripts.

**Authors:**

This project was created by [mervegunak](https://github.com/mervegunak) and [karakayautku4](https://github.com/karakayautku4).
