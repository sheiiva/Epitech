;
; EPITECH PROJECT, 2018
; ASM - MiniLibC
; File description:
; my_strcmp.asm
;

BITS 64

section .text
global strcmp

strcmp:
    xor rcx, rcx
    xor r8, r8

.loop:
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

.RETURN:
    sub al, r8b
    movsx rax, al
    ret