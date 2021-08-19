#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import datetime
import json
from collections import Counter


def get_operators():
    """
    Feel free to add your own 'operator' here;
    The input will be:
        generator_ad_archives: a generator of array of ad_archvie
        args: extra arguments passed in from CLI
        is_verbose: check this for debugging information
    """
    return {
        "count": count_ads,
        "save": save_to_file,
        "save_to_csv": save_to_csv,
        "start_time_trending": count_start_time_trending,
    }


def count_ads(generator_ad_archives, args, is_verbose=False):
    """
    Count how many ad_archives match your query
    """
    count = 0
    for ad_archives in generator_ad_archives:
        count += len(ad_archives)
        if is_verbose:
            print("counting %d" % count)
    print("Total number of ads match the query: {}".format(count))


def save_to_file(generator_ad_archives, args, is_verbose=False):
    """
    Save all retrieved ad_archives to the file; each ad_archive will be
    stored in JSON format in a single line;
    """
    if len(args) != 1:
        raise Exception("save action requires exact 1 param: output file")
    with open(args[0], "w+") as file:
        count = 0
        for ad_archives in generator_ad_archives:
            for data in ad_archives:
                file.write(json.dumps(data))
                file.write("\n")
            count += len(ad_archives)
            if is_verbose:
                print("Items wrote: %d" % count)

    print("Total number of ads wrote: %d" % count)


def save_to_csv(generator_ad_archives, args, fields, is_verbose=False):
    """
    Save all retrieved ad_archives to the output file. Each ad_archive will be
    stored as a row in the CSV
    """
    if len(args) != 1:
        raise Exception("save_to_csv action takes 1 argument: output_file")

    delimiter = ","
    total_count = 0
    output = fields + "\n"
    output_file = args[0]

    for ad_archives in generator_ad_archives:
        total_count += len(ad_archives)
        if is_verbose:
            print("Items processed: %d" % total_count)
        for ad_archive in ad_archives:
            for field in list(fields.split(delimiter)):
                if field in ad_archive:
                    value = ad_archive[field]
                    if (type(value) == list and type(value[0]) == dict) or type(
                        value
                    ) == dict:
                        value = json.dumps(value)
                    elif type(value) == list:
                        value = delimiter.join(value)
                    output += (
                        '"' + value.replace("\n", "").replace('"', "") + '"' + delimiter
                    )
                else:
                    output += delimiter
            output = output.rstrip(",") + "\n"

    with open(output_file, "w") as csvfile:
        csvfile.write(output)

    print("Successfully wrote data to file: %s" % output_file)


def count_start_time_trending(generator_ad_archives, args, is_verbose=False):
    """
    output the count trending of ads by start date;
    Accept one parameters:
        output_file: path to write the csv
    """
    if len(args) != 1:
        raise Exception("start_time_trending action takes 1 arguments: output_file")

    total_count = 0
    output_file = args[0]
    date_to_count = Counter({})
    for ad_archives in generator_ad_archives:
        total_count += len(ad_archives)
        if is_verbose:
            print("Item processed: %d" % total_count)
        start_dates = list(
            map(
                lambda data: datetime.datetime.strptime(
                    data["ad_delivery_start_time"], "%Y-%m-%d"
                ).strftime("%Y-%m-%d"),
                ad_archives,
            )
        )
        date_to_count.update(start_dates)

    with open(output_file, "w") as csvfile:
        csvfile.write("date, count\n")
        for date in date_to_count.keys():
            csvfile.write("%s, %s\n" % (date, date_to_count[date]))

    print("Successfully wrote data to file: %s" % output_file)
