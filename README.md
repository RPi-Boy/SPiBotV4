# SPiBotV4
A Raspberry pi 3b/b+/4 controlled buggy.

To download anydesk client for your device please visit:
https://anydesk.com/en

get your pi's ip address by enterring:
hostname -I
in commandline interface

download vlc for pi by enterring the following command:
sudo apt install -y vlc

to start streaming enter the following command on the terminal:
raspivid -o - -t 0 -n | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264

To start network stream on your computer:
1) Press Ctrl+N
2) Enter rtsp://###.###.###.###:8554/ and replace the octothorpes with the ip address
3) Press play
