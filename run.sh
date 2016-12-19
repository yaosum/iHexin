#!/usr/bin/env bash
#把pytest的配置信息从excel中读到pytestConfigure.txt中。
python -c 'from function.get_pytest_configure import get_pytest_configure; get_pytest_configure()'

#从pytestConfigure.txt把pytest的命令内容读出来
read number </Users/Hexin/Desktop/iHexin/temFile/pytestConfigure.txt
eval $number
#ios_webkit_debug_proxy -c 6d8f1f61fe31d1f74c18c63449fbeedd0e70b59f:27753 -d