# SSTEM-Learn-Github-and-Python 

##Intro

We're going to put all of your calculators from the last lab into this project. 

The Raspberry Pi already has git installed but if you're working on your own machine you can install it from here: https://git-scm.com/ or through the command line (apt get / brew). 

If you need a refresher on vim I suggest either http://www.openvim.com/ or at any command prompt type vimtutor

##Terms

Clone - Cloning is taking a snapshot of the project and storeing it into a new directory. 

Commit - Commiting is essentially saving any changes you've made to the project, this stays local until pushed. 

Pull - Pulling finds any changes made to the project that you cloned and adds them to your project. 

Push - Pushing adds your commits to the project you cloned.

##Steps

- You'll need to clone this project to the Raspberry Pi or your own machine. You can do this by running the command: 
``` bash
git clone https://github.com/scottshuffler/SSTEM-Learn-Github-and-Python.git
```

- Enter the directory and modify the main.py file by adding your code into the class with your name on it 
``` bash
cd SSTEM-Learn-Github-and-Python 
vim main.py
```

- Once you've tested your code, we're going to commit, and then push it back to Github
``` bash
git commit -a -m "Your descriptive commit message here"
git pull origin master
git push origin master
```
