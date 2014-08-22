Technical Details
=================

Internal Data Layout
--------------------

ASDF supports two fundamentally different layouts: one for data in the classical
SEED structure sorted by network, station, location, and channel, and a second
one for active source seismic data common in the industry. The demands of both
types of data are too distinct to allow for storage under one common structure.

SEED structure layout
---------------------

In this case the data is organized per station, each of which will have its own
folder. The metainformation for each station and receivers therein is described
in a StationXML file in the folder.

Metadata is available in one of the following forms.

Using the proven SEED channel ids and corresponding StationXML files for
example enables the storage of arbitrarily oriented components and the
identification of non-seismometer measurements like GPS or pressure data (we
should investigate if the GPS people actually use SEED, I know the SCEC serves
them as SAC and the actual raw GPS measurements are their own formats, but the
actual displacement could just as well be stored in a SEED file - then it would
also be suitable for ASDF).

The actual structure is defined as follows

.. code-block:: xml

    - QuakeML (optional)
    - Waveforms/
        |- NET.STA/
        |   |- StationXML (optional but recommended)
        |   |- NET.STA.LOC.CHAN_STARTTIME_ENDTIME[_TAG]/
        |   |    |- Provenance (optional, can be a reference)
        |   |    |- EventID (optional)
        |   |    |- OriginID (optional)
        |   |    |- MagnitudeID (optional)
        |   |    |- FocalMechanismID (optional)
        |   |    |- Data (Array)
        |   |    |   |- Starttime (Attribute)
        |   |    |   |- Sample Spacing (Attribute)
        |   |- NET.STA.LOC.CHAN_STARTTIME_ENDTIME[_TAG]/
        |   |    |- Provenance (optional, can be a reference)
        |   |    |- EventID (optional)
        |   |    |- OriginID (optional)
        |   |    |- MagnitudeID (optional)
        |   |    |- FocalMechanismID (optional)
        |   |    |- Data (Array)
        |   |    |   |- Starttime (Attribute)
        |   |    |   |- Sample Spacing (Attribute)
        |   |- ...
        |- ...
    - Provenances/ (optional)
        |- ...


The actual waveform data will reside in the *Waveforms* folder further sorted
per stations. This per-station sorting allows a natural use of the StationXML
format to describe all receivers of a single station.

Each station folder contains an arbitrary list of continuous waveform traces
identifiable via the locations and channel attributes and the start- and
endtime. ASDF defines a continuous trace as a single chunk of data without any
gaps or overlaps. This implies that the time of the first sample and the sample
spacing are enough to uniquely determine the time of every sample.


Diagram
-------

This simple diagrams aims to illustrate the main structure. Arrows denote links
either via ids or "symlinks". The diagram denotes the contents of the
container.

.. image:: https://raw.github.com/wiki/krischer/asdf/images/sdf.png
    :width: 100%
    :align: center

Naming Details
^^^^^^^^^^^^^^

**NET, STA, LOC, CHAN** are placeholders for the network, station, location,
and channel codes as defined in the [SEED
Manual](http://www.fdsn.org/seed_manual/SEEDManual_V2.4.pdf). They therefore
follow the same limitations regarding the allowed characters (alphanumeric
ASCII strings) and the length (network: 2, station: 5, location: 2, channel:
3).

The start- and endtimes for the folder name of the traces are to be specified
as UTC times as [ISO 8601](http://www.w3.org/TR/NOTE-datetime) datetime strings
with 4 digit year representations. Most programming languages have built-in
parsing routines for these strings. Note that the times here are just used for
a quick overview and sorting purposes. The high-precision time stored as an
attribute to the data array is the actually valid time.

The `_TAG` part of the name is used to differentiate traces with exactly the
same channel and duration, e.g. multiple synthetics from different simulations.

Active Source Seismic Data
^^^^^^^^^^^^^^^^^^^^^^^^^^
WIP

Should probably be defined as a new root folder. It is likely impossible to
shelter seismological time series under the same umbrella as active source
seismic data without jumping through some really awkward hoops. They are just
two very different data sets.

So I think the way to go is to defined two totally separate structures that can
coexist in the same file in peace.

The Time Datatype
^^^^^^^^^^^^^^^^^

The only slightly more complex data type in ASDF is the time data type.
Experience has shown that the available time resolution in preexisting data
formats is not fine enough for some applications like megahertz vibration
experiments. Although the aim of the ASDF format is to be as simplistic as
possible this slight complication is justified in the authors eyes making the
file format suitable for a whole new range of applications.

One possibility for this goal would be to specify times as follows, essentially
giving a timing accuracy of 10^(-19) seconds.

.. code-block:: xml

    - Time
        - UNIX timestamp (signed 64bit integer)
        - Decimals of the seconds (unsigned 64bit integer)

Data Streaming
^^^^^^^^^^^^^^

ASDF is well suited for the distribution and exchange of very large waveform
data sets. In order for data centers being able to support this pattern in a
reasonable manner the format needs to be streamable meaning it has to be
possible to create parts of the file, send them and in the meantime create the
next parts of the file, send them and so on...
This discards the need for creating large temporary files before they can be
sent to the user.


Test Suite
^^^^^^^^^^

To push and facilitate the adoption of the format into different tools, a
descriptive and comprehensive test suite should be made available. The test
suite should contains data descriptions and corresponding files so that any
implementations can be tested against it.


Potential Shortcomings
----------------------

This section aims to point out several shortcomings of the format and potential
ways to deal with them where applicable.

Irregularly sampled data
^^^^^^^^^^^^^^^^^^^^^^^^

The ASDF format in the initial definition can not deal with this and neither can
most signal processing tools in use in seismology. If this ever become a
serious issue, the format definition will have to be extended. One possibility
would be to use 2D arrays for irregularly sampled components; one dimension
denoting time, the other the data.

Finite Sources
^^^^^^^^^^^^^^

This is mainly a limitation of the QuakeML format and thus should be dealt with
therein.

Source Time Functions
^^^^^^^^^^^^^^^^^^^^^

This is mainly a limitation of the QuakeML format and thus should be dealt with
therein.
