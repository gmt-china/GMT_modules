.. index:: ! gmtlogo

gmtlogo
=======

:官方文档: :ref:`gmt:gmtlogo`
:说明: 在图上绘制GMT的图形logo

该模块将GMT的图形logo绘制在图上。GMT的图形logo默认宽2英寸，高1英寸。

选项
----

``-D[g|j|J|n|x]<refpoint>+w<width>[+j<justify>][+o<dx>[/<dy>]]``
    设置logo的位置。

    #. ``[g|j|J|n|x]<refpoint>`` 设置底图上的参考点， :ref:`doc:embellishments` 一节
    #. ``+j<justify>`` 设置logo上的锚点，见 :ref:`doc:embellishments` 一节
    #. ``+o<dx>[/<dy>]`` 设置参考点的额外偏移量，见 :ref:`doc:embellishments` 一节
    #. ``+w<width>`` 设置logo的宽度

``-F``
    设置logo的背景属性，见 :ref:`doc:embellishments` 一节

示例
----

单独绘制GMT logo::

    gmt logo -P -Dx0/0+w2i > logo.ps

将GMT logo作为图片的一个图层::

    gmt logo -O -K -R -J -DjTR+o0.1i/0.1i+w3i >> bigmap.ps
