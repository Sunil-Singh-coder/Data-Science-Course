---------------------------------------Today Agenda------------------------------------
1. Download Video from Youtube 
2. Convert that video into audio 



<--------------------------------1.Download Video from Youtube--------------------------------
 i )-> pip install yt-dlp
 ii)->yt-dlp "PLAYLIST_URL"  
   --> URLhttps://youtube.com/playlist?list=PLu0W_9lII9agq5TrH9XLIKQvv0iaF2X3w&si=LqW8RM-JqEmPwqsc

# for 20 video
 yt-dlp --playlist-items 1-20 "PLAYLIST_URL"v

# for audio from youtube
yt-dlp -x --audio-format mp3 --playlist-items 1-20 "PLAYLIST_URL"



<--------------------------------1.Convert Video into auido--------------------------------
If you have video then you have to convert in audio form 
NOTE:--> For Conversion of vodeo to audio we can use FFmpeg for this work  