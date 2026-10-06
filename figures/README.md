# Figures

`source/overall_accuracy.csv` is the source data for the derived overall
accuracy figure. `overall_accuracy.svg`, `overall_accuracy.png`, and
`overall_accuracy.pdf` are generated locally by the reproduction workflow when
the local ImageMagick SVG delegate is available. No source manuscript figure
files were present in the supplied workspace.

The package includes reproducible SVG figure output and its source tables under
`reproduced/`. The original workspace did not contain manuscript PDF/PNG figure
files, so no pre-existing binary figures could be archived. `reproduce_all.py`
regenerates the release SVG from the authoritative outcome matrix.
