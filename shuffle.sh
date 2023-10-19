#!/bin/bash

    	read -p 'Playlist ID or URL: ' PLAYLIST_ID
		read -p 'Playlist name: ' PLAYLIST_NAME

		yt-dlp -j --flat-playlist $PLAYLIST_ID | jq -r '.id' | sed 's_^_https://youtu.be/_' > $PLAYLIST_NAME.m3u