An Adaptable and Modern Seismic Data Format
===========================================

This document presents the current status of an attempt to develop and define a
new data format for modern seismology dubbed **ASDF** (**A**\ daptable **S**\
eismic **D**\ ata **F**\ ormat). It is divided into five parts:


1. The introduction demonstrates the necessity of a new format and gives a
   high-level overview of the format and the ideas behind it.

2. The next section deals with the technical details and is still very much
   subject to even fundamental changes.

3. The third part present two implementations of the format. One based on ADIOS
   and Fortran and the other implemented in Python with the help of the ObsPy
   framework and the HDF5 container format.

4. This section displays some use cases to demonstrate the wide range of
   possible uses.

5. The last part tries to define a new XML format for seismological provenance
   information dubbed *SEIS PROV*.

.. toctree::
   :maxdepth: 2

   introduction
   technical_details
   implementations
   use_cases
   provenance
