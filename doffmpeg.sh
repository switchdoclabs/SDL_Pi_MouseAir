
ffmpeg -i http://localhost:8088/stream.mjpg -v 200 -vcodec h264 -f rtsp -rtsp_transport tcp rtsp://localhost:23000

#ffmpeg -i "http://localhost:8088/stream.mjpg" -f rtsp -rtsp_transport tcp rtsp://localhost:8888/live.sdp


#ffmpeg -i "http://localhost:8088/stream.mjpg" -vcodec libx264 -vb 150000 -g 60 -vprofile baseline -level 2.1 -vbsf h264_mp4toannexb -strict experimental -f rtsp rtsp://127.0.0.1:10100/live/myStream.sdp 

#ffmpeg -re -i "http://localhost:8088/stream.mjpg"  -f rtsp -muxdelay 0.1 rtsp://localhost:10100/live.sdp
#ffmpeg -re -i "http://localhost:8088/stream.mjpg"  -f rtsp rtsp://localhost:10100/live.sdp

#ffmpeg -i "http://localhost:8088/stream.mjpg" -vcodec libx264 -vb 150000 -g 60 -vprofile baseline -level 2.1 -acodec aac -ab 64000 -ar 48000 -ac 2 -vbsf h264_mp4toannexb -strict experimental -f rtsp rtsp://127.0.0.1:10100/live/myStream.sdp 
#ffmpeg -i "http://localhost:8088/stream.mjpg" -vcodec libx264 -vb 150000 -g 60 -vprofile baseline -level 2.1 -acodec aac -ab 64000 -ar 48000 -ac 2 -vbsf h264_mp4toannexb -strict experimental -f rtsp rtsp://localhost:10100 

#ffmpeg -i "http://localhost:8088" -pix_fmt yuv420p -deinterlace -vf "scale=640:360" -vsync 1 -threads 0 -vcodec libx264 -r 29.970 -g 60 -sc_threshold 0 -b:v 1024k -bufsize 1216k -maxrate 1280k -preset medium -profile: v main -tune film -acodec aac -b:a 128k -ac 2 -ar 48000 -af "aresample=async=1:min_hard_comp=0.100000:first_pts=0" -vbsf h264_mp4toannexb -f mpegts udp://127.0.0.1:10000

