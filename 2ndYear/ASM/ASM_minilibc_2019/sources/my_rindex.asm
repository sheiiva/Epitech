;
; EPITECH PROJECT, 2018
; ASM - MiniLibC
; File description:
; my_rindex.asm
;

BITS 64

section .text
global rindex

rindex:
    xor ecx, ecx
	cmp rdi, 0
	je .RETURN_NULL
    jmp .GOTOEND

.GOTOEND:
    cmp BYTE [rdi+rcx], 0
    je .DECREMENT
    jmp .INCREMENT

.INCREMENT:
    inc rcx
    jmp .GOTOEND

.DECREMENT:
    dec rcx
    jmp .LOOP

.LOOP:
	cmp BYTE [rdi+rcx], sil
	je .RETURN
	cmp BYTE [rdi+rcx], 0
	je .RETURN_NULL
	jmp .DECREMENT

.RETURN:
	add rdi, rcx
	mov rax, rdi
	ret

.RETURN_NULL:
    xor rax, rax
    ret