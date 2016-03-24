.. index:: ! psimage

psimage
=======

:官方文档: :ref:`gmt:psimage`
:简介: 将图片或EPS文件放在地图上

该命令可以读取一个EPS文件或其他图片格式，并将其画在地图上，可以用于将自己单位的Logo放在GMT做的图上。

选项
----

``<imagefile>``
    EPS文件或其他光栅图片格式（GIF、PNG等）的文件

    - EPS文件必须包含合适的BoundingBox
    - 光栅文件的颜色深度可以是1、8、24、32位
    - 光栅文件是通过GDAL读入的，若安装GMT时未配置GDAL，则该命令只能读取Sun光栅文件

``-D[g|j|J|n|x]<refpoint>+e<dpi>+w[-]<width>[/<height>][+j<justify>][+n<nx>[/<ny>]][+o<dx>[/<dy>]]``
    指定图片的尺寸和位置。

    #. ``[g|j|J|n|x]<refpoint>`` 指定底图上的参考量，见 :ref:`doc:embellishments` 一节
    #. ``+j<justify>`` 指定色标上的锚点，默认锚点是 ``BL`` ，见 :ref:`doc:embellishments` 一节
    #. ``+o<dx>[/<dy>]`` 指定参考点的额外偏移量，见 :ref:`doc:embellishments`
    #. ``+e<dpi>`` 指定图片的DPI以间接指定图片的尺寸
    #. ``+w[-]<width>[/<height>]`` 直接指定图片的尺寸，若未给定 ``<height>`` 则按照 ``<width>`` 以及原图的横纵比进行缩放；若 ``<width>`` 为负值，则使用其绝对值作为宽度，并使用PS的图片操作符将图片插值到设备的分辨率
    #. ``+n<nx>/<ny>`` 使图片在水平方向重复 ``<nx>`` 次，垂直方向重复 ``<ny>`` 次，若省略 ``<ny>`` 则默认其与 ``<nx>`` 相等，默认值为 ``1/1``

``-F``
    为图片加上背景边框，见 :ref:`doc:embellishments` 一节

``-M``
    使用YIQ变换将彩图转换成灰度图

``-G[b|f|t]<color>``
    对图片颜色的一下设置

    1-bit图片默认为黑色和白色，可以通过如下选项进行修改：

    - ``-Gb<color>`` 设置背景色，即将白色替换成其他颜色
    - ``-Gf<color>`` 设置前景色，即将黑色替换成其他颜色
    - ``<color>`` 可以取 ``-`` ，表示透明

    对于8、24、32位图片而言：

    - ``-Gt<color>`` 将某个特定颜色设置为透明

``-I``
    绘图前对1-bit图片进行反转，即黑色变白色，白色变黑色

示例
----

::

    gmt psimage logo.jpg -Dx0/0+w1i -F+pthin,blue > image.ps

::

    gmt psimage tiger.eps -Dx2i/1i+jTR+w3i > image.ps

::

    gmt psimage 1_bit.ras -Gbbrown -Gfred -Dx0/0+w1c+n5 > image.ps
