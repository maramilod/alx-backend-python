#!/usr/bin/env python3
'''
h
e
y
'''
from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    ''' return first item of list or none if list is epmty  '''
    if lst:
        return lst[0]
    else:
        return None
