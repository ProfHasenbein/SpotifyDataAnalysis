```
             ___      ___    ___    _____    ___      ___  __   __
    o O O   / __|    | _ \  / _ \  |_   _|  |_ _|    | __| \ \ / /
   o        \__ \    |  _/ | (_) |   | |     | |     | _|   \ V / 
  TS__[O]   |___/   _|_|_   \___/   _|_|_   |___|   _|_|_   _|_|_ 
 {======| _|"""""|_| """ |_|"""""|_|"""""|_|"""""|_| """ |_| """ |
./o--000' "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'
```
---                                                                                                                                                                                                      
                                                                                                                                                                                                      
## Have you ever wondered if you're a real Swiftie?

Then you've come to the right place!
Whether you're a Taylor Swift fan or not, I've got the perfect way to find out about your listening habits

This Python script will list your...:
  
  └─ total streaming time

  └─ Most played artists
 
  └─ Devices, you used for Spotify

... and so much more!
  

Now comes the best part: All this **for free**! Unlike stats.fm or some other platform I won't charge you anything (it would still be nice if you could spare me a star UwU...)

---

# How to use the script

1. **Download your Spotify data**  
   First, head over to Spotify and download your personal streaming data. You can do this via [Spotify's Data Export Page](https://www.spotify.com/us/account/privacy/). After about one week you'll receive a ZIP file with your entire streaming history

   **_Sidenote:_** Depending on what you've selected on the Data Export Page, you'll receive multiple emails. Unfortunately, all of the download folders are named the same, so make sure to download the one that contains the "Spotify Extended Streaming History" folder.

3. **Install Python**  
   Make sure you have Python installed on your system. If you don't, download and install it from [python.org](https://www.python.org/downloads/)

4. **Clone or Download the script**  
   Clone or download this repository to your local machine. You can use `git clone https://github.com/ProfHasenbein/SpotifyDataAnalysis.git` or simply download the ZIP and extract it.

5. **Prepare your Data**  
   Extract the data from Spotify into a folder. You’ll need the `Streaming_History_Audio_YEAR-YEAR.json` files to use this script.

6. **Link the files**  
   Open the script in your preferred text editor and change the filenames to match the location of your data:
   ![image](https://github.com/user-attachments/assets/d0ab92e7-8af6-4c46-9033-1dc086f7d813)
(if the script and your streaming history files are in the same folder, the relative path is enough)

7. **Run the Script**  
   Open your terminal or command prompt, navigate to the folder where you have the script and your data, and run:

   ```bash
   python SpotifyAnalysis.py
