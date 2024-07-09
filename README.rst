=================
Iotawatt InfluxDB
=================



A functional example of using an `Iotawatt electric consumption monitor`_
 with InfluxDB and Grafana to create useful monitoring dashboards of your
 home electricity use.


* Free software: MIT license

Features
--------

* Automate installation and configuration of influxdb and grafana using
  docker compose. (Done)
  - Configuration scripts to run the docker compose app on rasberry pi. (ToDo)
* Jupyter notebooks for exploring the iotawatt data in influxdb interactively. (ToDo)
* Example dashboards
  - Total electricity consumption per day
  - Total running time per day of high power appliances (e.g. AC or hot water heater)
* Cloud backup of influxdb data. (ToDo)

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Iotawatt electric consumption monitor: https://iotawatt.com/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
