Header
======

This is the root element (``/``) of an HDF5 file satisfying the ASDF
definition.

Attributes
----------

``file_format``
^^^^^^^^^^^^^^^

**Description:** The file format version.

**Value:** |CODEVERSION|

**Details:**

.. code::

    ATTRIBUTE "file_format" {
        DATATYPE  H5T_STRING {
            STRPAD H5T_STR_NULLPAD;
            CSET H5T_CSET_ASCII;
            CTYPE H5T_C_S1;
        }
        DATASPACE  SCALAR;
    }

``file_format_version``
^^^^^^^^^^^^^^^^^^^^^^^

**Description:** The file format name.

**Value:** ``"ASDF"``

**Details:**

.. code::

    ATTRIBUTE "file_format_version" {
        DATATYPE  H5T_STRING {
            STRPAD H5T_STR_NULLPAD;
            CSET H5T_CSET_ASCII;
            CTYPE H5T_C_S1;
        }
        DATASPACE  SCALAR;
    }


Data Sets
---------

It potentially contains a single data set.

``QuakeML``
^^^^^^^^^^^

See :doc:`events` for further information


Groups
------

Additionally it can contain the following groups. ASDF files do not need to
contain all three.


``Waveforms``
^^^^^^^^^^^^^^

See :doc:`waveforms` for further information.


``AuxiliaryData``
^^^^^^^^^^^^^^^^^

See :doc:`auxiliary_data` for further information.


``Provenance``
^^^^^^^^^^^^^^

See :doc:`provenance` for further information.
