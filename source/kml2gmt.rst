.. index:: ! kml2gmt

kml2gmt
=======

:官方文档: :ref:`gmt:kml2gmt`
:简介: 将Google Earth的KML文件转换为GMT表数据

只有包含点、线或多边形的Google Earth KML才能被转换。

选项
----

``<kmlfiles>``
    要转换的KML文件

``-F[s|l|p]``
    指定要输出的特征类型

    默认会输出KML中所包含的所有点、线或多边形

    #. ``-Fs`` 只输出点
    #. ``-Fl`` 只输出线
    #. ``-Fp`` 只输出多边形

``-Z``
    默认只输出经纬度信息，若使用 ``-Z`` 选项，则输出坐标的高程信息作为GMT的Z值

示例
----

::

    gmt kml2gmt google.kml -V > google.txt

从一个KML文件中分别提取点和多边形到不同的文件::

    gmt kml2gmt google.kml -Fp -V > polygons.txt
    gmt kml2gmt google.kml -Fs -V > points.txt

也可以直接用外部命令 ``ogr2ogr`` 实现转换::

    ogr2ogr -f "GMT" somefile.gmt somefile.kml
