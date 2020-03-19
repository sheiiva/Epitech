/*
** EPITECH PROJECT, 2018
** CRITEST SOURCES
** File description:
** t_rindex.c
*/

#include <unistd.h>
#include "cri_func.h"

Test(rindex, with_normal_case, .init=libopen)
{
    char *str = my_rindex("Hello world!", 'w');

    cr_assert_str_eq(str, "world!");
}

Test(rindex, with_multiple_case, .init=libopen)
{
    char *str = my_rindex("Hello world!", 'l');

    cr_assert_str_eq(str, "ld!");
}

Test(rindex, with_no_match, .init=libopen)
{
    char *str = my_rindex("Hello world!", 'z');

    cr_assert_eq(str, NULL);
}

Test(rindex, with_null_catch, .init=libopen)
{
    char *str = my_rindex("Hello world!", 0);

    cr_assert_str_eq(str, "\0");
}

Test(rindex, with_null_string, .init=libopen)
{
    char *str = my_rindex(NULL, 'W');

    cr_assert_eq(str, NULL);
}

Test(rindex, with_first_catch, .init=libopen)
{
    char *str = my_rindex("Hello world!", 'H');

    cr_assert_str_eq(str, "Hello world!");
}

Test(rindex, with_last_catch, .init=libopen)
{
    char *str = my_rindex("Hello world!", '!');

    cr_assert_str_eq(str, "!");
}