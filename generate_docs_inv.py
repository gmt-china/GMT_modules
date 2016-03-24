#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Python Script to generate inventory file for docs.gmt-china.org
#
# http://pvbookmarks.readthedocs.org/en/master/devel/documentation/doc_generators/sphinx/rest_sphinx/hyperlinks.html
#

import zlib
inventory_header = '''\
# Sphinx inventory version 2
# Project: GMT
# Version: 5.2.1
# The remainder of this file is compressed with zlib.
'''.encode('utf-8')

docs = ['configurations', 'embellishments', 'grid-data', 'option-n', 'vectors',
        'cpt', 'text', 'character-escape', 'special-fonts', 'special-characters',
        'anchors', 'pen', 'lines',
       ]

payload_list = []
for item in docs:
    payload_list.append('{0} std:label -1 {0}.html {0}\n'.format(item))

inventory_payload = ''.join(payload_list).encode('utf-8')

# inventory_payload lines spec:
#   name domainname:type priority uri dispname
#
# * `name`     -- fully qualified name
# * `dispname` -- name to display when searching/linking
# * `type`     -- object type, a key in ``self.object_types``
# * `docname`  -- the document where it is to be found
# * `anchor`   -- the anchor name for the object
# * `priority` -- how "important" the object is
#                       (determines placement in search results)
#
#   - 1: default priority (placed before full-text matches)
#   - 0: object is important (placed before default-priority objects)
#   - 2: object is unimportant (placed after full-text matches)
#   - -1: object should not show up in search at all
#

inventory = inventory_header + zlib.compress(inventory_payload)
open('source/docs.inv', 'wb').write(inventory)
