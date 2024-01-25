# What is webcam_to_cli ?
Webcam_to_CLI is a python OpenCV project that aims to show the webcam flux into the console.\
It uses ANSI color codes and is able to show the flux with full colors and greyscale. Please note that the full color mode is slow for a resolution too high.\
You can also use it to print images with the CLI.

![Capture d'écran 2024-01-25 213914](https://github.com/belabon25/webcam_to_CLI/assets/74050200/b405a0cd-8c12-4248-abb8-26db8248cbc1)


# Commands

## -m [mode], --mode [mode]
fullcolor, fc : show the webcam flux as full colored ansi sequence (default mode).\
ascii, a : show the webcam flux in greyscale as ascii art.\
greyscale, gr : show the webcam flux as greyscale ansi sequence. This is way faster than the full color mode and still pretty.\
loadimagefc, lifc : load an image and print it to the terminal in full color.\
loadimagegr, libgr : load an image and print it to the terminal in greyscale.

## -i [path], --image-path [path]
Necessary for all the loadimage modes. Set the path to the image you want to load.
## -x [number], --xRes [number]
Set the number of columns of your flux/image. If not set, the image will wrap all the available space of your CLI.
## -y [number], --yRes [number]
Set the number of lines of your flux/image. If not set, the image will wrap all the available space of your CLI.
