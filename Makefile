run:
	python test.py
edit:
	nvim test.py
test:
	cat in | make -s run
convert:
	python convert2submit.py
