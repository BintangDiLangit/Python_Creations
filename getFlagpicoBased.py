from pwn import *

shell = remote('2019shell1.picoctf.com',28758)

biner = shell.recvuntil('Input:\n').split('\n')[2].split(' ')[3:-3]
biner = ''.join(map(lambda x:chr(int(x,2)),biner))  # 2 => biner
shell.sendline(biner)

octal = shell.recvuntil('Input:\n').split('\n')[0].split('the  ')[-1].split(' as')[0].split(' ')
octal = ''.join(map(lambda x: chr(int(x, 8)), octal))
shell.sendline(octal)

hexa = shell.recvuntil('Input:\n').split('\n')[0].split('the ')[-1].split(' as')[0]
hexa = hexa.decode('hex')
shell.sendline(hexa)

shell.interactive()