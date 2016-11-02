.. index:: ! isogmt

isogmt
======

:官方文档: :ref:`gmt:isogmt`
:简介: 在“隔离模式”下运行GMT命令或脚本

该命令本质上是一个Bash脚本，其脚本内容为::

    export GMT_TMPDIR=`mktemp -d ${TMPDIR:-/tmp}/gmt.XXXXXX`
    gmt "$@"
    rm -rf $GMT_TMPDIR
    unset GMT_TMPDIR

该脚本首先定义了环境变量 ``${GMT_TMPDIR}`` ，用于给GMT指定临时目录，接下来执行的GMT命令所生成的临时文件都会保存在该临时目录下。待命令/脚本执行完毕后，再删除临时目录和环境变量。

用法
----

::

    isogmt command

示例
----

隔离模式下运行一个GMT命令::

    isogmt psbasemap -R0/10/0/10 -JX10c/10c -B1 > test.ps

隔离模式下运行一个脚本::

    isogmt sh run.sh

BUGS
----

#. 无法在隔离模式下执行脚本（v5.2.1）
