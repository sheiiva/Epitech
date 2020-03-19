;
; EPITECH PROJECT, 2018
; ASM - MiniLibC
; File description:
; my_strchr.asm
;

BITS 64

section .text
global strchr

strchr:
    xor ecx, ecx
	cmp rdi, 0
	je .RETURN_NULL
    jmp .LOOP

.INCREMENT:
    inc rcx
    jmp .LOOP

.LOOP:
	cmp BYTE [rdi+rcx], sil
	je .RETURN
	cmp BYTE [rdi+rcx], 0
	je .RETURN_NULL
	jmp .INCREMENT

.RETURN:
	add rdi, rcx
	mov rax, rdi
	ret

.RETURN_NULL:
    xor rax, rax
    ret