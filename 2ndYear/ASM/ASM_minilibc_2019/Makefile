##
## EPITECH PROJECT, 2018
## MAKEFILE
## File description:
## ROOT
##

NAME 		= 	root_makefile

SRC_PATH	=	./sources/
TST_PATH	=	./tests/

CLEAN		=	clean
FCLEAN		=	fclean

$(NAME):
	@$(MAKE) -C $(SRC_PATH)

all: $(NAME)

clean:
	@$(MAKE) $(CLEAN) -C $(SRC_PATH)
	@$(MAKE) $(CLEAN) -C $(TST_PATH)

binary:
	@$(MAKE) binary -C $(SRC_PATH)

fclean:
	@$(MAKE) $(FCLEAN) -C $(SRC_PATH)
	@$(MAKE) $(FCLEAN) -C $(TST_PATH)

re: fclean all

tests_run: all
	@$(MAKE) -C $(TST_PATH)

.PHONY: all clean fclean re tests_run binary
