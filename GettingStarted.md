그런즉 너희가 먹든지 마시든지 무엇을 하든지 다 하나님의 영광을 위하여 하라 (고전10:31)

-------
<img src="https://github.com/idebtor/DSpy/blob/6b3676c3de29f85d2e7f30679676d1fd96d88b17/images/WelcomeToDataStructures.jpg?raw=true" width=1000>

__NOTE:__ The following materials have been compiled and adapted from the numerous sources including my own. Please help me to keep this tutorial up-to-date by reporting any issues or questions. Send any comments or criticisms to `idebtor@gmail.com` Your assistances and comments will be appreciated.
Lecture notes by idebtor@gmail.com

-----

# Getting Started
  __To get started__, do the first thing first:

  1. Read README.
  2. Read Syllabus.
  3. Read 'GettingStarted' - this file
  4. Follow instructions in 'GettingStarted' as soon as possible(ASAP).

  This is available at [github.com/idebtor/DSpy](https://github.com/idebtor/DSpy).

## Three ways to view markdown(.md) files

### GitHub 
  0. View them always in github website automatically and better.
  1. GitHub does not support `LaTex` yet. You may not see the well-formatted math equations.

### Web Browser (Chrome/Edge)
  1. Install `Markdown Preview Plus` extension in your browser(Chrome, Edge).
  2. Go to `extensions, 도구 더보기 혹은 확장` in the browser's setting 
  3. Locate `Markdown Preview Plus` and click on the `DETAILS 세부정보`
  4. Check the option `Allow access to file URLs, 파일 URL에 대한 액세스 허용`
  5. Drag and drop ~.md file in your brower.
  6. For `LaTex`, check the math option in `Markdown Preview Plus` icon in your brower top menubar'. 
  7. Enjoy nicely formatted HTML!

### Visual Studio Code
  1. Install `Markdown All in One` & `Auto-Open Preview` extensions in your `Code`.
  2. Enjoy nicely formatted HTML!
  
Refer to my tutorial: <https://youtu.be/sS1viPcXDIo> 

## Joining Piazza

There are two ways to join Piazza, connect to the www.piazza.com.
  - To join Piazza, you may need the following information and
    - School: __Handong Global University__
    - Course: __Data Structures in Python__
  - If you have an email address that ends with __~.hgu.edu__ or __~.handong.edu__ domain and use it everyday, go the www.piazza.com and follow the instructions in the website.

  - On your request with your email address, I may register it for you.  We'll be conducting all class-related discussion here this term. The quicker you begin asking questions on Piazza (rather than via emails), the quicker you'll benefit from the collective knowledge of your classmates and instructors. We encourage you to ask questions when you're struggling to understand a concept—you can even do so anonymously.

## Install Anaconda
Anaconda is  a Python and R distribution package. It aims to provide everything you need (python wise) for data science "out of the box".  It includes:
-	The core python language
-	200+ python "packages" (libraries)
-	Spyder (IDE/editor) and Jupyter Notebook
-	conda, Anaconda's own package manager, used for updating Anaconda and packages

#### To install the anaconda:

  - Visit website [Anaconda Distribution](https://www.anaconda.com/distribution/)
    - Choose one of Windows/MacOS/Linux
    - Python 3.x Version Download
  - At the beginning of installation, check the following option
      - Add Anaconda to my PATH environment variable as shown below:

    <p align="center"> <img src="https://github.com/idebtor/KMOOC-ML/blob/master/ipynb/images/anaconda_check_path.png" width=500> </p>

  - Need help? Follow [this guide](https://m.blog.naver.com/PostView.nhn?blogId=jooostory&logNo=221196479998&proxyReferer=https%3A%2F%2Fwww.google.com%2F).

#### After your installation
Do the following in cmd windows or in PowerShell to check your successful installation; ($ is just a prompt of your console, >>> is a prompt from Python.)

      ```
      $ python
      >>> Python 3.8.10 (default, May 19 2021, 11:45:54) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
          Type "help", "copyright", "credits" or "license" for more information.
      >>> import math
      >>> math.sqrt(2)
      1.4142135623730951
      >>> exit()
      ```

#### Need more installation?
Use the following command if you need more installation of packages (-U for upgrade only):
  ```
  $ pip install a_package_name
  $ pip install -U a_package_name              
  ```

## Install "Git" and "GitHub Desktop"
  - Install __git__ from [this site](https://git-scm.com/downloads) for your computer.
  - Install __GitHub Desktop__

After installation of __GitHub Desktop__, be a member if already not.

  - Clone the GitHub `DSpy` repository into your local computer (e.g. `C:/github/dspy`):
    - https://github.com/idebtor/DSpy  

  - How to clone a repository from GitHub:

      - Refer to [this site](https://help.github.com/desktop/guides/contributing-to-projects/cloning-a-repository-from-github-desktop/).
  - Click __'watch'__ and __'star'__ at the top of the web page^^.

  - Then, in your computer, you may have the following github/DSpy folder as shown below (`user` may be different in your system.):
    - ```C:\Users\user\Documents\GitHub\DSpy```   
    - ```C:\GitHub\DSpy```           
    I recommend you to make the path simple as possible like `C:\github\dspy`

  - Since this `DSpy` repository can be updated anytime, keep this local repository as "read-only".  Don't code yours here!.
  - Copy them into your own repository or your own local development folders in your computer you can easily access them.  They should look like the following:
    ```
    ~/DSpy/ppt
    ~/DSpy/ipynb
    ~/DSpy/GettingStarted.md
    ~/DSpy/README.md             
    ~/DSpy/AIX20001Syllabus       
    ```

      __Note for Multi-screen users:__ Remove the following file if GitHub Desktop is displayed off-screen. Restart Desktop GitHub. (`user` below may be different in your system.)
      ```
      C:\Users\user\AppData\Roaming\GitHub Desktop\window-state.json
      ```

## Are ready for 'Hello World!' program in Python?
  - Open a console. (You may use `Anaconda Prompt`, `cmd` or `powershell` in Windows.)  

  ```
  $ python
  >>> print('Hello World!')
  >>> 1 + 2
  3
  >>> exit()
  $
  ```

  ## A few ways to start Jupyter-lab or Jupyter notebook

__Method 1__:
This method may not work unless you have set PATH environment variable.
1. Using File Explorer, navigate to where your Jupyter notebook file is   
1. Using File menu in File Explorer, click Open PowerShell(PS).  
1. At PS console, enter the following:  
```
    PS C:\> jupyter-lab
    PS C:\> jupyter notebook
```
   
__Method 2__:
This is one-line batch command file that runs Jupyter-lab.  

1. Get a copy of the batch file `start_jupyter.bat` which is available at https://github.com/idebtor/DSpy  
1. Place the batch file at the folder where your notebook file is.  
1. Double-click the batch file.
    
__Method 3__:
This option always works:

1. Go to the Windows menu `<Start> -> <Anaconda 3> -> <Anaconda Prompt>`   
1. At a console, enter the following:  
```
    (base) C:\Users\user> jupyter-lab
    (base) C:\Users\user> jupyter notebook
```

__Method 4__:
This is not recommended since it is too slow to get into the notebook.  

1. Using Anaconda Navigator, choose Jupyter Notebook or Jupyter-lab

-----------------------------------------------

## Are ready for cloning another open-source program in GitHub?

Let's clone some open-source packages that uses with MNIST dataset and classifies user's hand-writing digits interactively.

  - Clone the following two github sites

  ```
  https://github.com/scrambledpie/Drawing-Mnist-and-Cifarizing-image-files
  https://github.com/rhammell/mnist-draw
  ```

## References
- [DrawMyOwnNumbers Notebook](https://github.com/scrambledpie/Drawing-Mnist-and-Cifarizing-image-files)
- [mnist-draw](https://github.com/rhammell/mnist-draw)

## What's Next?

- About Markdown: [this site in Korean](https://theorydb.github.io/envops/2019/05/22/envops-blog-how-to-use-md/)

- Learning Python and Numpy from the beginning, visit [this site](https://www.learnpython.org/en/Welcome). It is offered by learnpython.org.
-

----------------------------
_One thing I know, I was blind but now I see. John 9:25_

----------------------------
