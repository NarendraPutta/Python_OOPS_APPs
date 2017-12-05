In this Class, We will know how VCS(Version Control System) works & especially github configuration.

Its dificult to understand by reading it. I also took so much time for the first time.
But Once I explain it, you will get it easily. Dont worry on that part.

As a theory: Go through it & try to understand as much as possible.

Lets start the Class now............

github is going to play the major part through out the course. 

Please go to https://github.com/ & sign in.

If you dont have an acount. Please Create your account.

Once you have done that part, Please install git repository in your local machine(Ideally your
PC or laptop).

Mine is 64bit PC & the link is : https://git-scm.com/download/win

I suggest, Please check your operating system & download appropriate one.

Installation Steps:

As for all the executables, Please open the downloaded executable &
click next buttons 3times & select 3rd option 'Use Notepad ++' as Git's default editor' & press
next to continue the installation process by again clikcing next buttons untill you see
the 'Finish' Button.

Once You click on 'finish' button would open the Releasenotes.html.
Please go through for the changes & improvements (This one is not so important, But,
You may go through for the knowledge)

Once You done with the Installation. Please create a folder called 'Python_OOPs_Apps Project' in the local directory
 and open the folder.

 Inside the 'Python_OOPs_Apps Project', right click on the mouse & select 'Git Bash here'

 It opens up very colourful terminal & this is called Git Bash Emulator.

In order to create local repository, type command $git init & press 'Enter'

You will be typing all your commands & you will be doing all your work in the 'GitBash' .

You can see that C:\Python_OOPS_APPs_Project git repository is created.

Open the git folder & see all the configurations, object details & everything.

Now Your repository is initialized & this is going to be your local repository.

After we create our repository, It is very important to link the repository because how
would we know which repository to push into & pull all the information remotely
from your repository if there is no connection.

In order to connect both the sides, first thing that we need to do is add origin.

Now again Go to 'https://github.com/NarendraPutta/Python_OOPS_APPs/tree/master' (your's
will be on your name and your link will be different)

