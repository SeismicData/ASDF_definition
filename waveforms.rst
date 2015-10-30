Waveform Data
=============

Waveform data and station meta information is organized by utilizing the
network, station, location, and channel codes described in the `SEED Manual
<http://www.fdsn.org/seed_manual/SEEDManual_V2.4.pdf>`_. They are widely
employed in the seismological community and serve to uniquely identify a
recording instrument.

``ASDF`` organizes all data that can be considered a seismic waveform (an
actual seismic recording, barometric or temperature data, ...) under the
``/Waveforms`` group. Data within that group is organized per seismic station,
i.e. a unique combination of network and station code.

+----------------+-------------------------------------------------------------+
| ``/Waveforms`` Group                                                         |
+================+=============================================================+
| **Type**       | Group                                                       |
+----------------+-------------------------------------------------------------+
| **Path**       | ``/Waveforms``                                              |
+----------------+-------------------------------------------------------------+
| **Required**   | False                                                       |
+----------------+-------------------------------------------------------------+
| **Description**| Contains waveforms and station meta information.            |
+----------------+-------------------------------------------------------------+


Station Groups
--------------

Data under the ``/Waveforms`` group is organized per station in a separate
group, named  ``{NET}.{STA}`` where ``{NET}`` and ``{STA}`` are placeholders
for the network and station codes as defined by the SEED standard. The network
code can have 1 or 2 letter, the station code between 1 and 5.

+----------------+-------------------------------------------------------------+
| ``/Waveforms/{NET}.{STA}`` Group                                             |
+================+=============================================================+
| **Type**       | Group                                                       |
+----------------+-------------------------------------------------------------+
| **Full Path**  | ``/Waveforms/{NET}.{STA}``                                  |
+----------------+-------------------------------------------------------------+
| **RegEx**      | ``^[A-Z0-9]{1,2}\\.[A-Z0-9]{1,5}$``                         |
+----------------+-------------------------------------------------------------+
| **Required**   | False                                                       |
+----------------+-------------------------------------------------------------+
| **Description**| Contains waveforms and station meta information for a       |
|                | single station.                                             |
+----------------+-------------------------------------------------------------+


StationXML
^^^^^^^^^^

Each station can have a single `FDSN StationXML
<http://www.fdsn.org/xml/station/>`_ file associated with it. ``ASDF`` does not
care about the version of the StationXML file but the file must not contain
information about other channels. The file are stored as a binary dump in a
data set called ``StationXML``. Thus dealing with the encoding is delegated to
whatever XML library reads the binary dump.

+----------------+-------------------------------------------------------------+
| ``/Waveforms/{NET}.{STA}.StationXML`` Data Set                               |
+================+=============================================================+
| **Type**       | Data Set                                                    |
+----------------+-------------------------------------------------------------+
| **Path**       | ``/Waveforms/{NET}.{STA}.StationXML``                       |
+----------------+-------------------------------------------------------------+
| **Description**| Station information as a single StationXML file for a       |
|                | particular station.                                         |
+----------------+-------------------------------------------------------------+
| **Data Type**  | ``H5T_STD_I8LE``                                            |
+----------------+-------------------------------------------------------------+
| **Required**   | False                                                       |
+----------------+-------------------------------------------------------------+
| **Details**    |  .. code::                                                  |
|                |                                                             |
|                |      DATASET "StationXML" {                                 |
|                |          DATATYPE  H5T_STD_I8LE                             |
|                |          DATASPACE  SIMPLE { ( * ) / ( H5S_UNLIMITED ) }    |
|                |      }                                                      |
+----------------+-------------------------------------------------------------+


Waveform Traces
^^^^^^^^^^^^^^^

The actual waveform data is stored on a per trace basis. A trace is a
continuous nice behaving time series from a single channel with a regular
sampling interval. It has a defined start time and a sampling rate and no gaps
and overlaps. Gaps and overlaps are then represented by having multiple traces.
Each station group can have an arbitrary number of traces and each trace can be
arbitrarily long.

Allowed data types are single and double precision two's complement signed
integers and single and double precision IEEE 768 floating point numbers which
happen to be the native data types on most platforms. HDF5 transparently deals
with byte order issues so choose whichever endianness is most suitable for your
platform.

