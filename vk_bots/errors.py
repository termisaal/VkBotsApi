"""
VK Bots API Wrapper
Copyright (c) 2020-2021 termisaal
"""


class VKAPIError(Exception):
    """Base class for VK API errors"""
    def __init__(self, error_code, error_msg=''):
        """

        :param int error_code:
        :param str error_msg:
        """
        message = str(error_code) + (f' ({error_msg})' or '')
        super().__init__(message)