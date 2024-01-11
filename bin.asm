section .data
    message db 'Hello, Assembly!', 0

section .text
    global _start

_start:
    ; Write the message to stdout
    mov eax, 4
    mov ebx, 1
    mov ecx, message
    mov edx, 16
    int 0x80

    ; Exit the program
    mov eax, 1
    xor ebx, ebx
    int 0x80
