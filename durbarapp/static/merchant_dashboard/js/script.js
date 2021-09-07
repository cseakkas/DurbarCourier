function toggleMenu(){
    let toggle = document.querySelector('.toggle');
    let nav = document.querySelector('nav');
    let main = document.querySelector('main');
    toggle.classList.toggle('active');
    nav.classList.toggle('active');
    main.classList.toggle('active');
}



window.addEventListener('click',function(e){
    // dorpdown open code start
    let myDropdown = e.target.closest('.userInfo, .notification, .message');
    myDropdown     = (myDropdown) ? myDropdown.querySelector('div') : false;
    (myDropdown) ? myDropdown.classList.toggle('active') : '';
    // dorpdown open code end

    closeDropdown(myDropdown);
});

function closeDropdown(currentDropdown)
{
    let alldropdown = document.querySelectorAll('.userInfo>div, .notification>div, .message>div');
        alldropdown = Array.from(alldropdown);

    alldropdown.forEach(singleDropdown=>{
        if(currentDropdown.className != singleDropdown.className){
            singleDropdown.classList.remove('active');
        }
    });
}








var dropdown = document.getElementsByClassName("subMenu");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
  this.classList.toggle("active");
  var dropdownContent = this.nextElementSibling;
  if (dropdownContent.style.display === "block") {
  dropdownContent.style.display = "none";
  } else {
  dropdownContent.style.display = "block";
  }
  });
}