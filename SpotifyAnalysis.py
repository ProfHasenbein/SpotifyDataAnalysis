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

counter_songs = {}
rank_songs = 1

for entry in daten:
    song_name = entry.get("master_metadata_track_name")
    artist_name = entry.get("master_metadata_album_artist_name")
    
    if song_name and artist_name:
        duration = entry.get("ms_played", 0)
        
        if (song_name, artist_name) in counter_songs:
            counter_songs[(song_name, artist_name)]["count"] += 1
            counter_songs[(song_name, artist_name)]["time"] += duration
        else:
            counter_songs[(song_name, artist_name)] = {"count": 1, "time": duration}

sorted_songs = sorted(counter_songs.items(), key=lambda x: x[1]["count"], reverse=True)

top_15_songs = sorted_songs[:15]
for (song, artist), data in top_15_songs:
    
    songs_total_minutes = data["time"] / 1000 / 60
    songs_total_hours = songs_total_minutes / 60

    print(f"{NUMBER}{rank_songs}.{RESET} '{song}' by {artist} {IMPORTANT}{data['count']}x {RESET}||{IMPORTANT} {songs_total_minutes:.2f} min {RESET}||{IMPORTANT} {songs_total_hours:.2f}h {RESET}streamed")
    rank_songs += 1


print(f"\n{HEADER}---------------Most skipped songs---------------{RESET}\n")

sorted_skipped_songs = sorted(skipped_songs.items(), key=lambda x: x[1], reverse=True)

for rank, (song, count) in enumerate(sorted_skipped_songs[:10], start=1):
    for entry in daten:
        if entry.get("master_metadata_track_name") == song:
            artist = entry.get("master_metadata_album_artist_name", "Unknown Artist")
            break 

    print(f"{NUMBER}{rank}.{RESET} '{song}' by {artist} {IMPORTANT}{count}x {RESET} skipped")


print(f"\n{HEADER}---------------Most played artists---------------{RESET}\n")

counterSS = 1  # Swiftie Stats counter
counter_artists = {}
rank_artists = 1  

for entry in daten:
    if "master_metadata_album_artist_name" in entry:
        artist_name = entry["master_metadata_album_artist_name"]
        
        if artist_name is not None:
            if artist_name in counter_artists:
                counter_artists[artist_name]["count"] += 1
                if "ms_played" in entry:
                    counter_artists[artist_name]["time"] += entry["ms_played"]
            else:
                counter_artists[artist_name] = {"count": 1, "time": entry.get("ms_played", 0)}
            
        if artist_name == "Taylor Swift":  # Swiftie Stats counter
            counterSS += 1

sorted_artists = sorted(counter_artists.items(), key=lambda x: x[1]["time"], reverse=True)

top_10_artists = sorted_artists[:15]
for artist, data in top_10_artists:
    
    total_minutes = data["time"] / 1000 / 60
    total_hours = data["time"] / 1000 / 60 / 60

    print(f"{NUMBER}{rank_artists}.{RESET} '{artist}' {IMPORTANT}{data['count']}x {RESET}|| {IMPORTANT}{total_minutes:.2f} min {RESET}|| {IMPORTANT}{total_hours:.2f} h {RESET}streamed ")
    rank_artists += 1


print(f"\n{HEADER}---------------Devices used for Spotify---------------{RESET}\n")

counter_devices = {}
rank_devices = 1

for entry in daten:
    if "platform" in entry:
        user_agent = entry["platform"]

        if user_agent in counter_devices:
            counter_devices[user_agent] += 1
        else:
            counter_devices[user_agent] = 1

sorted_agents = sorted(counter_devices.items(), key=lambda x: x[1], reverse=True)

top_10_agents = sorted_agents[:10]
for agent, count in top_10_agents:
    print(f"{NUMBER}{rank_devices}.{RESET}'{agent}' {IMPORTANT}{count}x{RESET}")
    rank_devices += 1


print(f"\n{HEADER}---------------Countries listened in---------------{RESET}\n")

counter_countries = {}
rank_countries = 1

for entry in daten:
    if "conn_country" in entry:
        country = entry["conn_country"]

        if country in counter_countries:
            counter_countries[country] += 1
        else:
            counter_countries[country] = 1

sorted_countries = sorted(counter_countries.items(), key=lambda x: x[1], reverse=True)

top_10_countries = sorted_countries[:10]
for country, count in top_10_countries:
    print(f"{NUMBER}{rank_countries}.{RESET} '{country}' {IMPORTANT}{count}x{RESET}")
    rank_countries += 1


print(f"\n{HEADER}---------------Top Genres---------------{RESET}\n") # Not working just yet

# Spotify API Credentials
CLIENT_ID = ""
CLIENT_SECRET = ""

print(f"\n{HEADER}---------------Reasons for Song End---------------{RESET}\n")

counter_end_reasons = {} 
rank_end_reasons = 1 

for entry in daten:
    if "reason_end" in entry:
        reason = entry["reason_end"]

        if reason in counter_end_reasons:
            counter_end_reasons[reason] += 1
        else:
            counter_end_reasons[reason] = 1

sorted_reasons = sorted(counter_end_reasons.items(), key=lambda x: x[1], reverse=True)

for reason, count in sorted_reasons:
    print(f"{NUMBER}{rank_end_reasons}.{RESET} '{reason}' {IMPORTANT}{count}x{RESET}")
    rank_end_reasons += 1


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