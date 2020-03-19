;
; EPITECH PROJECT, 2018
; ASM - MiniLibC
; File description:
; my_strpbrk.asm
;

BITS 64

section .text
global strpbrk

strpbrk:
	cmp rdi, 0
	je .RETURN_NULL
	cmp rsi, 0
	je .RETURN_NULL
    xor rcx, rcx
    jmp .LOOP

.SUBINCREMENT:
    inc r8
    jmp .SUBLOOP

.SUBLOOP:
    cmp BYTE [rsi+r8], 0
    je .LOOP
    cmp BYTE [rsi+r8], al
    jne .SUBINCREMENT
    dec rcx
    jmp .RETURN

.SEARCH:
    inc rcx
    xor r8, r8
    jmp .SUBLOOP

.LOOP:
    mov al, BYTE [rdi+rcx]
    cmp al, 0
    je .RETURN_NULL
	jmp .SEARCH

.RETURN:
	add rdi, rcx
	mov rax, rdi
	ret

.RETURN_NULL:
    xor rax, rax
    ret