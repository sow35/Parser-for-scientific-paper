#!/bin/sh
[ $UID -ne 0 ] && echo "This script must be run as root" && exit
which pacman && pacman --noconfirm -S python-pdftotext
