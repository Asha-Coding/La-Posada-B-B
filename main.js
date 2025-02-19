const menu = document.getElementById('menu')
const navigation = document.getElementById('navigation')

menu.addEventListener('click',() => {
   navigation.classList.toggle('active');
});
