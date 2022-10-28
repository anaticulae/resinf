# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utila
import utilatest

import resinf.configure


def generated(folder: str = None, project: str = None) -> str:
    """\
    >>> resinf.setup('helm', validate=False)
    >>> generated(project='helm')
    '...generated/helm'
    >>> generated('alpha', project='helm')
    '...generated/helm/alpha'
    """
    assert resinf.configure.PROJECT or project, 'run resinf.setup before'
    path = resinf.configure.getroot(project=project)
    if folder:
        path = os.path.join(path, folder)
    result = utila.forward_slash(path)
    return result


def link(file, folder=None, project: str = None) -> str:
    """Determine link to expected generated path.

    >>> link(resinf.path.BACHELOR111_PDF, project='poc/helm')
    '...helm/bachelor_bachelor111'
    >>> link(resinf.path.BACHELOR111_PDF, folder='notoc', project='poc/helm')
    '...helm/notoc/bachelor_bachelor111'
    """
    mixed = [resinf.REPOSITORY, file]
    simple = utilatest.simplify_testfile_names(mixed)[0]
    result = os.path.join(generated(folder=folder, project=project), simple)
    result = utila.forward_slash(result)
    return result


def todo_new(path, pages: str = None, folder: str = None) -> tuple:
    """Determine todo entree as input for test data generator.

    >>> resinf.setup('poc', validate=False)
    >>> todo_new(resinf.path.BACHELOR111_PDF, '5:10')
    ('...itory/bachelor/bachelor111.pdf', '...generated/poc/bachelor_bachelor111', '5:10')
    """
    pages = ':' if pages is None else pages
    path = utila.forward_slash(path)
    dest = link(path, folder=folder)
    result = (path, dest, pages)
    return result
