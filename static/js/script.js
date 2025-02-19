const menu = document.getElementById('menu')
const navigation = document.getElementById('navigation')


menu.addEventListener('click', () => {
   navigation.classList.toggle('active');
});

const scriptURL = 'https://script.google.com/macros/s/AKfycbzuOXUaaXHCNICMu-Ogs3NxOxSD_bsPHkbPxVQskI7xGHObxX8uTjALl5ty0Y5lD8mo/exec'

const form = document.forms['form']

form.addEventListener('submit', e => {
  e.preventDefault();

  fetch('/', {
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
  .catch(error => console.error('Error!', error.message));
});
