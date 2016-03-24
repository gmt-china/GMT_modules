.. index:: ! grdconvert

grdconvert
==========

:官方文档: :ref:`gmt:grdconvert`
:简介: 在不同的网格格式之间互相转换

选项
----

``<ingrdfile>``
    要读入的网格文件，文件名格式见 :ref:`doc:grid-data`

``<outgrdfile>``
    要写入的网格文件，文件名格式见 :ref:`doc:grid-data`

``-N``
    不将GMT头段结构写到文件中。该选项用于写一个无头段的native的二进制文件，该文件可直接用于 :doc:`grdraster` 命令中。

选项
----

从一个三维网格文件中提取第二层数据::

    gmt grdconvert climate.nc?temp[1] temp.nc -V

将网格文件转换成四字节native浮点型网格::

    gmt grdconvert data.nc ras_data.b4=bf -V

将网格文件转换成二字节短整型文件，将其乘以10并减去32000，并设置无数据节点的值为-9999::

    gmt grdconvert values.nc shorts.i2=bs/10/-32000/-9999 -V

将网格文件转换为 :doc:`grdraster` 可直接使用的二进制文件::

    gmt grdconvert etopo2.nc etopo2.i2=bs -N -V

To creat a dumb file saved as a 32 bits float GeoTiff using GDAL::

    gmt grdmath -Rd -I10 X Y MUL = lixo.tiff=gd:GTiff
