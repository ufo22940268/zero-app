#
# Makefile
# garlic, 2013-11-26 13:05
#
#

touch:
	touch run.py

server:
	python local_run.py

testall:
	py.test -s -x zero/tests/test_main.py

deploy:
	fab deploy

test:
	fab test

# vim:ft=make
#

