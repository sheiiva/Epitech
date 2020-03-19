/*
** EPITECH PROJECT, 2019
** INCLUDE FILES
** File description:
** tested_func.h
*/

#ifndef TESTED_FUNC_H_
    #define TESTED_FUNC_H_

    #include "cri_func.h"
    #include <strings.h>
    #include <stdlib.h>
    #include <string.h>
    #include <unistd.h>
    #include <stdint.h>
    #include <stdio.h>
    #include <fcntl.h>
    #include <dlfcn.h>

    int	(*my_strcasecmp)(const char *str1, const char *str2);
    char *(*my_strchr)(const char *str, int c);
    int	(*my_strcmp)(const char *str1, const char *str2);
    size_t (*my_strcspn)(const char *str, const char *reject);
    size_t (*my_strlen)(const char *str);
    int	(*my_strncmp)(const char *str1, const char *str2, size_t n);
    char *(*my_strpbrk)(const char *str, const char *accept);
    char *(*my_strstr)(const char *haystack, const char *needle);
    void *(*my_memcpy)(void *dest, const void *strrc, size_t n);
    void *(*my_memmove)(void *dest, const void *strrc, size_t n);
    void *(*my_memset)(void *str, int c, size_t n);
    ssize_t	(*my_read)(int fd, void *buffer, size_t count);
    char *(*my_rindex)(const char *str, int c);
    ssize_t	(*my_write)(int fd, const void *buf, size_t count);

#endif /* !TESTED_FUNC_H_ */

