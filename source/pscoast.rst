.. index:: ! pscoast

pscoast
=======

:官方文档: :ref:`gmt:pscoast`
:简介: 在地图上绘制海岸线、河流、国界线

该命令除了可以用于绘制海岸线、河流、政治边界，还可以裁剪陆地区域或水域，也可以将数据导出到文件中。

选项
----

``-A``
    不绘制面积过小的湖泊的边界，或不绘制某个级别的湖泊边界。

    该选项的语法是::

        -A<min_area>[/<min_level>/<max_level>][+ag|i|s|S][+r|l][+p<percent>]

    在绘制湖泊时，若不管湖泊的面积大小而把所有湖泊的边界都画上去，可能导致图看上去比较乱，该选项用于对湖泊进行筛选。面积小于 ``<min_area>`` 平方千米或者湖泊级别不在 ``[min_level,max_level]`` 范围的边界都不会被绘制。默认值为 ``0/0/4`` ，即绘制所有湖泊边界。关于湖泊边界的等级，在下面会介绍。

    对于level=2，即湖岸线，包括常规的湖以及很宽的河流。加上 ``+r`` 则只绘制河流，加上 ``+l`` 则只绘制常规湖。

    对于南极洲而言，因为有冰层的存在，所以海岸线有多种处理方式：

    #. ``+ai`` 用ice shell boundary作为南极洲的海岸线，默认值
    #. ``+ag`` 以ice grounding line作为海岸线
    #. ``+as`` 跳过南纬60度以南的海岸线，这样用户即可使用 ``psxy`` 绘制自己的南极洲海岸线
    #. ``+aS`` 跳过南纬60度以北的海岸线

    ``+p<precent>`` ：一个多边形，降低精度后，边数减少，面积变化，当面积变化过大时再绘制这个多边形就不合适了，该子选项用于去除那些面积与最高精度面积之比小于 ``<percent>`` 的多边形。

``-C[l|r]<fill>``
    设置湖泊与河流湖的颜色。

    默认情况下，湖泊与河流湖会被当做wet区域，直接使用 ``-S`` 指定的填充值。该选项可以为湖泊和河流湖单独指定颜色，也可以多次使用该选项分别为湖泊和河流湖指定颜色。

    #. ``-G<fill>`` 同时指定湖泊和河流湖的颜色
    #. ``-Gl<fill>`` 指定湖泊（lake）颜色
    #. ``-Gr<fill>`` 指定河流湖（river-lake）颜色

``-D[a|f|h|i|l|c][+]``
    选择海岸线数据精度。

    GMT自带的GSHHG海岸线数据，有5个不同精度的版本，从高到低依次为：full、high、intermediate、low和crude。GMT默认使用低精度数据。该选项可以指定要使用的数据精度，其中 ``<resolution>`` 可以取 ``f|h|i|l|c`` 分别代表5种不同的精度，当然也可以用 ``-Da`` 选项，此时GMT会根据当前绘图区域的大小自动选择合适的数据精度。

    默认情况下，若找不到指定精度的海岸线数据，程序会自动报错退出。该选项中加上 ``+`` 则命令在找不到当前指定的精度数据时，自动寻找更低精度的数据。

