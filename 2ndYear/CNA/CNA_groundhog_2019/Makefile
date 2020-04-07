##
## EPITECH PROJECT, 2019
## GROUNDHOG
## File description:
## MAKEFILE
##

RM =	rm -f

NAME =	groundhog

$(NAME):
	cp src/main.py $@
	chmod +x $@

all: $(NAME)

clean:

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re