https://ects-cmp.com/course_content/git-basic-commands-concepts/

Info about how the project can be used or shared.
In short, a good README is your project’s user manual!

Copy the following into a README.md and use ctrl + shift + v to see it previewed in VS Code:

### ✅ **Basic Concepts**

1.  **Repository (Repo)**  
    A project folder that Git is tracking. Can be **local** (on your computer) or **remote** (like GitHub, GitLab, etc.).
2.  **Version Control**  
    A system that tracks changes to code over time, letting you revert to previous versions or collaborate with others.
3.  **Commit**  
    A snapshot of your changes. Includes a message describing what was changed.
4.  **Working Directory**  
    The current state of your files on disk.
5.  **Staging Area (Index)**  
    Where you prepare changes before committing. You “stage” files that are ready to be committed.

---

### 📄 **Common Commands**

6.  `git init`  
    Initializes a new Git repository in a folder.
7.  `git clone <repo>`  
    Copies a remote repository to your local machine.
8.  `git push`
    Sends local commits to the remote repository.
    - Add the remote URL (replace with your GitHub repo URL)
      git remote add origin https://github.com/your-username/my-first-repo.git
    - Push to GitHub git push -u origin main
9.  `git pull`  
    Fetches and merges changes from the remote repository to your local one.
10. `git fetch`  
    Downloads changes from the remote, but doesn’t merge them automatically.
11. `git merge`  
    Merges changes from one branch into another.

---

### 🌿 **Branching Concepts**

15. **Branch**  
    A separate line of development. `main` is the default, but you create others to work on features or fixes.
16. `git branch <name>`  
    Creates a new branch.
17. `git checkout <branch>`  
    Switches to another branch.
18. `git checkout -b <name>`  
    Creates and switches to a new branch.
19. **Merge Conflicts**  
    Happens when Git can’t automatically merge changes—requires manual resolution.

---

### 🌍 **Remote Concepts**

20. **Remote Repository**  
    A version of your project stored online, often on platforms like GitHub or GitLab.
21. `git remote add origin <url>`  
    Connects your local repo to a remote one.
22. `git remote -v`  
    Shows the URLs of the remote repositories connected.

---

### 🧼 **Undoing/Inspecting**

23. `git log`  
    Shows the commit history.
24. `git diff`  
    Shows differences between versions or branches.
25. `git restore` or `git checkout`  
    Reverts changes in the working directory.
26. `git reset`  
    Moves the current branch to a different commit. Useful for undoing commits.

---

### 🔧 **Collaboration Concepts**

27. **Forking**  
    Making your own copy of someone else’s repo (especially on GitHub) to make changes without affecting the original.
28. **Pull Request (PR)**  
    A way to propose changes you’ve made in your fork or branch to be merged into another branch or repository.
29. **.gitignore**  
    A file that tells Git which files/folders to ignore (e.g., `node_modules`, `.env` files).
30. **Conflicts**  
    Occur when changes made in two places overlap. Must be resolved before merging.

### 📄 **What is `.gitignore`?**

`.gitignore` is a **special file in a Git repository** that tells Git **which files or folders to ignore** (i.e., not track or include in commits).

---

### ✅ **Why use it?**

To avoid committing:

- Temporary files (e.g., `*.log`, `*.tmp`)
- System files (e.g., `.DS_Store`, `Thumbs.db`)
- Build artifacts (e.g., `dist/`, `node_modules/`)
- Sensitive files (e.g., `.env` with API keys)
- **Large files (github will not allow files over 100mb)**

---

### 🛠️ **How it works:**

You list file names, extensions, or folder paths in `.gitignore`, like this:

```
# Ignore node modulesnode_modules/# Ignore all .log files*.log# Ignore a specific filesecrets.txt
```

Once a file is **tracked by Git**, adding it to `.gitignore` won’t remove it—you’ll need to untrack it with `git rm --cached`.
 