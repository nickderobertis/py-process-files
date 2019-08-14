.. pypi-sphinx-quickstart documentation master file, created by
   pypi-sphinx-quickstart.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Python Process Files documentation!
************************************************

Use this tool to select files of given file types in a folder, and track whether these files have been processed,
regardless of whether the script needs to be run multiple times. Stores progress on the files as a text file in the
same folder, so that a long-running operation on many files can be resumed where it left off if it was stopped.
It will also automatically estimate time to completion.

.. toctree::

   tutorial


An overview
===========

.. autosummary::

      processfiles.files.FileProcessTracker
      processfiles.timing.TimeTracker


API Documentation
------------------

A full list of modules

.. toctree:: api/modules
   :maxdepth: 3

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
