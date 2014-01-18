{
  "title": "Vim",
  "date": "2014-01-18",
  "categories": [
    "tricks"
  ],
  "tags": [
    "setup"
  ]
}

##Setup

~~~ shell
cd #go home
`git clone https://github.com/buotex/dotvim .vim`
cd .vim
. initialize #init vundle
vim +BundleInstall +qall
~~~

##Fontconfig for vim-airline 

``zsh .vim/fontconfig``
- Switch to Terminess font in the console, size 10


##Youcomplete me
``zsh .vim/ycm``


~~~vim
- ``5i#<ESC>`` to create ##### heading
- ``s/[A-Z]\{2,} /\L&/g`` Replace all uppercase words with at least 2 letters to their 
  lowercase variant
- ``s/\([A-Z]\)\([A-Z]\{1,}\) /\1\L\2 /g`` Turn uppercase word into Upper+lowercase
~~~

~~~vim
- ``spar<TAB>`` expands to a snippet to write the section name in markdown
~~~
##TODO:

{{#todo_block}}
- [] Fix vim-internal syntax highlighting for embedded code blocks
- [] 
{{/todo_block}}
