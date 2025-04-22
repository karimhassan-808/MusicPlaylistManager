import io
import sys
from music_playlist_manager import add_song, remove_song, display_playlist, save_playlist, load_playlist, playlist




def test_add_song():
    add_song("Song 1")
    add_song("Song 2")
    assert "Song 1" in playlist, "Song 1 should be in the playlist."
    assert "Song 2" in playlist, "Song 2 should be in the playlist."
    playlist.clear()
    print("test_add_song passed.")

def test_remove_song():
    add_song("Song 1")
    add_song("Song 2")
    remove_song("Song 1")
    assert "Song 1" not in playlist, "Song 1 shouldn't be in the playlist."
    assert "Song 2" in playlist, "Song 2 should still be in the playlist."
    playlist.clear()
    print("test_remove_song passed.")

def test_display_playlist():
    add_song("Song 1")
    add_song("Song 2")
    display_playlist()
    captured = io.StringIO() #capture the output of display_playlist
    sys.stdout = captured  #redirect stdout
    display_playlist()
    sys.stdout = sys.__stdout__  #reset redirect

    output = captured.getvalue()
    assert "1. Song 1" in output, "Song 1 should be displayed"
    assert "2. Song 2" in output, "Song 2 should be displayed"
    playlist.clear()
    print("test_display_playlist passed.")

def test_save_and_load_playlist():
    global playlist
    playlist.clear()
    add_song("Song 1")
    add_song("Song 2")
    save_playlist("test_playlist.txt")

    load_playlist("test_playlist.txt")
    with open("test_playlist.txt", "r") as file: #loads the file by its name
            lines = file.readlines()
            print(lines)
    print(playlist)
    assert playlist == ["Song 1", "Song 2"], "Playlist should match the saved songs"
    playlist.clear()
    print("test_save_and_load_playlist passed.")

def run_tests():
    test_add_song()
    test_remove_song()
    test_display_playlist()
    test_save_and_load_playlist()
    print("All the tests passed.")


if __name__ == "__main__":
    run_tests()
