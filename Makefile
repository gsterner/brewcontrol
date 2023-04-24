MAKEFLAGS += -j2

mash: run-temp-check plot-temp

run-temp-check:
	python3 ds18b20_runner.py

plot-temp:
	gnuplot -geometry 200x200 -p plottemp.gnuplot

boil: run-hops-timer clock

run-hops-timer:
	lxterminal -e python3 boiltimer.py

clock:
	lxterminal -e tty-clock -s