Data sets are named according to the scheme

``{NET}.{STA}/{NET}.{STA}.{LOC}.{CHA}__{ST}__{ET}__{TAG}``

with the following placeholders:

* ``{NET}``: The network code.
* ``{STA}``: The station code.
* ``{LOC}``: The location code.
* ``{CHA}``: The channel code.
* ``{ST}``: The approximate start time in UTC as an
  `ISO 8601 <http://www.w3.org/TR/NOTE-datetime>`_ date time string. Serves only
  to generate a suitable data set name. The actual start time is specified as
  an attribute.
* ``{ET}``: The approximate end time in UTC as an
  `ISO 8601 <http://www.w3.org/TR/NOTE-datetime>`_ date time string. Serves
  only to generate a suitable data set name.
* ``{TAG}``: The hierarchical tag. Please read :doc:`of_tags_and_labels` for
  further explanations.

A full example is

``CN.FRB..BHZ__1998-09-01T10:24:49__1998-09-01T12:09:49__tag``

and the exact pattern is specificed as a regular expression in the following table.

+----------------+-----------------------------------------------------------------------+
| ``/Waveforms/{NET}.{STA}/{NET}.{STA}.{LOC}.{CHA}__{ST}__{ET}__{TAG}`` Data Set         |
+================+=======================================================================+
| **Type**       | Data Set                                                              |
+----------------+-----------------------------------------------------------------------+
| **Full Path**  | ``/Waveforms/{NET}.{STA}/{NET}.{STA}.{LOC}.{CHA}__{ST}__{ET}__{TAG}`` |
+----------------+-----------------------------------------------------------------------+
| **RegEx**      | ``^[A-Z0-9]{1,2}\\.[A-Z0-9]{1,5}\\.[A-Z0-9]{0,2}\\.[A-Z0-9]{3}__``    |
|                | ``(18|19|20|21)\\d{2}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T``     |
|                | ``([0-1][0-9]|2[0-4]):([0-5]\\d|60):[0-5]\\d__(18|19|20|21)\\d{2}-``  |
|                | ``(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-4]):``     |
|                | ``([0-5]\\d|60):[0-5]\\d__[a-z_0-9]+$``                               |
+----------------+-----------------------------------------------------------------------+
| **Description**| Waveform data for a single trace.                                     |
+----------------+-----------------------------------------------------------------------+
| **Data Type**  | ``H5T_IEEE_F32LE``, ``H5T_IEEE_F64LE``, ``H5T_IEEE_F32BE``,           |
|                | ``H5T_IEEE_F64BE``, ``H5T_STD_I32LE``, ``H5T_STD_I64LE``,             |
|                | ``H5T_STD_I32BE``, ``H5T_STD_I64BE``                                  |
+----------------+-----------------------------------------------------------------------+
| **Required**   | False                                                                 |
+----------------+-----------------------------------------------------------------------+
| **Details**    |  .. code::                                                            |
|                |                                                                       |
|                |      DATASET "NET.STA.LOC.CHA__ST__ET__TAG" {                         |
|                |          DATATYPE  H5T_IEEE_F32LE                                     |
|                |          DATASPACE  SIMPLE { ( * ) / ( H5S_UNLIMITED ) }              |
|                |      }                                                                |
+----------------+-----------------------------------------------------------------------+


Waveform Trace Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^

The attributes of each trace are described here. Only two are mandatory, the
time of the first sample and the sampling interval.

+----------------+-------------------------------------------------------------+
| ``sampling_rate`` Attribute                                                  |
+================+=============================================================+
| **Type**       | Attribute                                                   |
+----------------+-------------------------------------------------------------+
| **Name**       | ``sampling_rate``                                           |
+----------------+-------------------------------------------------------------+
| **Description**| The sampling rate of the the waveform trace in ``Hz``.      |
|                | Must naturally be positive and non-zero.                    |
+----------------+-------------------------------------------------------------+
| **Data Type**  | ``H5T_IEEE_F64LE``, ``H5T_IEEE_F64BE``                      |
+----------------+-------------------------------------------------------------+
| **Required**   | True                                                        |
+----------------+-------------------------------------------------------------+
| **Details**    |  .. code::                                                  |
|                |                                                             |
|                |      ATTRIBUTE "sampling_rate" {                            |
|                |         DATATYPE  H5T_IEEE_F64LE                            |
|                |         DATASPACE  SCALAR                                   |
|                |      }                                                      |
+----------------+-------------------------------------------------------------+

