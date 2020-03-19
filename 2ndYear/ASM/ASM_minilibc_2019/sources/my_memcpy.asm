;
; EPITECH PROJECT, 2018
; ASM - MiniLibC
; File description:
; my_memcpy.asm
;

BITS 64

section .text
global memcpy

memcpy:
    xor rcx, rcx
    xor r8, r8
    jmp .checkargs
    jmp .loop

.checkargs:
    cmp rsi, 0
    je .RETURN
    cmp rdi, 0
    je .RETURN

.loop:
    cmp rcx, rdx
    je .RETURN
    mov r8b, BYTE[rsi+rcx]
    mov BYTE [rdi+rcx], r8b
    jmp .INCREMENT

.INCREMENT:
    inc rcx
    jmp .loop

.RETURN:
    mov rax, rdi
    ret