``-E<code1>,<code2>,...[+l|L][+gfill][+ppen][+r|R[incs]]``
    绘制或导出行政区划边界（洲界、国界、省界）。

    除了海岸线数据GSHHG之外，GMT还自带了DCW（Digital Chart of World）数据，即全球的行政区划数据。DCW数据位于 ``${GMTHOME}/share/dcw`` 目录下，包含了全球各国的国界和各国的省界数据。该数据独立于GSHHG数据，因而 ``-A`` 和 ``-D`` 选项对该数据无效。

    说明：

    #. ``<code>`` 是要绘制或提取的边界数据的代码，多个代码之间用逗号分隔
    #. 具体的代码参考dcw目录下的文档。代码有如下几种形式

       #. 洲代码前加上 ``=`` 则绘制整个洲内所有国家边界，比如 ``=AS`` 会绘制所有亚洲国家的边界
       #. 直接使用国界代码，则绘制国界边界，比如 ``US`` 绘制美国边界
       #. 使用 ``国家代码.州代码`` ，则绘制州（省）边界，比如 ``US.TX`` 绘制美国Texas州的边界

    #. ``+l`` 仅列出所有国家及其对应代码，不绘制边界也不提取数据
    #. ``+L`` 列出部分国界的省及其代码
    #. ``+g<fill>`` 设置多边形的填充色
    #. ``+p<pen>`` 绘制多边形的轮廓
    #. ``+r`` 获取多边形所对应的区域范围，以便于直接从数据中提取 ``-R`` 选项的范围。 ``<incs>`` 可以是 ``<inc>`` 、 ``<xinc>/<yinc>`` 、 ``<winc>/<einc>/<sinc>/<ninc>`` 以调整区域范围使得范围是这些步长的整数倍
    #. ``+R`` 与 ``+r`` 类似，只是之后的 ``<incs>`` 等参数被解释为区域范围向外扩展的增量

    额外的说明：

    #. 除非使用了 ``+r`` 、 ``+R`` 或 ``-M`` 选项，否则必须指定 ``+p|+g`` 中的一个
    #. ``-E`` 选项可以重复出现多次，以分别为不同的多边形设置不同的属性
    #. 若使用了 ``+r|+R`` 但未使用 ``-J|-M`` ，则直接输出 ``-R<w>/<e>/<s>/<n>`` 格式的字符串
    #. 个别地方有BUG

``-F``
    控制比例尺和玫瑰图的背景边框，见 :ref:`doc:embellishments` 一节

``-G<fill>|c``
    设置dry区域的填充色或裁剪dry区域

    #. ``-G<fill>`` 设置dry区域（一般指陆地）的填充色
    #. ``-Gc`` 将dry区域裁剪出来，使得接下来的绘图只有dry区域内的才会被绘制

``-I<river>[/<pen>]``
    绘制河流。

    河流 ``<river>`` 可以取：

    - 0 = Double-lined rivers (river-lakes)
    - 1 = Permanent major rivers
    - 2 = Additional major rivers
    - 3 = Additional rivers
    - 4 = Minor rivers
    - 5 = Intermittent rivers - major
    - 6 = Intermittent rivers - additional
    - 7 = Intermittent rivers - minor
    - 8 = Major canals
    - 9 = Minor canals
    - 10 = Irrigation canals
    - a = All rivers and canals (0-10)
    - A = All rivers and canals except river-lakes (1-10)
    - r = All permanent rivers (0-4)
    - R = All permanent rivers except river-lakes (1-4)
    - i = All intermittent rivers (5-7)
    - c = All canals (8-10)

    ``<pen>`` 的默认值为 ``default,black,solid`` ， 该选项可以重复使用多次。

``-L``
    绘制比例尺。见 :doc:`psbasemap` 中该选项的介绍

``-M``
    将边界数据以多段ASCII表的形式导出到标准输出

    使用该选项，则只导出数据而不绘图，该选项需要与 ``-E|-I|-N|-W`` 选项一起使用。

``-N<border>[/<pen>]``
    绘制政治边界。

    该选项在某些地方与 ``-E`` 选项有重叠。边界类型 ``<border>`` 可以取：

    - ``1`` ：国界
    - ``2`` ：州界；（目前只有美国、加拿大、澳大利亚以及南美各国的数据）
    - ``3`` ：Marine boundaries
    - ``a`` ：1-3的全部边界；

    说明：

    #. ``<border>`` 是必须值， ``<pen>`` 是可选值
    #. 可以多次重复使用 ``-N`` 选项，指定不同级别的边界
    #. ``<pen>`` 的默认值是 ``default,black,solid``