+----------------+-------------------------------------------------------------+
| ``starttime`` Attribute                                                      |
+================+=============================================================+
| **Type**       | Attribute                                                   |
+----------------+-------------------------------------------------------------+
| **Name**       | ``starttime``                                               |
+----------------+-------------------------------------------------------------+
| **Description**| The time of the first sample as a UNIX epoch time in        |
|                | nanoseconds in UTC. It provides an approximate temporal     |
|                | range from the year 1680 to 2260 which is plenty for all    |
|                | envisioned applications.                                    |
+----------------+-------------------------------------------------------------+
| **Data Type**  | ``H5T_STD_I64LE``, ``H5T_STD_I64BE``                        |
+----------------+-------------------------------------------------------------+
| **Required**   | True                                                        |
+----------------+-------------------------------------------------------------+
| **Details**    |  .. code::                                                  |
|                |                                                             |
|                |      ATTRIBUTE "starttime" {                                |
|                |         DATATYPE  H5T_STD_I64LE                             |
|                |         DATASPACE  SCALAR                                   |
|                |      }                                                      |
+----------------+-------------------------------------------------------------+

Provenance for that trace can be stored as an identifier to a certain
provenance record which represents that particular trace in time. It is
possible (and recommended) but not necessary that a provenance document in the
:doc:`provenance` contains a record with that id.


+----------------+-------------------------------------------------------------+
| ``provenance_id`` Attribute                                                  |
+================+=============================================================+
| **Type**       | Attribute                                                   |
+----------------+-------------------------------------------------------------+
| **Name**       | ``provenance_id``                                           |
+----------------+-------------------------------------------------------------+
| **Description**| The id of a provenance record representing the current      |
|                | state of the waveform trace.                                |
+----------------+-------------------------------------------------------------+
| **Required**   | False                                                       |
+----------------+-------------------------------------------------------------+
| **Details**    |  .. code::                                                  |
|                |                                                             |
|                |      ATTRIBUTE "provenance_id" {                            |
|                |          DATATYPE  H5T_STRING {                             |
|                |              STRPAD H5T_STR_NULLPAD;                        |
|                |              CSET H5T_CSET_ASCII;                           |
|                |              CTYPE H5T_C_S1;                                |
|                |          }                                                  |
|                |          DATASPACE  SCALAR;                                 |
|                |      }                                                      |
+----------------+-------------------------------------------------------------+


Next are four optional identifiers that refer to different elements within a
QuakeML file and enable the association of a waveform trace with an event or a
specific origin, magnitude, or focal mechanism. The later three are mainly of
interest for synthetic data where these three are exactly known.

+----------------+-------------------------------------------------------------+
| ``event_id`` Attribute                                                       |
+================+=============================================================+
| **Type**       | Attribute                                                   |
+----------------+-------------------------------------------------------------+
| **Name**       | ``event_id``                                                |
+----------------+-------------------------------------------------------------+
| **Description**| The id of the event associated with that waveform.          |
+----------------+-------------------------------------------------------------+
| **Required**   | False                                                       |
+----------------+-------------------------------------------------------------+
| **Details**    |  .. code::                                                  |
|                |                                                             |
|                |      ATTRIBUTE "event_id" {                                 |
|                |          DATATYPE  H5T_STRING {                             |
|                |              STRPAD H5T_STR_NULLPAD;                        |
|                |              CSET H5T_CSET_ASCII;                           |
|                |              CTYPE H5T_C_S1;                                |
|                |          }                                                  |
|                |          DATASPACE  SCALAR;                                 |
|                |      }                                                      |
+----------------+-------------------------------------------------------------+

