<h2>Image Slideshow on Raspberry PI | Digital PhotoFrame</h2>
This repo holds code on running an image slideshow application built on python.
Compatibility for raspberry pi devices.<br>
Tested application in raspberry pi zero 2w.

<br><hr><br>
Required modules/packages can be found in: [setup.sh](https://github.com/paarthpm/my-slideshow-project/blob/main/setup.sh)
<br>
Installation for pi devices can be found in: [installation-readme.md](https://github.com/paarthpm/my-slideshow-project/blob/main/installation-readme.md)
<br>

The application is directly dependant on the number of images sent per batch for slideshow view. This has been restricted to lower integer as it is tested with pi zero 2w. The values can be tweaked depending on device performance.
<br><br>
The child script for slideshow is killed every time the slideshow display completes per batch and is controlled by the master script. This reduces resource consumption and the application has been able to continuously show image slideshows of 100 mid resoultion images with CPU and memory usages in range of 50-80%.
