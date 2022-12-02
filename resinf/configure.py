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

PROJECT = None
WORKER = None


def setup(root: str, worker: int = 6, validate: bool = True):
    """\
    Args:
        root(str): path to root of resource
        worker(int): select number of used processes, use -1 for os.cpu_count
        validate(bool): if True check that `root` exists

    >>> setup(__file__)
    """
    assert os.path.exists(root) or not validate, str(root)
    # allow to setup from any existing file
    if validate:
        root = utila.baw_root(root)
    global PROJECT  # pylint:disable=global-statement
    PROJECT = root
    # required to use updated PROJECT of getroot
    assert worker >= -1, f'invalid worker count: {worker}'
    global WORKER  # pylint:disable=global-statement
    WORKER = os.cpu_count if worker == -1 else worker


def mainpackage(root: str) -> str:
    """\
    >>> mainpackage(__file__)
    'resinf'
    """
    name = utila.baw_name(root)
    return name


GENERATED = 'resources/generated'


def getroot(project: str = None):
    if not project:
        project = PROJECT
    baw = os.environ.get('BAW', None)
    if not baw:
        # TODO: REMOVE OLD BEHAVIOR
        root = os.path.join(utila.tmp(project), GENERATED)
        utila.error(f'DEFINE $BAW USE OLD PATH INSTEAD: {root}')
        return root
    projectname = os.path.split(project)[1]
    root = os.path.join(baw, 'generated', projectname)
    return root


def worker_count():
    return WORKER
