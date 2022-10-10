# Project Evaluation

|Notes|Score|Evidence|
|-----|------|---------|
|Video1|N/A| New project| 
|Video2|3|Demo video in README.md| 
|Workload is spread over the whole team (one team member is often Xtimes more productive than the others...but nevertheless, here is a track record that everyone is contributing a lot)|3|[GitHub](https://github.com/VSangarya/AMATSA/graphs/contributors)|
|Number of commits|3|[GitHub](https://github.com/VSangarya/AMATSA/pulse)|
|Number of commits: by different people|3|[GitHub](https://github.com/VSangarya/AMATSA/pulse)|
|Issues reports: there are **many**|3|[GitHub](https://github.com/VSangarya/AMATSA/issues)|
|Issues are being closed|3|[GitHub](https://github.com/VSangarya/AMATSA/issues?q=is%3Aissue+is%3Aclosed)|
|DOI badge: exists|3|[README.md](https://github.com/VSangarya/AMATSA#-amatsa)|
|Docs: doco generated, format not ugly|3|docs directory|
|Docs: what: point descriptions of each class/function (in isolation)|3|All modules, Files, Classes, Methods have doc-strings|
|Docs: how: for common use cases X,Y,Z mini-tutorials showing worked examples on how to do X,Y,Z|3|[README.md](https://github.com/VSangarya/AMATSA#-amatsa)|
|Docs: why: docs tell a story, motivate the whole thing, deliver a punchline that makes you want to rush out and use the thing|3|[README.md](https://github.com/VSangarya/AMATSA#-amatsa)|
|Docs: short video, animated, hosted on your repo. That convinces people why they want to work on your code.|3|[README.md](https://github.com/VSangarya/AMATSA#-amatsa)|
|Use of version control tools|3|Git Version Control|
|Use of style checkers|3|Configured [pylintrc](https://github.com/VSangarya/AMATSA/blob/main/pylintrc) with Google's Python style-guide|
|Use of code formatters.|3|.vscode [dir](https://github.com/VSangarya/AMATSA/blob/main/.vscode/settings.json) with formatter settings used by every dev|
|Use of syntax checkers.|3| pylint runs on every pull request to check this.|
|Use of code coverage |3|Coverage reports are generated in [build](https://github.com/VSangarya/AMATSA/blob/main/.github/workflows/build.yml) GitHub Action|
|Other automated analysis tools|3|[Codacy](https://app.codacy.com/gh/VSangarya/AMATSA/dashboard?utm_source=github.com&utm_medium=referral&utm_content=VSangarya/AMATSA&utm_campaign=Badge_Grade) for static code analysis|
|Test cases exist|3|Tests are written using Pytest [here](https://github.com/VSangarya/AMATSA/tree/main/tests).|
|Test cases are routinely executed|3|Tests are run every pull request by GitHub Actions|
|The files CONTRIBUTING.md lists coding standards and lots of tips on how to extend the system without screwing things up|3|Info on style guide, branching strategies, how to raise a PR etc.|
|Issues are discussed before they are closed|3|GitHub Issue and PR comments|
|Chat channel: exists|3|[WhatsApp](Screenshot%202022-10-09%20at%2017.43.53.png)|
|Test cases: a large proportion of the issues related to handling failing cases.|3|Bugs reported: Issue 27, 35, 10|
|Evidence that the whole team is using the same tools: everyone can get to all tools and files|3|[dev environment setup](https://github.com/VSangarya/AMATSA#--developer-environment-setup), .vscode [dir](https://github.com/VSangarya/AMATSA/blob/main/.vscode/settings.json) for style configuration|
|Evidence that the whole team is using the same tools (e.g. config files in the repo, updated by lots of different people)|2|Tools/Style and Style checkers were setup as the first commit. All devs pulled these settings. Hence, no further changes were made.|
|Evidence that the whole team is using the same tools (e.g. tutor can ask anyone to share screen, they demonstrate the system running on their computer)|3|Code is deployed on every developer's PC|
|Evidence that the members of the team are working across multiple places in the code base|3|Every dev has worked on writing code, tests, documentation. Evidence in commits.|
|Short release cycles (hard to see in short projects) project members are committing often enough so that everyone can get your work|3|[Git branching strategy](https://github.com/VSangarya/AMATSA/blob/main/CONTRIBUTING.md#branching-strategy) and frequent [pull-requests](https://github.com/VSangarya/AMATSA/pulls?q=is%3Apr+is%3Aclosed)|
|Does your website and documentation provide a clear, high-level overview of your software?|3|[README.md](https://github.com/VSangarya/AMATSA/blob/main/README.md)|
|Does your website and documentation clearly describe the type of user who should use your software?|3| [README.md](https://github.com/VSangarya/AMATSA/blob/main/README.md) Yes, primary type of users are System Admins and describes the usecases as well |
|Do you publish case studies to show how your software has been used by yourself and others?|1|Have shown the use cases, how it can be setup and how it can be improved|
|Is the name of your project/software unique?|3|Yes, no other GitHub projects or other software with the same name exist|
|Is your project/software name free from trademark violations?|3|Yes, no prior software, product, business, design or corporation with the name AMATSA exsists. Verified using Trademark Electronic Search System (TESS).|
|Is your software available as a package that can be deployed without building it?|3|[Github](https://github.com/VSangarya/AMATSA/blob/main/INSTALL.md#-client) Yes, amasta-client can be installed without a build on any client to set up a period scheduled task to send the data.|
|Is your software available for free?|3|Yes, the software is available for free|
|Is your source code publicly available to download, either as a downloadable bundle or via access to a source code repository?|3|Can be downloaded or cloned through Github |
|Is your software hosted in an established, third-party repository likeGitHub (https://github.com), BitBucket (https://bitbucket.org),LaunchPad (https://launchpad.net) orSourceForge (https://sourceforge.net)?|3|Yes, it is hosted on GitHub|
|Is your documentation clearly available on your website or within your software?|3|All required documentation set up via the repositories readme, installation guides and setup steps.|
|Does your documentation include a "quick start" guide, that provides a short overview of how to use your software with some basic examples of use?|3|[GitHub](https://github.com/VSangarya/AMATSA/blob/main/INSTALL.md#-client) is available for installation and usage guides.|
|If you provide more extensive documentation, does this provide clear, step-by-step instructions on how to deploy and use your software?|2|No additonal documentation present. Installation and set up instructions provide all required details.|
|Do you provide a comprehensive guide to all your software’s commands, functions and options?|2|All client functions commands explaied in installation guide. Classes and methods in source code give an overview of the codes functionality.|
|Do you provide troubleshooting information that describes the symptoms and step-by-step solutions for problems and error messages?|0|Not present in the repository|
|If your software can be used as a library, package or service by other software, do you provide comprehensive API documentation?|N/A|The software does not provide API documentation and cannot be used a package for other software at present|
|Do you store your documentation under revision control with your source code?|3|[Github releases](https://github.com/VSangarya/AMATSA/releases)|
|Do you publish your release history e.g. release data, version numbers, key features of each release etc. on your web site or in your documentation?|3|[Github releases](https://github.com/VSangarya/AMATSA/releases)|
|Does your software describe how a user can get help with using your software?|3|[Github](https://github.com/VSangarya/AMATSA#readme) and [Issues](https://github.com/VSangarya/AMATSA/issues) E-mail address for contact is provided for help regarding the software. Installation and setup guides assist users in setting up and using the software as well|
|Does your website and documentation describe what support, if any, you provide to users and developers?|3|[Github](https://github.com/VSangarya/AMATSA#readme)  E-mail address for contact is provided. Issues tab can used for potential questions and help which will be addressed by one of the project developers|
|Does your project have an e-mail address or forum that is solely for supporting users?|3|[Github](https://github.com/VSangarya/AMATSA#readme) and [Issues](https://github.com/VSangarya/AMATSA/issues) E-mail address for contact is provided. Issues tab on the repository can be used for help regarding the software|
Are e-mails to your support e-mail address received by more than one person?|3 |Yes all members have access to respective support emails|
Does your project have a ticketing system to manage bug reports and feature requests?|3|Yes ([Issues](https://github.com/VSangarya/AMATSA/issues)  section in GitHub)|
Is your project's ticketing system publicly visible to your users, so they can view bug reports and feature requests?|3|	Yes, it is publicly available|
Software’s architecture and design is modular | 3 | Yes - There are many seperate modules for different functionality in our repository| 
Software uses an accepted coding standard or convention | 3 | Yes, coding standards are followed | 
Software allows data to be imported and exported using open data formats | --- | --- | 
Software allows communications using open communications protocols | 3 | Yes, our website uses HTTP to communicate. | 
Software cross-platform compatible | 3 | Yes - Works on Windows, Mac, Ubuntu--- | 
Software adhere to appropriate accessibility conventions or standards | --- | --- | 
Documentation adheres to appropriate accessibility conventions or standards | 3 | yes  | 
Source Code in a repository under revision control | 3 | Using git |
Each source code releases a snapshot of the repository | 3 | Yes, we have multipe releases.| 
Releases are tagged in the repository | 3 | --- | 
There is a branch of the repository that is always stable | 3 | Main branch is always stable | 
Back-up your repository | 3 | Yes, using git clone | 
Provide publicly available instructions for building the software from the source code | 3 | --- | 
Build, or package, the software using an automated tool | --- | --- | 
Provide publicly-available instructions for deploying the software | 3 | [README.md](https://github.com/VSangarya/AMATSA#-amatsa) | 
Documentation list all third-party dependencies | 3 | [requirements.txt](https://github.com/VSangarya/AMATSA/blob/main/requirements.txt) | 
Documentation lists the version number for all third-party dependencies | 3 | [requirements.txt](https://github.com/VSangarya/AMATSA/blob/main/requirements.txt)| 
Software list the web address, and licences for all third-party dependencies and say whether the dependencies are mandatory or optional | 3 | All can be downloaded using pip | 
Download dependencies using a dependency management tool or package manager | 3 | All can be downloaded using pip | 
Tests that can be run after your software has been built or deployed to show whether the build or deployment has been successful | 3 | 'tests' folder | 
Automated test suite for your software | 3 | [Github Workflows](https://github.com/VSangarya/AMATSA/blob/main/.github/workflows/build.yml) | 
Framework to periodically (e.g. nightly) run your tests on the latest version of the source code | 0 | We run tests when a branch is being merged to main | 
Using continuous integration, automatically running tests whenever changes are made to your source code | 3 | https://github.com/VSangarya/AMATSA/blob/main/.github/workflows/build.yml | 
Test results publicly visible | 3 | [Builds on a pull request](https://github.com/VSangarya/AMATSA/pulls) | 
Manually-run tests documented | --- | --- | 
Project has resources (e.g. blog, Twitter, RSS feed, Facebook page, wiki, mailing list) that are regularly updated with information about your software | 3 | All updates on the readme [README.md](https://github.com/VSangarya/AMATSA#-amatsa) | 
Documentation states how many projects and users are associated with your project | --- | --- | 
Provide success stories on your website | 0 | Software not yet used publicly | 
Listing the important partners and collaborators in your website | --- | --- | 
Listing the project's publications on our website or link to a resource where these are available | 0 | No publications | 
Listing third-party publications that refer to the software on our website or link to a resource where these are available | 0 | No publications | 
Users can subscribe to notifications to changes to your source code repository | 3 | Software is on Github | 
Since the software is developed as an open source project (and, not just a project developing open source software), do you have a governance model | 3 | 2 approvers required to merge into main | 
Do you accept contributions (e.g. bug fixes, enhancements, documentation updates, tutorials) from people who are not part of your project? | 3 | Software is open source, other collaborators can create a pull request for a change | 
Do you have a contributions policy | 3 | [CONTRIBUTING.md](../CONTRIBUTING.md) | 
Is your contributions' policy publicly available? | 3 | [CONTRIBUTING.md](../CONTRIBUTING.md) | 
Do contributors keep the copyright/IP of their contributions | 3 | Commits are public | 
Website and documentation clearly states the copyright owners of your software and documentation | 3 | [README.md](https://github.com/VSangarya/AMATSA#-amatsa) | 
Does each of your source code files include a copyright statement | 0 |  | 
The website and documentation clearly state the licence of your software | 3 | [LICENSE](../LICENSE) | 
Software released under an open source licence | 3 | [LICENSE](../LICENSE) | 
Software released under an OSI-approved open-source licence | 3 | [LICENSE](../LICENSE) | 
Source code files include a licence header | 0 |  | 
Do you have a recommended citation for your software | 3 | Zenodo Badge in [README]((https://github.com/VSangarya/AMATSA#-amatsa)) | 
Documentation includes a project roadmap (a list of project and development milestones for the next 3, 6 months) | 2 | Enhancements in [README]((https://github.com/VSangarya/AMATSA#-amatsa)) | 
Documentation describe how the project is funded, and the period over which funding is guaranteed? | 3 | We used free tools hence no funding required | 
Do you make timely announcements of the deprecation of components, APIs, etc. | 3 |  | 
