#global playlist
playlist = []

def main():
    while True:
        print("\nMusic Playlist Manager")
        print("1. Add Song")
        print("2. Remove Song")
        print("3. Display Playlist")
        print("4. Save Playlist")
        print("5. Load Playlist")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            song = input("Enter the song name: ")
            add_song(song)
        elif choice == "2":
            song = input("Enter the song name: ")
            remove_song(song)
        elif choice == "3":
            display_playlist()
        elif choice == "4":
            filename = input("Enter the file name:").strip()
            save_playlist(filename)
        elif choice == "5":
            filename = input("Enter the file name:").strip()
            load_playlist(filename)
        elif choice == "6":
            break
        else:
            print("Invalid choice, Please try again.")





def add_song(song):
    song = song.strip()
    if song.strip(): #ensure the song is not empty
        playlist.append(song)
        print(f"Added '{song}' to the playlist.")
    else:
        print("Error: Song name cannot be empty")


def remove_song(song):
    song = song.strip()
    if song in playlist: #ensures the song is previously in the playlist
        playlist.remove(song)
        print(f"Removed '{song}' from the playlist.")
    else:
        print("Error: the song isn't in the playlist.")


def display_playlist():
    if not playlist: #checks if the playlist doesn't have any songs
        print("The playlist is empty.")
    else:
        print("Playlist:")
        for i,song in enumerate(playlist, start = 1):
            print(f"{i}. {song}")


def save_playlist(filename = "playlist.txt"):
    with open(filename, "w") as file: #creates a file to write into
        for song in playlist:
            file.write(song + "\n")
    print(f"Playlist saved to '{filename}'.")
    playlist.clear() #clears the saved playlist for a new one


def load_playlist(filename = "playlist.txt"):
    global playlist
    try:
        with open(filename, "r") as file: #loads the file by its name
            lines = file.readlines()
            playlist.extend(line.strip() for line in lines)
        print(f"Playlist loaded from '{filename}'.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


if __name__ == "__main__":
    main()