drop down 'Clone or download' feature (Available in 'green' colour on the right top.
You will get it easily when you see it.  Not a big deal.

Copy the link &come back to the 'git bash' & give following commad followed by your copied link

$git remote add origin "https://github.com/NarendraPutta/Python_OOPS_APPs.git"

If you dont see any errors, It implies your origin has been added successfully.

Now we will pull all the  git information from central repository into the local repository.


In your 'git bash' type a command.
$git pull origin master   and press 'Enter'
You can observe that they have done some processing from master branch into the
master branch.

Let us see that whether all the branches are fetched or not.

Go to 'C:\Python_OOPS_APPs_Project' (This is the directory that you have created) &
 see files which are fetched.

Lets check about following commands.
                                       
$git status : To know what are the data available in the present directory
$git add : You can add the files in two types. As You can add single file also as well as multiple files also at a time.
Adding Multiple Files:  git add -A will add all the local files into the repository                                
$git commit : git commit -a -m "Added Python OOPs_Apps" will  commit the files to push to master repository.

$ssh-keygen : Give following command & press Enter would ask you the question to continue.
Please select 'y' and enter
Enter again two times will generate secured key.
Now copy  cat /c/Users/vinayb/.ssh/id_rsa.pub from the generated log when given $ssh-keygen command and
press Enter will genarate the key would look something like this.

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDHpsGTtTbzSNMxtxqklwYsVvi0MQ/Ks+apT8cYhwzY0uKKOfTf+
i/Lc+udqkPp5ca4MHVEt2/PRb3cWUwk36TOrO7Ykq1QZYuGfnN+GOgqtXCmSgbwp2v46/u7whNWNGj+mjvVg7Gra
NqiZLLnPFq0ZWQPlsC4D7QjNa0Nk6Ej3+wnhk+PY3uHgZOS+3MManKKwT2VocAeFp6j6Kup1O5Njq7Eg0pxP866lM1
WwZEmLcTxkTXIeFVqNyZXFHIalBgJuOBBBoTKIIOfwXd6Ov0JxJZ3fhwBuWJC1D9jx3vQHb1D+QaAdxA2gTU3PkGR
uKjlCoHm9O8xKoATkmj6rpvl vinayb@BDTBF8FBX1                                    

Copy the key & go to https://github.com/settings/ssh/new  & press Enter would show up Title & Key.
Give 'SSH1' in title & given copied key in the key field & click on 'Add SSH Key' will generate the key.

Once done, We need to get authenticated for which please give following command.

$ssh -T git@github.com & press 'Enter' would give you sucessfully authenticated message something like below.
                                       
Hi NarendraPutta! You've successfully authenticated, but GitHub does not provide shell access.

Now To push to the master repository (i.e: www.github.com), Please give following command.
$git push origin master  & Press 'Enter' would push all the files to master repository by showing some information
like as shown below.                                        

Counting objects: 32, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (32/32), done.
Writing objects: 100% (32/32), 30.50 KiB | 3.81 MiB/s, done.
Total 32 (delta 0), reused 0 (delta 0)
To https://github.com/NarendraPutta/Python_Documentation_till_OOPs.git
   f361b71..e02c0b4  master -> master
                                       
                                       
Thats all, You are done.  You have successfully uploaded all your local repository files to master repository.

Now refresh the github.com page would show you the newly uploaded files.                                      
                                       
                                       
                                  

####################################################################################################
This is just a log. Interested can view all the commands used
####################################################################################################                                      
This is just a log. Interested can view all the commands used
vinayb@BDTBF8FBX1 MINGW64 /c/Python_Documentation_till_OOPs
$ git init
Initialized empty Git repository in C:/Python_Documentation_till_OOPs/.git/

vinayb@BDTBF8FBX1 MINGW64 /c/Python_Documentation_till_OOPs (master)
$ git remote add origin "https://github.com/NarendraPutta/Python_Documentation_t

vinayb@BDTBF8FBX1 MINGW64 /c/Python_Documentation_till_OOPs (master)
$ git pull origin master
remote: Counting objects: 3, done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From https://github.com/NarendraPutta/Python_Documentation_till_OOPs
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> origin/master

vinayb@BDTBF8FBX1 MINGW64 /c/Python_Documentation_till_OOPs (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        Anonymous_Function.py
        Break&Continue.py
        Control Structures.py
        Dictionaries.py
        Dictionary_Programs.py
        Functions.py
        Functions_Actual_Formal_Parameters.py
        Identifiers-Keywords-Implicit-Explicit-Joining.py
        If-else_Programs.py
        Input_Output_Fundamentals.py
        Introduction.py
        IntroductiontoLIST_Part 1.py
        Keywords_Default_Arguments.py
        LIST_Operators.py
        LIST_Part 2.py
        List_Assignments_Copying_Range_Function.py
        Local_Global_Variables.py
        Many_Control_Staements_Examples.py
        Modules.py
        Operators Part1.py
        Operators Part2.py
        Precedence & Assosiativity.py
        Python_test.txt
        Range_Function.py
        Sequence_Operations_Part 1 & Part 2.py
        String_Functions.py
        Tuples.py
        Updating_Global_Variables.py
        Varible_Length_Arguments.py
        while_Loop.py

nothing added to commit but untracked files present (use "git add" to track)

vinayb@BDTBF8FBX1 MINGW64 /c/Python_Documentation_till_OOPs (master)
$ git add -A

vinayb@BDTBF8FBX1 MINGW64 /c/Python_Documentation_till_OOPs (master)
$ ls
 Anonymous_Function.py
'Break&Continue.py'
'Control Structures.py'
 Dictionaries.py
 Dictionary_Programs.py
 Functions.py
 Functions_Actual_Formal_Parameters.py
 Identifiers-Keywords-Implicit-Explicit-Joining.py
 If-else_Programs.py
 Input_Output_Fundamentals.py
 Introduction.py
'IntroductiontoLIST_Part 1.py'
 Keywords_Default_Arguments.py
 List_Assignments_Copying_Range_Function.py
 LIST_Operators.py
'LIST_Part 2.py'
 Local_Global_Variables.py
 Many_Control_Staements_Examples.py
 Modules.py
'Operators Part1.py'
'Operators Part2.py'
'Precedence & Assosiativity.py'
 Python_test.txt
 Range_Function.py
 README.md
'Sequence_Operations_Part 1 & Part 2.py'
 String_Functions.py
 Tuples.py
 Updating_Global_Variables.py
 Varible_Length_Arguments.py
 while_Loop.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_Documentation_till_OOPs (master)
$ git commit -a -m "Added Python Documentation"
[master e02c0b4] Added Python Documentation
 30 files changed, 2654 insertions(+)
 create mode 100644 Anonymous_Function.py
 create mode 100644 Break&Continue.py
 create mode 100644 Control Structures.py
 create mode 100644 Dictionaries.py
 create mode 100644 Dictionary_Programs.py
 create mode 100644 Functions.py
 create mode 100644 Functions_Actual_Formal_Parameters.py
 create mode 100644 Identifiers-Keywords-Implicit-Explicit-Joining.py
 create mode 100644 If-else_Programs.py
 create mode 100644 Input_Output_Fundamentals.py
 create mode 100644 Introduction.py
 create mode 100644 IntroductiontoLIST_Part 1.py
 create mode 100644 Keywords_Default_Arguments.py
 create mode 100644 LIST_Operators.py
 create mode 100644 LIST_Part 2.py
 create mode 100644 List_Assignments_Copying_Range_Function.py
 create mode 100644 Local_Global_Variables.py
 create mode 100644 Many_Control_Staements_Examples.py
 create mode 100644 Modules.py
 create mode 100644 Operators Part1.py
 create mode 100644 Operators Part2.py
 create mode 100644 Precedence & Assosiativity.py
 create mode 100644 Python_test.txt
 create mode 100644 Range_Function.py
 create mode 100644 Sequence_Operations_Part 1 & Part 2.py
 create mode 100644 String_Functions.py
 create mode 100644 Tuples.py
 create mode 100644 Updating_Global_Variables.py
 create mode 100644 Varible_Length_Arguments.py
 create mode 100644 while_Loop.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_Documentation_till_OOPs (master)
$ ls
 Anonymous_Function.py
'Break&Continue.py'
'Control Structures.py'
 Dictionaries.py
 Dictionary_Programs.py
 Functions.py
 Functions_Actual_Formal_Parameters.py
 Identifiers-Keywords-Implicit-Explicit-Joining.py
 If-else_Programs.py
 Input_Output_Fundamentals.py
 Introduction.py
'IntroductiontoLIST_Part 1.py'
 Keywords_Default_Arguments.py
 List_Assignments_Copying_Range_Function.py
 LIST_Operators.py
'LIST_Part 2.py'
 Local_Global_Variables.py
 Many_Control_Staements_Examples.py
 Modules.py
'Operators Part1.py'
'Operators Part2.py'
'Precedence & Assosiativity.py'
 Python_test.txt
 Range_Function.py
 README.md
'Sequence_Operations_Part 1 & Part 2.py'
 String_Functions.py
 Tuples.py
 Updating_Global_Variables.py
 Varible_Length_Arguments.py
 while_Loop.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_Documentation_till_OOPs (master)
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/vinayb/.ssh/id_rsa):
/c/Users/vinayb/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/vinayb/.ssh/id_rsa.
Your public key has been saved in /c/Users/vinayb/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:3y8zx5DapGrIxzUJ8dIDk6ZGfE6bO0GDaaosDsZjhr8 vinayb@BDTBF8FBX1
The key's randomart image is:
+---[RSA 2048]----+
|     . o .       |
|      * @        |
|     + B X       |
|    . o B +      |
|o. . .  S= o .   |
|+*o     o.+.+    |
|*o.  . o o.*.o   |
| ..   o + o =.o  |
|  E.   o..   =.  |
+----[SHA256]-----+

vinayb@BDTBF8FBX1 MINGW64 /c/Python_Documentation_till_OOPs (master)
$ cat /c/Users/vinayb/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDHpsGTtTbzSNMxtxqklwYsVvi0MQ/Ks+apT8cYhwzY0uKKOfTf+i/Lc+udqkPp5ca4MHVEt2/PRb3cWUwk36TOrO7Ykq1QZYuGfnN+GOgqtXCmSgbwp2v46/u7whNWNGj+mjvVg7GraNqiZLLnPFq0ZWQPlsC4D7QjNa0Nk6Ej3+wnhk+PY3uHgZOS+3MManKKwT2VocAeFp6j6Kup1O5Njq7Eg0pxP866lM1WwZEmLcTxkTXIeFVqNyZXFHIalBgJuOBBBoTKIIOfwXd6Ov0JxJZ3fhwBuWJC1D9jx3vQHb1D+QaAdxA2gTU3PkGRuKjlCoHm9O8xKoATkmj6rpvl vinayb@BDTBF8FBX1

vinayb@BDTBF8FBX1 MINGW64 /c/Python_Documentation_till_OOPs (master)
$ ssh -T git@github.com
Hi NarendraPutta! You've successfully authenticated, but GitHub does not provide shell access.

vinayb@BDTBF8FBX1 MINGW64 /c/Python_Documentation_till_OOPs (master)
$ ls
 Anonymous_Function.py
'Break&Continue.py'
'Control Structures.py'
 Dictionaries.py
 Dictionary_Programs.py
 Functions.py
 Functions_Actual_Formal_Parameters.py
 Identifiers-Keywords-Implicit-Explicit-Joining.py
 If-else_Programs.py
 Input_Output_Fundamentals.py
 Introduction.py
'IntroductiontoLIST_Part 1.py'
 Keywords_Default_Arguments.py
 List_Assignments_Copying_Range_Function.py
 LIST_Operators.py
'LIST_Part 2.py'
 Local_Global_Variables.py
 Many_Control_Staements_Examples.py
 Modules.py
'Operators Part1.py'
'Operators Part2.py'
'Precedence & Assosiativity.py'
 Python_test.txt
 Range_Function.py
 README.md
'Sequence_Operations_Part 1 & Part 2.py'
 String_Functions.py
 Tuples.py
 Updating_Global_Variables.py
 Varible_Length_Arguments.py
 while_Loop.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_Documentation_till_OOPs (master)
$ git log
commit e02c0b478afb77cd70f967a66800e35259ef4e84 (HEAD -> master)
Author: Narendra <naren4everr@gmail.com>
Date:   Tue Dec 5 13:46:15 2017 +0530

    Added Python Documentation

commit f361b71dda231116eaa2db87c73dcbd9b6a35dd8 (origin/master)
Author: NarendraPutta <31036861+NarendraPutta@users.noreply.github.com>
Date:   Tue Dec 5 12:16:53 2017 +0530

    Initial commit

vinayb@BDTBF8FBX1 MINGW64 /c/Python_Documentation_till_OOPs (master)
$ git push origin master
Counting objects: 32, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (32/32), done.
Writing objects: 100% (32/32), 30.50 KiB | 3.81 MiB/s, done.
Total 32 (delta 0), reused 0 (delta 0)
To https://github.com/NarendraPutta/Python_Documentation_till_OOPs.git
   f361b71..e02c0b4  master -> master

vinayb@BDTBF8FBX1 MINGW64 /c/Python_Documentation_till_OOPs (master)
$ ^C

vinayb@BDTBF8FBX1 MINGW64 /c/Python_Documentation_till_OOPs (master)
$ ^C

vinayb@BDTBF8FBX1 MINGW64 /c/Python_Documentation_till_OOPs (master)
$
                                       
git_Pull vs git_fetch:                               



Now lets understand how 'push' works.

                                       
                                       

                                       



How to Create Branches:
Local branches: Local brances are created in your local work spaces.
remtoe control branches: Remote branches are braches that are connected from your local repository to central
repository.

merging:

git_dash

Rebasing:Rebasing is also called meging. This is also a way of combining the work of different branhces. It can be
used to make a linear sequence of commits

Please inform me if you are struck anywhere during the installation process.

#####################################################################################################
More Log with Errors
######################################################################################################
vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        Oops_Apps1.py

nothing added to commit but untracked files present (use "git add" to track)

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git add Oops_Apps1.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   Oops_Apps1.py


vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git commit -m "adding first commit in local repo"

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'vinayb@BDTBF8FBX1.(none)')

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git config --global user.email "naren4everr@gmail.com"

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ get config --global user.name "Narendra"
bash: get: command not found

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git config --global user.name "Narendra"

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git commit -m "adding first commit in local repo"
[master b5fb9d0] adding first commit in local repo
 1 file changed, 177 insertions(+)
 create mode 100644 Oops_Apps1.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ clear

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        Turtle_Ex3.py
        Turtle_ex1.py
        Turtle_ex2.py

