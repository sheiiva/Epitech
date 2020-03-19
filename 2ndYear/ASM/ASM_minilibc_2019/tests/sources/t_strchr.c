/*
** EPITECH PROJECT, 2018
** CRITEST SOURCES
** File description:
** t_strchr.c
*/

#include <unistd.h>
#include "cri_func.h"

Test(strchr, with_normal_case, .init=libopen)
{
    char *str = my_strchr("Hello world!", 'w');

    cr_assert_str_eq(str, "world!");
}

Test(strchr, with_multiple_case, .init=libopen)
{
    char *str = my_strchr("Hello world!", 'l');

    cr_assert_str_eq(str, "llo world!");
}

Test(strchr, with_null_catch, .init=libopen)
{
    char *str = my_strchr("Hello world!", 0);

    cr_assert_str_eq(str, "\0");
}

Test(strchr, with_null_string, .init=libopen)
{
    char *str = my_strchr(NULL, 'W');

    cr_assert_eq(str, NULL);
}

Test(strchr, with_first_catch, .init=libopen)
{
    char *str = my_strchr("Hello world!", 'H');

    cr_assert_str_eq(str, "Hello world!");
}

Test(strchr, with_last_catch, .init=libopen)
{
    char *str = my_strchr("Hello world!", '!');

    cr_assert_str_eq(str, "!");
}