section .data
    msg:db 'Olá Programadores' ,10

section .text
    global _start

_start:
    mov rax,1
    mov rdi,1
    mov rsi,msg
    mov rdx,18
    syscall 
    mov rax,60
    xor rdi,rdi
    syscall
