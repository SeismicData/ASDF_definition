Implementations
===============

ADIOS and Fortran
-----------------


Reading file content
^^^^^^^^^^^^^^^^^^^^

The reader is designed to be flexible so that only content the user is
interested can be read into memory. Here are examples of how to read event.asdf

* Example 1: Read entire file into memory ```read_asdf event.asdf``` You can
  also do this in parallel. ```parallel_read_asdf event.asdf```

* Example 2: Read all waveforms associated with a specific station
  ```read_waveforms 'Station' event.asdf```

* Example 3: Read provenance associated with a specific waveforms
  ```read_provenance NET.STA.LOC.CHAN_STARTTIME_ENDTIME[_TAG] event.asdf```


Writing file content
^^^^^^^^^^^^^^^^^^^^

* Example 1: Writing all data to event.asdf ```write_asdf event.asdf```

* In parallel...```parallel_write_asdf event.asdf```


Converting other seismic data formats to ASDF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The format is designed to be exchangeable and in order to facilitate adoption
converters that take existing seismic data formats can go back and forth
between them.

How to convert SAC to ASDF


HDF5 and Python
---------------

This implementation is currently a rough protoytype realized using `ObsPy
<http://obspy.org>`_ and `h5py <http://www.h5py.org>`_. Usability while
retaining acceptable performance is the key design goal for this
implementation.

It is based around a data set class that has a nice interface to manipulate
data. All operations are transparently mapped to an HDF5 file on disc.

Creation of a new file
^^^^^^^^^^^^^^^^^^^^^^

This section quickly introduces the creation of a new SDF file.

.. code-block:: python

    from write_sdf import SDFDataSet

    # If the file does not exist, it will be created,
    # otherwise the old one will used.
    data_set = SDFDataSet("test_file.h5")

One can add waveform and station data in any order. The class will take care that everything is
mapped to the correct section in the HDF5 file. The use of ObsPy means that we get a converter
for effectively all seismic waveform formats in use to the new format for free.

.. code-block:: python

    import glob

    for filename in glob.glob("*.mseed"):
        data_set.add_waveform_file(filename, tag="raw_recording")

    for filename in glob.glob("*.xml"):
        data_set.add_stationxml(filename)

It is also possible to do this with an already existing file. HDF5 is flexible enough.


Accessing data
^^^^^^^^^^^^^^

This interactive session demonstrates how to use the class to access the data.

.. code-block:: python

    data_set = SDFDataSet("test_file.h5")

One can print some information.

.. code-block:: python

    >>> print data_set
    SDF file: 'test_file.h5' (2.7 GB)
        Contains data from 1392 stations.

And one can access waveforms and station. Tab completion works just fine. What
comes back are ObsPy objects which should enable a convenient way of working
with the data and outputting it to any other format.

The waveforms can be accessed via the tags. The return type is an ObsPy Stream
object which will be created on the fly when accessing it. This is essence
enables one to work with huge datasets on a laptop as only the part of the data
required at the moment is in memory.

.. code-block:: python

    >>> st = data_set.waveforms.AE_113A.raw_recording
    >>> print st
    AE.113A..BHE | 2013-05-24T05:40:00.000000Z - 2013-05-24T06:50:00.000000Z | 40.0 Hz, 168001 samples
    AE.113A..BHN | 2013-05-24T05:40:00.000000Z - 2013-05-24T06:50:00.000000Z | 40.0 Hz, 168001 samples
    AE.113A..BHZ | 2013-05-24T05:40:00.000000Z - 2013-05-24T06:50:00.000000Z | 40.0 Hz, 168001 samples
    >>> st.plot()

The same is true with the station information which return an ObsPy inventory
object.

.. code-block:: python

    >>> inv = data_set.waveforms.AE_113A.StationXML
    >>> print inv
    Inventory created at 2014-02-08T22:06:43.000000Z
            Created by: IRIS WEB SERVICE: fdsnws-station | version: 1.0.10
                        http://service.iris.edu/fdsnws/station/1/query?channel=BH%2A&statio...
            Sending institution: IRIS-DMC (IRIS-DMC)
            Contains:
                    Networks (1):
                            AE
                    Stations (1):
                            AE.113A (Mohawk Valley, Roll, AZ, USA)
                    Channels (3):
                            AE.113A..BHE, AE.113A..BHN, AE.113A..BHZ

So now one has all the information needed to process the data. The following
snippet will convert all data for the given station and tag to meters per
second.

.. code-block:: python

    >>> st.attach_response(inv)
    >>> st.remove_response(units="VEL")


Large Scale Processing
^^^^^^^^^^^^^^^^^^^^^^

This is not yet fully implemented but will be done soon. So the idea is to
define a function per station and tag. This function will then be applied to
all data and the result will be stored in a new file. If an MPI environment is
detected it will be distributed across all nodes and otherwise `os.fork` will
be used for shared memory multiprocessing. This should all happen behind the
scenes and the user does not have to bother with it.

.. code-block:: python

    def process(stream, station):
        stream.attach_resonse(station)
        stream.remove_response(units="VEL")

    data_set(process, output_filename="new.h5")
