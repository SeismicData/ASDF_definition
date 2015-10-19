Provenance
==========


* **Provenance** - This is where information about the history of the data is
  kept. All data processing operations included in the SAC library are
  included. Furthermore all possible operations available in the ObsPy program
  are included. The inclusion of these two sets enables the description of most
  common workflows in seismology within the container layout. They form a
  processing chain than can optionally be defined for each trace, containing
  processing elements. The goal for the core format specification is to include
  a set of generally accepted processing elements that the community can agree
  on. The need for describing and keeping track of custom processing not
  captured by the core processing elements set is acknowledged with the ability
  to create new processing elements. Furthermore a free-form processing element
  will be supplied able to contain arbitrary information. See
  `Provenance <https://github.com/krischer/ASDF/wiki/Provenance-Definition>`_
  for more information.

