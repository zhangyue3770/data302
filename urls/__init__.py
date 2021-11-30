# ----------------------------------------------------------------------------
# Copyright (c) 2016-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# flake8: noqa

from ._old import MAP_OLD
from ._permanent import MAP_PERMANENT
from ._2019 import MAP_2019
from ._2020 import MAP_2020
from ._2021 import MAP_2021
from ._2022 import MAP_2022


MAP = {
    **MAP_OLD,

    **MAP_PERMANENT,

    **MAP_2019,

    **MAP_2020,

    **MAP_2021,

    **MAP_2022,
}


__all__ = ['MAP']
