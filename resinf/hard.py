# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import resinf

HC_BACH106 = None
HC_BOOK636 = None
HC_DISS128 = None
HC_DISS148 = None
HC_DISS166 = None
HC_DISS171 = None
HC_DISS193 = None
HC_ALL = None

try:
    import hardcore.path
    import power
except ModuleNotFoundError:
    utila.debug('install hardcore to access HC_* resources')
else:
    HC_BACH106 = hardcore.path.BACHELOR106
    HC_BOOK636 = hardcore.path.BOOK636
    HC_DISS128 = hardcore.path.DISS128
    HC_DISS148 = hardcore.path.DISS148
    HC_DISS166 = hardcore.path.DISS166
    HC_DISS171 = hardcore.path.DISS171
    HC_DISS193 = hardcore.path.DISS193
    HC_ALL = [
        HC_BACH106,
        HC_BOOK636,
        HC_DISS128,
        HC_DISS148,
        HC_DISS166,
        HC_DISS171,
        HC_DISS193,
    ]

    WRAPPER = resinf.link

    def hclink(source, folder: str = None, project: str = None):
        generated = power.generated(folder=folder, project=project)
        directory = resinf.simple(source)
        result = utila.join(generated, directory)
        return result

    def hcwrapper(file, folder=None, project: str = None) -> str:
        if file in HC_ALL:
            return hclink(file, folder=folder, project=project)
        return WRAPPER(file, folder=folder, project=project)

    resinf.link = hcwrapper
