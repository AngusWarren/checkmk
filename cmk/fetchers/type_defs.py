#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
"""Package containing the fetchers to the data sources."""

from typing import TypeVar, Union

from cmk.utils.type_defs import AgentRawData

from cmk.snmplib.type_defs import SNMPRawData

__all__ = ["BoundedAbstractRawData"]

# TODO(ml): This type does not really belong here but there currently
#           is not better place.
AbstractRawData = Union[AgentRawData, SNMPRawData]
BoundedAbstractRawData = TypeVar("BoundedAbstractRawData", bound=AbstractRawData)
