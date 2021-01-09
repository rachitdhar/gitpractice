# gitpractice
To learn how to work with git through VSCode

Hi Arein! Rachit here.

Hope u r able to read this file.
U r already using vscode, and u also now hv a github account.
Now just one last thing is left that needs to done. U hv to install git.

---------------------------------------------
Why we need Git:

It is a version control software, which will help u see the changes that hv been made in any files in the repository of our project. Through Git, u can bring a repository from GitHub onto ur vscode workspace, so that u can work on it through the vscode editor itself.

U can keep making changes in the project files, and once u r done making ur changes u can make them permanent by sending those changes to github (by commit and push feature of git, which will be done  through vscode itself). [Note: although the changes will be made final upon commit and push, ur old versions will still remain in the file history and can be viewed through github]

Git will also allow us to see which changes hv been made to a file recently, which is important especially in collab, bcs if 2 people happen to work on the same file, then it can be v difficult to keep track of changes without this feature.
---------------------------------------------

I have just installed git and set it up after alot of trial and error (it was a mildly painful process of learning!). So now that I understood the process, I hv written done the exact steps that u can follow do get the same done more easily :)

HOW TO INSTALL GIT AND SET IT UP:

1. Download git setup from this link: https://git-scm.com/downloads. After the .exe file is downloaded, run it and complete its setup steps to install git.

2. Goto the location in ur file system where u saved the git folder. For example: I saved it in C:\Program Files\Git. Now go into this Git folder, and go into the "bin" folder located in it. Copy the path of this folder (eg: C:\Program Files\Git\bin), and add this path to ur system's environment variable paths.

SETTING UP VSCODE FOR GIT:

3. In case u hv not signed in to github from vscode, u can do that. (I guess it is done through the profile-like button located near the bottom-left of the vscode screen)

4. In case there are any folders that u hv kept open in ur workspace, then close them for now. (Goto the file explorer located near top-left of screen, and in the workspace, right-click on the outermost folder and select the option "Remove folder from workspace". Note: This will just remove the folder from ur vscode workspace. It is still existing on ur computer system and can be added back to the workspace later in case u need to work on it!)

5. Now goto GitHub and select this practice repository (to which I added u as a collaborator). Here u will see a green coloured "Code" button which upon pressing u will see an https link. Copy this link. Now go back to vscode. Press ctrl+shift+P to open the command palette, and type "Git: Clone" command. Here u hv to paste the link. Now u will be asked to choose a folder (Preferably, u could create a folder where u can store all ur future GitHub repositories as well) for storing the cloned repository from github. After this there would probably be a redirect to an authentication page on ur browser to just confirm that u r allowing access to github. Accept it, and the job is done. Ur repository from github has been cloned onto ur computer system successfully!

6. Now in ur workspace u will see the option "Add Folder". Select it, and choose the repository folder. Now u hv opened the folder and u hv access to all folders and files within the repository. U can now work on the repository and do whatever u want: make new files, edit them, delete them, etc.

7. Whenever u make any changes to this repository, these changes shall be visible in the "Source Control" (the middle button on the left side of vscode). This is place where Git actually works. Here u will see all files that hv been edited in some way. To see what changes were exactly made, u can click on the filename in the source control region, and the changes will be shown in green and/or red highlightings. Once u hv confirmed the changes for a particular file(s), u can place ur cursor above that filename and choose the "Stage changes" option (a plus symbol). This will add these files to a separte location called "Staged Changes".

8. Finally when u want to send these updated ("staged") files to github, just click the "Commit" button (a tick symbol) on the top of the source control region, and type in a commit message (just a one line statement that gives v brief info on the changes u hv made. this statement will later be visible next to the updated files on github). After this, at the bottom-left of the vscode screen u will see an up-down arrow like thing (where down means "pull" and up means "push"). U hv to click this. It will send the changes to the github repository, and u can reload the github page after this to view ur changes over there as well.


In case of some problem, u can refer to this video which covers this topic briefly too: https://www.youtube.com/watch?v=Fk12ELJ9Bww