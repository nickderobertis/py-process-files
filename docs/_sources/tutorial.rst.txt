Getting started with processfiles
**********************************

Install
=======

Install via::

    pip install processfiles

Usage
=========

This is a simple example::

    from processfiles import FileProcessTracker

    file_tracker = FileProcessTracker(
        folder='myfolder',
        restart=False,
        file_types=('csv',)
    )

    for file in file_tracker.file_generator():
        # Do stuff on each file here

Then say an error occurs while processing a file. The same exact script can be
run again, and it will resume with the last file, rather than processing all
files again.