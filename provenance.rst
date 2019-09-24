Provenance
==========

The ``/Provenance`` group contains any number of data sets, each containing a
`SEIS-PROV <http://seismicdata.github.io/SEIS-PROV/>`_ document.

+----------------+-------------------------------------------------------------+
| ``/Provenance`` Group                                                        |
+================+=============================================================+
| **Type**       | Group                                                       |
+----------------+-------------------------------------------------------------+
| **Full Path**  | ``/Provenance``                                             |
+----------------+-------------------------------------------------------------+
| **Required**   | False                                                       |
+----------------+-------------------------------------------------------------+
| **Description**| Contains a number of ``SEIS-PROV`` documents.               |
+----------------+-------------------------------------------------------------+


Each ``SEIS-PROV`` document is serialized with PROV-XML and stored as a binary
dump to a data set. Thus dealing with the encoding is once again delegated to
the XML libraries. The name of the data set is arbitrary but has to match the
pattern in the following table.

+----------------+-------------------------------------------------------------+
| ``/Provenance/{NAME}`` Data Set                                              |
+================+=============================================================+
| **Type**       | Data Set                                                    |
+----------------+-------------------------------------------------------------+
| **Full Path**  | ``/Provenance/{NAME}``                                      |
+----------------+-------------------------------------------------------------+
| **RegEx**      | ``^[ -~]+$``                                                |
+----------------+-------------------------------------------------------------+
| **Description**| A SEIS-PROV document with any number of records.            |
+----------------+-------------------------------------------------------------+
| **Data Type**  | ``H5T_STD_I8LE``                                            |
+----------------+-------------------------------------------------------------+
| **Required**   | False                                                       |
+----------------+-------------------------------------------------------------+
| **Details**    |  .. code::                                                  |
|                |                                                             |
|                |      DATASET "373fe_9bca_43ed10b" {                         |
|                |          DATATYPE  H5T_STD_I8LE                             |
|                |          DATASPACE  SIMPLE {                                |
|                |              ( * ) / ( H5S_UNLIMITED )                      |
|                |          }                                                  |
|                |      }                                                      |
+----------------+-------------------------------------------------------------+
