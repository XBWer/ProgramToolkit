# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     diff_util
   Description :
   Author :       bowenxu
   date：          30/4/18
-------------------------------------------------
   Change Activity:
                   30/4/18:
-------------------------------------------------
"""

from unidiff import PatchSet


class Diff:
    source = ''
    target = ''
    diff = ''

    def __init__(self, source=None, target=None, diff=None):
        self.source = source
        self.target = target
        self.diff = diff


def diff_parser_from_file(diff_path):
    patches = []
    try:
        patches = PatchSet.from_filename(diff_path, encoding='utf-8')
    except Exception as e:
        print(e.message)
        print('***parse failed*** Please manually fix it: %s' % diff_path.split('/')[-1])
    return patches


def diff_parser_from_str(diff_str):
    patches = []
    try:
        patches = PatchSet.from_string(diff_str, encoding='utf-8')
    except Exception as e:
        print(e.message)
        print('***parse failed*** Please manually fix it: %s' % diff_str.split('/')[-1])
    return patches


def get_modified_contract_linenums_from_diff(diff_file_path):
    patches = diff_parser_from_file(diff_file_path)
    p = patches[0]
    modified_file = str(p.source_file).split('/contracts/')[-1]
    modified_line_list = []
    for hunk in p:
        for line in hunk:
            # if source
            if str(line.line_type) == '-':
                # if comment
                if str(line.value).strip().startswith('//') or str(line.value).strip().startswith('/*') \
                        or str(line.value).strip().endswith('*/') or str(line.value).strip().startswith('*') \
                        or str(line.value).strip() == '':
                    continue
                modified_line_list.append(line.source_line_no)
    return modified_file, modified_line_list