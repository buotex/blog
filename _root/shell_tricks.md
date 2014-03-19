{
  "title": "Shell tricks",
  "date": "2013-12-06",
  "categories": [
    
  ],
  "tags": [
  "tricks"    
  ]
}

`find . -name "*"`
: Search for file in current path and subdirectories


`tree -P "*foo"`
: Search for filename, with a tree diagram


`pdftk rtree_1.pdf cat 1-endeast output rtree_1rotated.pdf`
: Rotate all pages of a pdf by 90 degrees.


`source ~/.oh-my-zsh/custom/cmdline.zsh` 
: reload the cmdline plugin


`vim --servername MAIN --remote-send ":PomodoroStart()<CR>"` 
: send a command to the vim server session with the name MAIN

`wget -r --no-parent ftp://slackbuilds.org/14.1/source/l/qt/` 
: Download folder with wget

`sshfs hci:/home/users/mip/data ../mip` 
: sshfs link

`convert 0049_cam.tiff -resize 50% 0049_cam.png` 
: resize image to 50% of original size while converting it to png

`plt.xlabel("Microscope Column",fontsize = 30)` 
: How to set the xlabel of a plot in matplotlib

