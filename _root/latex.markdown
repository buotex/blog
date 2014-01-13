{
  "title": "",
  "date": "2014-01-10",
  "categories": [
    
  ],
  "tags": [
   "latex" 
  ]
}

``\\*`` Linebreak, but not a new paragraph


Workarounds:
If the document is not readable via acrobat reader, set
``\pdfobjcompresslevel=0`` in the beginning of the .tex file.
An alternative is setting the pdfminorversion to 4, because pdf 1.4 works as
well.
Apparently a pdftex bug!?