nothing added to commit but untracked files present (use "git add" to track)

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ get add -A
bash: get: command not found

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git add -A

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   Turtle_Ex3.py
        new file:   Turtle_ex1.py
        new file:   Turtle_ex2.py


vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git comment -a -m "adding 3files together"
git: 'comment' is not a git command. See 'git --help'.

The most similar command is
        commit

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git commit -a -m "adding 3 files together"
[master 929f0a0] adding 3 files together
 3 files changed, 44 insertions(+)
 create mode 100644 Turtle_Ex3.py
 create mode 100644 Turtle_ex1.py
 create mode 100644 Turtle_ex2.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git log
commit 929f0a03a8420b59962f199d6a271225cf9bbd38 (HEAD -> master)
Author: Narendra <naren4everr@gmail.com>
Date:   Sun Dec 3 18:22:17 2017 +0530

    adding 3 files together

commit b5fb9d0ee16f478e20c303c9954b6876689ad109
Author: Narendra <naren4everr@gmail.com>
Date:   Sun Dec 3 18:12:27 2017 +0530

    adding first commit in local repo

commit 43b478d3421c2585d1a513e205f7c1f9633f92ea (origin/master)
Author: NarendraPutta <31036861+NarendraPutta@users.noreply.github.com>
Date:   Sun Dec 3 15:45:03 2017 +0530

    Create README.md

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$
vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git branch firstbranch

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git checkout firstbranch
Switched to branch 'firstbranch'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ git add OOPS_APPS2.1.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ git commit -m "making changes in firstbranch"
[firstbranch 9e507c8] making changes in firstbranch
 1 file changed, 29 insertions(+)
 create mode 100644 OOPS_APPS2.1.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ ls
