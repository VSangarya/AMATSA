# 📒 Guidelines for contributing to the AMATSA

Kudos if you are reading this page! You are thinking about making your first contribution to this repository. 

This page lists the guidelines to keep in mind while working with files in this repository. As a new project, this is an evolving page. Contributors are welcome to propose standard practices (and suggest improvements!) that we can follow to maintain this repository.

<details>
  <summary><h2>𝌞 Table of Contents</h2></summary>
  <p>
  
  - [Getting Started](#getting-started)
    - [Branching Strategy](#branching-strategy)
    - [Style Guides](#style-guides)
  - [How to report an issue?](#how-to-report-an-issue)
  - [How to create a pull request?](#how-to-create-a-pull-request)
  - [Contributors](#contributors)

  </p>
</details>

## Getting Started
### Branching Strategy
`main` is the latest stable branch that can be deployed on production workloads.

To work on a new feature or bugfix:
1. Create a new branch, say `add-new-icons` from `main`.
2. Make changes to files in `add-new-icons` branch, commit regularly and push the changes to remote.
3. When the task is complete, create a pull request to merge your changes from `add-new-icons` to `main`. 
4. Request feedback from other collaborators on the pull request and incorporate changes if any.
5. Once the review cycle is over, merge the pull request using a **merge-commit**.
6. After successful merge, delete branch `add-new-icons`.

### Style Guides
This project uses Python linter to ensure the code style is uniform and conforms to a well known syntactical style. [Pylint analyser](https://pylint.pycqa.org/en/latest/)

## How to report an issue?
This project uses [GitHub Issues](https://github.com/VSangarya/AMATSA/issues) to track bugs. 

### Before you report an issue
- Check the debugging section to see solutions for frequently encountered problems.
- Attempt to reproduce the bug on the latest release version of the project (bugs are fixed regularly! 😎).

### Submitting a bug report
1. Give a clear and concise summary to the issue.
2. Add labels that seem fit to the issue.
3. A good report has the following sections:
    - Steps to reproduce the problem (if any)
    - Expected behavior
    - Actual behavior
    - Any special case where this issue is encountered (if any)
    - Additional notes (if any)

## How to create a pull request?
- Target your pull request to `main` branch.
- Give a concise summary and a short description of what changed in files that have beed added/modified.
- Link the issue to the pull request if fixing a reported bug.

## Contributors
- Atharv Pandit
- Muhammad Ali Qureshi
- Shivangi Chopra
- Vaishnav Nagarajan
- Vishwesh Sangarya
