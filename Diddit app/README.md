# Diddit



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:
=======

# diddit frontend

<div>
  <h1 align="center">Getting Started with Flutter 🚀 </h1>
  <strong>
    Generated with ❤️ from Diddit's frontend team
  </strong>
  <p>
    This is the documentation of Flutter Applications.
    It contains all the information you need to get started with
    and make changes to your App
  </p>
</div>


### Table of Contents
- [Install Flutter](#install-flutter)
- [Download VS Code](#download-vs-code)
- [Enable Flutter and Dart](#enable-flutter-and-dart)
- [Clone Our Repository](#clone-our-repository)
- [Our File Structure](#our-file-structure)
- [Push Changes to Gitlab](#push-changes-to-gitlab)
- [Helpful Commands](#helpful-commands)
- [Running the Code](#running-the-code)
- [Pull Code](#pull-code)
- [Dhiwise Libraries and tools used](#dhiwise-libraries-and-tools-used)
- [Dhiwise Support](#dhiwise-support)
- [Dhiwise Image Assets](#dhiwise-image-assets)
- [Requirements for Running Flask Endpoints] (#requirements-for-running-flask-endpoints)

### Install Flutter
First, download **Flutter**: https://docs.flutter.dev/get-started/install using the instructions appropriate for your device.

### Download VS Code
Then, download **VS Code** onto your device: https://code.visualstudio.com/ 

### Enable Flutter and Dart
Open VS Code and go to **Extensions** (on the left, there will be an icon with four squares; if you hover over it, it will say Extensions). 
Type **Flutter** in the extensions search field, and click on the install button. This should automatically install the **Dart** extension as well, but search up Dart in the search field to ensure that it is also installed.

### Clone Our Repository
Type the command: **git clone https://gitlab.com/pl246901/diddit.git**

This should clone the repository from our gitlab.

### Our File Structure
After successful build, your application structure should look like this:
>>>>>>> Stashed changes

```
cd existing_repo
git remote add origin https://gitlab.com/pl246901/diddit.git
git branch -M main
git push -uf origin main
```

<<<<<<< Updated upstream
## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.com/pl246901/diddit/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Automatically merge when pipeline succeeds](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***
=======
### Push Changes to Gitlab
Add a remote repository using the command: **git remote add ORIGIN_NAME https://gitlab.com/pl246901/diddit.git**

Then, to put your code onto the staging area to get it ready to be pushed to gitlab, run: **git add -u**

To check the status of the working directory/staging area and see what changes have been made, run: **git status**

Now, to make a new branch and go to it, use: **git checkout -b BRANCH_NAME**

Or, use:
  **git branch BRANCH_NAME** (to create the branch)
  **git switch BRANCH_NAME** (to go to that branch)

Both these commands have the same outcome.

To push to a branch, run the command: **git push gitlaborigin BRANCH_NAME**

### Helpful Commands
If you need to see all remote repositories, use: **git remote show**

If you need to remove a remote repository, use: **git remote remove ORIGIN_NAME**

If you need to see all branches, use: **git branch**

If you need to remove a branch, use: **git branch -D BRANCH_NAME**

### Running the Code
Select **Run** from the upper left hand corner of your VS Code window, and select **Start Debugging** from the dropdown menu.

Or, to simply view the app without debugging, select a device from the lower right corner of the blue menu at the bottom of your screen (which, at the start, should say **No Device**)

### Pull Code
git fetch origin branch
git pull origin branch

Note: In the **package_config.json** file in the **.dart_tool** folder, everyone has different file paths, so make sure you change yours to make the code work!!

### Dhiwise Libraries and tools used

- get - State management
  https://pub.dev/packages/get
- connectivity_plus - For status of network connectivity
  https://pub.dev/packages/connectivity_plus
- pull_to_refresh - For list functionalities
  https://pub.dev/packages/pull_to_refresh
- cupertino_icons - For iOS icons
  https://pub.dev/packages/cupertino_icons
- shared_preferences - Provide persistent storage for simple data
  https://pub.dev/packages/shared_preferences
- cached_network_image - For storing internet image into cache
  https://pub.dev/packages/cached_network_image
    
### Dhiwise Support
If you have problems or questions go to our Discord channel, we will then try to help you as quickly as possible: https://discord.com/invite/rFMnCG5MZ7

### Dhiwise Image Assets
We were unable to find Images, Please add manually to ```project/assets``` and replace image_not_found Image constant with original file 
>>>>>>> Stashed changes

# Editing this README

<<<<<<< Updated upstream
When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thank you to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
=======
### Requirements for Running Flask Endpoints
To install the necessary packages on windows, type in the VS Code terminal: 

**py -m pip install --upgrade pip** UPDATES PIP

**py -m pip install Flask** INSTALLS FLASK

**py -m pip install PyJWT** INSTALLS JWT

To install the necessary packages on mac, use:

**pip3 install Flask

**pip3 install PyJWT

Once these are all installed, you can run the file using **python return_jwt.py**. Endpoints will be located at *http://127.0.0.1:5000/login* and *http://127.0.0.1:5000/refresh*.

Requirements for running the mock Flask service return_jwt.py are as follows:

Server side packages:
- Flask (Flask, request, jsonify, make_response)
- uuid
- werkzeug.security (generate_password_hash, check_password_hash)
- jwt
- datetime (datetime, timedelta)
- functools (wraps)

**UI Client Side:**
The client side of the mock connection will use HTTP POST to send fake form data containing a username and password
to the service, which will return a JSON Web Token (JWT) to be used for future authentication. The terminal command 
to send this form is as follows:
$ curl -X POST -H "Content-type: multipart/form-data"  -F "email=user@diddit.com" -F "password=password" "localhost:5000/login"

* localhost may need to be changed to the IP address of the device running the service, in this case 127.0.0.1