Oops_Apps1.py    README.md      Turtle_ex2.py
OOPS_APPS2.1.py  Turtle_ex1.py  Turtle_Ex3.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ git checkout

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ ls
Oops_Apps1.py    README.md      Turtle_ex2.py
OOPS_APPS2.1.py  Turtle_ex1.py  Turtle_Ex3.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        Turtle_Ex3.py
        Turtle_ex1.py
        Turtle_ex2.py

nothing added to commit but untracked files present (use "git add" to track)

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ get add -A
bash: get: command not found

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git add -A

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   Turtle_Ex3.py
        new file:   Turtle_ex1.py
        new file:   Turtle_ex2.py


vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git comment -a -m "adding 3files together"
git: 'comment' is not a git command. See 'git --help'.

The most similar command is
        commit

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git commit -a -m "adding 3 files together"
[master 929f0a0] adding 3 files together
 3 files changed, 44 insertions(+)
 create mode 100644 Turtle_Ex3.py
 create mode 100644 Turtle_ex1.py
 create mode 100644 Turtle_ex2.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git log
commit 929f0a03a8420b59962f199d6a271225cf9bbd38 (HEAD -> master)
Author: Narendra <naren4everr@gmail.com>
Date:   Sun Dec 3 18:22:17 2017 +0530

    adding 3 files together

