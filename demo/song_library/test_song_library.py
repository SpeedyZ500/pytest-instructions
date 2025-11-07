import pytest
from song_library import Song, SongLibrary

song_library = SongLibrary()

def test_add_song_positive():
    song_library.clear()
    song_library.add_song(Song("We Built This City", "Rock"))
    assert 1 == len(song_library.songs)

def test_add_song_negative():
    # TODO: Impelement
    raise NotImplementedError

def test_remove_song_positive():
    # TODO: Impelement
    raise NotImplementedError

def test_remove_song_negative():
    # TODO: Impelement
    raise NotImplementedError

def test_get_songs_in_genre_positive():
    # TODO: Impelement
    raise NotImplementedError

def test_get_songs_in_genre_negative():
    # TODO: Impelement
    raise NotImplementedError