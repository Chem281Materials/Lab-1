#!/bin/bash
docker run -it --rm -e DISPLAY=$DISPLAY --net=host -v /tmp/.X11-unix:/tmp/.X11-unix vim-x11-lab
