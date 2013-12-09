import evernote
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
import binascii,hashlib, mimetypes
developer_token = "S=s14:U=19e32f:E=14a2c91b921:C=142d4e08d25:P=1cd:A=en-devtoken:V=2:H=5bbc678525612663ac9f267a42a4f997"
 
# Set up the NoteStore client 
client = EvernoteClient(sandbox=False, token=developer_token)
note_store = client.get_note_store()
 
note = Types.Note()
note.title = "Test note from EDAMTest.py"
image = open('./test.pdf', 'rb').read()
md5 = hashlib.md5()
md5.update(image)
hash = md5.digest()

data = Types.Data()
data.size = len(image)
data.bodyHash = hash
data.body = image

resource = Types.Resource()
resource.mime = 'image/png'
resource.data = data

# Now, add the new Resource to the note's list of resources
note.resources = [resource]

# To display the Resource as part of the note's content, include an <en-media>
# tag in the note's ENML content. The en-media tag identifies the corresponding
# Resource using the MD5 hash.
hash_hex = binascii.hexlify(hash)

# The content of an Evernote note is represented using Evernote Markup Language
# (ENML). The full ENML specification can be found in the Evernote API Overview
# at http://dev.evernote.com/documentation/cloud/chapters/ENML.php
note.content = '<?xml version="1.0" encoding="UTF-8"?>'
note.content += '<!DOCTYPE en-note SYSTEM ' \
    '"http://xml.evernote.com/pub/enml2.dtd">'
note.content += '<en-note>Here is the Evernote logo:<br/>'
note.content += '<en-media type="application/pdf" hash="' + hash_hex + '"/>'
note.content += '</en-note>'

# Finally, send the new note to Evernote using the createNote method
# The new Note object that is returned will contain server-generated
# attributes such as the new note's unique GUID.
created_note = note_store.createNote(note)
