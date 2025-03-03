import json

#change file location here:
files = [
    "/home/nibblus/Documents/SpotifyData/Spotify Extended Streaming History/Streaming_History_Audio_2021-2023_0.json",
    "/home/nibblus/Documents/SpotifyData/Spotify Extended Streaming History/Streaming_History_Audio_2023-2024_1.json",
    "/home/nibblus/Documents/SpotifyData/Spotify Extended Streaming History/Streaming_History_Audio_2024-2025_2.json"
]
#up there ^

daten = []

for file_name in files:
    with open(file_name, "r", encoding="utf-8") as file:
        daten.extend(json.load(file)) 

print(f"\n---------------General information---------------\n")

total_ms = sum(entry["ms_played"] for entry in daten)

total_minutes = total_ms / (1000 * 60)
total_hours = total_minutes / 60
total_days = total_hours /24

print(f"Total listening time: {total_minutes:.2f} minutes || {total_hours:.2f} hours || {total_days:.0f} days")

total_skipped = 0
for entry in daten:
    if entry["skipped"] == True:
        total_skipped += 1

print(f"{total_skipped}x songs skipped")

print(f"\n---------------Most played artists---------------\n")

count_dict = {}
rank = 1

for entry in daten:
    if "master_metadata_album_artist_name" in entry:
        artist_name = entry["master_metadata_album_artist_name"]
        
    if artist_name != None:
        if artist_name in count_dict:
            count_dict[artist_name] += 1
        else:
            count_dict[artist_name] = 1

sorted_artists = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

top_10_artists = sorted_artists[:15]
for artist, count in top_10_artists:
    print(f"{rank}. '{artist}' {count}x streamed")
    rank+= 1


print(f"\n---------------Devices used for Spotify---------------\n") 

count2_dict = {}
rank2 = 1

for entry in daten:
    if "platform" in entry:
        user_agent = entry["platform"]
        
        if user_agent in count2_dict:
            count2_dict[user_agent] += 1
        else:
            count2_dict[user_agent] = 1

sorted_agents = sorted(count2_dict.items(), key=lambda x: x[1], reverse=True)

top_10_agents = sorted_agents[:10]
for agent, count in top_10_agents:
    print(f"{rank2}. '{agent}' {count}x")
    rank2 += 1
