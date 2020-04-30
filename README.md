[![Updates](https://pyup.io/repos/github/nicholasks/ios-img-generator/shield.svg)](https://pyup.io/repos/github/nicholasks/ios-img-generator/)
--
# IOS Image Generator
***[WIP]*** (This is a working in progress project).

Generate IOS 3 size image set

Input formats
---
`.xml`, `svg` and `png`.
As the quality gets lost, its recomended to use xml and svg as input.

For png image it should be on 3x scale in order to work.

For more information about IOS image scales check [this](https://developer.apple.com/design/human-interface-guidelines/ios/icons-and-images/image-size-and-resolution/).



Output
---
The image in `.png` format on scales 1x, 2x, 3x.

Usage
---
Install all dependencies
`pip3 install -r requirements.txt`

Put all images on the same directory as the script and run it
`python3 IOSImgGenerator.py`


Thanks
---
Thanks to Alessandro Lucchet, responsible for the [VectorDrawable to Svg script](https://gitlab.com/AlessandroLucchet/VectorDrawable2Svg/).
