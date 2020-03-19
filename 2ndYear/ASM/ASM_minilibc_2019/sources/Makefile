##
## EPITECH PROJECT, 2018
## SOURCES MAKEFILE
## File description:
## BINARY MAKER
##

CC			=	gcc
ASM			=	nasm
PRINT		=	@echo -e
RM          =   @rm -f

ROOT_PATH		=	../

LIB		 	= 	$(ROOT_PATH)libasm.so

override CFLAGS 	+=
override LDFLAGS 	+= 	-L./$(ROOT_PATH)
override LDLIBS 	+=	-lasm
ASFLAGS				=	-f elf64


MINILIB		=	my_memcpy.asm		\
				my_memmove.asm		\
				my_memset.asm		\
				my_rindex.asm		\
				my_strcasecmp.asm	\
				my_strchr.asm		\
				my_strcmp.asm		\
				my_strlen.asm		\
				my_strcspn.asm		\
				my_strncmp.asm		\
				my_strpbrk.asm		\
				my_strstr.asm		\

MINILIBOBJ	=	$(MINILIB:.asm=.o)


$(LIB): $(MINILIBOBJ)
	$(PRINT) "\n------->\tCOMPILED MINILIB DEPENDENCIES.\n\nLET'S LINK IT ALL:\n"
	$(CC) -nostdlib -shared -fPIC $(MINILIBOBJ) -o $@
	$(PRINT) "\n------->\tCONGRATS !\n"

all: $(LIB)

%.o :	%.asm
	$(ASM) $(ASFLAGS) -o $@ $<

clean:
	$(PRINT) "\n------->\tREMOVE TMP FILES\n"
	$(RM) $(MINILIBOBJ) $(MINILIBOBJ:.o=.gcno) $(MINILIBOBJ:.o=.gcda)
	$(RM) $(OBJ) $(OBJ:.o=.gcno) $(OBJ:.o=.gcda)

fclean: clean
	$(PRINT) "------->\tREMOVE BINARY\n"
	$(RM) $(NAME)
	$(RM) $(LIB)

re: fclean all

.PHONY: all clean fclean re