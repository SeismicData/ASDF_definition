Of Tags and Labels
==================

The ``ASDF`` data format has tags and labels which, while similar to a certain
extent, serve a different purpose. This is sometimes a bit confusing to
people new to the format - this page explains and clarifies everything.


Tags
----

**Tags are used as an additional hierarchical layer.** They are for example
used to distinguish observed and synthetic data or two synthetic waveforms
calculated with slightly different earth models. Each waveform trace must
have a tag - it is used as part of the arrays' names in the HDF5 file.
There are little rules to them but they should be pretty short.

**The** ``raw_recording`` **tag is by convention reserved for raw data counts
straight from a digitizer**.

Other names depend on the use case - common choices are ``synthetic_prem`` or
``processed_1_10_s``.


Labels
------

Labels on the other hand are an optional list of words potentially assigned to
a waveform. They can be used to describe and label similar
waveforms without influencing how they are stored on disc. **They are a
piece of meta information** useful to organize the data a bit better. Its
always a list of simple UTF-8 encoded words.

