;
; EPITECH PROJECT, 2018
; ASM - MiniLibC
; File description:
; my_strcasecmp.asm
;

BITS 64

section .text
global strcasecmp

strcasecmp:
    xor rcx, rcx
    xor r8, r8

.loop:
    mov al, BYTE[rdi + rcx]
    mov r8b, BYTE[rsi + rcx]
    cmp al, 0
    je .RETURN
    cmp al, 'A'
    jge .TOLOWERCASE_FIRST
    jmp .CHECKSECOND

.INCREMENT:
    inc rcx
    jmp .loop

.LOWER_FIRST:
    add al, 32
    jmp .CHECKSECOND

.TOLOWERCASE_FIRST:
    cmp al, 'Z'
    jle .LOWER_FIRST
    jmp .CHECKSECOND

.LOWER_SECOND:
    add r8b, 32
    jmp .CHECKDIFF

.TOLOWERCASE_SECOND:
    cmp r8b, 'Z'
    jle .LOWER_SECOND
    jmp .CHECKDIFF

.CHECKSECOND:
    cmp r8b, 'A'
    jge .TOLOWERCASE_SECOND

.CHECKDIFF:
    cmp al, r8b
    jne .RETURN
    jmp .INCREMENT

.RETURN:
    sub al, r8b
    movsx rax, al
    ret