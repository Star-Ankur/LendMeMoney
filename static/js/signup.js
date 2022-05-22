function seterror(id, error) {
  element = document.getElementById(id);
  element.getElementsByClassName('error')[0].innerHTML = error;
}

function validateForm() {
  var returnValue = true;
  // performing password validation 
  var password = document.forms['form']['floatingPassword'].value;
  var username = document.forms['form']['floatingUsername'].value;
  var email = document.forms['form']['floatingEmail'].value;
  var pass = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
  if (password.match(pass) == null) {
      seterror("Password", "*The password must be atleast 8 characters long and should contain at least one lowercase letter, one uppercase letter, one numeric digit and one special character");
      returnValue = false;
  }
  return returnValue;
}