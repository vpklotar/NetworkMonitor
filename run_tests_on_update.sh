#!/bin/bash
clear
while inotifywait -e close_write tests.py; do clear && ./tests.py; done
