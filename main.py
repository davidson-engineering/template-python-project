#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Matthew Davidson
# Created Date: 2024-01-01
# version ='0.0.1'
# ---------------------------------------------------------------------------
"""a_short_project_description"""
# ---------------------------------------------------------------------------

import logging
from logging.config import dictConfig

# Import the load_configs function
from config_loader import load_configs

LOGGING_CONFIG_FILEPATH = "config/logging.yaml"
APP_CONFIG_FILEPATH = "config/application.toml"

# Load user configurations using the config_loader module
configs = load_configs([APP_CONFIG_FILEPATH, LOGGING_CONFIG_FILEPATH])

# Configure logging using the specified logging configuration
dictConfig(configs["logging"])


def main():
    logging.info(configs["application"])


if __name__ == "__main__":
    main()
