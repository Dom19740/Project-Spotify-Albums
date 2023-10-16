import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up your Spotify API credentials
CLIENT_ID = '902f9b04121246ae818790a54e1b3e6d'
CLIENT_SECRET = '4e4fa071ece04fe292b336a55247c623'
REDIRECT_URI = 'http://localhost:3000'

# Set up authentication and create Spotify API client
scope = 'user-library-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope))

# Get a list of your liked albums
results = sp.current_user_saved_albums(limit=50)  # Adjust the limit as needed
albums = results['items']

# Iterate over pages of liked albums
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

# Extract album names and artists
liked_albums = []
for album in albums:
    album_name = album['album']['name']
    artists = ', '.join([artist['name'] for artist in album['album']['artists']])
    liked_albums.append(f"{album_name} - {artists}")

# Save liked albums to a .txt file
file_path = 'liked_albums.txt'
with open(file_path, 'w') as file:
    file.write('\n'.join(liked_albums))

print(f"List of liked albums saved to {file_path}.")
