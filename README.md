# 🎵 Music Playlist Manager  
**Final Project – CS50’s Introduction to Programming with Python**

## 📜 Overview

This is a simple yet functional **Music Playlist Manager** written in Python. It allows users to interactively create, manage, save, and load a music playlist via a command-line interface.

Developed as the **final project** for Harvard’s CS50: *Introduction to Programming with Python*, this script encapsulates core programming concepts including loops, conditionals, functions, file handling, and string manipulation.

---

## 🚀 Features

- ✅ **Add Song** — Insert a new song into your playlist.
- ❌ **Remove Song** — Delete an existing song from the playlist.
- 📋 **Display Playlist** — View the current playlist with numbered entries.
- 💾 **Save Playlist** — Save the current playlist to a text file.
- 📂 **Load Playlist** — Load a playlist from a previously saved file.
- 🚪 **Exit** — Exit the manager cleanly.

---

## 🧠 How It Works

The program uses a global Python list (`playlist`) to manage songs in memory. It offers a simple menu-based interaction pattern and persists data using basic file I/O operations.

### Menu System

Users are continuously prompted with a menu until they choose to exit:
```
Music Playlist Manager

1- Add Song
2- Remove Song
3- Display Playlist
4- Save Playlist
5- Load Playlist
6- Exit
```

### File Persistence

- **Saving** creates or overwrites a `.txt` file, writing each song on a new line.
- **Loading** reads from a given `.txt` file and appends the contents to the current in-memory playlist.

> ⚠️ After saving, the current playlist is **cleared**, simulating a fresh session for a new playlist.

---

## 📦 Requirements

This script runs on **Python 3.x** and does not depend on any external libraries.

To check your Python version:

```bash
python --version
```
## ▶️ Running the Program
- Save the script in a file, e.g. playlist_manager.py.

- In your terminal, run:
```
python playlist_manager.py
```
- Follow the on-screen prompts to interact with the playlist.

## 📁 Example Use Case
```
> Enter your choice: 1
> Enter the song name: Blinding Lights

Added 'Blinding Lights' to the playlist.

> Enter your choice: 3
Playlist:
1. Blinding Lights

> Enter your choice: 4
> Enter the file name: my_playlist.txt
Playlist saved to 'my_playlist.txt'.

> Enter your choice: 6
```

## ⚠️ Notes
- Song names are stored exactly as entered (case-sensitive).

- Whitespace is trimmed automatically.

- If a file isn't found during loading, an error is printed, and the program continues.


## 🧑‍🎓 Author
This project was developed as part of CS50’s Introduction to Programming with Python final project submission by a passionate student dedicated to mastering Python and software fundamentals.


## 📜 License
This project is for educational purposes under CS50's open course policy. Feel free to modify, reuse, or enhance it as a personal or academic project.

[project video](https://www.youtube.com/watch?v=L5BDn8OAj-8&ab_channel=KarimHassan)