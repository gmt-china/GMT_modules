.. index:: ! gmtlogo

gmtlogo
=======

:官方文档: :ref:`gmt:gmtlogo`
:说明: 在图上绘制GMT的图形logo

该模块将GMT的图形logo绘制在图上。默认情况下，GMT的图形logo默认宽2英寸，高1英寸，将放在当前的绘图原点处。

必须选项
--------

无

可选选项
--------

``-D[g|j|J|n|x]<refpoint>[+w<width>][+j<justify>][+o<dx>[/<dy>]]``
    设置logo在图中的位置

    - ``[g|j|J|n|x]<refpoint>`` 设置底图上的参考点，见 :ref:`doc:embellishments` 一节
    - ``+j<justify>`` 设置logo上的锚点，见 :ref:`doc:embellishments` 一节
    - ``+o<dx>[/<dy>]`` 设置参考点的额外偏移量，见 :ref:`doc:embellishments` 一节
    - ``+w<width>`` 设置logo的宽度

``-F[+c<clearance(s)>][+g<fill>][+i[[<gap>/]<pen>]][+p[<pen>]][+r[<radius>]][+s[<dx>/<dy>/][<fill>]]``
    在 logo 后加一个背景面板，见 :ref:`doc:embellishments` 一节

    - ``+p<pen>`` 面板边框的画笔属性
    - ``+g<fill>`` 面板填充色
    - ``+c<clearances>`` 设置 logo 与面板边框之间空白区域的大小
    - ``+i<gap>/<pen>`` 为背景面板加上额外的内边框
    - ``+r<radius>`` 面板使用圆角矩形边框
    - ``+s<dx>/<dy>/<fill>`` 为面板增加阴影区

示例
----

单独绘制一个2英寸宽的GMT logo::

    gmt logo -P -Dx0/0+w2i > logo.ps

将GMT logo作为一个图层放在当前底图的左上角::

    gmt logo -R -J -DjTR+o0.1i/0.1i+w3i -F+glightblue+s -K -O >> bigmap.ps
