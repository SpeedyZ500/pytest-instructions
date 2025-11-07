from song_library import Song, SongLibrary

def test_add_song():
    pass

    song_library = SongLibrary()
    test_song = Song("We Built This City", "Rock")

    expected:list[Song] = [test_song]

    assert  expected == song_library.get_songs()