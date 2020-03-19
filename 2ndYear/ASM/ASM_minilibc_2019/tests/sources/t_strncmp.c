/*
** EPITECH PROJECT, 2018
** CRITEST SOURCES
** File description:
** t_strncmp.c
*/

#include <unistd.h>
#include "cri_func.h"

Test(strncmp, with_normal_case, .init=libopen)
{
    int ret = my_strncmp("Hello world!", "Hello world!", 15);

    cr_assert_eq(ret, 0);
}

Test(strncmp, with_first_longer, .init=libopen)
{
    int ret = my_strncmp("Hello world!", "Hello", 15);
   
    cr_assert_eq(ret, 32);
}

Test(strncmp, with_second_longer, .init=libopen)
{
    int ret = my_strncmp("Hello", "Hello world!", 15);

    cr_assert_eq(ret, -32);
}

Test(strncmp, with_short_n_same_string, .init=libopen)
{
    int ret = my_strncmp("Hello world!", "Hello world!", 2);

    cr_assert_eq(ret, 0);
}

Test(strncmp, with_sort_n_different_string, .init=libopen)
{
    int ret = my_strncmp("Hello world!", "Hello Kreooog!", 5);

    cr_assert_eq(ret, 0);
}

Test(strncmp, with_second_empty_string, .init=libopen)
{
    int ret = my_strncmp("Hello world!", "", 5);

    cr_assert_eq(ret, 72);
}

Test(strncmp, with_first_empty_string, .init=libopen)
{
    int ret = my_strncmp("", "Hello world!", 5);

    cr_assert_eq(ret, -72);
}

Test(strncmp, with_both_empty_string, .init=libopen)
{
    int ret = my_strncmp("", "", 5);

    cr_assert_eq(ret, 0);
}

Test(strncmp, with_no_n, .init=libopen)
{
    int ret = my_strncmp("Hello world!", "Hello Kreooog!", 0);

    cr_assert_eq(ret, 0);
}