``-Q``
    关闭区域裁剪。

    使用 ``-Gc`` 和 ``-Sc`` 可以分别裁剪出dry区域和wet区域，接下来的其他绘图命令中只有在裁剪区域内的部分才会被绘制。在绘图结束后，需要关闭裁剪，就需要再次调用 ``pscoast`` ，并加上 ``-Q`` 选项。若在开启裁剪后使用了 ``-X`` 和 ``-Y`` 选项，则在关闭时也要记得使用 ``-X`` 和  ``-Y`` 。

``-S``
    设置wet区域的填充色或裁剪wet区域

    #. ``-G<fill>`` 设置wet区域（一般指海洋或湖泊）的填充色
    #. ``-Gc`` 将wet区域裁剪出来，使得接下来的绘图只有wet区域内的才会被绘制

``-T``
    绘制方向玫瑰图或磁场玫瑰图，见 :doc:`psbasemap` 中的选项介绍

``-W[<level>/]<pen>``
    绘制湖岸线（shoreline）。

    shore指水与陆地交界的“岸”（如：海岸、湖岸、河岸等），是一个较为笼统的说法。

    GMT将shoreline分成四个等级（ ``<level>`` 取1-4）：

    #. coastline：海岸线
    #. lakeshore：湖泊与陆地的岸线
    #. island-in-lake shore：首先要有陆地，陆地中有个湖，湖里有个岛。即岛的岸线
    #. lake-in-island-in-lake shore：首先有陆地，陆地中有个湖，湖中有个岛，岛里又有个湖。这里指的是湖的岸线

    使用时需要注意：

    #. 不使用 ``-W`` 选项，则不绘制任何shore
    #. 使用 ``-W`` ，给定画笔属性 ``<pen>`` ，但不给出 ``<level>`` ，则绘制四个level的shore
    #. 可以用 ``-W<level>/<pen>`` 的方式指定要绘制哪一个level的shore，并指定线条属性，在同一个命令中可以多次使用 ``-W`` ，以指定不同level的shore的画笔属性
    #. ``-W`` 选项中 ``<level>`` 是可选的，而 ``<pen>`` 是必须的！因而 ``-W2`` 会被解释为所有level的画笔属性，而不是level 2

示例
----

::

    gmt pscoast -R-30/30/-40/40 -Jm0.1i -B5 -I1/1p,blue -N1/0.25p,- \
            -I2/0.25p,blue -W0.25p,white -Ggreen -Sblue -P > africa.ps

::

    gmt pscoast -R-30/-10/60/65 -Jm1c -B5 -Gp100/28 > iceland.ps

将非洲区域裁剪出来，并在其中的陆地部分绘制地形::

    gmt pscoast -R-30/30/-40/40 -Jm0.1i -B5 -Gc -P -K > africa.ps
    gmt grdimage -Jm0.1i etopo5.nc -Ccolors.cpt -O -K >> africa.ps
    gmt pscoast -Q -O >> africa.ps

绘制部分国家的国界线（似乎有BUG）::

    gmt pscoast -JM6i -P -Baf -EGB,IT,FR+gblue+p0.25p,red+r -EES,PT,GR+gyellow > map.ps

提取冰岛的海岸线数据::

    gmt pscoast -R-26/-12/62/68 -Dh -W -M > iceland.txt

FAQ
---

#. 错误消息::

       pscoast: low resolution shoreline data base not installed.

   出现该错误的原因有如下几种：

   #. 未安装GSHHG海岸线数据
   #. 安装了但路径不正确（建议的做法是把所有GSHHG的文件放在 ``$GMTHOME/share/coast`` 目录下）
   #. 安装的netCDF版本号为3.x而不是4.x
   #. 自行编译了netCDF 4.x，且编译时使用了 ``--disbale-netcdf4`` 选项

BUGS
----

#. ``-E`` 选项有尚未确定的BUG （v5.2.1）
