Introduction
============

The upcoming paper contains a large section about the motivation for this new
format and why we think we really need this.

Why introduce a new seismic data format?
----------------------------------------

1. The amount of seismic data available for analysis worldwide is rapidly growing. Seismic arrays, such as USArray and ChinaArray, give access to datasets on the terabyte scale that need a high-performance data format for processing an visualization.

2. Disk space is rapidly growing and data organization can improve such that the different types of seismic data (waveforms, receivers, earthquakes, adjoint sources, cross correlations, etc.) can be easily exchanged among the community under one container.

3. Modern workflows in seismology use supercomputers and the number of files is an I/O bottleneck. The performance of these workflows would be increased if the data was stored by combining all time series into one file and taking advantage of parallel processing capabilities.

4. Modern seismology often requires exchanging complex data sets using an open, well-defined, and well-documented format with proven implementations.

5. New methods, such as ambient-noise seismology, are limited by the fixed structure of older data formats that were developed for other methods in seismology. In addition, seismologists often ignore standards because adherence increases development time. An adaptable seismic data format with an open, modular design will be able to evolve and handle future advances in seismology.

6. Reproducibility is always a goal in science and seismology has yet to develop a standardized way of storing provenance in any of the current seismic data formats. Instead of limiting data exchange by using in-house formats, we introduce an open-format that contains flexible provenance that lets the user know where the data comes from and what has been done to it.
