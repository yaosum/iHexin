#!/usr/bin/env bash
py.test \
    --platform_name='iOS' \
    --platform_version='9.3' \
    --device_name='iPhone 6' \
    --device_udid='6d8f1f61fe31d1f74c18c63449fbeedd0e70b59f' \
    --bundle_id='cn.com.10jqka.iHexinFee' \
    --html=report.html \
    --rerun 1 \
    --junitxml=report.xml \


# 57e95712fdd52a1fce030ed46808f1a98e9b2f5e

# 23f7c26d8cd5097555991644f657ba515401ebac

#ios_webkit_debug_proxy -c 6d8f1f61fe31d1f74c18c63449fbeedd0e70b59f:27753 -d