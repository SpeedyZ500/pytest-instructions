import pytest
from song_library import Song, SongLibrary

song_library = SongLibrary()

# ======== add_song tests ========

def test_add_song_positive():
    song_library.clear()
    song_library.add_song(Song("We Built This City", "Rock"))

    assert 1 == len(song_library.songs)


def test_add_song_negative():
    song_library.clear()

    with pytest.raises(TypeError):
        song_library.add_song(27) # type: ignore

# ======== remove_song tests ========

def test_remove_song_positive():
    song_library.clear()
    song_library.add_song(Song("We Built This City", "Rock"))
    song_library.remove_song("We Built This City")

    assert 0 == len(song_library.songs)


def test_remove_song_negative():
    song_library.clear()
    song_library.remove_song("The Unsung Song")

# ======== get_songs_in_genre tests ========

def test_get_songs_in_genre_positive():
    song_library.clear()
    song_library.add_song(Song("We Built This City", "Rock"))
    song_library.add_song(Song("Hello World", "Pop"))
    song_library.add_song(Song("Take Me Home, Country Roads", "Country"))

    assert 1 == len(song_library.get_songs_in_genre("Rock"))


def test_get_songs_in_genre_negative():
    song_library.clear()
    song_library.add_song(Song("We Built This City", "Rock"))
    song_library.add_song(Song("Hello World", "Pop"))
    song_library.add_song(Song("Take Me Home, Country Roads", "Country"))

    assert 0 == len(song_library.get_songs_in_genre("Classical"))