// Portions of this code have been provided by W3 https://www.w3schools.com/howto/howto_css_modals.asp
// Portions of said code have been edited by me and de-bugged by ChatGPT (It was a capitalization error)

// Get the create review modal
var reviewModal = document.getElementById("review-modal");

// Get the my account modal
var accountModal = document.getElementById("account-modal");

// Get the <span> elements that close the modals
var reviewCloseSpan = document.getElementById("reviewCancelBtn");
var accountCloseSpan = document.getElementById("accountCancelBtn");

// Get the cancel buttons inside the modals
var reviewCancelBtn = document.getElementById("cancelReviewBtn");
var accountCancelBtn = document.getElementById("cancelAccountBtn");

// When the user clicks the create review button, open the create review modal
function open_create_review_modal() {
    reviewModal.style.display = "block";
}

// When the user clicks the my account button, open the my account modal
function open_my_account_modal() {
    accountModal.style.display = "block";
}

// When the user clicks on <span> (x) or outside of the modals, close them
window.onclick = function (event) {
    if (event.target == reviewModal || event.target == reviewCloseSpan || event.target == reviewCancelBtn) {
        reviewModal.style.display = "none";
    }
    if (event.target == accountModal || event.target == accountCloseSpan || event.target == accountCancelBtn) {
        accountModal.style.display = "none";
    }
};