+----------------+-------------------------------------------------------------+
| ``origin_id`` Attribute                                                      |
+================+=============================================================+
| **Type**       | Attribute                                                   |
+----------------+-------------------------------------------------------------+
| **Name**       | ``origin_id``                                               |
+----------------+-------------------------------------------------------------+
| **Description**| The id of the origin associated with that waveform.         |
+----------------+-------------------------------------------------------------+
| **Required**   | False                                                       |
+----------------+-------------------------------------------------------------+
| **Details**    |  .. code::                                                  |
|                |                                                             |
|                |      ATTRIBUTE "origin_id" {                                |
|                |          DATATYPE  H5T_STRING {                             |
|                |              STRPAD H5T_STR_NULLPAD;                        |
|                |              CSET H5T_CSET_ASCII;                           |
|                |              CTYPE H5T_C_S1;                                |
|                |          }                                                  |
|                |          DATASPACE  SCALAR;                                 |
|                |      }                                                      |
+----------------+-------------------------------------------------------------+

+----------------+-------------------------------------------------------------+
| ``magnitude_id`` Attribute                                                   |
+================+=============================================================+
| **Type**       | Attribute                                                   |
+----------------+-------------------------------------------------------------+
| **Name**       | ``magnitude_id``                                            |
+----------------+-------------------------------------------------------------+
| **Description**| The id of the magnitude associated with that waveform.      |
+----------------+-------------------------------------------------------------+
| **Required**   | False                                                       |
+----------------+-------------------------------------------------------------+
| **Details**    |  .. code::                                                  |
|                |                                                             |
|                |      ATTRIBUTE "magnitude_id" {                             |
|                |          DATATYPE  H5T_STRING {                             |
|                |              STRPAD H5T_STR_NULLPAD;                        |
|                |              CSET H5T_CSET_ASCII;                           |
|                |              CTYPE H5T_C_S1;                                |
|                |          }                                                  |
|                |          DATASPACE  SCALAR;                                 |
|                |      }                                                      |
+----------------+-------------------------------------------------------------+

+----------------+-------------------------------------------------------------+
| ``focal_mechanism_id`` Attribute                                             |
+================+=============================================================+
| **Type**       | Attribute                                                   |
+----------------+-------------------------------------------------------------+
| **Name**       | ``focal_mechanism_id``                                      |
+----------------+-------------------------------------------------------------+
| **Description**| The id of the focal_mechanism associated with that waveform.|
+----------------+-------------------------------------------------------------+
| **Required**   | False                                                       |
+----------------+-------------------------------------------------------------+
| **Details**    |  .. code::                                                  |
|                |                                                             |
|                |      ATTRIBUTE "focal_mechanism_id" {                       |
|                |          DATATYPE  H5T_STRING {                             |
|                |              STRPAD H5T_STR_NULLPAD;                        |
|                |              CSET H5T_CSET_ASCII;                           |
|                |              CTYPE H5T_C_S1;                                |
|                |          }                                                  |
|                |          DATASPACE  SCALAR;                                 |
|                |      }                                                      |
+----------------+-------------------------------------------------------------+


Last but not least each waveform trace can also have any number of labels
associated with it. Please note that these are different from tags, see
:doc:`of_tags_and_labels` for details. The labels are stored as comma separated
UTF-8 strings so the two labels ``label 1``, and ``äöü`` would be
stored as ``"label 1, äöü"``.

+----------------+-------------------------------------------------------------+
| ``labels`` Attribute                                                         |
+================+=============================================================+
| **Type**       | Attribute                                                   |
+----------------+-------------------------------------------------------------+
| **Name**       | ``labels``                                                  |
+----------------+-------------------------------------------------------------+
| **Description**| The labels of this waveform as a comma-separated UTF-8      |
|                | string.                                                     |
+----------------+-------------------------------------------------------------+
| **Required**   | False                                                       |
+----------------+-------------------------------------------------------------+
| **Details**    |  .. code::                                                  |
|                |                                                             |
|                |      ATTRIBUTE "labels" {                                   |
|                |         DATATYPE  H5T_STRING {                              |
|                |            STRSIZE H5T_VARIABLE;                            |
|                |            STRPAD H5T_STR_NULLTERM;                         |
|                |            CSET H5T_CSET_UTF8;                              |
|                |            CTYPE H5T_C_S1;                                  |
|                |         }                                                   |
|                |         DATASPACE  SCALAR                                   |
|                |      }                                                      |
+----------------+-------------------------------------------------------------+
