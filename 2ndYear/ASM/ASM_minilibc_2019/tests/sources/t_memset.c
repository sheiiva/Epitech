/*
** EPITECH PROJECT, 2018
** CRITEST SOURCES
** File description:
** t_memset.c
*/

#include <unistd.h>
#include "cri_func.h"

Test(memset, with_normal_case, .init=libopen)
{
    char str[6] = "aaaaa\0";

    my_memset(str, 'b', 5);
    cr_assert_str_eq(str, "bbbbb");
}

Test(memset, with_short_size, .init=libopen)
{
    char str[6] = "aaaaa\0";

    my_memset(str, 'b', 2);
    cr_assert_str_eq(str, "bbaaa");
}


Test(memset, with_no_size, .init=libopen)
{
    char str[6] = "aaaaa\0";

    my_memset(str, 'b', 0);
    cr_assert_str_eq(str, "aaaaa");
}