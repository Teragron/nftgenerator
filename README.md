# NFT - Generator

This Application helps you create NFT with GUI.

## What is NFT Generator ?

Combining and overlaying image datas on top of each other from 4 categories. The categories can vary from background to body-parts. In the following parts of the README.md i will generally refer the category as body-parts. 



## Demo

[![Watch the video](https://i.imgflip.com/604ad4.jpg)](https://www.youtube.com/watch?v=KeLu6wteRGI)

This demo is a demonstration for the NFT project "ANANASMAN", which showcases the combination of 3 body-parts and 1 background category. The GUI usage is quite simple as it can be seen from the demo video.


## How it works?

Running through every possible combination of the given categories is the principal of the script. Then overlaying the combination in the correct order (Background->Upper body->Head->Lower body) gives the result. Although this may seem like permutation since it looks like an order, the Sequencing is only neccessary for the overlaying. So for example with 4 combined categories each having 5 images would give us 5x5x5x5 images, which is 625. (I will look to the definition of this iterative process again)

![](githowto.png)


## Running the Script

The Application has (yet) no executable file, so running it directly from terminal or jupyter notebook (DEMO) is what i would recommend.


## How to prepare the necessary data?

The most vital data is the body-part data, which has (for now) 4 sub paths.

The body-part paths and "generated2" path  should exist in following directorial tree way:

![](ditree.png)


## GUI Part


![](gui.png)

 With the help of pysimplegui i've added a simple user interface to the script, which makes the path selection way faster. This way, we can also give the size for the output data. The size is by default set to 512x512
 
 # Showcase
 
![1](https://user-images.githubusercontent.com/54573938/161191477-8dea14d3-6da8-495e-9598-9f8356585f52.png)
![190](https://user-images.githubusercontent.com/54573938/161191488-8117e9f7-cfea-4c45-8577-de7f8b21f8d0.png)
![89](https://user-images.githubusercontent.com/54573938/161191505-31f3efc7-ddf0-423d-8cfb-1952f9799701.png)

 
## Suggestions

Adapting to dynamic changes and creating new variables for body parts can make the script more useful.




## Conclusion

The script is able to generate simple NFT sets without taking the rarity factor into account. Combining a python
script with GUI brings new challenges for the optimization, hence the script is slower if we compare the GUI version
with raw terminal script.

Created by Can Günen
