#/usr/local/bin/mjpg_streamer -i "/usr/local/lib/mjpg-streamer/input_uvc.so -n -f 10 -r 1280x720" \
 -o "/usr/local/lib/mjpg-streamer/output_http.so -p 8085 -w /usr/local/share/mjpg-streamer/www"
/usr/local/bin/mjpg_streamer -i "/usr/local/lib/mjpg-streamer/input_file.so -f /home/pi/SDL_Pi_MouseAir/static -e "   -o "/usr/local/lib/mjpg-streamer/output_http.so -p 8085 -w /usr/local/share/mjpg-streamer/www"

