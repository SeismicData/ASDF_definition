Potential Shortcomings
======================

This section aims to point out several shortcomings of the format and potential
ways to deal with them where applicable.

Irregularly sampled data
------------------------

The ASDF format in the initial definition can not deal with this and neither can
most signal processing tools in use in seismology. If this ever become a
serious issue, the format definition will have to be extended. One possibility
would be to use 2D arrays for irregularly sampled components; one dimension
denoting time, the other the data.

Finite Sources
--------------

This is mainly a limitation of the QuakeML format and thus should be dealt with
therein. Currently this could be worked around by

Source Time Functions
---------------------

This is mainly a limitation of the QuakeML format and thus should be dealt with
therein.
