## This file is part of Scapy
## See http://www.secdev.org/projects/scapy for more informations
## Copyright (C) Alexander Bluhm <alexander.bluhm@gmx.net>
## Copyright (C) Philippe Biondi <phil@secdev.org>
## This program is published under a GPLv2 license

from scapy.consts import OPENBSD
from scapy.packet import *
from scapy.fields import *
from scapy.layers.inet import IP
if conf.ipv6_enabled:
    from scapy.layers.inet6 import IPv6
from scapy.config import conf

class Loop(Packet):
    name = "Loop"
    # from OpenBSD src/sys/net/if_loop.c
    fields_desc = [ IntEnumField("addrfamily", 2, { socket.AF_INET: "IPv4",
                                                    socket.AF_INET6: "IPv6" }),
                    ]
    def mysummary(self):
        return self.sprintf("%Loop.addrfamily%")

bind_layers(Loop, IP, addrfamily=socket.AF_INET)
if conf.ipv6_enabled:
    bind_layers(Loop, IPv6, addrfamily=socket.AF_INET6)

if OPENBSD:
    conf.l2types.register(12, Loop)
else:
    conf.l2types.register(108, Loop)
