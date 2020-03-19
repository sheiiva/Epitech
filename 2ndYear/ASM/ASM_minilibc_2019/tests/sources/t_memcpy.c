/*
** EPITECH PROJECT, 2018
** CRITEST SOURCES
** File description:
** t_memcpy.c
*/

#include <unistd.h>
#include "cri_func.h"

Test(memcpy, with_normal_case, .init=libopen)
{
    char src[6] = "aaaaa\0";
    char dest[6] = "\0\0\0\0\0\0";

    my_memcpy(dest, src, 5);
    cr_assert_str_eq(dest, "aaaaa");
}

Test(memcpy, with_short_size, .init=libopen)
{
    char src[6] = "aaaaa\0";
    char dest[6] = "\0\0\0\0\0\0";

    my_memcpy(dest, src, 2);
    cr_assert_str_eq(dest, "aa");
}

Test(memcpy, with_zero_size, .init=libopen)
{
    char src[6] = "aaaaa\0";
    char dest[6] = "\0\0\0\0\0\0";

    my_memcpy(dest, src, 0);
    cr_assert_str_eq(dest, "\0\0\0\0\0\0");
}

Test(memcpy, with_first_null, .init=libopen)
{
    char src[6] = "aaaaa\0";
    char *dest = NULL;

    my_memcpy(dest, src, 5);
    cr_assert_eq(dest, NULL);
}

Test(memcpy, with_second_null, .init=libopen)
{
    char *src = NULL;
    char dest[6] = "\0\0\0\0\0\0";

    my_memcpy(dest, src, 5);
    cr_assert_str_eq(dest, "\0\0\0\0\0\0");
}