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
        """_summary_
        Args:
            path (str): _description_
            excluded_paths (List[str]): _description_
        Returns:
            bool: _description_
        """
        if path is not None and path[-1] != "/":
            temp_path = path
            path = f"{temp_path}/"

        if excluded_paths is None or len(excluded_paths) < 1:
            return True

        if path not in excluded_paths or path is None:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """_summary_
        Args:
            request (_type_, optional): _description_. Defaults to None.
        Returns:
            str: _description_
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """_summary_
        """
        return None
