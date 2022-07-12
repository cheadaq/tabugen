"""
Copyright (C) 2018-present ichenq@outlook.com. All rights reserved.
Distributed under the terms and conditions of the Apache License.
See accompanying files LICENSE.
"""

import os
import tabugen.predef as predef
import tabugen.typedef as types
import tabugen.util.strutil as strutil
import tabugen.util.tableutil as tableutil
import tabugen.util.structutil as structutil
import tabugen.parser.xlsxhelp as xlsxhelp


# 使用excel解析结构描述
class ExcelStructParser:

    def __init__(self):
        self.filedir = ''
        self.skip_names = ''
        self.with_data = True
        self.filenames = []
        self.skipped_fields = []

    @staticmethod
    def name():
        return "excel"

    def init(self, args):
        self.filedir = args.asset_path
        if args.without_data:
            self.with_data = False
        if args.skip_files is not None:
            self.skip_names = [x.strip() for x in args.skip_files.split(' ')]
        self.enum_filenames(self.filedir)

    # 跳过忽略的文件名
    def enum_filenames(self, filedir: str):
        filenames = []
        if not os.path.exists(filedir):
            print('file path [%s] not exist' % filedir)
            return

        # filename is a directory
        if os.path.isdir(filedir):
            filedir = os.path.abspath(filedir)
            print('parse files in directory:', filedir)
            filenames = xlsxhelp.enum_excel_files(filedir)
        else:
            assert os.path.isfile(filedir)
            filename = os.path.abspath(filedir)
            filenames.append(filename)

        if len(self.skip_names) == 0:
            self.filenames = filenames
            return

        print('skipped file names:', self.skip_names)
        for filename in filenames:
            ignored = False
            for skip_name in self.skip_names:
                if len(skip_name) > 0:
                    if filename.find(skip_name) >= 0:
                        ignored = True
                        break
            if not ignored:
                self.filenames.append(filename)

    def parse_kv_table(self, meta, table):
        for row in table:
            pass

    def parse_struct_table(self, meta, table):
        struct = {
            'fields': [],
            'comment': meta.get(predef.PredefClassComment, ""),
        }
        if len(table) <= predef.PredefDataStartRow:
            return struct

        class_name = meta[predef.PredefClassName]
        assert len(class_name) > 0
        struct['name'] = class_name
        struct['camel_case_name'] = strutil.camel_case(class_name)

        type_row = table[predef.PredefFieldTypeRow]
        comment_row = table[predef.PredefCommentRow]

        fields_names = {}
        prev_field = None
        for col, name in enumerate(table[predef.PredefFieldNameRow]):
            # skip empty column
            if name == '' or name.startswith('#') or name.startswith('//') or type_row[col] == "":
                continue
            field_type = types.get_type_by_name(type_row[col])

            assert name not in fields_names, name
            fields_names[name] = True

            field = {
                "name": name,
                "camel_case_name": strutil.camel_case(name),
                "original_type_name": type_row[col],
                "type": field_type,
                "type_name": types.get_name_of_type(field_type),
                "column_index": col + 1,
                "comment": comment_row[col],
                "enable": name not in self.skipped_fields,
            }

            if prev_field is not None:
                is_vector = strutil.is_vector_fields(prev_field, field)
                # print('is vector', is_vector, prev_field, field)
                if is_vector:
                    prev_field["is_vector"] = True
                    field["is_vector"] = True
            prev_field = field

            assert field["type"] != types.Type.Unknown
            assert field["type_name"] != ""

            struct['fields'].append(field)

        struct["options"] = meta

        if self.with_data:
            data = table[predef.PredefDataStartRow:]
            data = strutil.pad_data_rows(struct['fields'], data)
            data = tableutil.convert_table_data(struct, data)
            data = tableutil.blanking_disabled_columns(struct, data)
            struct["data_rows"] = data

        return struct

    # 解析数据列
    def parse_data_sheet(self, meta, table):
        if meta[predef.PredefParseKVMode]:  # 全局KV模式
            return self.parse_kv_table(meta, table)
        return self.parse_struct_table(meta, table)

    # 解析所有文件
    def parse_all(self):
        descriptors = []
        for filename in self.filenames:
            print(strutil.current_time(), "start parse", filename)
            struct = self.parse_one_file(filename)
            if struct is None:
                print('parse file %s failed' % filename)
            else:
                structutil.setup_struct(struct)
                struct['source'] = filename
                descriptors.append(struct)
        return descriptors

    # 解析单个文件
    def parse_one_file(self, filename):
        data_table, meta = xlsxhelp.read_workbook_data(filename)

        if predef.PredefIgnoredFields in meta:
            text = meta[predef.PredefIgnoredFields]
            self.skipped_fields = [x.strip() for x in text.split(',')]

        tableutil.set_meta_kv_mode(data_table, meta)
        struct = self.parse_data_sheet(meta, data_table)
        struct['file'] = os.path.basename(filename)
        return struct

