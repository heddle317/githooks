The official rhino.js has been discontinued:

https://github.com/douglascrockford/JSLint/commit/ca120a731db548c0014320fa0c196edc613536ae#diff-3

The announcement is here:

http://tech.groups.yahoo.com/group/jslint_com/message/1636

I am dropping support for rhino.js and wsh.js because others have improved on
them. If you have such an improvement, please add a record describing it.
Thank you.

The rhino.js has been adapted from the jslint-utils, which we use for Hudson checks (figured we
might as well keep them consistent):

https://github.com/mikewest/jslint-utils/blob/master/lib/rhino.js

To compile a new version of JSLint that provides a wrapper to support Rhino, you can run "make".
Take a look at the Makefile for more details.

This updated JSLint version seems to complain more about whitespace errors, so they have
been turned off for now (white = False)

JSLint seems to have a bug in passfail bug that has been reported to the author:

https://github.com/rogerhu/JSLint/commit/ac9e88a1aadcc26eb7f5d8b76abdb0fe2854c71b