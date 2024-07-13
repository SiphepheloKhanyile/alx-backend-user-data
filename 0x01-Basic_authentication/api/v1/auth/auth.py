#!/usr/bin/env python3
"""
API Authentication
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """
    Authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """check if path requires authentication
        Args:
            path (str): request path
            excluded_paths (List[str]): excluded paths
        Returns:
            bool: boolean
        """
        if path is not None and path[-1] != "/":
            temp_path = path
            path = f"{temp_path}/"

        if excluded_paths is None or len(excluded_paths) < 1:
            return True

        if path not in excluded_paths or path is None:
            return True

        return False

    def authorization_header(self, request_obj=None) -> str:
        """check if `Authorization` header exists
        Args:
            request_obj (_type_): request. Defaults to None.
        Returns:
            str: _description_
        """
        if request_obj is None:
            return None
        if request_obj.headers.get("Authorization") is None:
            return None
        return request_obj.headers.get("Authorization")

    def current_user(self, request_obj=None) -> TypeVar('User'):
        """_summary_
        """
        return None
