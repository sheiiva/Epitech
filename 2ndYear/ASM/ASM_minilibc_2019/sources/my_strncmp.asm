;
; EPITECH PROJECT, 2018
; ASM - MiniLibC
; File description:
; my_strncmp.asm
;

BITS 64

section .text
global strncmp

strncmp:
    xor rcx, rcx
    xor r8, r8
    cmp rcx, rdx
    je .RETURN_NULL
    jmp .loop

.loop:
    cmp rcx, rdx
    je .RETURN
    mov al, BYTE[rdi, rcx]
    mov r8b, BYTE[rsi, rcx]
    cmp al, 0
    je .RETURN
    cmp al, r8b
    jne .RETURN
    jmp .INCREMENT

.INCREMENT:
    inc rcx
    jmp .loop

.RETURN_NULL:
    mov rax, 0
    ret

.RETURN:
    sub al, r8b
    movsx rax, al
    ret