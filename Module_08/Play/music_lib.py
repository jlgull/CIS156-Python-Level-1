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


music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': [ 'Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
            'platinum': True
        },
        'The Wall': {
            'songs': [ 'Another Brick in the Wall', 'Mother', 'Hey you'],
            'year': 1979,
            'platinum': True
        }
    },
    'Justin Bieber': {
        'My World':{
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010,
            'platinum': True
        }
    }
}

# First, add a command that adds an artist name to the music dictionary.

# Get user input

artist_name = input('Enter the artist name to add or review data, "exit" to quit ')

# While user input != 'exit'
    # ....

if artist_name in music:
    print(f'For the artist {artist_name}')
    print(f'Songs: {music[artist_name][songs]}')

    print(f'Released: {music[artist_name]:year}')

#f'is {music[artist_name]}')

# End of Program
