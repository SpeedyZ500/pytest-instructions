class Song:

    def __init__(self, name:str, genre:str) -> None:
        self.name = name
        self.genre = genre

class SongLibrary:

    songs:list[Song] = []

    def __init__(self) -> None:
        pass

    def get_songs(self) -> list[Song]:
        return self.songs


    def add_song(self, song:Song) -> None:
        self.songs.append(song)
        print(f"Added: {song.name}")


    def remove_song(self, song_name:str) -> None:
        for i in range(len(self.songs)):
            if self.songs[i].name == song_name:
                self.songs.pop(i)
                print(f"Removed: {song_name}")
                return
        print("No song found")

    def print_songs_in_genre(self, genre:str) -> None:

        songs_found:bool = False

        for i in range(len(self.songs)):
            if self.songs[i].genre == genre:
                print(self.songs[i].name)
        
        if not songs_found:
            print("No songs in genre")