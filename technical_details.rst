Technical Details
=================

Internal Data Layout
--------------------

SDF supports two fundamentally different layouts: one for data in the classical
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
also be suitable for SDF).

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
endtime. SDF defines a continuous trace as a single chunk of data without any
gaps or overlaps. This implies that the time of the first sample and the sample
spacing are enough to uniquely determine the time of every sample.


Diagram
-------

This simple diagrams aims to illustrate the main structure. Arrows denote links
either via ids or "symlinks". The diagram denotes the contents of the
container.

.. image:: https://raw.github.com/wiki/krischer/sdf/images/sdf.png
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

The only slightly more complex data type in SDF is the time data type.
Experience has shown that the available time resolution in preexisting data
formats is not fine enough for some applications like megahertz vibration
experiments. Although the aim of the SDF format is to be as simplistic as
possible this slight complication is justified in the authors eyes making the
file format suitable for a whole new range of applications.

One possibility for this goal would be to specify times as follows, essentially
giving a timing accuracy of 10^(-19) seconds.

.. code-block:: xml

    - Time
        - UNIX timestamp (signed 64bit integer)
        - Decimals of the seconds (unsigned 64bit integer)

Provenance
^^^^^^^^^^

They form a processing chain than can optionally be defined for each trace,
containing processing elements. The goal for the core format specification is
to include a set of generally accepted processing elements that the community
can agree on. The need for describing and keeping track of custom processing
not captured by the core processing elements set is acknowledged with the
ability to create new processing elements. Furthermore a free-form processing
element will be supplied able to contain arbitrary information.

Software reading these custom elements will at least be able to qualitatively
describe what happened to the data.

Processing Chain
^^^^^^^^^^^^^^^^

The applied processing is described in a so-called processing chain consisting
of an arbitrary number of ordered processing elements. The order in which the
processing elements appear inside the processing chain corresponds to the order
in which the processing has been applied to the data. This corresponds to the
way seismic data is usually processed: as a linear workflow one operation
acting after another.

The following section will detail the single processing elements. Each
processing element will contain a link to a potential next processing element.\

XML Format
^^^^^^^^^^

We propose a new XML structure to store the provenance information. In the
future we will provide a proper XSD file and introduce XML namespaces. The
format describes a linear chain of applied processing operators. One always has
to strictly follow the next. Each element of chain inherits from a base
structure that defines some common traits.

The following is an example of an XML file describing a synthetic waveform that
has been filtered after the generation.

.. code-block:: xml

    <processing_description id="asdf-344-s34f-dsfg">

       <processing_element stage="0" id="fdue-adn34-sdfj4-34id">
          <software_description>
              <name>SPECFEM3D_Cartesian</name>
              <version>2.0.2</version>
              <uri>http://www.geodynamics.org/cig/software/specfem3d</uri>
              <command>main</command>
          </software_description>
          <comment>Each stage can have</comment>
          <comment>multiple comments</comment>
          <element_description type="SyntheticOrigin">
              <date>2013-1-1</date>
              <solver_input_files>
                  <file name="Parfile">...</file>
                  <file name="CMTSOLUTION">...</file>
                  <file name="STATIONS">...</file>
              </solver_input_files>
          </element_description>
          <model>Earth</model>
       </processing_element>

       <processing_element stage="1" id="435h-fh5-sdfj4-34id">
          <software_description>
              <name>ObsPy</name>
              <version>0.8.4</version>
              <uri>http://obspy.org</uri>
              <command>stream.filter("lowpass", freq=0.1, zerophase=True, corners=2)</command>
          </software_description>
          <element_description type="LowpassFilter">
              <type>Lowpass Filter</type>
              <corner_frequency>0.1</corner_frequency>
              <number_of_corners>2</number_of_corners>
              <zerophase>True</zerophase>
          </element_description>
       </processing_element>

    </processing_description>

Description of Processing Elements
----------------------------------

Software Description.
^^^^^^^^^^^^^^^^^^^^^

Each element will be able to specify the software that has been used to apply
it.  The specification is uniform across processing elements.

.. code-block:: xml

    - SoftwareDescription
        |- Name
        |- Version
        |- URI (optional)
        |- Command (optional)

SyntheticOriginPE
^^^^^^^^^^^^^^^^^

The SyntheticOriginPE should be used as the first element in a processing chain
if the waveform in question is the output of a numeric simulation as opposed to
a waveform recorded with an instrument. It provides a basic set of information
about the solver, model and settings used to generate the waveform.

.. code-block:: xml

    - SyntheticOriginPE/
        |- DateGeneratedAt
        |- SoftwareDescription
        |- SolverInputFiles/ (optional)
        |    |- input_file_2 (optional)
        |    |- input_file_2 (optional)
        |    |- ...
        |- Model
        |- ModelURI (optional)
        |- ModelDescription (optional)
        |- Comments (optional)
        |- Statistics/ (optional)
        |    |- RunTime (optional)
        |    |- Cost (optional)
        |    |- MaxMemory (optional)
        |- NextPE

DetrendPE
^^^^^^^^^

The DetrendPE describes different methods to remove trends from data.

.. code-block:: xml

    - DetrendPE/
        |- Type (Enum of FirstLast, Linear, Demean)
        |- SoftwareDescription
        |- NextPE

* **FirstLast**: substract a linear function defined by the first and last sample
* **Linear**: Remove a linear least squares lines
* **Demean**: Remove the mean of the data


