#!/usr/bin/env python
import copy_reg
from twisted.internet import reactor

# This is a hack to overcome a bug in python
from ooni.utils.hacks import patched_reduce_ex
copy_reg._reduce_ex = patched_reduce_ex

# from ooni.oonicli import run
# run()
from ooni.oonicli import runWithDaemonDirector
runWithDaemonDirector()
reactor.run()
