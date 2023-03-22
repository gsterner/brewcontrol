MAKEFLAGS += -j2

tempplot: run-temp-check plot-temp

run-temp-check:
	python3 ds18b20_runner.py

plot-temp:
	gnuplot -geometry 200x200 -p plottemp.gnuplot
