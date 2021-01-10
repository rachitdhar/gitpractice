for i in range(5):
    print("Hello world")
    print("adding a new line now")

# To check if we can view the changes made when someone else has edited ur file
def testfunc():
    print("Let\'s gooo")

# ok, so I found that when someone else directly makes a change and commits it to the main branch, then it won't highlight that change in vscode
# it will only show the updated file directly which can be viewed when u press synchronize button (on bottom-left) in vscode.

# let's try using a pull request option and see what happens in that case

def pulltest():
    print("Hello world pt2")

# ok great, so now whenever someone makes a change in a file that someone else is working on, then
# it is better to make a pull request rather than directly add it to the main branch, bcs that might
# make it difficult for the other person in case he has already made his own changes without including
# the other guy's code yet.

# let's see if we can make a pull request from vscode

for _ in range(len(str(12334))):
    testfunc()
    pulltest()

    print("Hello world! (pt3)")

# ok so what we have to do is, click the "main" written at the bottom-left of vscode. This tells what
# the branch is within which we are working.
# on clicking it, u can choose "create a new branch from" option. Enter the new name. (eg: rachitdhar-patch-2)
# and then select the branch name from which u have created this new branch. (In this case, that is the "main" branch)
# then just do a commit and push normally as we did before

# just a test file to see if git commit and git push works properly
