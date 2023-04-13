#!/usr/bin/env bash

cat file.txt | grep -E '^\({0,1}[0-9]{3}\){0,1}[ \-]{1}[0-9]{3}\-[0-9]{4}$'