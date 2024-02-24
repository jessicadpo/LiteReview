# LiteReview
#### IRM3004 - Group Project
#### Team Stonks (#8)


---
**App Description**

**Product Goal**

**Definition of Done**

**End-Sprint Screenshot(s)**


### Features (Progress Summary)
> **Done**
> - Basic HTML & CSS layout of sign-up/log-in page
> - Basic HTML & CSS layout of homepage
> - Basic HTML & CSS layout of user page (template)
> - Basic HTML & CSS layout of "Create Review" & "My Account" modal forms (in temporary files, ready to be merged into homepage & user page next sprint)
> - **JavaScript:** Create Review & My Account forms appear/disappear on button click
> - **Backend:** Database models for user accounts and reviews (ready for next sprint)

> **Not yet done**
> - <u>**HTML & CSS**</u>
>   - CSS colors for all pages
>   - Replace placeholder logo and icons with "official" versions
>   - Plug data received from views into HTML templates (i.e., implement curly brackets)
>   - "Delete Account" & "Delete Review" confirmation popup
>   - "Edit Account" modal form (variation of Create Review form)
>   - Dropdown menu for "My Account" & "Sign out" options in top-right corner of homepage & user pages
>   - Filter menu
>   - Sort menu
> - <u>**JavaScript**</u>
>   - Show/Hide Filter & Sort menus on button click
>   - Make reviews collapsible
>   - Show search results as a dropdown menu when the search bar is not empty
>   - Switch top-right dropdown menu to a button saying "Sign up / Login" if user is logged out
>   - Hide "+" button if user is logged out
>   - Only show "Edit Review" buttons if user is viewing their own page
>   - Form validation for Sign-Up, Login, Create Review, Edit Review & Edit Account forms
> - <u>**Backend**</u>
>   - Filtering reviews
>   - Sorting reviews
>   - Generate a unique url for every new user signing up
>   - Login functionality (might already be handled by Django Authentication system?)
>   - (More) Form validation for Sign-Up, Login, Create Review, Edit Review & Edit Account forms
>   - Add/Update/Delete users in database when receive valid POST requests
>   - Add/Update/Delete reviews in database when receive valid POST requests
>   - Retrieve the 20 most recent reviews to display on homepage
>   - Retrieve all reviews made by a user to display on their user page
>   - Retrieve all users whose usernames match the text entered in the search bar

> **Cancelled**
> - "Add Creator" button in "Create Review" form (multiple creators will be treated as a single string; users can use whatever punctuation they want to separate individual names)

---
# SET UP PROJECT
1. In terminal: Go to the folder you want to put the project in (Hint: use `cd` command)
2. In terminal: `git clone https://github.com/jessicadpo/LiteReview.git`
3. Navigate to the LiteReview folder in your file explorer.
4. Open the LiteReview folder in PyCharm.
5. In PyCharm's terminal:
   1. Windows: `pip install django`
   2. macOS: `pip3 install django`

# CREATE A NEW BRANCH
1. Create a new branch per JIRA task, NOT per person.
2. `git pull origin main` Make sure you have the most recent version of the main branch.
3. `git checkout -b task-branch-name` Create and switch to your task branch at the same time.
4. `git status`. Double-check you're in the correct branch.
5. To run the server/website:
   1. Windows: `python manage.py runserver`
   2. macOS: `python3 manage.py runserver`
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
14. In JIRA: Paste the link to the pull request in as the JIRA task's Comment or Description box.
15. Ping the Discord server to ask someone to review your code.

# PEER-REVIEW CODE
1. `git fetch origin branch-to-review`
2. `git checkout branch-to-review`
3. To run the server/website:
   1. Windows: `python manage.py runserver`
   2. macOS: `python3 manage.py runserver`
4. Access application at http://127.0.0.1:8000
5. Test that all buttons, links, and form inputs work correctly (pretend you're a user)
6. If FAIL: Reject pull request & let the code author know which tests didn't pass on Discord.
7. If PASS: Accept pull request & let the code author know that they can merge the branch.