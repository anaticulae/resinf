# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import os

import utila

import resinf.configure

Todo = collections.namedtuple('Todo', 'resource name pages config')


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


def link(path, folder=None, project: str = None) -> str:
    """Determine link to expected generated path.

    >>> import power
    >>> link(power.path.BACHELOR111_PDF, project='poc/helm')
    '...helm/bachelor_bachelor111'
    >>> link(power.path.BACHELOR111_PDF, folder='notoc', project='poc/helm')
    '...helm/notoc/bachelor_bachelor111'
    """
    gen = generated(folder=folder, project=project)
    result = os.path.join(gen, simple(path))
    result = utila.forward_slash(result)
    return result


def todo_new(path, pages: str = None, folder: str = None) -> tuple:
    """Determine todo entree as input for test data generator.

    >>> import power
    >>> resinf.setup('poc', validate=False)
    >>> todo_new(power.path.BACHELOR111_PDF, '5:10')
    ('...itory/bachelor/bachelor111.pdf', '...generated/poc/bachelor_bachelor111', '5:10')
    """
    pages = ':' if pages is None else pages
    path = utila.forward_slash(path)
    dest = link(path, folder=folder)
    result = (path, dest, pages)
    return result


def todo(resource: str, name: str = None, pages: tuple = None, **kwargs):
    """\
    >>> todo('resource/master116.pdf', pages=(1,2, 3), groupme=True)
    Todo(resource='resource/master116.pdf', name='resource_master116', pages=(1, 2, 3), config={'groupme': True})
    >>> todo('resource/master116.pdf', name='master_master116', pages=None)
    Todo(resource='resource/master116.pdf', name='master_master116', pages=None, config=None)
    """
    config = kwargs if kwargs else None
    if name is None:
        name = simple(resource)
    result = Todo(resource, name=name, pages=pages, config=config)
    return result


def prepares(files, pages: tuple = (5, 6)) -> list:
    """\
    >>> prepares(['resource/master116.pdf', ('resource/mitpage', (1, 2, 3))])
    [Todo(resource='resource/master116.pdf',...pages=(5, 6),...Todo(...pages=(1, 2, 3), config=None)]
    >>> prepares([Todo('resource/master116.pdf', 'master116', 116, {})])
    [Todo(resource='resource/master116.pdf', name='master116', pages=116, config={})]
    """
    result = []
    for item in files:
        if isinstance(item, Todo):
            result.append(item)
            continue
        if isinstance(item, str):
            result.append(todo(item, pages=pages))
            continue
        if isinstance(item, tuple):
            result.append(todo(resource=item[0], pages=item[1]))
            continue
    return result


def simple(path: str) -> str:
    parent = utila.file_name(utila.path_parent(path))
    filename = utila.file_name(path)
    result = f'{parent}_{filename}'
    return result


def pdf(item):
    """Determine file path for path page tuple.

    >>> import power; pdf((power.DISS173_PDF, '10:45'))
    '...diss173.pdf'
    >>> import power; pdf(power.DISS173_PDF)
    '...diss173.pdf'
    """
    if not isinstance(item, str):
        return item[0]
    return item
