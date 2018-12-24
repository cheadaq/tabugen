# Copyright (C) 2018-present ichenq@outlook.com. All rights reserved.
# Distributed under the terms and conditions of the Apache License.
# See accompanying files LICENSE.

#
# Excel导入器
#

PredefFilenameOption = "file"
PredefSkipFileOption = "skip"

PredefMetaSheet = "meta"                # meta sheet名称
PredefStructTypeRow = "type-row"        # 这一行描述类型
PredefStructNameRow = "name-row"        # 这一行描述名称
PredefCommentRow = "comment-row"        # 这一行描述注释蚊子
PredefDataStartRow = "data-start-row"   # 数据从这一行开始
PredefDataEndRow = "data-end-row"       # 数据从这一行结束，默认为末尾行
PredefClassName = "class-name"          # 生成的class名称
PredefClassComment = "class-comment"    # 生成的class注释

PredefParseKVMode = "parse-kv-mode"         # 是否是KV模式
PredefKeyValueColumn = "key-value-column"   # KV模式中的key和value所在列，如 1，2
PredefKeyColumn = "key-column"              # KV模式种的key所在列，从PredefKeyValueColumn解析
PredefValueColumn = "value-column"          # KV模式种的value所在列，从PredefKeyValueColumn解析
PredefValueTypeColumn = "value-type-column" # KV模式中的value类型所在列
PredefCommentColumn = "comment-column"      # KV模式中的注释所在列


PredefGetMethodKeys = "get-keys"        # 生成的Get()函数的参数列表
PredefRangeMethodKeys = "range-keys"    # 生成的GetRange()函数的参数列表

PredefInnerClassRange = "inner-class-range"
PredefInnerClassName = "inner-class-name"

OptionOutDataDir = "outdata-dir"        # 输出的csv文件路径
OptionOutSourceFile = "out-src-file"    # 输出的源文件路径
OptionAutoVector = "auto-vector"        # 自动把名称相近的字段合并为数组
OptionDataOnly = "data-only"            # 只导出数据，不导出源文件
OptionNoData = "no-data"                # 只导出源文件，不导出数据
OptionArrayDelimeter = "array-delim"    # array类型的分隔符，如|，不能使用csv的逗号
OptionMapDelimeters = "map-delim"       # map类型的分隔符，如;=，不能使用csv的逗号

DefaultArrayDelimiter = '\\'    # 默认的array分隔符号
DefaultMapDelimiters = ';='     # 默认的map分隔符号


#
# SQL导入器
#
OptionCamelcaseField = "camelcase-field"
OptionFieldGetterSetter = "field-getset"
OptionNamePrefix = "prefix"