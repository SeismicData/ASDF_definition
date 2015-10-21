Header
======

This section defines all elements that the root group (``/``) of a proper ASDF
file should contain.

Attributes
----------

The root group contains two attributes that serve to mark the format and the
version of the format for a particular file.

+----------------+-------------------------------------------------------------+
| ``file_format`` Attribute                                                    |
+================+=============================================================+
| **Type**       | Attribute                                                   |
+----------------+-------------------------------------------------------------+
| **Name**       | ``file_format``                                             |
+----------------+-------------------------------------------------------------+
| **Description**| The file format name                                        |
+----------------+-------------------------------------------------------------+
| **Required**   | True                                                        |
+----------------+-------------------------------------------------------------+
| **Value**      | ``"ASDF"``                                                  |
+----------------+-------------------------------------------------------------+
| **Details**    |  .. code::                                                  |
|                |                                                             |
|                |      ATTRIBUTE "file_format" {                              |
|                |          DATATYPE  H5T_STRING {                             |
|                |              STRPAD H5T_STR_NULLPAD;                        |
|                |              CSET H5T_CSET_ASCII;                           |
|                |              CTYPE H5T_C_S1;                                |
|                |          }                                                  |
|                |          DATASPACE  SCALAR;                                 |
|                |      }                                                      |
+----------------+-------------------------------------------------------------+


+----------------+-------------------------------------------------------------+
| ``file_format_version`` Attribute                                            |
+================+=============================================================+
| **Type**       | Attribute                                                   |
+----------------+-------------------------------------------------------------+
| **Name**       | ``file_format_version``                                     |
+----------------+-------------------------------------------------------------+
| **Description**| The file format version.                                    |
+----------------+-------------------------------------------------------------+
| **Required**   | True                                                        |
+----------------+-------------------------------------------------------------+
| **Value**      | |CODEVERSION|                                               |
+----------------+-------------------------------------------------------------+
| **Details**    |  .. code::                                                  |
|                |                                                             |
|                |      ATTRIBUTE "file_format_version" {                      |
|                |          DATATYPE  H5T_STRING {                             |
|                |              STRPAD H5T_STR_NULLPAD;                        |
|                |              CSET H5T_CSET_ASCII;                           |
|                |              CTYPE H5T_C_S1;                                |
|                |          }                                                  |
|                |          DATASPACE  SCALAR;                                 |
|                |      }                                                      |
+----------------+-------------------------------------------------------------+



Data Sets
---------

It can optionally contain a data set representing a QuakeML file.

Data Set - ``/QuakeML``
^^^^^^^^^^^^^^^^^^^^^^^

See :doc:`events` for further information


Groups
------


Waveform, auxiliary, and provenance data is stored into three sub groups.


Group - ``/Waveforms``
^^^^^^^^^^^^^^^^^^^^^^

See :doc:`waveforms` for further information.


Group - ``/AuxiliaryData``
^^^^^^^^^^^^^^^^^^^^^^^^^^

See :doc:`auxiliary_data` for further information.


Group - ``/Provenance``
^^^^^^^^^^^^^^^^^^^^^^^

See :doc:`provenance` for further information.
