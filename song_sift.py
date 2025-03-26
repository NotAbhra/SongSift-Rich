import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from time import sleep

console = Console()

client_id = "your_client_id"
client_secret = "client_secret_id"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
console.print("This is [bold magenta]songsift[/bold magenta]!!, we recommend tracks based on your taste in music. Enter a song to tickle your wonder.....")

def get_recommendations(track_name):
    results = sp.search(q=track_name, type='track')
    if not results['tracks']['items']:
        console.print(f"No results found for '{track_name}'", style="bold red")
        return []

    track_uri = results['tracks']['items'][0]['uri']
    recommendations = sp.recommendations(seed_tracks=[track_uri])['tracks']
    return recommendations

while True:
    songname = input("Enter your song: ")

  
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console) as progress:
        task = progress.add_task("[bold green]Fetching recommendations...", start=False)
        progress.start_task(task)
        
        
        sleep(2)
        recommendations = get_recommendations(songname)
        progress.stop()

    if recommendations:
        table = Table(title="Song Recommendations")

        table.add_column("Track Name", style="green", no_wrap=True)
        table.add_column("Artist", style="red", no_wrap=True)

        for track in recommendations:
            table.add_row(track['name'], track['artists'][0]['name'])

        console.print(table)
    else:
        console.print(f"No recommendations found for '{songname}'", style="bold red")
    
    again = input("Wanna go again? (yes/no): ").strip().lower()
    if again != 'yes':
        console.print("Goodbye!", style="bold red")
        break
