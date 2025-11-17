import pytest
from .song_library_solution import Song, SongLibrary

song_library = SongLibrary()

# ======== add_song tests ========

# 🟢 Positive Test
def test_add_valid_song():
    song_library.clear()
    song_library.add_song(Song("We Built This City", "Rock"))

    assert 1 == len(song_library.songs)

# 🔴 Negative Test
def test_add_invalid_song():
    song_library.clear()

    with pytest.raises(TypeError):
        song_library.add_song(27) # type: ignore

# ======== remove_song tests ========

# 🟢 Positive Test
def test_remove_present_song():
    song_library.clear()
    song_library.add_song(Song("We Built This City", "Rock"))
    song_library.remove_song("We Built This City")

    assert 0 == len(song_library.songs)

# 🔴 Negative Test
def test_remove_absent_song():
    song_library.clear()
    song_library.remove_song("The Unsung Song")

    assert 0 == len(song_library.songs)

# ======== get_songs_in_genre tests ========

# 🟢 Positive Test
def test_get_present_song_in_genre():
    song_library.clear()
    song_library.add_song(Song("We Built This City", "Rock"))
    song_library.add_song(Song("Hello World", "Pop"))
    song_library.add_song(Song("Take Me Home, Country Roads", "Country"))

    assert 1 == len(song_library.get_songs_in_genre("Rock"))

# 🔴 Negative Test
def test_get_absent_song_in_genre():
    song_library.clear()
    song_library.add_song(Song("We Built This City", "Rock"))
    song_library.add_song(Song("Hello World", "Pop"))
    song_library.add_song(Song("Take Me Home, Country Roads", "Country"))

    assert 0 == len(song_library.get_songs_in_genre("Classical"))