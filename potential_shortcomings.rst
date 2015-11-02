Potential Shortcomings
======================

This section aims to point out several shortcomings of the ``ASDF`` format and
potential ways to deal with them where applicable.

Irregularly sampled data
------------------------

The ASDF format in the initial definition can not deal with this and neither
can most signal processing tools in use in seismology. If this ever become a
serious issue, the format definition will have to be extended. One possibility
would be to use 2D arrays for irregularly sampled components; one dimension
denoting time, the other the data.

Finite Sources
--------------

This is mainly a limitation of the QuakeML format and thus should be dealt with
therein. Currently this could be worked around by either specifying a finite
source as a large number of point sources in a QuakeML file or by storing a
more appropriate representation of finite sources in the auxiliary data section
of ``ASDF``.

Source Time Functions
---------------------

This is mainly a limitation of the QuakeML format and thus should be dealt with
therein. As of now this can be worked around by storing the source time
functions in the auxiliary data section.
