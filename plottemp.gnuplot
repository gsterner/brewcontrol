set datafile separator ','
set xdata time # tells gnuplot the x axis is time data
set timefmt "%H:%M:%S" # specify our time string format
set format x "%H:%M:%S" # otherwise it will show only MM:SS
set yrange [16:25]

while (1) {
      plot 'tempdata.csv' using 1:2 with lines, \
           'tempdata.csv' using 1:3 with lines, \
           'tempdata.csv' using 1:4 with lines
      pause 1      # waiting time in seconds
}
