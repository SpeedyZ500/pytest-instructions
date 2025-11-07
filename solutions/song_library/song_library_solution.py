class Song:

    def __init__(self, name:str, genre:str) -> None:
        self.name = name
        self.genre = genre


    def __repr__(self) -> str:
        return f"\"{self.name}\""


class SongLibrary:

    songs:list[Song] = []


    def __init__(self) -> None:
        pass


    def clear(self) -> None:
        self.songs.clear()


    def add_song(self, song:Song) -> None:

        if not isinstance(song, Song):
            raise TypeError

        self.songs.append(song)
        print(f"Added: {song.name}")


    def remove_song(self, song_name:str) -> None:

        for i in range(len(self.songs)):
            if self.songs[i].name == song_name:
                self.songs.pop(i)
                print(f"Removed: {song_name}")
                return
        print("No song found")


    def get_songs_in_genre(self, genre:str) -> list[Song]:

        genre_songs:list[Song] = []

        for i in range(len(self.songs)):
            if self.songs[i].genre == genre:
                genre_songs.append(self.songs[i])
        
        return genre_songs


    def __repr__(self) -> str:
        return f"Library({repr(self.songs)})"