.. index:: ! grdimage

grdimage
==========

:官方文档: :ref:`gmt:grdimage`
:简介: 在地图上绘制网格数据

必须选项
--------

``<grid>``
    该命令的输入文件必须是2D网格文件，可以是一个只包含Z数据的网格文件，也可以是
    三个分别包含R、G、B值的网格文件。

可选选项
--------

``-A<out_img>[=<driver>]``
    将图片以光栅格式保存

    默认图片会以PostScript代码的形式输出，使用此选项可以以其他图片格式保存。
    文件名中使用后缀 ``.ppm`` 则会以Portable Pixel Map格式保存。

    若GMT支持GDAL，则可以以更多的光栅格式保存。

    #. ``<out_img>`` 为要保存的文件名
    #. ``<driver>`` 图片格式，见GDAL的文档

``-C<cpt>``
    绘图时要使用的CPT文件名。

    也可以直接使用GMT自带的CPT文件名，此时GMT会自动根据网格文件的Z值范围将
    自带的CPT采样成16级的连续CPT文件。也可以通过 ``-C<color1>,<color2>[,<color3>,..]``
    的语法构建一个线性连续CPT文件。

``-D[r]``
    表明输入的网格文件是需要通过GDAL读取的图片文件，见官方文档。

``-E[i|<dpi>]``
    设置投影后网格的精度，默认值为100。

``-G[f|b]<color>``
    该选项仅当生成的图片是黑白图时才可用。

    This option will instead use the image as a transparent mask and paint
    the mask (or its inverse, with **-Gb**) with the given color combination.

``-I[<intensfile>|<intensity>|<modifiers>]``
    增加光照效果

    可以给一个常数值，也可以给一个Z值范围在-1到1的网格文件。通常该强度文件用
    ``grdgradient`` 生成，若不指定该强度文件，则GMT会自动调用 ``grdgradient``
    并使用参数 ``-A-45 -Nt1`` 根据输入网格数据生成强度文件。

``-M``
    使用YIQ转换强制将其转换为灰度图。

``-N``
    对于非矩形地图，在地图边界处不对图片做裁剪。

``-Q``
    将值为NaN的节点处设置为透明色
