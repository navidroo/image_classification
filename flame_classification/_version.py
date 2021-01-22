"""Versioning information."""

#__version_info__ = (0, 2, x, '-beta')
__author__ = 'Seyed Navid Roohani Isfahani'
__version_info__ = (0, 1, 0)
__version__ = '.'.join(map(str, __version_info__[:3]))
if len(__version_info__) == 4:
    __version__ += __version_info__[-1]
