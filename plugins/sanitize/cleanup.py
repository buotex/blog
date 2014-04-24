#Check for all markdown files in posts if they have a correct yaml header
import datetime
import fnmatch
import os

header = """{{
  "title": "Placeholder",
  "date": "{0}",
  "categories": [
    "unsorted"
  ],
  "tags": [
    
  ]
}}

""".format(datetime.date.today().isoformat())


filelist = []
for root, dirnames, filenames in os.walk('posts'):
      for filename in fnmatch.filter(filenames, '*.markdown'):
                filelist.append(os.path.join(root, filename))
      for filename in fnmatch.filter(filenames, '*.md'):
                filelist.append(os.path.join(root, filename))

for f in filelist:
    with open(f,'r') as filehandle:
        temp = filehandle.read()

    if temp[0] is not '{':
        with open(f,'w') as filehandle:
            filehandle.write(header)
            filehandle.write(temp)



