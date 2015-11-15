Big Picture
===========

ASDF stores everything in an HDF5 file with a layout that is illustrated by the
following picture. It contains four parts, all of which are elaborated upon in
another section:

1. Earthquake information (yellow) is stored in the form of a single QuakeML
   file. It can store an arbitrary number of seismic events of various types.
2. Waveform information is stored in the green part at a per station
   granularity. This section also contains the station meta information in form
   of StationXML files. Please also note the possible associations of waveforms
   with parts of a seismic event and the possible provenance links.
3. Anything not a waveform is stored in the red section. Arbitrary nesting is
   possible alongside the capability to store provenance information.
4. The blue section finally contains a collection of provenance documents that
   can be referred to from other parts of the ASDF file.

.. image:: images/ASDF_container.*
    :width: 100%
    :align: center
