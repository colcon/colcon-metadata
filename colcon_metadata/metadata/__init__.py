# Copyright 2016-2018 Dirk Thomas
# Licensed under the Apache License, Version 2.0

from collections import defaultdict
import os

from colcon_core.location import get_config_path

metadata_by_name = defaultdict(dict)
metadata_by_path = defaultdict(dict)


def get_metadata_path():
    """
    Get the path where metadata is stored.

    :rtype: Path
    """
    return get_config_path() / 'metadata'


def get_metadata_files(path=None):
    """
    Get the paths of all metadata files.

    The metadata path is recursively being crawled for files ending in `.meta`.
    Directories starting with a dot (`.`) are being ignored.

    :rtype: list
    """
    metadata_path = path or get_metadata_path()
    if not metadata_path.is_dir():
        return []

    files = []
    for dirpath, dirnames, filenames in os.walk(
        str(metadata_path), followlinks=True
    ):
        # skip subdirectories starting with a dot
        dirnames[:] = filter(lambda d: not d.startswith('.'), dirnames)
        dirnames.sort()

        for filename in sorted(filenames):
            if not filename.endswith('.meta'):
                continue
            path = os.path.join(dirpath, filename)
            files.append(path)
    return files
