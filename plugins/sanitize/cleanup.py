#Check for all markdown files in posts if they have a correct yaml header
import datetime
import fnmatch
import os


header = """{{
  "title": "{0}",
  "date": "{1}",
  "categories": [
    "{2}"
  ],
  "tags": [

  ]
}}

"""


filelist = []
for root, dirnames, filenames in os.walk('posts'):
      for filename in fnmatch.filter(filenames, '*.markdown'):
                filelist.append(os.path.join(root, filename))
      for filename in fnmatch.filter(filenames, '*.md'):
                filelist.append(os.path.join(root, filename))

postspath=os.path.abspath('posts')

for f in filelist:
    with open(f,'r') as filehandle:
        temp = filehandle.read()

    if temp[0] is not '{':
        dirpath = os.path.dirname(f)
        title = os.path.splitext(os.path.basename(f))[0].title()
        today = datetime.date.today().isoformat()
        category = os.path.relpath(dirpath, postspath)

        with open(f,'w') as filehandle:
            filehandle.write(header.format(title, today, category))
            filehandle.write(temp)



