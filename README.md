# Asterisk Odoo Project

Don't mind this readme file for the moment. A lot needs to be modified.



Has to be done only once (the first time you spin the compose file)

execute the following command:

.. code:: bash

  docker-compose up

When the container is up and running, open a shell inside the container:

.. code:: bash

  docker-compose exec odoo bash

once inside the container execute the following command to initialise the base:

##TODO: write a script to automate this

.. code:: bash

  odoo -i base -c /etc/odoo/odoo.conf --stop-after-init


Now stop the containers and restart them

.. code:: bash

  docker-compose up

Odoo is running!