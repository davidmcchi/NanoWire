reset

set term pngcairo enhanced color \
font "Helvetica Bold, 32" \
size 1280,960

set output "PES.png"

set palette defined (0 0.0 0.0 0.5, \
1 0.0 0.0 1.0, \
2 0.0 0.5 1.0, \
3 0.0 1.0 1.0, \
4 0.5 1.0 0.5, \
5 1.0 1.0 0.0, \
6 1.0 0.5 0.0, \
7 1.0 0.0 0.0, \
8 0.5 0.0 0.0 )

set border lw 3

set multiplot title "Terphenyl Rotational Potential Energy (Hartree)"

unset key

set xtics (0, "" 10, "" 20, 30, "" 40, "" 50, 60, "" 70, "" 80, 90) out nomirror textcolor rgb "#00CC00"
set ytics (0, "" 10, "" 20, 30, "" 40, "" 50, 60, "" 70, "" 80, 90) out offset 0,-0.5,0 nomirror textcolor rgb "#1240AB"

set pm3d at s interpolate 10,10;
set view 60,300,0.95,1.1
set contour
set cntrparam levels 30
set cntrparam cubicspline

set lmargin at screen 0.15
set rmargin at screen 0.65

set xl "{/Symbol q}_1 (deg)" offset 2.0,-0.5 textcolor rgb "#00CC00"
set yl "{/Symbol q}_2 (deg)" offset -2.0,-1.0 textcolor rgb "#1240AB"

set cbtics (-694.550,-694.552,-694.550,-694.554,-694.556)
#set ztics ("" -694.550,"" -694.552,"" -694.550,"" -694.554,"" -694.556) nomirror

set colorbox user origin 0.76,0.45 size 0.05,0.45

splot "PES.txt" u 1:2:3 w l lw 3 palette notitle

unset contour

splot "PES.txt" u 1:2:3 w lp lc rgb "black" ps 0.8 pt 7

unset multiplot
