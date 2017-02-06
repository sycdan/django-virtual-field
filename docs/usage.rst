=====
Usage
=====

To use Django Virtual Field in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'virtual_field.apps.VirtualFieldConfig',
        ...
    )

Add Django Virtual Field's URL patterns:

.. code-block:: python

    from virtual_field import urls as virtual_field_urls


    urlpatterns = [
        ...
        url(r'^', include(virtual_field_urls)),
        ...
    ]
