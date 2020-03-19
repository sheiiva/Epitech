;
; EPITECH PROJECT, 2018
; ASM - MiniLibC
; File description:
; my_strcspn.asm
;

BITS 64

section .text
global strcspn

strcspn:
    xor rcx, rcx
    xor r8, r8
    jmp .LOOP

.SUBINCREMENT:
    inc r9
    jmp .SUBLOOP

.SUBLOOP:
    mov r8b, BYTE [rsi+r9]
    cmp r8b, 0
    je .LOOP
    cmp r8b, al
    jne .SUBINCREMENT
    dec rcx
    jmp .RETURN

.LOOP:
    mov al, BYTE [rdi+rcx]
    cmp al, 0
    je .RETURN
    inc rcx
    xor r9, r9
    jmp .SUBLOOP

.RETURN:
    mov eax, ecx
    ret