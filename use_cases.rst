Use Cases
=========

To push and facilitate the adoption of the format into different tools, a
descriptive and comprehensive test suite should be made available. The test
suite should contains data descriptions and corresponding files so that any
implementations can be tested against it.

To demonstrate the usability and versatility of the new format it should be
able to deal with these three use cases.

Earthquake data
^^^^^^^^^^^^^^^

The earthquake data use case demonstrates the applicability of the format to
workflows typical for global and continental scale seismic tomography. A
natural way to organize data in these cases is to have one file per event
containing everything necessary. A further requirement is to store generated
synthetics, again one file per event is desirable.

An exemplary data set containing one hour of data for an earthquake recorded at
5000 stations will require around

.. code-block:: xml

    5000 Stations * 3 Components / Stations * 3600 s / component * 100.0 Hz *
    4 bytes / sample = 20.12 GB

Realistic data sets in use today are oftentimes an order of magnitude smaller
because data is rarely available for that many stations and data at 10 Hz is
usually more then sufficient for use in global and continental scale
tomography.

We will demonstrate the file format by implementing two parts of a workflow.
The first part will read a file and apply some time series analysis and save it
to another file. This needs to happen completely in parallel.

The other part means reading two file, one containing data, the other
synthetics, find suitable windows, make misfit measurements and design adjoint
sources.

Adjoint Sources
^^^^^^^^^^^^^^^

...


Ambient Noise Cross Correlations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

...
