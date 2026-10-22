# Submitting Assignments with Classroom 50

Complete instructions for submitting programming assignments in COMP 354 and COMP 454.

> **If you took this course before Fall 2026:** we used GitHub Classroom, which GitHub shut down in August 2026. We now use **Classroom 50**, an open-source replacement from the team behind Harvard's CS50. The workflow is much the same. The main differences are that you accept assignments at **classroom50.org**, and your grade arrives as a **Release** on your repository.

## Overview

Assignments are distributed and submitted through **Classroom 50**, which stores everything in GitHub. Each assignment is **autograded** with input/output test cases. When you push your code, the tests run and a scored result appears on your repository within a minute or two.

**You do not need to install anything.** Everything below can be done in a web browser.

Your classroom is one of:

| Course | Classroom |
|---|---|
| COMP 354 | `comp354-f26` |
| COMP 454 | `comp454-f26` |

## Accepting an assignment

**Click the assignment link in Canvas.** Every assignment in Canvas carries an accept link. That is the only step.

1. Open the assignment in Canvas and click the accept link
2. Sign in with GitHub if you are not already, and authorize the app
3. Click **Accept**

That creates a private repository for you, copied from the starter code:

```
RueDeFoix/<classroom>-<assignment>-<yourusername>
```

for example `RueDeFoix/comp354-f26-stockprofit-yourusername`. Grading is already wired up. There is nothing to configure.

The first time you accept anything, GitHub also asks you to join the **RueDeFoix** organization. Accept that invitation, or your repository cannot be created.

**No link handy?** Go to **https://classroom50.org**, sign in with GitHub, open the **RueDeFoix** organization listed under Student, pick your classroom, and choose the assignment from the list.

Assignments appear on their release date, not before. The schedule is on the syllabus.

### Assignment names

**COMP 354:** `stockprofit`, `jobscheduling`, `mergesort`, `longestunimodalsubs`

**COMP 454:** `dfa3`, `re2c-lexer`, `bison-json-parser`, `busybeaver`

## Option 1: GitHub Codespaces (recommended)

A complete VS Code environment in your browser. Nothing to install, and it works from any computer, including a lab machine or a Chromebook.

**Open it:**

1. Go to your assignment repository on GitHub
2. Click the green **Code** button
3. Select the **Codespaces** tab
4. Click **Create codespace on main**
5. Wait under a minute for it to load

You now have a full editor, a terminal, and Python already installed.

**Work on it:**

Edit files in the editor. Use the built-in terminal (**Terminal > New Terminal**) to test:

```bash
echo "7 1 5 3 6 4" | python3 stockprofit.py
```

**Submit:**

1. Click the **Source Control** icon in the left sidebar, or press `Ctrl+Shift+G`
2. Click the `+` next to each changed file to stage it
3. Type a short message in the box
4. Click **Commit**
5. Click **Sync Changes** to push

Pushing is what triggers grading.

**Two things to know about Codespaces:**

- It **stops after 30 minutes of inactivity**, which is fine. Your files persist and you can reopen it. But commit and push before you walk away, because uncommitted work in a deleted codespace is gone.
- Every GitHub account includes a free monthly allowance of Codespaces hours, which is far more than these assignments need. Delete codespaces you have finished with, from https://github.com/codespaces, to stay well inside it.

## Option 2: Work on your own computer

Choose this if you prefer your own editor and setup, or want to work offline.

```bash
git clone https://github.com/RueDeFoix/<classroom>-<assignment>-<yourusername>.git
cd <classroom>-<assignment>-<yourusername>
```

Edit with whatever you like. Test locally:

```bash
echo "7 1 5 3 6 4" | python3 stockprofit.py
python3 stockprofit.py < test_input.txt
```

Submit:

```bash
git add .
git commit -m "Describe your changes"
git push
```

## Option 3: The command line, start to finish

If you prefer to stay in a terminal, there is a CLI that does everything, including accepting the assignment, so you never need the website. Entirely optional.

**One-time setup:**

