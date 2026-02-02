# Submitting Assignments with GitHub Classroom

This document provides complete instructions for submitting programming assignments using GitHub Classroom.

## Overview

Assignments are distributed and submitted using **GitHub Classroom**. Each assignment will be **autograded** using input/output test cases. When you push your code to GitHub, automated tests run and your grade is calculated immediately.

## Two Ways to Work on Assignments

You have two options for working on your assignments:

### Option 1: Clone to Your Computer (Traditional)

This approach gives you full control over your development environment.

**Steps:**
1. Accept the assignment link provided by your instructor
2. This creates a private repository for you (e.g., `assignment-name-yourusername`)
3. Clone the repository to your computer:
   ```bash
   git clone https://github.com/RueDeFoix/assignment-name-yourusername.git
   ```
4. Work on the assignment using your favorite editor/IDE
5. Test your code locally before pushing
6. Commit and push your changes:
   ```bash
   git add .
   git commit -m "Completed assignment"
   git push
   ```

**Advantages:**
- Use your preferred development environment (VS Code, PyCharm, vim, etc.)
- Full access to debugging tools
- Works offline
- Better for larger projects

### Option 2: GitHub Codespaces (Cloud-Based)

GitHub Codespaces provides a complete development environment in your browser - no installation required!

**Steps:**
1. Accept the assignment link provided by your instructor
2. Go to your assignment repository on GitHub
3. Click the green **Code** button
4. Select the **Codespaces** tab
5. Click **Create codespace on main**
6. Wait for the environment to load (usually under a minute)
7. You now have a full VS Code editor in your browser!
8. Edit files, run tests, and commit directly from Codespaces

**Advantages:**
- No local setup required
- Works from any computer with a browser
- Pre-configured with necessary tools (Python, Bison, Flex, etc.)
- Automatic git integration
- Great for quick edits or when using shared computers

**To commit from Codespaces:**
1. Make your changes in the editor
2. Click the Source Control icon in the left sidebar (or press `Ctrl+Shift+G`)
3. Stage your changes by clicking the `+` next to modified files
4. Enter a commit message
5. Click the checkmark to commit
6. Click "Sync Changes" to push to GitHub

## Step-by-Step Submission Process

### 1. Accept the Assignment

- Click the assignment invitation link provided by your instructor
- If prompted, authorize GitHub Classroom
- Click "Accept this assignment"
- Wait for your repository to be created
- Click the repository link to view it

### 2. Work on Your Assignment

**Using your local computer:**
```bash
# Clone the repository
git clone <your-repository-url>
cd <repository-name>

# Edit the required files (e.g., program.py)
# Test your solution locally
python3 program.py < test_input.txt

# Or use echo for quick tests
echo "input data" | python3 program.py
```

**Using Codespaces:**
- Open the repository on GitHub
- Click Code > Codespaces > Create codespace
- Edit files directly in the browser-based VS Code
- Use the integrated terminal to run tests

### 3. Test Your Solution

Before submitting, always test your code locally:

```bash
# Example for Python assignments
echo "test input" | python3 program.py

# Example for compiled assignments (C, Bison, etc.)
make
echo "test input" | ./program
```

**Important:** Your output must match the expected format **exactly**:
- No extra spaces or newlines
- No debug print statements
- No prompts like "Enter input:"
- Case-sensitive (if output should be `VALID`, don't write `valid`)

### 4. Commit and Push

**From command line:**
```bash
git add <filename>
git commit -m "Describe your changes"
git push
```

**From Codespaces:**
Use the Source Control panel (Ctrl+Shift+G) to stage, commit, and sync.

### 5. Verify Autograding Results

After pushing:
1. Go to your repository on GitHub
2. Click the **Actions** tab
3. Click on the most recent workflow run
4. View the results of each test case
5. Green checkmarks = passed, Red X = failed

You can also see your grade in the GitHub Classroom dashboard.

## Important Tips

### Do's

- **DO** test your code locally before pushing
- **DO** read the assignment README carefully for exact I/O format
- **DO** check the Actions tab after pushing to see test results
- **DO** push multiple times - only your latest commit is graded
- **DO** start early to have time for debugging

### Don'ts

- **DON'T** modify files you weren't asked to modify
- **DON'T** change filenames or folder structure
- **DON'T** add extra print statements or prompts
- **DON'T** leave debug output in your final submission
- **DON'T** wait until the last minute to submit

### Common Mistakes

1. **Extra output:** Remove all `print()` statements except the required output
2. **Wrong format:** Match the exact format specified (spaces, newlines, case)
3. **Wrong filename:** Don't rename the template file
4. **Not pushing:** Remember to `git push` after committing!
5. **Testing on wrong input:** Make sure you understand the input format

## Troubleshooting

### "Permission denied" when cloning
- Make sure you've accepted the assignment first
- Verify you're using the correct repository URL
- Check that you're logged into the correct GitHub account

### Tests fail but code works locally
- Check for trailing whitespace or extra newlines
- Ensure output format matches exactly
- Remove any debug print statements
- Check for platform-specific issues (Windows vs. Linux line endings)

### Codespace won't start
- Try refreshing the page
- Check GitHub's status page for outages
- Try creating a new codespace

### "Nothing to commit"
- Make sure you saved your files
- Check that you're in the correct directory
- Use `git status` to see what's changed

## Getting Help

If you encounter issues:
1. Check the assignment README for specific instructions
2. Review the test output in the Actions tab for error details
3. Ask on the course discussion forum
4. Contact your instructor during office hours

## Resources

- **GitHub Docs:** https://docs.github.com/
- **GitHub Classroom Student Guide:** https://docs.github.com/en/education/manage-coursework-with-github-classroom/learn-with-github-classroom
- **Git Tutorial:** https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control
- **VS Code in Codespaces:** https://docs.github.com/en/codespaces/developing-in-codespaces/using-github-codespaces-in-visual-studio-code

---

*Last updated: February 2026*
