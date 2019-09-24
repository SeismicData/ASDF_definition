ASDF
====

.. |br| raw:: html

    <br />

.. image:: images/asdf_logo.*
    :width: 80%
    :align: center


This is the formal definition of the *Adaptable Seismic Data Format*
(**ASDF**).



.. note:: **For more details please see our paper:**

    *Lion Krischer, James Smith, Wenjie Lei, Matthieu Lefebvre, Youyi Ruan, Elliott Sales de Andrade, Norbert Podhorszki, Ebru Bozdağ and Jeroen Tromp* (2016), |br|
    **An Adaptable Seismic Data Format**, |br|
    Geophysical Journal International, 207(2). |br|
    `http://dx.doi.org/10.1093/gji/ggw319 <http://dx.doi.org/10.1093/gji/ggw319>`_


.. note::

    This document is for version |BOLDVERSION| of the format.

    This is the **A**\ daptable **S**\ eismic **D**\ ata **F**\ ormat - if you
    are looking for the **A**\ dvanced **S**\ cientific **D**\ ata **F**\
    ormat, go here: https://asdf.readthedocs.io/en/latest/


For further information and contact information please see these two web sites:

* Landing page of the ASDF data format: http://seismic-data.org
* Github repository of this document http://www.github.com/SeismicData/ASDF_definition


Additionally these pages and software projects are of further interest:

* C/Fortran implementation intended to be integrated into numerical solvers: https://github.com/SeismicData/asdf-library
* Python implementation: http://seismicdata.github.io/pyasdf/
* ASDF validation tool: https://github.com/SeismicData/asdf_validate
* Graphical user interface for ASDF: https://github.com/SeismicData/asdf_sextant
* SEIS-PROV: http://seismicdata.github.io/SEIS-PROV/


ASDF Format Changelog
---------------------

.. topic:: Version 1.0.3 (September 24th, 2019)

    * Allow all ASCII chars in the names of provenance data sets.
    * Allow the following extra characters in the names of auxiliary data sets
      and their path names: ``_\.!#$%&*+,:;<=>\?@\^~``

.. topic:: Version 1.0.2 (March 1st, 2018)

    * Allow adding very short waveforms that might start and end within the same second.

.. topic:: Version 1.0.1 (Oktober 19th, 2017)

    * Allow little and big endian 16 bit integer waveform data.

.. topic:: Version 1.0.0 (March 22nd, 2016)

    * Initial ASDF version.


.. toctree::
   :hidden:
   :maxdepth: 2


   introduction
   big_picture
   container
   header
   events
   waveforms
   auxiliary_data
   provenance
   potential_shortcomings
   of_tags_and_labels
