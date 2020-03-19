;
; EPITECH PROJECT, 2018
; ASM - MiniLibC
; File description:
; my_strlen.asm
;

BITS 64

section .text
global strlen

strlen:
    xor ecx, ecx
    jmp .LOOP

.INCREMENT:
    inc ecx
    jmp .LOOP

.LOOP:
    movsx rdx, ecx
    mov al, BYTE [rdi+rdx]
    cmp al, 0
    jne .INCREMENT
    jmp .RETURN

.RETURN:
    mov eax, ecx
    ret