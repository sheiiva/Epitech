/*
** EPITECH PROJECT, 2018
** CRITEST SOURCES
** File description:
** t_strcspn.c
*/

#include <unistd.h>
#include "cri_func.h"

Test(strcspn, with_normal_case, .init=libopen)
{
    size_t value = my_strcspn("Hello world!", "o");

    cr_assert_eq(value, 4);
}

Test(strcspn, with_first_case, .init=libopen)
{
    size_t value = my_strcspn("Hello world!", "H");

    cr_assert_eq(value, 0);
}

Test(strcspn, with_no_catch, .init=libopen)
{
    size_t value = my_strcspn("Hello world!", "zzzz");

    cr_assert_eq(value, 12);
}

Test(strcspn, with_empty_catch, .init=libopen)
{
    size_t value = my_strcspn("Hello world!", "");

    cr_assert_eq(value, 12);
}

Test(strcspn, with_empty_string, .init=libopen)
{
    size_t value = my_strcspn("", "Hello world!");

    cr_assert_eq(value, 0);
}

Test(strcspn, with_empty_case_and_string, .init=libopen)
{
    size_t value = my_strcspn("", "");

    cr_assert_eq(value, 0);
}