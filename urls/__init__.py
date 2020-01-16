# ----------------------------------------------------------------------------
# Copyright (c) 2016-2020, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# flake8: noqa

from ._old import MAP_OLD
from ._2019 import MAP_2019
from ._2020 import MAP_2020


MAP = {
    'distro/core/aws-amis.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/aws-amis.txt',
    'distro/core/virtualbox-images.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/virtualbox-images.txt',

    **MAP_OLD,

    **MAP_2019,

    **MAP_2020,
}


__all__ = ['MAP']
