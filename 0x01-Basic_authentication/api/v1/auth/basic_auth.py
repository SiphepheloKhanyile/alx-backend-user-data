#!/usr/bin/env python3
"""
API Authentication
"""
import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Inherits from Auth class
    """
    def extract_base64_authorization_header(self, authorization_header: str)\
            -> str:
        """
        Args:
            authorization_header (str): Authorization header
        Returns:
            str: Base64 part of the Authorization header
            for a Basic Authentication
        """
        if authorization_header is None:
            return None

        if isinstance(authorization_header, str) is False:
            return None  # type: ignore

        auth_header_list = authorization_header.split(" ")

        if len(auth_header_list) < 2:
            return None  # type: ignore

        if auth_header_list[0] != "Basic":
            return None  # type: ignore

        return auth_header_list[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64 string
            `base64_authorization_header`
        Args:
            base64_authorization_header (str):
        Returns:
            str: decoded base64 authorization
        """
        if base64_authorization_header is None:
            return None

        if isinstance(base64_authorization_header, str) is False:
            return None  # type: ignore

        try:
            decoded_string = base64.b64decode(base64_authorization_header)
            decoded_value = decoded_string.decode("utf-8")
            return decoded_value
        except Exception:
            return None  # type: ignore
