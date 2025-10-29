function submitFeedback() {
  let feedback = document.getElementById("feedback").value;
  let msg = document.getElementById("feedbackMsg");

  if (feedback.trim() === "") {
    msg.innerText = "⚠ Please enter feedback before submitting.";
    msg.style.color = "red";
  } else {
    msg.innerText = "✅ Thank you for your feedback!";
    msg.style.color = "green";
    document.getElementById("feedback").value = "";
  }
}

function openForm() {
  window.location.href = "form.html"; // Redirect to form page
}