LowpassFilterPE
^^^^^^^^^^^^^^^

The LowpassFilterPE describes a lowpass filter.

.. code-block:: xml

    - LowpassFilterPE/
        |- Type (Enum of Butterworth, Bessel, ChebyshevTypeI, ChebyshevTypeII)
        |- CornerFrequency
        |- NumberOfCorners
        |- Zerophase (Boolean)
        |- Chebyshev transition band width (if applicable)
        |- Chebyshev transition attenuation factor (if applicable)
        |- SoftwareDescription
        |- NextPE


HighpassFilterPE
^^^^^^^^^^^^^^^^

The HighpassFilterPE describes a highpass filter.

.. code-block:: xml

    - HighpassFilterPE/
        |- Type (Enum of Butterworth, Bessel, ChebyshevTypeI, ChebyshevTypeII)
        |- CornerFrequency
        |- NumberOfCorners
        |- Zerophase (Boolean)
        |- Chebyshev transition band width (if applicable)
        |- Chebyshev transition attenuation factor (if applicable)
        |- SoftwareDescription
        |- NextPE


BandpassFilterPE
^^^^^^^^^^^^^^^^

The BandpassFilterPE describes a bandpass filter.

.. code-block:: xml

    - BandpassFilterPE/
        |- Type (Enum of Butterworth, Bessel, ChebyshevTypeI, ChebyshevTypeII)
        |- LowerCornerFrequency
        |- UpperCornerFrequency
        |- NumberOfCorners
        |- Zerophase (Boolean)
        |- Chebyshev transition band width (if applicable)
        |- Chebyshev transition attenuation factor (if applicable)
        |- SoftwareDescription
        |- NextPE


BandstopFilterPE
^^^^^^^^^^^^^^^^

The BandstopFilterPE describes a bandstop filter.


.. code-block:: xml

    - BandstopFilterPE/
        |- Type (Enum of Butterworth, Bessel, ChebyshevTypeI, ChebyshevTypeII)
        |- LowerCornerFrequency
        |- UpperCornerFrequency
        |- NumberOfCorners
        |- Zerophase (Boolean)
        |- Chebyshev transition band width (if applicable)
        |- Chebyshev transition attenuation factor (if applicable)
        |- SoftwareDescription
        |- NextPE


IntegerDecimationPE
^^^^^^^^^^^^^^^^^^^

The IntegerDecimationPE describes a integer decimation. Any prior lowpass
filter has to be described with the corresponding

.. code-block:: xml

    - IntegerDecimationPE/
        |- InitialSampleRate
        |- FinalSampleRate
        |- DecimationFactor
        |- SoftwareDescription
        |- NextPE

**Note:** The initial and final sampling rate are redundant information but
ease the interpretation of the processing element. Should they be there?

ResamplingPE
^^^^^^^^^^^^

The ResamplingPE describes a frequency domain resampling.

.. code-block:: xml

    - ResamplingPE/
        |- InitialSampleRate
        |- FinalSampleRate
        |- SoftwareDescription
        |- NextPE

TaperPE
^^^^^^^

The TaperPE describes the application of a taper.

.. code-block:: xml

    - TaperPE/
        |- Type (Enum of one of the options listed below)
        |- Additonal Parameters dependent on the type of taper
        |- SoftwareDescription
        |- NextPE

Defined taper types:

* **cosine**: Cosine taper
* **bartlett**: Bartlett window taper.
* **blackman**: Blackman window taper.
* **gaussian**: Gaussian taper. Additional parameter: *StandardDeviation*.
* **hamming**: Hamming window taper.
* **hann**: Hann window taper.
* **kaiser**: Bessel function taper. Additional parameter: *Beta* (shape parameter)
* **slepian**: Slepian or DPSS (Discrete prolate spheroidal sequence). Additional parameter: *Bandwidth*


TrimPE
^^^^^^

The TrimPE describes a processing element that cuts a data at the beginning and
the end.

.. code-block:: xml

    - TrimPE/
        |- InitialStarttime
        |- InitialEndtime
        |- FinalStarttime
        |- FinalEndtime
        |- SoftwareDescription
        |- NextPE


PaddingPE
^^^^^^^^^

The PaddingPE describes a processing element that adds additional data in form
of a constant pad value.

.. code-block:: xml

    - PaddingPE/
        |- InitialStarttime
        |- InitialEndtime
        |- FinalStarttime
        |- FinalEndtime
        |- PadValue
        |- SoftwareDescription
        |- NextPE

InstrumentCorrectionPE
^^^^^^^^^^^^^^^^^^^^^^

The InstrumentCorrectionPE describes a processing element removing the response
of seismic instrument.

.. code-block:: xml

    - InstrumentCorrectionPE/
        |- InitialUnits
        |- FinalUnits
        |- Poles (optional)
        |- Zeros (optional)
        |- FIRcoefficients (optional)
        |- NormalizationFactor (optional)
        |- OverallSensitivity (optional)
        |- SoftwareDescription
        |- NextPE

This is not really complete. We should also think about multi-stage corrections
and potentially polynomial instrument responses. Potentially we could also just
refer to the corresponding StationXML file and be done with it. It also needs a
sister PE, an InstrumentSimulationPE.

Data Streaming
^^^^^^^^^^^^^^

SDF is well suited for the distribution and exchange of very large waveform
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

The SDF format in the initial definition can not deal with this and neither can
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
