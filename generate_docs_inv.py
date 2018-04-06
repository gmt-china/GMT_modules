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
# Version: 5.4.3
# The remainder of this file is compressed with zlib.
'''.encode('utf-8')

docs = {
    'configurations': 'configurations',
    'embellishments': 'basic/embellishments',
    'grid-data': 'io/grid-data',
    'vectors': 'basic/vectors',
    'cpt': 'io/cpt',
    'text': 'basic/text',
    'character-escape': 'basic/character-escape',
    'special-fonts': 'basic/special-fonts',
    'special-characters': 'basic/special-characters',
    'anchors': 'basic/anchors',
    'pen': 'basic/pen',
    'lines': 'basic/lines',
    'fill': 'basic/fill',
    'unit': 'basic/unit',
    'option-binary': 'option/binary',
    'option-n': 'option/n'
}

payload_list = []
for key, value in docs.items():
    payload_list.append('{0} std:label -1 {1} {0}\n'.format(key, value))

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
