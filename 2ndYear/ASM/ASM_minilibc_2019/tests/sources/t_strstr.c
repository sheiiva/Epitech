/*
** EPITECH PROJECT, 2018
** CRITEST SOURCES
** File description:
** t_strstr.c
*/

#include <unistd.h>
#include "cri_func.h"

Test(strstr, with_normal_case, .init=libopen)
{
    char *str = my_strstr("Hello world!", "Hello");

    cr_assert_str_eq(str, "Hello world!");
}


Test(strstr, with_tricky_case, .init=libopen)
{
    char *str = my_strstr("Hell Hello", "Hello");

    cr_assert_str_eq(str, "Hello");
}

Test(strstr, with_double_occurence_case, .init=libopen)
{
    char *str = my_strstr("Hello Hello", "Hello");

    cr_assert_str_eq(str, "Hello Hello");
}

Test(strstr, with_non_matching_case, .init=libopen)
{
    char *str = my_strstr("Hello world!", "lord lord!");

    cr_assert_eq(str, NULL);
}

Test(strstr, with_null_catch, .init=libopen)
{
    char *str = my_strstr("Hello world!", NULL);

    cr_assert_eq(str, NULL);
}

Test(strstr, with_null_string, .init=libopen)
{
    char *str = my_strstr(NULL, "Hello world!");

    cr_assert_eq(str, NULL);
}