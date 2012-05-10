all: 2

2:
	pyuic4 -i 2 -o interface.py interface.ui
	python2 ./plock

clean:
	rm *.pyc
