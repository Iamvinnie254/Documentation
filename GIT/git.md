# 📘 Git and GitHub Documentation

## 📌 Table of Contents

- [📘 Git and GitHub Documentation](#-git-and-github-documentation)
  - [📌 Table of Contents](#-table-of-contents)
  - [1. What is Git?](#1-what-is-git)
    - [✅ Key Features](#-key-features)
  - [2. What is GitHub?](#2-what-is-github)
  - [3. Setting Up Git](#3-setting-up-git)
    - [🔧 Install Git](#-install-git)
    - [🛠️ Configure Git](#️-configure-git)
  - [4. Initializing a Git Repository](#4-initializing-a-git-repository)
    - [Create a repository on Github](#create-a-repository-on-github)
  - [5. Git basics: Key commands](#5-git-basics-key-commands)
  - [6. Collaboration on Github](#6-collaboration-on-github)
    - [Ways to collaborate](#ways-to-collaborate)
    - [Typical workflow](#typical-workflow)
  - [Pros and Cons of Collaboration with Git/GitHub](#pros-and-cons-of-collaboration-with-gitgithub)
    - [Pros](#pros)
    - [Cons](#cons)
  - [7. Github Actions](#7-github-actions)
    - [🧩 What are GitHub Actions?](#-what-are-github-actions)
      - [GitHub Actions is a CI/CD tool that lets you](#github-actions-is-a-cicd-tool-that-lets-you)
    - [📁 Components](#-components)
  - [8. Project Contributions Using GitHub](#8-project-contributions-using-github)
    - [🙌 How to Contribute](#-how-to-contribute)
  - [✅ Good Practices](#-good-practices)
  - [9. Conclusion](#9-conclusion)

---

## 1. What is Git?

**Git** is a free, open-source **distributed version control system** that allows multiple developers to work on the same codebase simultaneously without overwriting each other’s changes. Git helps track changes, manage branches, and merge code efficiently.

### ✅ Key Features

- Distributed architecture
- Version tracking
- Branching and merging
- Local and remote repositories

---

## 2. What is GitHub?

**GitHub** is a cloud-based platform built on top of Git that offers:

- A **web-based interface** to manage Git repositories
- **Collaboration tools** like pull requests, issues, and projects
- **CI/CD pipelines** through GitHub Actions

---

## 3. Setting Up Git

### 🔧 Install Git

- **Windows/macOS/Linux**: [https://git-scm.com/downloads](https://git-scm.com/downloads)

### 🛠️ Configure Git

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

```

## 4. Initializing a Git Repository

### Create a repository on Github

- On github navigate to create a new repository and name it accordingly

- on the local machine in the terminal of your choice [Preferrably VsCode Terminal] navigate to the project folder and run these commands.

```bash

1. git init -> to initialize a local repository
2. git add . -> to stage all files for committing
3. git commit -m "commit message" -> to commit all the file and/or changes
4. git branch -m main -> to switch to branch main. This is different from checking out from a branch
5. git remote add origin https://github.com/your-username/your-repo.git -> to link your local repo to the github repo
6. git push -u origin main -> to push changes or files to github
 
```

- Later changes are commited to github following these commands

```bash
git add .
git commit -m "commit message"
git push origin main/master/dev -> depending on which branch you are working on

```

## 5. Git basics: Key commands

- `git status` check status
- `git add <file>` or `git add .` Add files
- `git commit -m "message"` Commit changes
- `git log` View logs
- `git branch` Check which branch you are on
- `git branch new-feature` Create branch
- `git checkout new-feature` Switch to a new branch
- `git merge new-feature` Merge branches
- `git pull origin main` Pull latest changes
- `git push origin main` Push changes

## 6. Collaboration on Github

### Ways to collaborate

- Forking: Clone a repo and suggest changes via pull request.

- Cloning: Download a repo locally to contribute directly.

- Pull Requests (PRs): Suggest code changes for review.

- Branches: Create isolated branches for features or bug fixes.

- Issues: Track bugs or request features.

- Projects: Organize tasks and timelines.

### Typical workflow

1. Fork or clone a repo

2. Create a feature branch

3. Make changes and commit

4. Push to your fork/branch

5. Create a pull request

6. Review and merge

## Pros and Cons of Collaboration with Git/GitHub

### Pros

- 🚀 Easy to track changes and versions

- 🤝 Multiple contributors can work in parallel

- 🛠️ Built-in code review and CI/CD

- 🌍 Community and open-source friendly

### Cons

- 🔄 Merge conflicts can be complex

- 🧠 Requires understanding of Git concepts

- 🔒 Private repos are limited on free plans

- 🐛 Misuse of branches or PRs can lead to issues

## 7. Github Actions

### 🧩 What are GitHub Actions?

#### GitHub Actions is a CI/CD tool that lets you

- Automate testing

- Deploy apps

- Run scheduled tasks

- Manage issues and PRs

### 📁 Components

- Workflows: Automation defined in YAML files

- Jobs: Set of steps in a workflow

- Runners: Machines that run your jobs

- Steps: Individual tasks like install, test, deploy

## 8. Project Contributions Using GitHub

### 🙌 How to Contribute

- Fork the project

- Clone your fork:

```bash
git clone https://github.com/your-username/project-name.git
```

- Create a new branch:

```bash

git checkout -b feature-branch

```

1. Make changes, commit and push:

```bash

git add .
git commit -m "Add new feature"
git push origin feature-branch
```

- Create a pull request from Github interface

- Wait for review and feedback

## ✅ Good Practices

- Write clear commit messages

- Follow coding conventions

- Always sync with the main branch

- Add tests where needed

- Respect the CONTRIBUTING.md file if present

## 9. Conclusion

Git and GitHub are essential tools for modern software development. They offer robust version control, team collaboration, and automated workflows through GitHub Actions.

Whether you're working solo or on a team, understanding and utilizing these tools effectively will significantly boost productivity and code quality