commit b5fb9d0ee16f478e20c303c9954b6876689ad109
Author: Narendra <naren4everr@gmail.com>
Date:   Sun Dec 3 18:12:27 2017 +0530

    adding first commit in local repo

commit 43b478d3421c2585d1a513e205f7c1f9633f92ea (origin/master)
Author: NarendraPutta <31036861+NarendraPutta@users.noreply.github.com>
Date:   Sun Dec 3 15:45:03 2017 +0530

    Create README.md

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ^C

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ clear

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git branch firstbranch

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git checkout firstbranch
Switched to branch 'firstbranch'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ git add OOPS_APPS2.1.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ git commit -m "making changes in firstbranch"
[firstbranch 9e507c8] making changes in firstbranch
 1 file changed, 29 insertions(+)
 create mode 100644 OOPS_APPS2.1.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ ls
Oops_Apps1.py    README.md      Turtle_ex2.py
OOPS_APPS2.1.py  Turtle_ex1.py  Turtle_Ex3.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ git checkout

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ ls
Oops_Apps1.py    README.md      Turtle_ex2.py
OOPS_APPS2.1.py  Turtle_ex1.py  Turtle_Ex3.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ ^C

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ checkout
bash: checkout: command not found

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ git checkout

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ git checkout firstbranch
Already on 'firstbranch'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ git checkin master
git: 'checkin' is not a git command. See 'git --help'.

The most similar commands are
        check-ignore
        checkout

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ ls
Oops_Apps1.py    README.md      Turtle_ex2.py
OOPS_APPS2.1.py  Turtle_ex1.py  Turtle_Ex3.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ git merge firstbranch
Already up to date.

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ ls
Oops_Apps1.py    README.md      Turtle_ex2.py
OOPS_APPS2.1.py  Turtle_ex1.py  Turtle_Ex3.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ git master
git: 'master' is not a git command. See 'git --help'.

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ git checkout master
Switched to branch 'master'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git merge firstbranch
Updating 929f0a0..9e507c8
Fast-forward
 OOPS_APPS2.1.py | 29 +++++++++++++++++++++++++++++
 1 file changed, 29 insertions(+)
 create mode 100644 OOPS_APPS2.1.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ls
