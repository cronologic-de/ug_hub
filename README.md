# ug_hub

This is a [Sphinx](https://www.sphinx-doc.org) project that gives an overview of
all the user guides for all the products of
[cronologic GmbH & Co. KG](https://www.cronologic.de), such as cronologic's
highspeed
[analog-to-digital](https://www.cronologic.de/products/products-overview#adcdata)
(ADC) and
[time-to-digital](https://www.cronologic.de/products/products-overview#tdcdata)
(TDC) converters.

The resulting HTML is hosted online at
[docs.cronologic.de](https://docs.cronologic.de).

## Prerequisites

Python is necessary for creating the HTML output.

Python and LuaLaTeX are necessary for creating the LaTeX/PDF output.

Dependencies are managed using [uv](https://docs.astral.sh/uv).

## Building

Run

```shell
make html
```

to compile the project as html. The html output is in `build/html/`.

## License

![Creative Commons by-nd 4.0](https://i.creativecommons.org/l/by-nd/4.0/88x31.png)

This documentation is licensed under the
[CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/) license (see
[LICENSE](LICENSE)). You are free to copy and redistribute the material in any
medium or format for any purpose, even commercially unchanged if you give
appropriate credit to cronologic GmbH & Co. KG. A link to
[this repository](https://github.com/cronologic-de/ug_timetagger4) or the
[product page](https://www.cronologic.de/product/timetagger) is sufficient. If
you decide to contribute to this repository, you transfer non-exclusive but
unlimited rights to your edit to cronologic GmbH & Co. KG.

The Montserrat font is licensed under the [SIL OPEN FONT LICENSE](OFL.txt).
