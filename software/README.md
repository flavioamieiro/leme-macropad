This keyboard will run top of [QMK](https://qmk.fm/). The `leme`
directory is a keyboard definition meant for QMK.

To setup your environment, make sure you have the QMK CLI installed with:

```
pip install qmk
```

Then setup the QMK build environment:

```
qmk setup
```

This keyboard is not yet supported in the QMK repository, but after
setting the development enviroment up, you can create a link in the
QMK `keyboard` directory our definition here:

```
ln -s "$(pwd)/leme" "$(qmk config -ro user.qmk_home | cut -f2 -d=)/keyboards/leme"
```

You can now build the firmware with:

```
qmk compile -kb leme -km default
```

which will generate a .uf2 image (in the qmk directory) you can flash
onto the RP2040.
