/*
** EPITECH PROJECT, 2018
** CRITEST SOURCES
** File description:
** t_strcasecmp.c
*/

#include <unistd.h>
#include "cri_func.h"

Test(strcasecmp, with_normal_case, .init=libopen)
{
    int ret = my_strcasecmp("Hello world!", "Hello world!");

    cr_assert_eq(ret, 0);
}

Test(strcasecmp, with_case, .init=libopen)
{
    int ret = my_strcasecmp("HELLO WORLD!", "Hello world!");

    cr_assert_eq(ret, 0);
}

Test(strcasecmp, with_first_uppercase_and_second_nonletter, .init=libopen)
{
    int ret = my_strcasecmp("HELLO WORLDD", "Hello world!");

    cr_assert_eq(ret, 67);
}

Test(strcasecmp, with_second_uppercase_and_first_nonletter, .init=libopen)
{
    int ret = my_strcasecmp("HELLO WORLD!", "Hello worldD");

    cr_assert_eq(ret, -67);
}

Test(strcasecmp, with_first_longer, .init=libopen)
{
    int ret = my_strcasecmp("Hello world!", "Hello");

    cr_assert_eq(ret, 32);
}

Test(strcasecmp, with_second_longer, .init=libopen)
{
    int ret = my_strcasecmp("Hello", "Hello world!");

    cr_assert_eq(ret, -32);
}