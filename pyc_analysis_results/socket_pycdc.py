# Source Generated with Decompyle++
# File: socket.pyc (Python 3.10)

__doc__ = "This module provides socket operations and some related functions.\nOn Unix, it supports IP (Internet Protocol) and Unix domain sockets.\nOn other systems, it only supports IP. Functions specific for a\nsocket are available as methods of the socket object.\n\nFunctions:\n\nsocket() -- create a new socket object\nsocketpair() -- create a pair of new socket objects [*]\nfromfd() -- create a socket object from an open file descriptor [*]\nsend_fds() -- Send file descriptor to the socket.\nrecv_fds() -- Recieve file descriptors from the socket.\nfromshare() -- create a socket object from data received from socket.share() [*]\ngethostname() -- return the current hostname\ngethostbyname() -- map a hostname to its IP number\ngethostbyaddr() -- map an IP number or hostname to DNS info\ngetservbyname() -- map a service name and a protocol name to a port number\ngetprotobyname() -- map a protocol name (e.g. 'tcp') to a number\nntohs(), ntohl() -- convert 16, 32 bit int from network to host byte order\nhtons(), htonl() -- convert 16, 32 bit int from host to network byte order\ninet_aton() -- convert IP addr string (123.45.67.89) to 32-bit packed format\ninet_ntoa() -- convert 32-bit packed format IP to string (123.45.67.89)\nsocket.getdefaulttimeout() -- get the default timeout value\nsocket.setdefaulttimeout() -- set the default timeout value\ncreate_connection() -- connects to an address, with an optional timeout and\n                       optional source address.\n\n [*] not available on all platforms!\n\nSpecial objects:\n\nSocketType -- type object for socket objects\nerror -- exception raised for I/O errors\nhas_ipv6 -- boolean value indicating if IPv6 is supported\n\nIntEnum constants:\n\nAF_INET, AF_UNIX -- socket domains (first argument to socket() call)\nSOCK_STREAM, SOCK_DGRAM, SOCK_RAW -- socket types (second argument)\n\nInteger constants:\n\nMany other constants may be defined; these may be used in calls to\nthe setsockopt() and getsockopt() methods.\n"
import _socket
from _socket import *
import os
import sys
import io
import selectors
from enum import IntEnum, IntFlag
# WARNING: Decompyle incomplete
