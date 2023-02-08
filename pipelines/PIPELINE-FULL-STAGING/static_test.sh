#!/bin/bash

source todo-list-aws/bin/activate
set -x

RAD_ERRORS=$(radon cc src -nc | wc -l)

if [[ $RAD_ERRORS -ne 0 ]]
then
    echo 'Ha fallado el análisis estatico de RADON. La calidad de la complejidad ciclomatica ' \
	    '(flag cc), es inferior a la B' \
	    '(flag -nc Errores de calidad C o inferior)'
    exit 1
fi
RAD_ERRORS=$(radon mi src -nc | wc -l)
if [[ $RAD_ERRORS -ne 0 ]]
then
	echo 'Ha fallado el análisis estatico de RADON - MI (Maintainability Index) (flag MI)'
    exit 1
fi

flake8 src/*.py
if [[ $? -ne 0 ]]
then
    exit 1
fi
bandit src/*.py
if [[ $? -ne 0 ]]
then
    exit 1
fi
