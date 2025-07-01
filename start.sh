#!/bin/bash

# تحقق من المتغيرات البيئية الأساسية
required_vars=("COINEX_ACCESS_ID" "COINEX_SECRET_KEY")
missing_vars=()

for var in "${required_vars[@]}"; do
    if [ -z "${!var}" ]; then
        missing_vars+=("$var")
    fi
done

if [ ${#missing_vars[@]} -ne 0 ]; then
    echo "خطأ: المتغيرات البيئية التالية مفقودة: ${missing_vars[*]}"
    exit 1
fi

# تشغيل البوت
exec python bot_service.py
