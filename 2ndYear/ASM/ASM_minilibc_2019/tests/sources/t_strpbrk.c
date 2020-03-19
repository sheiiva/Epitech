/*
** EPITECH PROJECT, 2018
** CRITEST SOURCES
** File description:
** t_strpbrk.c
*/

#include <unistd.h>
#include "cri_func.h"

Test(strpbrk, with_normal_case, .init=libopen)
{
    char *str = my_strpbrk("Hello world!", "e");

    cr_assert_str_eq(str, "ello world!");
}

Test(strpbrk, with_multiple_case, .init=libopen)
{
    char *str = my_strpbrk("Hello world!", "lord lord!");

    cr_assert_str_eq(str, "llo world!");
}

Test(strpbrk, with_null_catch, .init=libopen)
{
    char *str = my_strpbrk("Hello world!", NULL);

    cr_assert_eq(str, NULL);
}

Test(strpbrk, with_no_catch, .init=libopen)
{
    char *str = my_strpbrk("Hello world!", "Zzzz");

    cr_assert_eq(str, NULL);
}

Test(strpbrk, with_null_string, .init=libopen)
{
    char *str = my_strpbrk(NULL, "Hello world!");

    cr_assert_eq(str, NULL);
}

Test(strpbrk, with_first_catch, .init=libopen)
{
    char *str = my_strpbrk("Hello world!", "Hello");

    cr_assert_str_eq(str, "Hello world!");
}

Test(strpbrk, with_last_catch, .init=libopen)
{
    char *str = my_strpbrk("Hello world!", "!?:");

    cr_assert_str_eq(str, "!");
}