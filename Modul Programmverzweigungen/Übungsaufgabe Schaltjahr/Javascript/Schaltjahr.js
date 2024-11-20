function isSchaltjahr(year) {

  if(year == 0 || year < 0 || isNaN(year)){ 
    alert('Please enter a correct year');
    return;
  } else if (year == null){
    return;
  }

  if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
    alert('true');
  } else {
    alert('false');
  }

}

isSchaltjahr(prompt('Choose a year'));
