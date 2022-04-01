# NFT - Generator

This Application helps you create NFT with a simple python script.

## What is NFT Generator ?

Combining and overlaying image datas on top of each other from 4 categories. The categories can vary from background to body-parts. In the following parts of the README.md i will generally refer the category as body-parts. 



## Demo

[![Watch the video](https://i.imgflip.com/604ad4.jpg)](https://www.youtube.com/watch?v=KeLu6wteRGI)

This demo is a demonstration for the NFT project "ANANASMAN", which showcases the combination of 3 body-parts and 1 background category. The GUI usage is quite simple as it can be seen from the demo video.


## How it works?

Running through every possible combination of the given categories is the principal of the script. Then overlaying the combination in the correct order (Background->Upper body->Head->Lower body) gives the result.

![](githowto.png)


## Running the Script

The Application has (yet) no executable file, so running it directly from terminal or jupyter notebook (DEMO) is what i would recommend.


## How to prepare the necessary data?

The most vital data is the body-part data, which has (for now) 4 sub paths.

The body-part paths and "generated2" path  should exist in following directorial tree way:

![](ditree.png)



## Suggestions

Adapting to dynamic changes and creating new variables for body parts can make the script more useful.




## Conclusion

The script is able to generate simple NFT sets without taking the rarity factor into account. Combining a python
script with GUI brings new challenges for the optimization, hence the script is slower if we compare the GUI version
with raw terminal script.

Created by Can Günen