Oops_Apps1.py    README.md      Turtle_ex2.py
OOPS_APPS2.1.py  Turtle_ex1.py  Turtle_Ex3.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ls
Oops_Apps1.py    README.md      Turtle_ex2.py
OOPS_APPS2.1.py  Turtle_ex1.py  Turtle_Ex3.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ^C

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git checkout firstbranch
Switched to branch 'firstbranch'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ git commit -a -m "modifying OOPS_APPS2.1.py"
On branch firstbranch
nothing to commit, working tree clean

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ cat OOPS_APPS2.1.py
How to Install Anaconda + Python on the Windows.

Download Anaconda @ https://www.anaconda.com/download/

Note: 515MB file. I have already downloaded  & will give you when you need it.
Please inform me when you need it. I will install in your PC.
Installation is process is very simple. Just click on next buttons untill you see finish button.

Once installation procedure is done. Go to Run -> Type 'cmd' -> Press 'Enter' would
launch windows command prompt.

Now type 'python' on the command prompt & press enter would launch the Python.
Now Type
>>>import tkinter -> Press 'Enter'
>>>import turtle -> Press 'Enter'

If you dont see any errors. you are perfectly on the track. Incase if you see any issues,
Please do let me know. I will try to fix the problem & help you up with the setup.

We will end the class here. Thank you for choosing the OOPs_Apps Course & We will learn
fundamentals of developing the Apps by end of the Course.
vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$
$git pull and git fetch


#Today Practice: #######################################################################################


vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ git checkout master
Switched to branch 'master'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git log
commit 9e507c811acd6fe23d986fd201646dd8fb57086d (HEAD -> master, firstbranch)
Author: Narendra <naren4everr@gmail.com>
Date:   Sun Dec 3 18:31:29 2017 +0530

    making changes in firstbranch

commit 929f0a03a8420b59962f199d6a271225cf9bbd38
Author: Narendra <naren4everr@gmail.com>
Date:   Sun Dec 3 18:22:17 2017 +0530

    adding 3 files together

commit b5fb9d0ee16f478e20c303c9954b6876689ad109
Author: Narendra <naren4everr@gmail.com>
Date:   Sun Dec 3 18:12:27 2017 +0530

    adding first commit in local repo

commit 43b478d3421c2585d1a513e205f7c1f9633f92ea (origin/master)
Author: NarendraPutta <31036861+NarendraPutta@users.noreply.github.com>
Date:   Sun Dec 3 15:45:03 2017 +0530

    Create README.md

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ls
Oops_Apps1.py    README.md      Turtle_ex2.py
OOPS_APPS2.1.py  Turtle_ex1.py  Turtle_Ex3.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git status
On branch master
nothing to commit, working tree clean

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git log
commit 9e507c811acd6fe23d986fd201646dd8fb57086d (HEAD -> master, firstbranch)
Author: Narendra <naren4everr@gmail.com>
Date:   Sun Dec 3 18:31:29 2017 +0530

    making changes in firstbranch

commit 929f0a03a8420b59962f199d6a271225cf9bbd38
Author: Narendra <naren4everr@gmail.com>
Date:   Sun Dec 3 18:22:17 2017 +0530

    adding 3 files together

commit b5fb9d0ee16f478e20c303c9954b6876689ad109
Author: Narendra <naren4everr@gmail.com>
Date:   Sun Dec 3 18:12:27 2017 +0530

    adding first commit in local repo

commit 43b478d3421c2585d1a513e205f7c1f9633f92ea (origin/master)
Author: NarendraPutta <31036861+NarendraPutta@users.noreply.github.com>
Date:   Sun Dec 3 15:45:03 2017 +0530

    Create README.md

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ clear

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ it branch firstbranch
bash: it: command not found

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git branch firstbranch
fatal: A branch named 'firstbranch' already exists.

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git create a secondbranch
git: 'create' is not a git command. See 'git --help'.

