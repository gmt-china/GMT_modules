#!/bin/bash
ps=psbasemap_ex2.ps

# 绘制澳大利亚的海岸线
gmt pscoast -R110E/170E/44S/9S -JM6i -P -Baf -BWSne -Wfaint -N2/1p -EAU+gbisque \
        -Gbrown -Sazure1 -Da -K -Xc --FORMAT_GEO_MAP=dddF > $ps

# 在右上角绘制insert box
gmt psbasemap -R -J -O -K -DjTR+w1.5i+o0.15i+stmp -F+gwhite+p1p+c0.1c+s >> $ps
# 从临时文件中读取insert box的左下角的位置
read x0 y0 w h < tmp
# 在insert box内绘制全球地图，并突出显示澳大利亚
gmt pscoast -Rg -JG120/30S/$w -Da -Gbrown -A5000 -Bg -Wfaint -EAU+gbisque -O -K -X$x0 -Y$y0 >> $ps

gmt psxy -R -J -O -T  -X-${x0} -Y-${y0} >> $ps

rm gmt.* tmp
