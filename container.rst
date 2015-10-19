The Container
=============

The chosen container format for ASDF is `HDF5 <http://www.hdfgroup.org/>`_.
The Hierarchical Data Format version 5 is a quasi standard format for binary
data with a large amount of tools and support available. This format has also
shown promise for dealing with large datasets in other applications.


ASDF delegates the allowed compression, chunking, checksumming, etc. settings
to the HDF5 definition. Best to not use use custom filters that are not
shipping with the HDF5 library as it will severely hurt exchangeability and
possibly future safety. The HDF5 group put a lot of emphasis on backwards
compatibility.
