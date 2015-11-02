Auxiliary Data
==============

Anything that is not a seismic waveform will be stored here. Conceptually this
group stores any data array (arbitrary data type and number of dimensions) with
associated meta information in an arbitrarily nested path.

+----------------+-------------------------------------------------------------+
| ``/AuxiliaryData`` Group                                                     |
+================+=============================================================+
| **Type**       | Group                                                       |
+----------------+-------------------------------------------------------------+
| **Full Path**  | ``/AuxiliaryData``                                          |
+----------------+-------------------------------------------------------------+
| **Required**   | False                                                       |
+----------------+-------------------------------------------------------------+
| **Description**| Any data that cannot be considered a waveform will be       |
|                | stored here.                                                |
+----------------+-------------------------------------------------------------+


The path is intended to group the data by data type and whatever grouping makes
sense for the data at hand. For cross correlations this might be
``/CrossCorrelations/Station_A/Station_B`` and for adjoint sources
``/AdjointSources/Event_A``. This is, by design, not fixed within the ``ASDF``
format as we are not experts in every field and it would take a long time to
come up with the definitions. Additionally many areas are still actively
researched so flexibility to store any data and meta data in whatever grouping
must be retained. The minimum nesting is 1 layer, e.g. one cannot directly
attach data to the ``/AuxiliaryData`` group.

Each path segment is just an HDF5 group whose name has to match a certain
pattern. Keep in mind that you can nest any number of these.

+----------------+-------------------------------------------------------------+
| ``/AuxiliaryData/{...}/{...}`` Group                                         |
+================+=============================================================+
| **Type**       | Group                                                       |
+----------------+-------------------------------------------------------------+
| **Full Path**  | ``/AuxiliaryData/{...}/{...}``                              |
+----------------+-------------------------------------------------------------+
| **RegEx**      | ``^[A-Z][A-Za-z0-9_]*[a-zA-Z0-9]$``                         |
+----------------+-------------------------------------------------------------+
| **Required**   | False                                                       |
+----------------+-------------------------------------------------------------+
| **Description**| A group storing further auxiliary data groups and/or actual |
|                | auxiliary data.                                             |
+----------------+-------------------------------------------------------------+

Data itsself is stored in a data set within one of these groups. The name of
data set can be freely chosen but has to match the regular expression in the
following table.

+----------------+-----------------------------------------------------------------------+
| ``/AuxiliaryData/{...}/{...}/{TAG}`` Data Set                                          |
+================+=======================================================================+
| **Type**       | Data Set                                                              |
+----------------+-----------------------------------------------------------------------+
| **Full Path**  | ``AuxiliaryData/{...}/{...}/{TAG}``                                   |
+----------------+-----------------------------------------------------------------------+
| **RegEx**      | ``^[a-zA-Z0-9][a-zA-Z0-9_]*[a-zA-Z0-9]$``                             |
+----------------+-----------------------------------------------------------------------+
| **Description**| Auxiliary Data.                                                       |
+----------------+-----------------------------------------------------------------------+
| **Data Type**  | Any data type and dimension. For interoperability best keep to data   |
|                | types supported by HDF5.                                              |
+----------------+-----------------------------------------------------------------------+
| **Required**   | False                                                                 |
+----------------+-----------------------------------------------------------------------+

Meta information is stored as attributes on the data sets and they are once
again completely free form and highly dependent on the application. The only
reserved attribute is the ``provenance_id`` attribute which works exactly as in
the waveform traces.

Provenance for a particular piece of auxiliary data can be stored as an
identifier to a certain provenance record which represents that piece of data.
It is possible (and recommended) but not necessary that a provenance document
in the :doc:`provenance` contains a record with that id.


+----------------+-------------------------------------------------------------+
| ``provenance_id`` Attribute                                                  |
+================+=============================================================+
| **Type**       | Attribute                                                   |
+----------------+-------------------------------------------------------------+
| **Name**       | ``provenance_id``                                           |
+----------------+-------------------------------------------------------------+
| **Description**| The id of a provenance record representing the current      |
|                | state of the auxiliary data piece.                          |
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
