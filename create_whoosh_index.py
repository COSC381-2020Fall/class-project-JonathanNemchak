import os
import sys
import json

from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID

Schema = Schema(id=ID(stored=True), title=TEXT(stored=True), description=TEXT(stored=True))

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = create_in("indexdir", Schema)
writer = ix.writer()

with open('data_for_indexing.json') as f:
    youtube_array = json.load(f)
    for item in youtube_array:
        writer.add_document(id=item['id'], title=item['title'], description=item['description'])

writer.commit()