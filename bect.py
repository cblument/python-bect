#!/usr/bin/env python

import argparse
import os

def get_files_with_extension(path, extension, recursive):
    hits = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if not recursive:
                if path != root:
                    continue
            if file.endswith('.' + extension):
                hits.append(root + '/' + file)
    return hits

def rename_files(files, new_extension):
    for file in files:
        new_file = file.rsplit(".", 1)[0]
        new_file = ".".join([new_file, new_extension])
        os.rename(file, new_file)
        print "Renamed %s to %s" % (file, new_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", required=True,
                        help="Path to change extensions in")
    parser.add_argument("-o", "--old_extension", required=True,
                        help="The extension to be changed")
    parser.add_argument("-n", "--new_extension", required=True,
                        help="The new extension")
    parser.add_argument("-r", "--recursive", action="store_true",
                        help="Whether to rename in subdirectories")
    args = parser.parse_args()

    src_files = get_files_with_extension(args.path, args.old_extension, args.recursive)
    rename_files(src_files, args.new_extension)
