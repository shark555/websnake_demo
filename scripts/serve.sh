#!/bin/sh
trap "echo -e '\nKONIEC!';killall -s SIGTERM serve.py;exit;" SIGINT
while [ true ]; do ./serve.py & inotifywait --exclude .+\.swp --exclude \.idea -e modify -r ../ *.py && killall serve.py && sleep 1; done
