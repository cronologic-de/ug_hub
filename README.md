# ug_hub
This is a [Sphinx](https://www.sphinx-doc.org) project that gives an overview
of all the user guides for all the products by
[cronologic GmbH & Co. KG](https://www.cronologic.de). The HTML output is
available online at [docs.cronologic.de](https://docs.cronologic.de).

## Setup and installation
A Python installation is necessary to compile the user guide.

Optionally, create and activate a virtual environment
```shell
python -m venv .venv
. .\.venv\Scripts\activate
``` 

Install the requirements of the project
```shell
pip install -r requirements.txt
```

After that, run
```shell
make html
```
to compile the project as html. The html output is in build/html/.

## License
This documentation is licensed under an
[Creative Commons Attribution-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nd/4.0/).
You are free to copy and redistribute the material in any medium or format 
for any purpose (even commercially) unchanged if you give appropriate credit
to cronologic GmbH & Co. KG. A link to
[this repository](https://github.com/cronologic-de/ug_hub) is sufficient.

If you decide to contribute to this repository you transfer non-exclusive
but unlimited rights to your edit to cronologic GmbH & Co. KG.
![Creative Commons by-nd 4.0](https://i.creativecommons.org/l/by-nd/4.0/88x31.png) 
