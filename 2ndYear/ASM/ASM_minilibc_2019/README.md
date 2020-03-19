MiniLibC
===

Time:       3 weeks

Team:       1

Language:   x86-64Assembly


The project
----
The objective of this project is to **create a dynamic ELF library** to replace (to a certain extent) the **standard C library** you use every day on your system.

Here are the functions implemented in the MiniLibC:

* strlen
* strchr
* memset
* memcpy
* strcmp
* memmove
* strncmp
* strcasecmp
* rindex
* strstr
* strpbrk
* strcspn

## USAGE:

* To generate the library

```
>> make
```

* To execute tests

```
>> make tests_run
``` 

 > other rules: `make fclean`, `make clean`, `make re`

Author **Corentin COUTRET-ROZET**