;
; EPITECH PROJECT, 2018
; ASM - MiniLibC
; File description:
; my_strstr.asm
;

BITS 64

section .text
global strstr

strstr:
	cmp rdi, 0
	je .RETURN_NULL
	cmp rsi, 0
	je .RETURN_NULL
    xor rcx, rcx
    xor r8, r8
    xor r9, r9
    xor bl, bl

.LOOP:
    mov al, BYTE [rdi+rcx]
    cmp al, 0
    je .RETURN_NULL
    cmp al, BYTE [rsi]
    je .SEARCH

.INCREMENT:
    inc rcx
    jmp .LOOP

.SEARCH:
    xor r8, r8
    mov r9, rcx

.SUBLOOP:
    mov bl, BYTE [rdi+r9]
    cmp BYTE [rsi+r8], 0
    je .RETURN
    cmp BYTE [rsi+r8], bl
    jne .INCREMENT

.SUBINCREMENT:
    inc r8
    inc r9
    jmp .SUBLOOP

.RETURN:
	add rdi, rcx
	mov rax, rdi
	ret

.RETURN_NULL:
    xor rax, rax
    ret