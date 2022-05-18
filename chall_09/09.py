from pwn import *
binary = context.binary = ELF('./chall_09')
p = process(binary.path)
bhex = bytes.fromhex("3d01001a49001a074e1d49191e0700070e491d01001a49001a491b0c1f0c1b1a00070e454905000f0c49001a49084905000c")
p.sendline(xor(bhex, b'\x69'))
#string needs to be gotten manually you can set a break point at the 
#key. You need to check the stack and get the key value
p.interactive()
#FINISHED
