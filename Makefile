.PHONY: train test nltrain nltest clean
train:
	./generator.py -f -n 100000 | ./train.py > trained
test:
	./generator.py -f -n 100000 | ./tester.py
nltrain:
	./generator.py -f -n 100000 -nl | ./train.py > trained
nltest:
	./generator.py -f -n 100000 -nl | ./tester.py
nltt: nltrain nltest
tt: train test
clean:
	rm ./trained ./param
init: clean
	./generate_param.py -n 10 > param
