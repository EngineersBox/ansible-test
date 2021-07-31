#!/bin/bash

[[ $1 =~ (^|[[:space:]])$2($|[[:space:]]) ]] && echo "Valid input for '$3'" || echo "Invalid"