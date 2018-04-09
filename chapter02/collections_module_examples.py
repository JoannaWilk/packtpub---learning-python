print("\n---------------------------\n")
print("the usual tuple\n")
vision = (9.5, 8.8)
print("vision = (9.5, 8.8). vision:", vision)
print("vision[0]:", vision[0])
print("vision[1]:", vision[1])
print("\n---------------------------\n")
print("the named tuple\n")

from collections import namedtuple
print("from collections import namedtuple")
Vision = namedtuple('Vision', ['left', 'right'])
print("Vision = namedtuple('Vision', ['left', 'right'])")
vision = Vision(9.5, 8.8)
print("vision = Vision(9.5, 8.8)")
print("vision[0]:", vision[0])
print("vision.left:", vision.left)
print("vision.right:", vision.right)

print("\n---------------------------\n")
print("the usual dictionary\n")
d = {}
print("d = {}. d:", d)
d['age'] = d.get('age', 0) + 1
print("d['age'] = d.get('age', 0) + 1\n"
      "d:", d)
d = {'age': 39}
print("d = {'age': 39}. d:", d)
d['age'] = d.get('age', 0) + 1
print("d['age'] = d.get('age', 0) + 1\n"
      "d:", d)

print("\n---------------------------\n")
print("the defaultdict\n")
from collections import defaultdict
print("from collections import defaultdict")
dd = defaultdict(int)
print("dd = defaultdict(int). dd:", dd)
dd['age'] += 1
print("dd['age'] += 1. dd:", dd)
dd['age'] = 39
print("dd['age'] = 39. dd:", dd)
dd['age'] += 1
print("dd['age'] += 1. dd:", dd)

print("\n---------------------------\n")
print("the ChainMap\n")
from collections import ChainMap
print("from collections import ChainMap")
default_connection = {'host': 'localhost', 'port': 4567}
print("default_connection = {'host': 'localhost', 'port': 4567}")
connection = {'port': 5678}
print("connection = {'port': 5678}")
conn = ChainMap(connection, default_connection)
print("map creation:\n"
      "conn = ChainMap(connection, default_connection)\n"
      "conn:", conn)
print("conn['port']:", conn['port'])
print("conn['host']:", conn['host'])
print("conn.maps:", conn.maps)
conn['host'] = 'packtpub.com'
print("conn['host'] = 'packtpub.com'\n"
      "conn.maps:", conn.maps)
del conn['port']
print("del conn['port']\n"
      "conn.maps:", conn.maps)
print("conn['port']:", conn['port'])
# the line below throws error
# only first list can be edited
# del conn['port']
print("dict(conn):", dict(conn))
