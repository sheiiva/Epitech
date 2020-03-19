/*
** EPITECH PROJECT, 2018
** CRITEST SOURCES
** File description:
** t_strlen.c
*/

#include <unistd.h>
#include "cri_func.h"

Test(strlen, with_normal_case, .init=libopen)
{
    size_t value = my_strlen("Hello world!");

    cr_assert_eq(value, 12);
}

Test(strlen, with_empty_case, .init=libopen)
{
    size_t value = my_strlen("");

    cr_assert_eq(value, 0);
}