# LiteReview
IRM3004 - Group Project

# SET UP PROJECT
1. In terminal: Go to the folder you want to put the project in (Hint: use `cd` command)
2. In terminal: `git clone https://github.com/jessicadpo/LiteReview.git`
3. Navigate to the LiteReview folder in your file explorer.
4. Open the LiteReview folder in PyCharm.

# CREATE A NEW BRANCH
1. Create a new branch per JIRA task, NOT per person.
2. `git pull origin main` Make sure you have the most recent version of the main branch.
3. `git checkout -b task-branch-name` Create and switch to your task branch at the same time.
4. `git status`. Double-check you're in the correct branch.
5. To run the server/website: `python manage.py runserver`
6. Access application at http://127.0.0.1:8000
7. Open a 2nd terminal for entering git commands.

# UPLOADING CHANGES TO GITHUB
### IF NOT DONE YET = Commit
1. `git add .`. Adds all the files to be committed.
2. `git status`. Double-check that all relevant files are in green.
3. `git commit -m "Descriptive commit message here"`
4. Press ENTER.
5. `git checkout main` Switch to local main branch.
6. `git pull origin main` Update local main branch to match GitHub's most recent main branch.
7. `git checkout task-branch-name` Switch back to your task branch.
8. `git merge main` Merge local main branch into your task branch.
9. If there are merge conflicts, resolve (if you can) or ask for clarifications on Discord.
10. `git push origin task-branch-name` DO NOT WRITE "git push origin main". DO NOT WRITE "git merge task-branch-name".

### IF DONE = Commit & Pull Request
1. `git add .` Adds all the files to be committed.
2. `git status` Double-check that all relevant files are in green.
3. `git commit -m "Descriptive commit message here"`
4. Press ENTER.
5. `git checkout main` Switch to local main branch (VERY IMPORTANT)
6. `git pull origin main` Update local main branch to match GitHub's most recent main branch.
7. `git checkout task-branch-name` Switch back to your task branch (VERY IMPORTANT)
8. `git merge main` Merge local main branch into your task branch.
9. If there are merge conflicts, resolve (if you can) or ask for clarifications on Discord.
10. [SKIP THIS STEP FOR SPRINT #1] ~~`python -m unittest discover` Make sure your task branch passes everyone's test.~~
11. `git push origin task-branch-name` DO NOT WRITE "git push origin main". DO NOT WRITE "git merge task-branch-name".
12. In GitHub: Make sure your code passes all linters & tests
13. In GitHub: If the code is complete and tested, create a pull request.

# PEER-REVIEW CODE
1. `git pull branch-to-review`
2. `git checkout branch-to-review`
3. `python manage.py runserver`
4. Access application at http://127.0.0.1:8000
5. Test that all buttons, links, and form inputs work correctly (pretend you're a user)
6. If FAIL: Reject pull request & let the code author know which tests didn't pass on Discord.
7. If PASS: Accept pull request & let the code author know that they can merge the branch.