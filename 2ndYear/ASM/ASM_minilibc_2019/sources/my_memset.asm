;
; EPITECH PROJECT, 2018
; ASM - MiniLibC
; File description:
; my_memset.asm
;

BITS 64

section .text
global memset

memset:
    xor rcx, rcx
    jmp .loop

.loop:
    cmp rcx, rdx
    je .RETURN
    mov BYTE [rdi+rcx], sil
    jmp .INCREMENT

.INCREMENT:
    inc rcx
    jmp .loop

.RETURN:
    ret