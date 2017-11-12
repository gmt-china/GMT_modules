.. index:: ! gmt

gmt
===

:官方文档: :ref:`gmt:gmt`
:说明: GMT的主程序，也是GMT5中唯一的一个二进制文件，GMT的所有模块都需要通过该命令调用

调用模块
--------

GMT的所有功能通过如下语法调用::

    gmt <module> <module-options>

其中， ``<module>`` 是GMT模块名， ``<module-options>`` 是模块所支持的选项。

比如，想要调用GMT的psbasemap模块::

    gmt psbasemap -JX10c/10c -R0/20/0/5 -Bafg > test.ps

特殊模块
--------

``gmt clear`` 可以用于清理缓存文件或历史文件::

    gmt clear history|conf|cache|all

- `gmt clear history`: 删除当前目录下的 ``gmt.history`` 文件
- `gmt clear conf`: 删除当前目录下的 ``gmt.conf`` 文件
- `gmt clear cache`: 删除用户目录（ ``~/.gmt`` ）下的缓存文件夹
- `gmt clear all`: 清理 history、conf 和 cache

其他选项
--------

``gmt`` 还可以跟一些其他选项：

- ``gmt --help`` ：列出GMT提供的所有模块名及其功能
- ``gmt --version`` ：显示GMT版本
- ``gmt --show-bindir`` ：显示GMT的bin目录
- ``gmt --show-datadir`` ：显示GMT的数据目录，默认为空
- ``gmt --show-sharedir`` ：显示GMT的share目录
- ``gmt --show-plugindir`` ：显示GMT的插件目录
- ``gmt --show-modules`` ：列出GMT的所有模块名
- ``gmt --show-cores`` ：显示当前计算机可以使用的核数
- ``gmt <module> =`` ：检测模块 ``<module>`` 是否存在，若存在则返回0，否则返回非零值


现代模式
--------

GMT 6开始提供了现代模式以简化代码。

- ``gmt begin`` 用于初始化一个新的GMT会话。
- ``gmt figure`` 用于指定当前图件的文件名、格式以及其他选项
- ``gmt subplot`` 用于指定子图相关信息
- ``gmt revert`` 撤销当前图片的最近几个图层
- ``gmt end`` 结束当前绘图

具体用法见参考手册中相关章节。
