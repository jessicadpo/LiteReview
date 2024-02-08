# LiteReview
IRM3004 - Group Project

HOW TO SET UP
1. In terminal: `git clone https://github.com/jessicadpo/LiteReview.git`
2. Create branch: `git checkout -b yourBranchName`. This creates and switches you to that branch at the same time.
3. `git status`. Double-check you're in the correct branch.
4. To run the server/website: `python manage.py runserver`
5. Access application at http://127.0.0.1:8000

HOW TO UPLOAD CHANGES TO GITHUB:
1. `git add .`. Adds all the files to be committed.
2. `git status`. Double-check that all relevant files are in green.
3. `git commit`
4. Write commit message.
5. Press Ctrl+C.
6. `:wq`
7. Press ENTER.
8. TO ASK PROF: How "merge" main branch INTO feature branch? (NOT the other way around)
8. `git push origin yourBranchName`. DO NOT WRITE "git push origin main". DO NOT WRITE "git merge yourBranchName".
9. If the code is complete and tested, go to GitHub & create a pull request.
