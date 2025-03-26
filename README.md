# SongSift

**SongSift** is a command-line application that provides music track recommendations based on user input. It utilizes the Spotify API to search for songs and suggest tracks similar to the provided input. The application features a progress indicator and displays recommendations in a well-formatted table.

## Features

- **Search for Songs**: Enter a song title to receive recommendations based on that track.
- **Track Recommendations**: Fetch and display song recommendations using Spotify's API.
- **User Interface**: Console-based UI with progress indicators and styled output using Rich.

## Requirements

- Python 3.x
- `spotipy` library for interacting with the Spotify API
- `rich` library for console output and progress indicators

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NotAbhra/SongSift-Rich.git
   ```

2. Navigate to the project directory:

   ```bash
   cd SongSift-Rich
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Replace the placeholder `client_id` and `client_secret` in the code with your own Spotify credentials.

## Usage

1. Run the script:

   ```bash
   python song_sift.py
   ```

2. Enter a song title when prompted.

3. View the recommendations displayed in a table format.

4. Decide whether you want to search for more songs or exit the application.

## Example

```
Enter your song: Shape of You
[progress] Fetching recommendations...
Track Name                    | Artist
------------------------------|---------------------------
Shape of You (Remix)          | Ed Sheeran
Perfect                      | Ed Sheeran
Castle on the Hill            | Ed Sheeran
...

Wanna go again? (yes/no): no
Goodbye!
```

## Screenshot

![image](https://github.com/user-attachments/assets/5cd004b7-2ec5-4eb5-80b7-82e28f259669)


## Notes

- Ensure you have a Spotify Developer account and create a new application to get your `client_id` and `client_secret`.
- The script will prompt for user input in the command line and will continue running until you choose to exit.

## License

This project is licensed under the MIT License. 

## Contributing

Feel free to fork the repository and submit pull requests. For issues or feature requests, please open an issue in the GitHub repository.

