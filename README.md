# gitpractice

To learn how to work with git through VSCode

Hi Arein! Rachit here.

Hope you are able to read this file.
You are already using vscode, and you also now hv a github account.
Now just one last thing is left that needs to done. You hv to install git.

## Why we need Git

It is a version control software, which will help you see the changes that hv been made in any files in the repository of our project. Through Git, you can bring a repository from GitHub onto your vscode workspace, so that you can work on it through the vscode editor itself.

You can keep making changes in the project files, and once you are done making your changes you can make them permanent by sending those changes to github (by commit and push feature of git, which will be done  through vscode itself). [Note: although the changes will be made final upon commit and push, your old versions will still remain in the file history and can be viewed through github]

Git will also allow us to see which changes hv been made to a file recently, which is important especially in collab, bcs if 2 people happen to work on the same file, then it can be v difficult to keep track of changes without this feature.


I have just installed git and set it up after alot of trial and error (it was a mildly painful process of learning!). So now that I understood the process, I hv written done the exact steps that you can follow do get the same done more easily.

### How to install git and set it up

1. Download git setup from this link: https://git-scm.com/downloads. After the .exe file is downloaded, run it and complete its setup steps to install git.

2. Goto the location in your file system where you saved the git folder. For example: I saved it in C:\Program Files\Git. Now go into this Git folder, and go into the "bin" folder located in it. Copy the path of this folder (eg: C:\Program Files\Git\bin), and add this path to your system's environment variable paths.

### Setting up VSCode for git

3. In case you hv not signed in to github from vscode, you can do that. (I guess it is done through the profile-like button located near the bottom-left of the vscode screen)

4. In case there are any folders that you hv kept open in your workspace, then close them for now. (Goto the file explorer located near top-left of screen, and in the workspace, right-click on the outermost folder and select the option "Remove folder from workspace". Note: This will just remove the folder from your vscode workspace. It is still existing on your computer system and can be added back to the workspace later in case you need to work on it!)

5. Now goto GitHub and select this practice repository (to which I added you as a collaborator). Here you will see a green coloured "Code" button which upon pressing you will see an https link. Copy this link. Now go back to vscode. Press ctrl+shift+P to open the command palette, and type "Git: Clone" command. Here you hv to paste the link. Now you will be asked to choose a folder (Preferably, you could create a folder where you can store all your future GitHub repositories as well) for storing the cloned repository from github. After this there would probably be a redirect to an authentication page on your browser to just confirm that you are allowing access to github. Accept it, and the job is done. your repository from github has been cloned onto your computer system successfully!

6. Now in your workspace you will see the option "Add Folder". Select it, and choose the repository folder. Now you hv opened the folder and you hv access to all folders and files within the repository. you can now work on the repository and do whatever you want: make new files, edit them, delete them, etc.

7. Whenever you make any changes to this repository, these changes shall be visible in the "Source Control" (the middle button on the left side of vscode). This is place where Git actually works. Here you will see all files that hv been edited in some way. To see what changes were exactly made, you can click on the filename in the source control region, and the changes will be shown in green and/or red highlightings. Once you hv confirmed the changes for a particular file(s), you can place your cursor above that filename and choose the "Stage changes" option (a plus symbol). This will add these files to a separte location called "Staged Changes".

8. Finally when you want to send these updated ("staged") files to github, just click the "Commit" button (a tick symbol) on the top of the source control region, and type in a commit message (just a one line statement that gives v brief info on the changes you hv made. this statement will later be visible next to the updated files on github). After this, at the bottom-left of the vscode screen you will see an up-down arrow like thing (where down means "pull" and up means "push"). You hv to click this. It will send the changes to the github repository, and you can reload the github page after this to view your changes over there as well.


In case of some problem, you can refer to this video which covers this topic briefly too: https://www.youtube.com/watch?v=Fk12ELJ9Bww