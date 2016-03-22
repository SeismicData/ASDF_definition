Introduction
============

We submitted a paper containing a large section about the motivation for this
new format and why we think we really need this. Once published we will put a
link to it here.

Why introduce a new seismic data format?
----------------------------------------

1. The amount of seismic data available for analysis worldwide is rapidly
   growing. Seismic arrays, such as USArray and ChinaArray, give access to
   datasets on the terabyte scale that are not suited for existing seismic data
   formats.

2. Disk space is rapidly growing and data organization should improve such that
   the different types of seismic data (waveforms, receivers, earthquakes,
   adjoint sources, cross correlations, etc.) can be easily exchanged among the
   community under one container.

3. Modern workflows in seismology use supercomputers and the number of files is
   an I/O bottleneck. The performance of these workflows would be increased if
   the data was stored by combining all time series into one file and taking
   advantage of parallel processing capabilities.

4. New methods, such as ambient-noise seismology, should not be limited by data
   formats that were developed for other applications in seismology. In
   addition, seismologists often ignore standards because adherence increases
   development time. An adaptable seismic data format with an open, modular
   design will be able to evolve and handle future advances in seismology.

5. Reproducibility is a goal in science and seismology has yet to develop a
   standardized way of storing provenance in the current seismic data formats.
   We introduce a format that contains flexible provenance that lets the user
   know where the data comes from and what has been done to it.
