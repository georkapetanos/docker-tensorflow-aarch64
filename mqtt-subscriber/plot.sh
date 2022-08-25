#!/bin/bash
# Use Gnuplot to generate graph from file with 3 columns time, temperature, pressure, separated by tabs
gnuplot -p -e 'set term wxt title "Gnuplot - Temperature"; set xdata time; set terminal wxt size 1280,720; set grid; set timefmt "%H:%M:%S"; plot "'$1'" using 1:2 lt '$2' lc 6 title "Temperature (C)"'
gnuplot -p -e 'set term wxt title "Gnuplot - Pressure"; set xdata time; set terminal wxt size 1280,720; set grid; set timefmt "%H:%M:%S"; plot "'$1'" using 1:3 lt '$2' lc 7 title "Pressure (hPa)"'
