=============================
Django Virtual Field
=============================

.. image:: https://badge.fury.io/py/django-virtual-field.svg
    :target: https://badge.fury.io/py/django-virtual-field

.. image:: https://travis-ci.org/sycdan/django-virtual-field.svg?branch=master
    :target: https://travis-ci.org/sycdan/django-virtual-field

.. image:: https://codecov.io/gh/sycdan/django-virtual-field/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/sycdan/django-virtual-field

Define annotations directly on your models.

Documentation
-------------

The full documentation is at https://django-virtual-field.readthedocs.io.

Quickstart
----------

Install Django Virtual Field::

    pip install django-virtual-field

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'virtual_field.apps.VirtualFieldConfig',
        ...
    )

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
