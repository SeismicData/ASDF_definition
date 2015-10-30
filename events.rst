Events
======

Event information is stored as a `QuakeML <https://quake.ethz.ch/quakeml/>`_
file in the ``/QuakeML`` data set. It contains a binary dump (determining the
encoding is left to the XML header which is quite good at it) of a QuakeML
file.

It is recommended to always use the most wide-spread QuakeML version but ASDF
will work fine as long as the QuakeML version has the concept of resource
identifiers and public IDs.



+----------------+-------------------------------------------------------------+
| ``/QuakeML`` Data Set                                                        |
+================+=============================================================+
| **Type**       | Data Set                                                    |
+----------------+-------------------------------------------------------------+
| **Path**       | ``/QuakeML``                                                |
+----------------+-------------------------------------------------------------+
| **Description**| Event information as a single QuakeML file.                 |
+----------------+-------------------------------------------------------------+
| **Data Type**  | ``H5T_STD_I8LE``                                            |
+----------------+-------------------------------------------------------------+
| **Required**   | False                                                       |
+----------------+-------------------------------------------------------------+
| **Details**    |  .. code::                                                  |
|                |                                                             |
|                |      DATASET "QuakeML" {                                    |
|                |          DATATYPE  H5T_STD_I8LE                             |
|                |          DATASPACE  SIMPLE { ( * ) / ( H5S_UNLIMITED ) }    |
|                |      }                                                      |
+----------------+-------------------------------------------------------------+
