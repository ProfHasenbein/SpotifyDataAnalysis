import json

# Change file locations here:
files = [
    "/home/nibblus/Documents/SpotifyData/Spotify Extended Streaming History/Streaming_History_Audio_2021-2023_0.json",
    "/home/nibblus/Documents/SpotifyData/Spotify Extended Streaming History/Streaming_History_Audio_2023-2024_1.json",
    "/home/nibblus/Documents/SpotifyData/Spotify Extended Streaming History/Streaming_History_Audio_2024-2025_2.json"
]
# Up there ^

# ANSI codes for colors
RESET = "\033[0m"
CERO = "\033[95m"
UNO = "\033[94m"  
DOS = "\033[92m" 
TRES = "\033[93m"
CINCO = "\033[91m"
BOLD = "\033[1m"

HEADER = TRES + BOLD
IMPORTANT = UNO + BOLD
NUMBER = CERO + BOLD


daten = []

# Load data from each JSON file into list
for file_name in files:
    with open(file_name, "r", encoding="utf-8") as file:
        daten.extend(json.load(file))


print(f"\n{HEADER}---------------General information---------------{RESET}\n")

total_songs = len(daten)  
print(f"Total songs listened: {total_songs} songs")

total_ms = sum(entry["ms_played"] for entry in daten)

total_minutes = total_ms / (1000 * 60)
total_hours = total_minutes / 60
total_days = total_hours / 24

print(f"Total listening time: {total_minutes:.2f} minutes || {total_hours:.2f} hours || {round(total_days)} days")

total_skipped = 0
skipped_songs = {}
skipped_artists = {}

for entry in daten:
    if entry.get("skipped", False):
        total_skipped += 1
        skipped_song_name = entry.get("master_metadata_track_name", "Unknown")
        artist_name = entry.get("master_metadata_album_artist_name", "Unknown Artist")

        if skipped_song_name and artist_name:
            if skipped_song_name in skipped_songs:
                skipped_songs[skipped_song_name] += 1
            else:
                skipped_songs[skipped_song_name] = 1
                
            if artist_name in skipped_artists:
                skipped_artists[artist_name] += 1
            else:
                skipped_artists[artist_name] = 1

print(f"Total songs skipped: {total_skipped} songs")


print(f"\n{HEADER}---------------Most played Songs---------------{RESET}\n")

counter0 = {}
rank0 = 1

for entry in daten:
    song_name = entry.get("master_metadata_track_name")
    artist_name = entry.get("master_metadata_album_artist_name")

    if song_name and artist_name:
        if (song_name, artist_name) in counter0:
            counter0[(song_name, artist_name)] += 1
        else:
            counter0[(song_name, artist_name)] = 1 

sorted_songs = sorted(counter0.items(), key=lambda x: x[1], reverse=True)

top_10_songs = sorted_songs[:15]
for (song0, artist), count in top_10_songs:
    print(f"{NUMBER}{rank0}.{RESET} '{song0}' by {artist} {IMPORTANT}{count}x {RESET}streamed")
    rank0 += 1


print(f"\n{HEADER}---------------Most skipped songs---------------{RESET}\n")

# Sortiere und zeige die meistübersprungenen Songs an
sorted_skipped_songs = sorted(skipped_songs.items(), key=lambda x: x[1], reverse=True)
for rank, (song, count) in enumerate(sorted_skipped_songs[:10], start=1):
    # Finde den Künstlernamen für das aktuelle Lied
    for entry in daten:
        if entry.get("master_metadata_track_name") == song:
            artist = entry.get("master_metadata_album_artist_name", "Unknown Artist")
            break 
    print(f"{NUMBER}{rank}.{RESET} '{song}' by {artist} {IMPORTANT}{count}x {RESET} skipped")


print(f"\n{HEADER}---------------Most played artists---------------{RESET}\n")

counterSS = 1 #Swiftie Stats counter
counter = {}
rank = 1

for entry in daten:
    if "master_metadata_album_artist_name" in entry:
        artist_name = entry["master_metadata_album_artist_name"]

    if artist_name is not None:
        if artist_name in counter:
            counter[artist_name] += 1
        else:
            counter[artist_name] = 1
    if artist_name == "Taylor Swift":  # SS counter
        counterSS += 1 



sorted_artists = sorted(counter.items(), key=lambda x: x[1], reverse=True)

top_10_artists = sorted_artists[:15]
for artist, count in top_10_artists:
    print(f"{NUMBER}{rank}.{RESET} '{artist}' {IMPORTANT}'{count}x{RESET} streamed")
    rank += 1

print(f"\n{HEADER}---------------Devices used for Spotify---------------{RESET}\n")

counter2 = {}
rank2 = 1

for entry in daten:
    if "platform" in entry:
        user_agent = entry["platform"]

        if user_agent in counter2:
            counter2[user_agent] += 1
        else:
            counter2[user_agent] = 1

sorted_agents = sorted(counter2.items(), key=lambda x: x[1], reverse=True)

top_10_agents = sorted_agents[:10]
for agent, count in top_10_agents:
    print(f"{NUMBER}{rank2}.{RESET}'{agent}' {IMPORTANT}{count}x{RESET}")
    rank2 += 1

print(f"\n{HEADER}---------------Countries listened in---------------{RESET}\n")

counter3 = {}
rank3 = 1

for entry in daten:
    if "conn_country" in entry:
        country = entry["conn_country"]

        if country in counter3:
            counter3[country] += 1
        else:
            counter3[country] = 1

sorted_countries = sorted(counter3.items(), key=lambda x: x[1], reverse=True)

top_10_countries = sorted_countries[:10]
for country, count in top_10_countries:
    print(f"{NUMBER}{rank3}.{RESET} '{country}' {IMPORTANT}{count}x{RESET}")
    rank3 += 1

print(f"\n{HEADER}---------------SS - Swiftie Stats---------------{RESET}\n")

taylor_swift_songs = {} 

for entry in daten:
    artist_name = entry.get("master_metadata_album_artist_name")
    song_name = entry.get("master_metadata_track_name")

    if artist_name == "Taylor Swift" and song_name:
        if song_name in taylor_swift_songs:
            taylor_swift_songs[song_name] += 1
        else:
            taylor_swift_songs[song_name] = 1

print(f"Total Taylor Swift songs listened: {counterSS}\n")

rankSS = 1

for song, count in sorted(taylor_swift_songs.items(), key=lambda x: x[1], reverse=True)[:20]:
    print(f"{NUMBER}{rankSS}.{RESET} '{song}' {IMPORTANT}{count}x{RESET} streamed")
    rankSS += 1

logo= r"""
+--------------------------------------------------------+
|┌─┐┌─┐┌─┐┌┬┐┬┌─┐┬ ┬  ┌┬┐┌─┐┌┬┐┌─┐  ┌─┐┌┐┌┌─┐┬ ┬ ┬┌─┐┬┌─┐|
|└─┐├─┘│ │ │ │├┤ └┬┘   ││├─┤ │ ├─┤  ├─┤│││├─┤│ └┬┘└─┐│└─┐|
|└─┘┴  └─┘ ┴ ┴└   ┴   ─┴┘┴ ┴ ┴ ┴ ┴  ┴ ┴┘└┘┴ ┴┴─┘┴ └─┘┴└─┘|
+--------------------------------------------------------+
"""
print("\n" + logo)
print("written by ProfHasenbein")
print("https://github.com/ProfHasenbein/SpotifyDataAnalysis")