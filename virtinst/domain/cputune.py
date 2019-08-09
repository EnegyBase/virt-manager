# Copyright (c) 2018 Oracle and/or its affiliates. All rights reserved.
#
# This work is licensed under the GNU GPLv2 or later.
# See the COPYING file in the top-level directory.

from ..xmlbuilder import XMLBuilder, XMLProperty, XMLChildProperty


class _VCPUPin(XMLBuilder):
    """
    Class for generating <cputune> child <vcpupin> XML
    """
    XML_NAME = "vcpupin"
    _XML_PROP_ORDER = ["vcpu", "cpuset"]

    vcpu = XMLProperty("./@vcpu", is_int=True)
    cpuset = XMLProperty("./@cpuset")


class _CacheCPU(XMLBuilder):
    """
    Class for generating <cachetune> child <cache> XML
    """
    XML_NAME = "cache"
    _XML_PROP_ORDER = ["level", "id", "type", "size", "unit"]

    level = XMLProperty("./@level", is_int=True)
    id = XMLProperty("./@id", is_int=True)
    type = XMLProperty("./@type")
    size = XMLProperty("./@size", is_int=True)
    unit = XMLProperty("./@unit")


class _CacheTuneCPU(XMLBuilder):
    """
    Class for generating <cputune> child <cachetune> XML
    """
    XML_NAME = "cachetune"
    _XML_PROP_ORDER = ["vcpus", "caches"]

    vcpus = XMLProperty("./@vcpus")
    caches = XMLChildProperty(_CacheCPU)


class DomainCputune(XMLBuilder):
    """
    Class for generating <cpu> XML
    """
    XML_NAME = "cputune"
    _XML_PROP_ORDER = ["vcpus", "cachetune"]

    vcpus = XMLChildProperty(_VCPUPin)
    cachetune = XMLChildProperty(_CacheTuneCPU)
