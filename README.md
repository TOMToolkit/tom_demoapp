 
tom-demoapp
===========

tom-demoapp is a Django app that serves as a demonstration and code example for a tomtoolkit app.
This app contains all of the integration points and features that a TOM developer can use in their custom
TOM project.

Detailed documentation can be found in the tomtoolkit docs.

Quick start
-----------

1. Add "tom_demoapp" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "tom_demoapp",
    ]

2. Paths should be automatically included via tom_common.

3. Run ``python manage.py migrate`` to create the models.

4. Start the development server and visit your tom to see any changes.