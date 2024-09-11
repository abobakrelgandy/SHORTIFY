// Get the modal
var modal = document.getElementById("shortenModal");
        
// Get the button that opens the modal
var btn = document.getElementById("btn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

var modalContent = document.getElementsByClassName("modal-content");

var errorMessage = document.getElementById("error-message");

var shortenedLink = document.getElementById("shortenedLink");


// Function to show the modal with the short link
function showModal(shortLink) {
    shortenedLink.innerHTML = shortLink;
    modal.style.display = "block";
}

// Copy to clipboard function
shortenedLink.onclick = function() {
  var textArea = document.createElement("textarea");
  textArea.value = shortenedLink.innerHTML;
  document.body.appendChild(textArea);
  textArea.select();
  document.execCommand("copy");
  document.body.removeChild(textArea);

  // Display a "Copied!" message
  var copyMessage = document.getElementById("copyMessage");
  copyMessage.style.display = "block";

  // Hide the message after 2 seconds
  setTimeout(function() {
      copyMessage.style.display = "none";
  }, 2000);
}


// When the user clicks the shorten button, submit the form via AJAX
btn.onclick = function() {
  var inputField = document.querySelector('input[name="original_url"]');
  var originalUrl = inputField.value.trim();
  
  errorMessage.style.display = "none";


  if (originalUrl === "") {
    errorMessage.innerHTML = "URL Required*";
    errorMessage.style.display = "block";
    return;
}

    var form = document.getElementById("shortenForm");
    var formData = new FormData(form);
    
    // Send form data to server and get shortened link
    fetch(form.action, {
        method: 'POST',
        body: formData
    }).then(response => response.json())
      .then(data => {
          var shortLink = data.short_code;
          showModal(shortLink);
      });
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}        