The most similar command is
        reset

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git branch secondbranch

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git checkout secondbranch
Switched to branch 'secondbranch'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ git add Turtle.txt

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ git commit -m "making changes in firstbranch"
[secondbranch e2c6363] making changes in firstbranch
 1 file changed, 1 insertion(+)
 create mode 100644 Turtle.txt

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ ls
Oops_Apps1.py    README.md   Turtle_ex1.py  Turtle_Ex3.py
OOPS_APPS2.1.py  Turtle.txt  Turtle_ex2.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ git checkout masterbranch
error: pathspec 'masterbranch' did not match any file(s) known to git.

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ git checkout master
Switched to branch 'master'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ls
Oops_Apps1.py    README.md      Turtle_ex2.py
OOPS_APPS2.1.py  Turtle_ex1.py  Turtle_Ex3.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ls
Oops_Apps1.py    README.md      Turtle_ex2.py
OOPS_APPS2.1.py  Turtle_ex1.py  Turtle_Ex3.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git merge firstbranch
Already up to date.

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ls
Oops_Apps1.py    README.md      Turtle_ex2.py
OOPS_APPS2.1.py  Turtle_ex1.py  Turtle_Ex3.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git merge secondbranch
Updating 9e507c8..e2c6363
Fast-forward
 Turtle.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 Turtle.txt

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ls
Oops_Apps1.py    README.md   Turtle_ex1.py  Turtle_Ex3.py
OOPS_APPS2.1.py  Turtle.txt  Turtle_ex2.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git checkout firstbranch
Switched to branch 'firstbranch'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ ls
Oops_Apps1.py    README.md      Turtle_ex2.py
OOPS_APPS2.1.py  Turtle_ex1.py  Turtle_Ex3.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ git checkout secondbranch
Switched to branch 'secondbranch'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ ls
Oops_Apps1.py    README.md   Turtle_ex1.py  Turtle_Ex3.py
OOPS_APPS2.1.py  Turtle.txt  Turtle_ex2.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ git commit -a -m "modified again"
[secondbranch d1c36a8] modified again
 1 file changed, 2 insertions(+), 1 deletion(-)

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ cat Turtle
Turtle.txt     Turtle_ex1.py  Turtle_ex2.py  Turtle_Ex3.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ cat Turtle.txt
Turtles are very good vistualing games.
So, thankyou turtle
vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ git checkout master
Switched to branch 'master'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ls
Oops_Apps1.py    README.md   Turtle_ex1.py  Turtle_Ex3.py
OOPS_APPS2.1.py  Turtle.txt  Turtle_ex2.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ cat Turtle.txt
Turtles are very good vistualing games
vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git checkout firstbranch
Switched to branch 'firstbranch'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (firstbranch)
$ git checkout secondbranch
Switched to branch 'secondbranch'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ ls
Oops_Apps1.py    README.md   Turtle_ex1.py  Turtle_Ex3.py
OOPS_APPS2.1.py  Turtle.txt  Turtle_ex2.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ git add -A

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ git commit -a -m "adding for rebasing"
[secondbranch 990a500] adding for rebasing
 2 files changed, 2 insertions(+)
 create mode 100644 Turtle1 (2).txt
 create mode 100644 Turtle1.txt

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ ls
 Oops_Apps1.py     README.md    Turtle_ex1.py   Turtle_Ex3.py      Turtle1.txt
 OOPS_APPS2.1.py   Turtle.txt   Turtle_ex2.py  'Turtle1 (2).txt'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ git checkout master
Switched to branch 'master'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ls
Oops_Apps1.py    README.md   Turtle_ex1.py  Turtle_Ex3.py
OOPS_APPS2.1.py  Turtle.txt  Turtle_ex2.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git checkout secondbranch
Switched to branch 'secondbranch'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ git rebase master
Current branch secondbranch is up to date.

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ git checkout master
Switched to branch 'master'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git rebase firstbranch
Current branch master is up to date.

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git rebase secondbranch
First, rewinding head to replay your work on top of it...
Fast-forwarded master to secondbranch.

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ls
 Oops_Apps1.py     README.md    Turtle_ex1.py   Turtle_Ex3.py      Turtle1.txt
 OOPS_APPS2.1.py   Turtle.txt   Turtle_ex2.py  'Turtle1 (2).txt'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/vinayb/.ssh/id_rsa):
