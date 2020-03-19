/*
** EPITECH PROJECT, 2018
** CRITEST SOURCES
** File description:
** t_memmove.c
*/

#include <unistd.h>
#include "cri_func.h"

Test(memmove, with_normal_case, .init=libopen)
{
    char src[6] = "aaaaa\0";
    char dest[6] = "\0\0\0\0\0\0";

    my_memmove(dest, src, 5);
    cr_assert_str_eq(dest, "aaaaa");
}

Test(memmove, with_short_size, .init=libopen)
{
    char src[6] = "aaaaa\0";
    char dest[6] = "\0\0\0\0\0\0";

    my_memmove(dest, src, 2);
    cr_assert_str_eq(dest, "aa");
}

Test(memmove, with_zero_size, .init=libopen)
{
    char src[6] = "aaaaa\0";
    char dest[6] = "\0\0\0\0\0\0";

    my_memmove(dest, src, 0);
    cr_assert_str_eq(dest, "\0\0\0\0\0\0");
}

Test(memmove, with_first_null, .init=libopen)
{
    char src[6] = "aaaaa\0";
    char *dest = NULL;

    my_memmove(dest, src, 5);
    cr_assert_eq(dest, NULL);
}

Test(memmove, with_second_null, .init=libopen)
{
    char *src = NULL;
    char dest[6] = "\0\0\0\0\0\0";

    my_memmove(dest, src, 5);
    cr_assert_str_eq(dest, "\0\0\0\0\0\0");
}