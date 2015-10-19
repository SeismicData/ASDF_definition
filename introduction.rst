Introduction
============

The upcoming paper contains a large section about the motivation for this new
format and why we think we really need this.

Why introduce a new seismic data format?
----------------------------------------

1. The amount of seismic data available for analysis worldwide is rapidly
   growing. Seismic arrays, such as USArray and ChinaArray, give access to huge
   datasets that are not suited for older data formats. This creates datasets
   on the terabyte scale and processing this data is often limited by archaic
   file structures. It is time to introduce a new seismic data format that is
   capable of handling these larger datasets.

2. Disc space is rapidly growing and data organization needs to be able to keep
   up with it.

3. Modern workflows in seismology take advantage of supercomputing resources
   and the number of files is an I/O bottleneck. The performance of these
   workflows on supercomputers would be increased if the data was stored by
   combining all time series into one file and taking advantage of parallel
   processing capabilities.

4. Data exchange and collaboration is necessary for many modern problems. Well
   documented format with proven implementations.

5. New methods, such as ambient-noise seismology, are limited by the fixed
   structure of older data formats that were meant for specific applications
   and for much more limited computing power. In addition, seismologists often
   ignore standards because adherence increases development time. An adaptable
   seismic data format with an open, modular design will be able to evolve and
   handle future advances in seismology.

6. Reproducibility is always a goal in science and seismology has yet to
   develop a standardized way of storing provenance in any of the current
   seismic data formats. Instead of limiting data exchange by using in-house
   formats it is time for an open-format that contains flexible provenance that
   lets the user know where the data comes from and what has been done to it.

7. By taking advantage of open-source software and the internet, the
   development of a modern seismic data format can be done in a cooperative
   manner with input from seismologists across different research areas. This
   will also allow a modular data format to evolve and adapt to problems in the
   future. An open wiki for development that allows for contributions from the
   community will help grow seismology as a science.
