#!/bin/python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#

#
# Define functions
#

"""

The following program uses nested dictionaries to store a small music library.
    Extend the program such that a user can add artists, albums, and songs to the library.
First, add a command that adds an artist name to the music dictionary.
    Then add commands for adding albums and songs.
    Take care to check that an artist exists in the dictionary before adding an album,
        and that an album exists before adding a song.

"""

"""

# raw data:
employees = {1000: {'name': 'Derek', 'job': 'support', 'salary': 89567},
             1001: {'name': 'Alice', 'job': 'coder', 'salary': 94275},
             1002: {'name': 'Lucia', 'job': 'writer', 'salary': 76500},
             1003: {'name': 'Micah', 'job': 'trainer', 'salary': 81354},
             1004: {'name': 'Sarah', 'job': 'sales', 'salary': 64152}}

for id in employees:
    name = employees[id].get('name')
    pay = employees[id].get('salary')
    print(f'{name} gets paid ${pay:.2f}')

"""
music = {
    'Pink Floyd':
        { 'album': 'The Dark Side of the Moon', {
                    'songs': ['Speak to Me', 'Breathe', 'On the Run', 'Money'],
                   'year': 1973, 'platinum': True
                    },
        { 'album:': 'The Wall', {
                     'songs': ['Another Brick in the Wall', 'Mother', 'Hey you'],
                    'year': 1979, 'platinum': True
                    }
        },
    'Justin Bieber':
        { 'album': 'My World', {
                    'songs': ['One Time', 'Bigger', 'Love Me'],
                    'year': 2010, 'platinum': True
                    }
                }


# First, add a command that adds an artist name to the music dictionary.

# Get user input
print(music)
artist_name = input('Enter the artist name to add or review data, "exit" to quit ')

# While user input != 'exit'
    # ....

if artist_name in music:
    for album in music[artist_name]:
        print(f'For the artist {artist_name}')
        print(album)
        album_list = music[artist_name].get('album')
        print(album_list)
        song_list = album_list.get('songs')
        print(f'Song list: {song_list}')

    #print(f'Released: {music[artist_name]:year}')

"""

# End of Program
