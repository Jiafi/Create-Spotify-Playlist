#!/usr/bin/env python
import spotipy
import sys
import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

username = '1219154282'
scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope)
if token:
    spotify = spotipy.Spotify(auth=token)

if len(sys.argv) > 1:
    file_name = ' '.join(sys.argv[1:])
else:
    file_name = './songs.txt'

# Read in the names and artist of the songs
with open(file_name) as my_file:
    songs = my_file.read().splitlines()
songs = [(x.split('-')[0].strip(), x.split('-')[1].strip()) for x in songs]

song_ids = []
for song in songs:
    name = song[0]
    track = song[1]
    results = spotify.search(q='artist:' + name + ' track: ' + track, type='track')
    items = results['tracks']['items']
    song_ids.append(items[0]['id'])
results = spotify.user_playlist_create(username, "new temp playlist", description='created through my script')
playlist_id = results['id']

results = spotify.user_playlist_add_tracks(username, playlist_id, song_ids)
print(results)