Created directory '/c/Users/vinayb/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/vinayb/.ssh/id_rsa.
Your public key has been saved in /c/Users/vinayb/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:usbIfPwTpelUj8bD41HHkBjwvyogc92gUQX/8yn9JMg vinayb@BDTBF8FBX1
The key's randomart image is:
+---[RSA 2048]----+
|        o+oo .   |
|        .o. o    |
|       .  o  o   |
|      . . oo. o  |
|       +SX ++.   |
|    o +.* X..* . |
|   o B.+ + +E = .|
|    + =.+ .. . + |
|     o...o.     .|
+----[SHA256]-----+

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ cat /c/Users/vinayb/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAMmwdRwsuOl87Fanf0HSdu6HL0do+bTNDk4H84ejkGVgFlcU3ITTGN83fOTJ9bLeszySDt7pssdPSkX7uK97xWClfsl37M9sNEt7Kew7WPD7K2NpgT9cgCCnnZJaWLFnCxmIj4pJnkW7ftys1dqM39HvGBaRKwRghJN0P7D9VqqI/X3IiGzbvBbhHAivm8r899KGf4wtedweuZuEqpbNKG3XGDw2jluuX+5ebXfuqJCxG9CCJeDl3c2HZ7ki529qG/ivjdp282yu9s2gNDEKm1zAFL27AcLJ1Yrf/gLcQwFgQDSNUMiOLxGOidfegibGVZFh/ejlWLWsB6Zg9Rcqd vinayb@BDTBF8FBX1

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ssh -T git@github.com
The authenticity of host 'github.com (192.30.253.112)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)? y

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ssh -T git@github.com
The authenticity of host 'github.com (192.30.253.113)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,192.30.253.113' (RSA) to the list of known hosts.
Hi NarendraPutta! You've successfully authenticated, but GitHub does not provide shell access.

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git checkout secondbranch
Switched to branch 'secondbranch'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ ls
 Oops_Apps1.py     README.md    Turtle_ex1.py   Turtle_Ex3.py      Turtle1.txt
 OOPS_APPS2.1.py   Turtle.txt   Turtle_ex2.py  'Turtle1 (2).txt'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ git commit -a -m "made some changes"
[secondbranch 244ca8a] made some changes
 2 files changed, 2 deletions(-)
 delete mode 100644 Turtle1 (2).txt
 delete mode 100644 Turtle1.txt

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ ls
Oops_Apps1.py    README.md   Turtle_ex1.py  Turtle_Ex3.py
OOPS_APPS2.1.py  Turtle.txt  Turtle_ex2.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)


vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ add -A
bash: add: command not found

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ git push origin secondbranch
Counting objects: 22, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (19/19), done.
Writing objects: 100% (22/22), 3.87 KiB | 1.29 MiB/s, done.
Total 22 (delta 6), reused 0 (delta 0)
remote: Resolving deltas: 100% (6/6), done.
To https://github.com/NarendraPutta/Python_OOPS_APPs.git
 * [new branch]      secondbranch -> secondbranch

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ ls
Oops_Apps1.py    README.md   Turtle_ex1.py  Turtle_Ex3.py
OOPS_APPS2.1.py  Turtle.txt  Turtle_ex2.py

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (secondbranch)
$ git checkout master
Switched to branch 'master'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ls
 Oops_Apps1.py     README.md    Turtle_ex1.py   Turtle_Ex3.py      Turtle1.txt
 OOPS_APPS2.1.py   Turtle.txt   Turtle_ex2.py  'Turtle1 (2).txt'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ git push origin master
Total 0 (delta 0), reused 0 (delta 0)
To https://github.com/NarendraPutta/Python_OOPS_APPs.git
   43b478d..990a500  master -> master

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ls
 Oops_Apps1.py     README.md    Turtle_ex1.py   Turtle_Ex3.py      Turtle1.txt
 OOPS_APPS2.1.py   Turtle.txt   Turtle_ex2.py  'Turtle1 (2).txt'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ del Turtle1
Turtle1 (2).txt  Turtle1.txt

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ del Turtle1
Turtle1 (2).txt  Turtle1.txt

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ del Turtle1
Turtle1 (2).txt  Turtle1.txt

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ del Turtle
Turtle.txt       Turtle_ex2.py    Turtle1 (2).txt
Turtle_ex1.py    Turtle_Ex3.py    Turtle1.txt

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ del TurtleTurtle
bash: del: command not found

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ del Turtle1 (2).txt
bash: syntax error near unexpected token `('

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ del Turtle1.txt
bash: del: command not found

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ delete Turtle1
Turtle1 (2).txt  Turtle1.txt

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ delete Turtle1.txt
bash: delete: command not found

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ dir
Oops_Apps1.py    README.md   Turtle_ex1.py  Turtle_Ex3.py     Turtle1.txt
OOPS_APPS2.1.py  Turtle.txt  Turtle_ex2.py  Turtle1\ (2).txt

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ pwd
/c/Python_OOPS_APPs_Project

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ cd..
bash: cd..: command not found

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ cd\
> ^C

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$ ls
 Oops_Apps1.py     README.md    Turtle_ex1.py   Turtle_Ex3.py      Turtle1.txt
 OOPS_APPS2.1.py   Turtle.txt   Turtle_ex2.py  'Turtle1 (2).txt'

vinayb@BDTBF8FBX1 MINGW64 /c/Python_OOPS_APPs_Project (master)
$
                                       








