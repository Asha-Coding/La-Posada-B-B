const menu = document.getElementById('menu')
const navigation = document.getElementById('navigation')


menu.addEventListener('click', () => {
   navigation.classList.toggle('active');
});

const scriptURL = 'https://script.google.com/macros/s/AKfycbzuOXUaaXHCNICMu-Ogs3NxOxSD_bsPHkbPxVQskI7xGHObxX8uTjALl5ty0Y5lD8mo/exec'

const form = document.forms['form']

form.addEventListener('submit', e => {
   e.preventDefault();

   // Send data to Google Sheets
   fetch(scriptURL, {
      method: 'POST',
      body: new FormData(form)
   })
      .then(response => {
         if (response.ok) {
            console.log("Form Submitted!");
            return response.json();
         } else {
            throw new Error('Network response was not ok.');
         }
      })
      .catch(error => console.error('Error!', error.message));

   // Send data to Database
   fetch('/reservation', {
      method: 'POST',
      body: new FormData(form)
   })
      .then(response => {
         if (response.ok) {
            alert("Database Updated!");
            return response.json();
         } else {
            throw new Error('Network response was not ok.');
         }
      })
      // .catch(error => console.error('Error!', error.message))
      .finally(() => {
         // Reset form after both requests are completed
         form.reset();
      });
});


function emailSend() {
   Email.send({
      Host: "smtp.mailendo.com",
      Username: "username",
      Password: "password",
      To: 'them@website.com',
      From: "you@isp.com",
      Subject: "This is the subject",
      Body: "And this is the body"
   }).then(
      message => alert(message)
   );
}
