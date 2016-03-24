.. index:: ! grdpaste

grdpaste
========

:官方文档: :ref:`gmt:grdpaste`
:简介: 将两个网格沿着其共同边界拼接成一个文件

要合并的两个网格文件必须拥有相同的网格间隔以及一条共同的边。若不满足，则需要使用 :doc:`grdcut` 、 :doc:`grdsample` 命令对网格数据做处理再拼接。

示例
----

一个简单的示例::

    gmt grdpaste file_a.nc file_b.nc -Goutfile.nc


对于地理网格而言，可能需要使用 ``-f`` 选项处理网格的经度周期性问题::

    gmt grdpaste file_a.nc file_b.nc -Goutfile.nc -V -fg
