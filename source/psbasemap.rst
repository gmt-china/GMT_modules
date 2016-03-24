.. index:: ! psbasemap

psbasemap
=========

:官方文档: :ref:`gmt:psbasemap`
:简介: 绘制底图

该命令用于绘制底图边框（标注、刻度、标签等）、标题、比例尺、方向玫瑰等。

选项
----

``-B``
    绘制底图边框，见关于 ``-B`` 选项的介绍。

    示例代码::

        gmt psbasemap -R-180/180/-70/70 -JM10c -Bx60 -By30 > test.ps

``-A[<file>]``
    不绘制图形，仅输出矩形底图的边框坐标。

    该选项会将矩形底图的边框坐标输出到标准输出或文件中。使用该选项时，必须通过 ``-J`` 和 ``-R`` 指定绘图区域，且不能同时使用其他选项。若不指定 ``<file>`` 则默认输出到标准输出，否则输出到文件 ``<file>`` 中

    说明：

    #. 该选项似乎仅适用于矩形底图边框，非矩形边框会输出一堆NaN
    #. 尚不清楚该选项存在的意义
    #. 边框的采样间隔由参数 ``MAP_LINE_STEP`` 决定
    #. 该选项似乎有bug

    示例::

        gmt psbasemap -R0/10/0/10 -JX10c/5c -Aoutline.txt

``-D``
    在底图中绘制图中图（insert map box），需要 ``-F`` 选项，其语法有两种::

        -D[<unit>]<xmin>/<xmax>/<ymin>/<ymax>[r][+s<file>]
        -D[g|j|J|n|x]<refpoint>+w<width>[/<height>][+j<justify>][+o<dx>[/<dy>]][+s<file>]

    先解释图中图（insert box）的概念。在绘制一个小区域时，为了表明该小区域在地球上的位置，通常需要在一张更大范围（比如整个中国或整个地球）的底图上标出小区域所在的位置，这种绘图形式通常称为insert map。而insert box就是insert map的边框。

    指定insert map box的范围有三种方法：

    #. ``-D<xmin>/<xmax>/<ymin>/<ymax>[r]`` ：类似 ``-R`` 的语法，直接指定insert box在地图上的范围
    #. ``-D<unit><xmin>/<xmax>/<ymin>/<ymax>`` ：类似 ``-R`` 的语法，指定投影后的坐标范围， ``<unit>`` 为投影后的坐标单位
    #. 指定参考点和锚点，见 :ref:`doc:embellishments` 一节

       #. ``[g|j|J|n|x]<refpoint>`` 指定大区域底图上的参考点
       #. ``+j<justify>`` 指定insert box上的锚点
       #. ``+o<dx>/<dy>`` 指定参考点的额外偏移量
       #. ``+w<width>[/<height>]`` 指定insert box的宽度或/和高度

    使用 ``+s<file>`` 选项，会将insert box的左下角位置以及其长宽写到文件中，坐标值以及长度值均使用当前地图单位。

``-F``
    控制insert box、比例尺和方向玫瑰的背景边框的属性。

    其语法为::

        -F[d|l|t][+c<clearances>][+g<fill>][+i[[<gap>/]<pen>]][+p[<pen>]][+r[<radius>]][+s[[<dx>/<dy>/][<shade>]]]

    说明：

    #. 见 :ref:`doc:embellishments` 一节的详细介绍
    #. 该选项用于给insert box、比例尺和方向玫瑰绘制背景边框，默认同时控制三者的属性
    #. ``d|l|t`` 表示该选项定义的属性仅适用于 ``-D`` 、 ``-L`` 或 ``-T`` 选项
    #. 直接使用 ``-F`` 选项，则绘制背景边框，边框属性由参数 ``MAP_FRAME_PEN`` 控制

``-L``
    在地图上绘制比例尺。

    该选项的语法为::

        -L[g|j|J|n|x]<refpoint>+c[<slon>/]<slat>+w<length>[e|f|k|M|n|u][+a<align>][+f][+l[<label>]][+u]

    说明：

    #. 大部分在 :ref:`doc:embellishments` 一节已经介绍了
    #. ``[g|j|J|n|x]<refpoint>`` 指定地图上的参考点，比例尺的锚点位于比例尺的中心
    #. ``+c<slon>/<slat>`` 要绘制哪一个点的比例尺
    #. ``+w<length>[e|f|M|n|k|u]`` 比例尺的长度，默认单位为km，也可使用其他长度单位
    #. ``+a<align>`` 修改比例尺标签的位置，默认位于比例尺上方中文，可以取 ``l`` 、 ``r`` 、 ``t``` 、 ``b`` 分别代表左右上下
    #. ``+l<label>`` 为比例尺加标签；若不指定 ``<label>`` ，默认的标签是比例尺所使用的长度单位
    #. ``+u`` 比例尺的标注默认只有值没有单位，该选项会给标注加上单位
    #. ``+f`` 默认是简单的比例尺，使用该选项则绘制fancy比例尺，即火车轨道比例尺

    相关参数：

    #. ``FONT_LABEL`` 控制比例尺的标签字体
    #. ``FONT_ANNOT_PRIMARY`` 控制比例尺的标注字体
    #. ``MAP_SCALE_HEIGHT`` 控制比例尺的高度
    #. ``MAP_TICK_PEN_PRIMARY`` 控制比例尺的刻度属性

    示例::

        gmt psbasemap -R90/110/30/40 -JM10c -Bx5 -By5 -Lg95/35+c35+w800k+lscale+u+f > test.ps

        gmt psbasemap -R90/180/-50/50 -Jm0.025i -Bafg -B+tMercator -Lx1i/1i+c0+w5000k > mercator.ps

