#!/usr/bin/env python

##This will work in development on a relative folder basis
##It will then work when installed in site-packages on a target system
##where the runner script is in /usr/bin (or wherever)
##
##So, you don't need anything special - no fancy path tricks.

import package.module

package.module.start ()