```bash
# 1. Install the GitHub CLI (https://cli.github.com/)
brew install gh                 # macOS
sudo apt install gh             # Debian/Ubuntu
winget install GitHub.cli       # Windows

# 2. Install the student extension and log in
gh extension install foundation50/gh-student
gh student login
```

**Per assignment:**

```bash
gh student accept RueDeFoix comp354-f26 stockprofit
git clone https://github.com/RueDeFoix/comp354-f26-stockprofit-yourusername.git
cd comp354-f26-stockprofit-yourusername
# ... edit and test ...
gh student submit
```

`gh student submit` does the same job as commit and push, and additionally pulls down any fixes the instructor has made to the starter files. That last part is the one thing the CLI gives you that the other two options do not.

`gh student whoami` confirms which account you are signed in as. `gh student accept` also handles the organization invitation for you, so you do not need to accept that separately on github.com.

## Seeing your grade

A minute or two after you push, your score appears as a **Release** on your repository.

1. Open your repository on GitHub
2. Find **Releases** in the right-hand sidebar
3. Open the most recent one

It lists every test, whether it passed, and the points awarded.

For the raw output, including error messages when your program crashes, open the **Actions** tab and click the most recent run. This is the first place to look when a test fails and you cannot see why.

**Submit as often as you like.** Every push is graded and only the latest one counts. There is no penalty for submitting early and often, and it is the best way to catch formatting problems before the deadline.

### Feedback pull request

Every repository has one long-lived pull request titled **Feedback**. That is where your instructor leaves inline comments on your code. **Do not close or merge it.** Check it after each assignment is graded.

## Getting the output format right

Most failed tests are formatting, not logic. Your output must match exactly:

- No extra spaces or blank lines
- No debugging output
- No prompts such as `Enter input:`
- Correct capitalisation; if the answer should be `VALID`, then `valid` fails

Always run your own test before submitting.

## Tips

### Do

- Test before submitting
- Read the assignment README for the exact input and output format
- Check the Release afterwards to confirm your score
- Submit repeatedly; only the latest counts
- Start early, so a formatting problem does not become a missed deadline

### Do not

- Modify files you were not asked to modify
- Rename files or change the folder structure
- Add extra printing or prompts
- Leave debugging output in your submission
- Close or merge the Feedback pull request
- Wait until the last minute

### Common mistakes

1. **Extra output.** Remove every `print()` except the required answer.
2. **Wrong format.** Match spacing, line breaks, and capitalisation exactly.
3. **Renamed file.** The autograder runs a specific filename; keep it.
4. **Committed but not pushed.** In Codespaces, remember **Sync Changes**.
5. **Misread the input format.** Read the README before writing code.

## Troubleshooting

**The assignment is not listed on classroom50.org**
It may not have been released yet; check the syllabus for the date. Otherwise confirm you are signed in with the GitHub account you gave your instructor, and that you have accepted the invitation to the RueDeFoix organization.

**No Release appeared after pushing**
Wait two minutes and refresh. If there is still nothing, open the **Actions** tab; a failed run there explains why.

**Tests fail although the code works locally**
Almost always formatting. Look for trailing spaces, a missing or extra final newline, leftover debugging output, or Windows versus Linux line endings.

**"Permission denied" when cloning**
Accept the assignment first, and confirm you are signed into the right GitHub account.

**The codespace will not start**
Refresh, check https://www.githubstatus.com, or create a new one.

**"Nothing to commit"**
Save your files first. In Codespaces, check that changes appear in the Source Control panel.

## Getting help

1. Read the assignment README
2. Read the failing test's output in the **Actions** tab
3. Ask on the course discussion forum
4. Come to office hours

## Resources

- **Classroom 50:** https://classroom50.org
- **Student guide:** https://github.com/foundation50/classroom50/wiki/Web-Student-Guide
- **Codespaces:** https://docs.github.com/en/codespaces
- **Git basics:** https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control

---

*Last updated: August 2026 (migrated from GitHub Classroom to Classroom 50)*
