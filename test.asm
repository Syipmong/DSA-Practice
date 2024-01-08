section .data
    message db 'Hello, World!', 0

section .text
    global _start

_start:
    ; write the message to stdout
    mov eax, 4
    mov ebx, 1
    mov ecx, message
    mov edx, 13
    int 0x80

    ; exit the program
    mov eax, 1
    xor ebx, ebx
    int 0x80



