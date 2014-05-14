#!/bin/bash

#Make basic plotting script
echo '
reset
set term pngcairo enhanced size 1600,900 font "Helvetica bold,28"
set output "XXXX"
set pm3d map
set title "|E|^2"
set xlabel "Distance / 100 nm"
set ylabel "Distance / 100 nm"
set cbr [0:0.04]
unset key
set palette defined (0 "yellow", 1 "green", 2 "blue")
splot "YYYY" every 2 u ($1/10):($2/10):3
' > plotTEMP.plt


#Check to see if there's a plotting directory, make one if it doesn't exist
if [ ! -d "Plots" ]; then
	mkdir Plots
fi

for H5FILE in $(ls -1 | grep ".h5"); do
	echo $H5FILE;
#Get the value for the last time slice
	NUM=$(h5ls AgFilm-final_dpwr.h5 | awk '{print $5}' | tr -d '\/Inf}');
	NUM=$(expr $NUM - 1);
#Convert from h5 to txt file
	RAWDATA=$(basename $H5FILE .h5)_raw.txt;
	h5totxt -t$NUM $H5FILE > $RAWDATA;
#Convert to 3-column format
	DATAFILE=$(basename $H5FILE .h5)_3col.txt;
	ConvertData.py $RAWDATA $DATAFILE;
#Plot the Data
	PLOTFILE=$(basename $H5FILE .h5)_plot.plt;
	PNGFILE=$(basename $H5FILE .h5)_plot.png;
	cat plotTEMP.plt | sed "s/XXXX/$PNGFILE/g" | sed "s/YYYY/$DATAFILE/g" > $PLOTFILE;
	gnuplot $PLOTFILE;
#Move Files to Directory
	mv $PLOTFILE Plots/;
	mv $PNGFILE Plots/;
	mv $DATAFILE Plots/;
	rm $RAWDATA;
done

rm plotTEMP.plt;