``-Td``
    绘制方向玫瑰图，其语法为::

        -Td[g|j|J|n|x]<refpoint>+w<width>[+f[<level>]][+j<justify>][+l<w,e,s,n>][+o<dx>[/<dy>]]

    说明：

    #. 大部分在 :ref:`doc:embellishments` 一节已经介绍了
    #. ``[g|j|J|n|x]<refpoint>`` 指定地图上的参考点
    #. ``+j<justify>`` 指定玫瑰图上的锚点（默认为 ``MC`` ）
    #. ``+o<dx>/<dy>`` 指定参考点的偏移量
    #. ``+w<width>`` 玫瑰图的宽度
    #. ``+f<level>`` 绘制fancy玫瑰图， ``<level>`` 指定了fancy玫瑰图的不同类型， ``<level>`` 可以取：

       - ``1`` 绘制E-W和N-S四个方向
       - ``2`` 绘制8个方向
       - ``3`` 绘制16个方向

    #. ``+l<w>,<e>,<s>,<n>`` 为四个方向分别指定标签，默认标签是四个方向的单字母代码（英文语言下是W、E、S、N，具体值由参数 ``GMT_LANGUAGE`` ），四个方向的标签之间用逗号分隔，比如 ``+lw,e,s,n`` 或 ``+l",,Down,Up"``

    下图展示了方向玫瑰图的效果图：

    .. figure:: /images/psbasemap_ex3.*
       :width: 600px
       :align: center

       方向玫瑰图

       （左） ``-Tdg0/0+w1i+jCM``
       （中） ``-Tdg0/0+w1i+f1+jCM``
       （右） ``-Tdg0/0+w1i+f3+l+jCM``

``-Tm``
    绘制磁场玫瑰图，用于展示磁场方向。

    其语法为::

        -Tm[g|j|J|n|x]<refpoint>+w<width>[+d<dec>[/<dlabel>]]][+i<pen>][+j<justify>][+l<w>,<e>,<s>,<n>][+p<pen>][+t<ints>][+o<dx>[/<dy>]]

    磁场玫瑰包括两个同心圆环，其中外环用于展示方向信息，内环用于显示磁场方向。

    说明：

    #. 大部分在 :ref:`doc:embellishments` 一节已经介绍了
    #. ``[g|j|J|n|x]<refpoint>`` 指定地图上的参考点
    #. ``+j<justify>`` 指定玫瑰图上的锚点（默认为 ``MC`` ）
    #. ``+o<dx>/<dy>`` 指定参考点的偏移量
    #. ``+w<width>`` 玫瑰图的宽度
    #. ``+p<pen>`` 绘制外环的轮廓
    #. ``+i<pen>`` 绘制内环的轮廓
    #. ``+d<dec>/<dlabel>`` 设置磁倾角以及罗盘指针上的磁倾角标签。若 ``<dlabel>`` 为空，则使用默认标签 ``d = <dec>`` ；若 ``<dlabel>`` 为 ``-`` ，则不绘制标签。当使用 ``+d`` 子选项时，会同时绘制地理方向和磁场方向
    #. ``+l<w>,<e>,<s>,<n>`` 为四个方向的标签，默认标签是四个方向的单字母代码（英文语言下是W、E、S、N，具体值由参数 ``GMT_LANGUAGE`` ；若 ``<n>`` 取值为 ``*`` ，则会在北方向标签处绘制星代表北极星
    #. 内外环都可以设置标注、刻度和网格的间隔。内外环的间隔默认值都是 ``30/5/1`` 。可以使用 ``+t<ints>`` 选项，后面接6个斜杠分隔的值，以分别指定两个圆环的3种刻度值，其中前三个值控制内环属性，后三个值控制外环属性

示例
----

下面的脚本展示了一种insert box的用法：

.. literalinclude:: ../scripts/psbasemap_ex1.sh
   :language: bash

.. figure:: /images/psbasemap_ex1.*
   :width: 600px
   :align: center

   用psbasemap命令-D选项绘制图中图

下面的脚本绘制了另一种不同的insert box：

.. literalinclude:: ../scripts/psbasemap_ex2.sh
   :language: bash

.. figure:: /images/psbasemap_ex2.*
   :width: 600px
   :align: center

   用psbasemap命令-D选项绘制另一种图中图

下面的脚本绘制了磁场玫瑰图：

.. literalinclude:: ../scripts/psbasemap_ex4.sh
   :language: bash

.. figure:: /images/psbasemap_ex4.*
   :width: 600px
   :align: center

   磁场玫瑰图

BUGS
----

#. 使用 ``-A`` 选项可以正常输出结果，但会出现 ``double free`` 的错误（v5.2.1）
