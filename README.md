---
published: false #Exempts page from jekyll site creation (aka completely removes from site)
---

# how to install jekyll on windows for github pages
based off [this guide](https://jekyllrb.com/docs/installation/windows/)

## Install ruby via rubyinstaller

* Grab the latest Ruby+DevKit installer for your system from: [here](https://rubyinstaller.org/downloads/)
* Launch the downloaded installer
* make sure to run the ```ridk install``` step on the last stage of installation
* upon completion of installer open new command prompt window
* OPTIONAL: check that the ```PATH``` variable has been correctly changed

## Install jekyll via ruby

* in command prompt run ```gem install jekyll bundler```
* once installation complete check that jekyll was correctly installed via the ```jekyll -v``` command


## Setting up a github repo for use as your github page

* create new repo
* make sure the you have a branch called gh-pages 
  * only the gh-pages branch will be published via github pages, so other branches can be used to store related materials, but gh-pages is where you should push your website files
* the URL for your repo, example: ```AlexHill-SD/Data-Visualsation-with-Python---INTP-315-Blog``` forms the basis of your github pages URL
* Format for github pages URL is: ```username.github.io/repo-name```
 * So in my case it's ```AlexHill-SD.github.io/Data-Visualsation-with-Python---INTP-315-Blog```

## Starting your site

* Preferred: Find a theme online in such places like [jekyllthemes.dev](https://jekyllthemes.dev/) or [jekyllthemes.org](http://jekyllthemes.org/)
* download the theme
* make sure you have your previously created repo on your pc
* extract the theme into your gh-pages repo branch locally
* follow installation instructions (if applicable)
  * Usually involves changing config properties, etc 
* Optionally: follow the github pages [quickstart guide](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll)

## Hosting your site

* push your jekyll repo to github, github pages will automatically run it through their serverside jekyll and your page will be hosted at the previously mentioned URL
* For example see: [my repo](https://github.com/AlexHill-SD/Data-Visualsation-with-Python---INTP-315-Blog)
