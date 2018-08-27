from MyQR import myqr
import os

words="http://www.naodongopen.com"
version, level, qr_name = myqr.run(
    words,
    version=10,
    level='Q',
    picture='cat.png',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name='love.png',
    save_dir=os.getcwd()
    )


# Optional parameters
#    version: int, from 1 to 40
#    level: str, just one of ('L','M','Q','H')
#    picutre: str, a filename of a image
#    colorized: bool
#    constrast: float
#    brightness: float
#    save_name: str, the output filename like 'example.png'
#    save_dir: str, the output directory
