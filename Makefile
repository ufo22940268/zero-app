#
# Makefile
# garlic, 2013-11-26 13:05
#

all:
	python run.py

testall:
	py.test -s -x zero/tests/test_main.py

# vim:ft=make
#

