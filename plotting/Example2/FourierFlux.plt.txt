reset

set term pngcairo enhanced color \
font "Helvetica Bold, 28" \
size 1600,900
set output "FourierFluxPlot.png"

# set term pdfcairo enhanced color \
# font "Helvetica Bold"
# set output "FourierFluxPlot.pdf"

# set term cairolatex pdf font 'phv,bx,it' standalone header \
#      "\\usepackage[T1]{fontenc}\n\\usepackage{mathptmx}\n\\usepackage{helvet}"
# set output "FourierFluxPlot.tex"

set multiplot

set border lw 3

#Upper Left Plot

set bmargin at screen 0.50
set tmargin at screen 0.85
set rmargin at screen 0.48
set lmargin at screen 0.15

unset key
unset xtics
unset ytics
unset x2tics
unset y2tics
unset xl
unset yl
unset x2l
unset y2l

set label "a)" at -10,5e-5 font "Helvetica Bold"
set label "b)" at 100,5e-5 font "Helvetica Bold"

set x2tics nomirror
set ytics nomirror out

set x2tics (25,50,75,100) offset 0,-0.5
set x2l "Time (fs)" offset 0,-0.5

set ytics ("0" 0, "" 1e-5, "2" 2e-5, "" 3e-5, "4" 4e-5)
set yl "Trans. Flux (1e-5)"

set yr [-0.15e-5:*]

plot "FluxTransNoCouple.txt" u ($1/41):2 w l lw 3 lc rgb "dark-red" axes x2y1

#Lower Left Plot

unset label
set bmargin at screen 0.15
set tmargin at screen 0.50
set rmargin at screen 0.48
set lmargin at screen 0.15

unset key
unset xtics
unset ytics
unset x2tics
unset y2tics
unset xl
unset yl
unset x2l
unset y2l

set xr [-0.04:2.5]
set xl "Energy (eV)"
set xtics (-2, "" -1, 0, 1, 2) nomirror out

set ytics ("0" 0, "" 0.001, "2" 0.002, "" 0.003, "4" 0.004, "" 0.005, "6" 0.006) nomirror out
set yl "FT (1e-3)"

set arrow from 1.19,4.5e-3 to 1.19,2.0e-3 lw 3 filled

plot "FluxTransNoCoupleFFT.txt" u ($1*27.21*6.28):2 w boxes lw 3 lc rgb "dark-red" axes x1y1

#Upper Right Plot

set bmargin at screen 0.50
set tmargin at screen 0.85
set rmargin at screen 0.85
set lmargin at screen 0.52

unset key
unset xtics
unset ytics
unset x2tics
unset y2tics
unset xl
unset yl
unset x2l
unset y2l

set x2tics nomirror
set y2tics nomirror

set x2tics (25,50,75,100) offset 0,-0.5
set x2l "Time (fs)" offset 0,-0.5

set y2tics ("0" 0, "" 1e-5, "2" 2e-5, "" 3e-5, "4" 4e-5)
set y2l "Trans. Flux (1e-5)"

set y2r [-0.15e-5:*]

plot "FluxTransCouple.txt" u ($1/41):2 w l lw 3 lc rgb "dark-blue" axes x2y2

#Lower Right Plot

set bmargin at screen 0.15
set tmargin at screen 0.50
set rmargin at screen 0.85
set lmargin at screen 0.52

unset key
unset xtics
unset ytics
unset x2tics
unset y2tics
unset xl
unset yl
unset x2l
unset y2l
unset label

set xr [-0.04:2.5]
set xl "Energy (eV)"
set xtics (-2, "" -1, 0, 1, 2) nomirror out

set y2tics
set y2r [0:0.007]
set y2tics ("0" 0, "" 0.001, "2" 0.002, "" 0.003, "4" 0.004, "" 0.005, "6" 0.006) nomirror
set y2l "FT (1e-3)"

set arrow from 0.835,4.0e-3 to 0.835,1.5e-3 lw 3 filled
set arrow from 0.4242,6.5e-3 to 0.4242,4.0e-3 lw 3 filled


plot "FluxTransCoupleFFT.txt" u ($1*27.21*6.28):2 w boxes lw 3 lc rgb "dark-blue" axes x1y2




unset multiplot

