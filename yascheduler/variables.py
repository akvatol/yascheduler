#!/usr/bin/env python3

from os import getenv

__version__ = "0.9.9"

CONFIG_FILE = getenv("YASCHEDULER_CONF_PATH", "/etc/yascheduler/yascheduler.conf")
LOG_FILE = getenv("YASCHEDULER_LOG_PATH", "/var/log/yascheduler.log")
PID_FILE = getenv("YASCHEDULER_PID_PATH", "/var/run/yascheduler.pid")
