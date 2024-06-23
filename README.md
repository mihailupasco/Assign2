# Guess the Four Digit Code Game

This project is a multi-player game called "Guess the Four Digit Code" that uses sockets for communication between clients and the server, and SQLite3 for data storage. 

## Project Structure
```angular2html
├── .venv  
├── recordings  
│ ├── 2players.mp4  
│ └── 4players.mp4  
├── client.py  
├── data.db  
├── schema.sql   
└── server.py  
```


## Description

### Server

The server handles the connections from multiple clients, managing the game logic and communication. It is responsible for:
- Handling client connections and disconnections
- Managing game sessions
- Authenticating users
- Storing and retrieving data from the SQLite3 database

### Client

The client allows players to connect to the server and play the game. It handles:
- Connecting to the server
- Sending and receiving messages
- Displaying game information to the user

### Database

The project uses an SQLite3 database (`data.db`) to store user information and game data. The schema is defined in `schema.sql`.

## How to Run

1. **Install the requirements:**
   - Install necessary packages (if any are defined, otherwise ensure `sqlite3` and `socket` modules are available in your Python environment).

2. **Set up the database:**
   - Initialize the database using the provided `schema.sql`:
     ```sh
     sqlite3 data.db < schema.sql
     ```

3. **Run the server:**
   - Start the server by running:
     ```sh
     python server.py
     ```

4. **Run the client:**
   - In a new terminal, start the client(s) by running:
     ```sh
     python client.py
     ```
   - You can start multiple clients to simulate multiple players.

## Game Play

Each player will:
- Connect to the server.
- Follow prompts to authenticate or register.
- Play the game by guessing the four-digit code.

The server will:
- Handle multiple players.
- Provide feedback to players about their guesses.

## Recordings

There are two recordings demonstrating gameplay:
- `2players.mp4`: Example of two players playing the game.
- `4players.mp4`: Example of four players playing the game.

These recordings showcase the interaction between clients and the server during the game.

