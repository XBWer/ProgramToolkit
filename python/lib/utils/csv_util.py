# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       csv_util
   Description:
   Author:     bowen
   date:        6/16/19
-------------------------------------------------
"""


def write_row_to_csv(row, fpath):
    import csv
    with open(fpath, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(row)


def write_rows_to_csv(rows, fpath):
    for row in rows:
        write_row_to_csv(row, fpath)


def append_new_row(row, fpath):
    import csv
    with open(fpath, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)


def read_csv_with_header(csv_fpath):
    import csv
    with open(csv_fpath) as f:
        csv_data = [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
    return csv_data


def append_new_rows(rows, fpath):
    for row in rows:
        append_new_row(row, fpath)
