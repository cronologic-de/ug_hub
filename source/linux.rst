=============
Linux Support
=============

In order to set up your cronologic device with your Linux machine, you
need to

- install our ``cronologic_linux_kernel``, an open-source
  project availabe on our
  `GitHub <https://github.com/cronologic-de/cronologic_linux_kernel>`_.
- get the necessary libraries for the particular device you bought. They are
  provided with our wrappers, utilities, and examples availabe on GitHub:

    - `xHPTDC8 <https://github.com/cronologic-de/xhptdc8_babel>`_
    - `xTDC4 <https://github.com/cronologic-de/xtdc_babel>`_
    - `TimeTagger4 <https://github.com/cronologic-de/xtdc_babel>`_
    - `Ndigo6G-12 <https://github.com/cronologic-de/ug_ndigo6g>`_
    - `Ndigo5G-10 <https://github.com/cronologic-de/ndigo5g_babel>`_

You can find detailed instructions for the installation on the respective 
GitHub repositories, as well.

Install ``cronologic_linux_kernel``
===================================

The ``cronologic_linux_kernel`` has been tested on the following 64-bit
distributions (see the `GitHub README 
<https://github.com/cronologic-de/cronologic_linux_kernel/tree/main?tab=readme-ov-file#supported-distributions>`_
for details on the particular versions):

- Ubuntu
- CentOS
- Fedora
- Debian
- openSUSE


-----------

Install the prerequisites
-------------------------

Make sure to install the prerequisites before attempting to install
``cronologic_linux_kernel``. ``sudo`` priviliges are necessary for
installation.

We strongly recommend using ``dkms`` to manage the kernel installation.



.. tabs::

    .. tab:: Ubuntu

        Install ``make`` and ``gcc``:

        .. code:: shell

            sudo apt-get install make gcc

        Install ``modules`` and ``headers`` of your current kernel version:

        .. code:: shell

            sudo apt-get install linux-headers-$(uname -r) linux-modules-$(uname -r)

        Install ``dkms``:

        .. code:: shell

            sudo apt-get install dkms



    .. tab:: CentOS

        Install ``make`` and ``gcc``:

        .. code:: shell

            sudo yum install gcc make

        Install kernel development:

        .. code:: shell

            sudo rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
            sudo yum install https://www.elrepo.org/elrepo-release-9.el9.elrepo.noarch.rpm

        If you use a *Long Term Support* version, you need to run:

        .. code:: shell

            sudo dnf --enablerepo=elrepo-kernel install kernel-lt
            sudo dnf --enablerepo=elrepo-kernel install kernel-lt-devel

        If you use a *Long Mainline Stable* version, you need to run:

        .. code:: shell

            sudo dnf --enablerepo=elrepo-kernel install kernel-ml
            sudo dnf --enablerepo=elrepo-kernel install kernel-ml-devel

        Install ``dkms``:

        .. code:: shell

            sudo apt-get install dkms


    .. tab:: Fedora

       Install ``make`` and ``gcc``:

       .. code:: shell

           sudo yum install gcc make

       Install kernel development:

       .. code:: shell

           sudo apt-get install linux-headers-$(uname -r) 

       Install ``dkms``:

       .. code:: shell

           sudo apt-get install dkms
        
    .. tab:: Debian

        Install ``make`` and ``gcc``:

        .. code:: shell

            sudo apt-get install make gcc

        Install ``modules`` and ``headers`` of your current kernel version:

        .. code:: shell

            sudo apt-get install linux-headers-$(uname -r)

        Install ``dkms``:

        .. code:: shell

            sudo apt-get install dkms

    .. tab:: openSUSE

        Install ``make`` and ``gcc``:
       
        .. code:: shell

             sudo zypper install make gcc

        Install ``modules`` and ``headers`` of your current kernel version:

         .. code:: shell

             sudo zypper in kernel-devel kernel-default-devel
             sudo zypper up

        Install ``dkms``:

         .. code:: shell

             sudo apt-get install dkms




Clone the GitHub repository 
---------------------------

.. code:: shell

    git clone https://github.com/cronologic-de/cronologic_linux_kernel.git

Alternatively, download the `latest release
<https://github.com/cronologic-de/cronologic_linux_kernel/releases/latest>`_
and unpack it.

Install the kernel using ``DKMS``
---------------------------------

We strongly recommend using ``DKMS`` to manage your installation. 

In a terminal, navigate to the project folder you just cloned 
(or downloaded and unpacked) and run

.. code:: shell

    sudo dkms install .

If you
are unable to use ``DKMS``, you can find instructions on a manual installation
`here <https://github.com/cronologic-de/cronologic_linux_kernel/tree/main?tab=readme-ov-file#manual-installation>`_.

.. warning::

    If you don't use ``DKMS`` to manage the installation, you have to reinstall
    ``cronologic_linux_kernel`` for every change to your linux kernel.


Compile and run the GitHub example
==================================

Clone or download the ``_babel`` project.
Do things