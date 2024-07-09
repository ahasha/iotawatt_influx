.. highlight:: shell

============
Installation
============

From sources
------------

The sources for Iotawatt InfluxDB can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/ahasha/iotawatt_influx

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL https://github.com/ahasha/iotawatt_influx/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/ahasha/iotawatt_influx
.. _tarball: https://github.com/ahasha/iotawatt_influx/tarball/master

Run InfluxDB using Docker
-------------------------

First, install Docker as directed on the `Docker website`_.

Then, pull verison 1.8.3 of the influxdb docker container.  At the time this was written,
the latest stable release was 1.8.3, and iotawatt was not yet compatible with version 2+.

.. code-block:: console

    $ docker pull influxdb:1.8.3

Detailed instructions for running and configuring the influxdb database in the
container are given on `this link`_.


.. _Docker website: https://docs.docker.com/get-docker/
.. _this link: https://hub.docker.com/_/influxdb?tab=description&page=1&ordering=last_updated

Stable release (not yet available)
----------------------------------

In the future, stable releases of this package may be uploaded to pypi.  For now,
please disregard this section.

To install Iotawatt InfluxDB, run this command in your terminal:

.. code-block:: console

    $ pip install iotawatt_influx

This is the preferred method to install Iotawatt InfluxDB, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/
