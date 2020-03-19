/*
** EPITECH PROJECT, 2018
** CRITEST SOURCES
** File description:
** t_strcmp.c
*/

#include <unistd.h>
#include "cri_func.h"

Test(strcmp, with_normal_case, .init=libopen)
{
    int ret = my_strcmp("Hello world!", "Hello world!");

    cr_assert_eq(ret, 0);
}

Test(strcmp, with_first_longer, .init=libopen)
{
    int ret = my_strcmp("Hello world!", "Hello");

    cr_assert_eq(ret, 32);
}

Test(strcmp, with_second_longer, .init=libopen)
{
    int ret = my_strcmp("Hello", "Hello world!");

    cr_assert_eq(ret, -32);
}