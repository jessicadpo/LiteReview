# LiteReview
#### IRM3004 - Group Project
#### Team Stonks (#8)

---
**App Description**

A lightweight web application titled LiteReview. In the same vein as social media review websites such as Goodreads, MyAnimeList, and Letterboxd, LiteReview will be a simple website enabling users to track, rate, and review the entertainment media they consume. Unlike Goodreads, MyAnimeList or Letterboxd, however, LiteReview will not restrict itself to only one type of media (e.g., only books, only TV shows, or only movies). Instead, users will be able to post reviews for books, films, TV shows, and music media. They will also be able to search for other users and see what they have posted.

**Product Goal**

By the end of March 2024, we will have designed, developed, and implemented both the front- and back-end of our web application to fulfill the needs of entertainment media consumers looking for a single, centralized platform with comprehensive media tracking and review features; the product will be ready to attract and serve a growing number of users and be well-positioned for monetization through advertisements. The front-end will constitute a simple, easy-to-use, and visually appealing user interface with search bar, sort, and filter functionalities. The back-end will involve a server-side database supporting the following user activities: account creation, automated profile page creation, login authentication, and postings (i.e., reviews).

**Definition of Done (Sprint #2)**
- Buttons behave as expected/perform expected functions
- Website has colors (i.e., is not light mode) & official icons (not placeholders)
- No known defects/issues/bugs/glitches
- “python manage.py runserver” executes with no issues
- All branches have been merged to main branch
  - By definition, this means all pull requests passed all linters & automatic tests, and have been peer-reviewed.

**End-Sprint Screenshot(s)**

<ins>Homepage (logged out)</ins>
![homepage-logged-out.png](screenshots%2Fhomepage-logged-out.png)

<ins>Homepage (logged in)</ins>
![homepage-logged-in.png](screenshots%2Fhomepage-logged-in.png)

<ins>Sign Up / Login page</ins>
![signup-login-page.png](screenshots%2Fsignup-login-page.png)

<ins>Create Review modal</ins>
![create-review-modal.png](screenshots%2Fcreate-review-modal.png)

<ins>My Account modal</ins>
![my-account-modal.png](screenshots%2Fmy-account-modal.png)

<ins>User profile page (logged in, collapsed)</ins>

<ins>User profile page (logged out, expanded)</ins>

### Features (Progress Summary)
> **Done**
> - Basic HTML & CSS layout of sign-up/log-in page
> - Basic HTML & CSS layout of homepage
> - Basic HTML & CSS layout of user page (template)
> - Basic HTML & CSS layout of "Create Review" & "My Account" modal forms
> - **JavaScript:** Create Review & My Account forms appear/disappear on button click
> - **Backend:** Database models for user accounts and reviews
> - CSS colors for all pages
> - Replace placeholder logo and icons with "official" versions 
> - Plug data received from views into HTML templates (i.e., implement curly brackets)
> - Replaced "Signup/Login button" with "My Account" & "Logout" button in top-right corner when user is logged in
> - Hide "+" button if user is logged out
> - Make reviews collapsible
> - Form validation for Sign-up & login forms
> - Generate a unique url for every new user signing up 
> - Login functionality 
> - Add users in database when receive valid POST requests 
> - Add reviews in database when receive valid POST requests 
> - Retrieve the 20 most recent reviews to display on homepage 
> - Retrieve all reviews made by a user to display on their user page

> **Not yet done**
> - <u>**HTML & CSS**</u>
>   - Responsive layout for mobile devices
>   - Add current account information to "My Account" modal
>   - "Delete Account" & "Delete Review" confirmation popup
>   - "Edit Account" modal form (variation of Create Review form)
>   - Filter menu
>   - Sort menu
> - <u>**JavaScript**</u>
>   - Show/Hide Filter & Sort menus on button click
>   - Access user profile pages via search bar
>   - Only show "Edit Review" buttons if user is viewing their own page
>   - Form validation for Create Review, Edit Review & Edit Account forms
>   - Pre-fill "Edit Review" form with review data
>   
> - <u>**Backend**</u>
>   - Filtering reviews
>   - Sorting reviews
>   - Update/Delete users in database when receive valid POST requests
>   - Update/Delete reviews in database when receive valid POST requests
>   - Retrieve the 20 most recent reviews to display on homepage
>   - Retrieve all reviews made by a user to display on their user page
>   - Pre-fill "My Account" form with logged-in user's account data