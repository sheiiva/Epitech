##
## EPITECH PROJECT, 2018
## TESTS
## File description:
## MAKEFILE
##

NAME 	= 	critests

CC		= 	gcc
LD		=	$(CC)

PRINT		=	@echo -e
RM			=	@rm -f

ADD_COVERAGE	=	'CFLAGS	+=	--coverage'
ADD_LCRITERION	=	'LDLIBS	+=	-lcriterion'

TEST_SRC		=	sources/
REC_FUNC		=	generic/

ROOT_PATH		=	../
I_PATH			=	include/
SOURCE_PATH		=	$(ROOT_PATH)sources/

override CFLAGS	    +=	-I./$(I_PATH) --coverage -fPIE
override LDFLAGS    += 	-L./$(ROOT_PATH)
override LDLIBS     +=	-lasm -lcriterion -ldl

SRC 	= 	$(TEST_SRC)t_memcpy.c		\
			$(TEST_SRC)t_memmove.c		\
			$(TEST_SRC)t_memset.c		\
			$(TEST_SRC)t_rindex.c		\
			$(TEST_SRC)t_strcasecmp.c	\
			$(TEST_SRC)t_strchr.c		\
			$(TEST_SRC)t_strcmp.c		\
			$(TEST_SRC)t_strcspn.c		\
			$(TEST_SRC)t_strlen.c		\
			$(TEST_SRC)t_strncmp.c		\
			$(TEST_SRC)t_strpbrk.c		\
			$(TEST_SRC)t_strstr.c		\
			$(REC_FUNC)libopen.c		\
			$(REC_FUNC)redirect.c

OBJ 	= 	$(SRC:.c=.o)

$(NAME): $(OBJ)
	$(PRINT) "\n------->\tCOMPILED TESTS SRC DEPENDECIES.\n"
	@$(MAKE) -C $(SOURCE_PATH) $(ADD_COVERAGE) $(ADD_LCRITERION)
	$(LD) $^ -o $@ $(CFLAGS) $(LDFLAGS) $(LDLIBS)
	$(PRINT) "\n------->\tIT COMPILED TESTS SRC DEPENDECIES.\n"
	$(PRINT) "\n\n"
	./$(NAME)
	$(PRINT) "\n\n"

all: $(NAME)

clean:
	$(PRINT) "\n------->\tREMOVE TESTS TMP FILES\n"
	$(RM) $(OBJ) $(OBJ:.o=.gcno) $(OBJ:.o=.gcda)

fclean: clean
	$(PRINT) "------->\tREMOVE TESTS\n"
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re