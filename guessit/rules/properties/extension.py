#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Season/Episode numbering support
"""
from rebulk import Rebulk

import regex as re

EXTENSION = Rebulk().regex_defaults(flags=re.IGNORECASE)
EXTENSION.defaults(name='extension', formatter=lambda value: value[1:], conflict_solver=lambda match, other: other)

EXTENSION.regex(r'\.\L<exts>$', exts=['srt', 'idx', 'sub', 'ssa', 'ass'], tags=["subtitle"])
EXTENSION.regex(r'\.\L<exts>$', exts=['nfo'], tags=["info"])
EXTENSION.regex(r'\.\L<exts>$', exts=['3g2', '3gp', '3gp2', 'asf', 'avi', 'divx', 'flv', 'm4v', 'mk2',
                                      'mka', 'mkv', 'mov', 'mp4', 'mp4a', 'mpeg', 'mpg', 'ogg', 'ogm',
                                      'ogv', 'qt', 'ra', 'ram', 'rm', 'ts', 'wav', 'webm', 'wma', 'wmv',
                                      'iso', 'vob'], tags=["video"])