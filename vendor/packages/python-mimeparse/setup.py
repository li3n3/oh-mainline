#!/usr/bin/env python

from distutils.core import setup
import mimeparse

setup(
    name="python-mimeparse",
    py_modules=["mimeparse"],
    version=mimeparse.__version__,
    description="A module provides basic functions for parsing mime-type names and matching them against a list of media-ranges.",
    author="David Tsai",
    author_email="dbtsai@dbtsai.com",
    url="https://github.com/dbtsai/python-mimeparse",
    download_url="http://pypi.python.org/packages/source/p/python-mimeparse/python-mimeparse-0.1.4.tar.gz",
    keywords=["mime-type"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description="""
This module provides basic functions for handling mime-types. It can handle
matching mime-types against a list of media-ranges. See section 14.1 of
the HTTP specification [RFC 2616] for a complete explanation.

   http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.1

Contents:
    - parse_mime_type():   Parses a mime-type into its component parts.
    - parse_media_range(): Media-ranges are mime-types with wild-cards and a "q" quality parameter.
    - quality():           Determines the quality ("q") of a mime-type when compared against a list of media-ranges.
    - quality_parsed():    Just like quality() except the second parameter must be pre-parsed.
    - best_match():        Choose the mime-type with the highest quality ("q") from a list of candidates.
"""
)
