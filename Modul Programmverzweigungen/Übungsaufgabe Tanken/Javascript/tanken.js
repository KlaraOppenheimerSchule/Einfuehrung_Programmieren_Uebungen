class Tanken{

  calculate(chosenSort, anzahl){

    let calculatePrice = function(price) {
      if(anzahl >= 100){
        totalPrice = anzahl * price * 0.95;
      } else{
        totalPrice = anzahl * price;
      }
    }

    let price;
    let totalPrice;

    switch(chosenSort) {
      
      case "1": 
      price = 1;
      calculatePrice(price);
      break;

      case "2": 
      price = 1.5;
      calculatePrice(price);
      break;

      case "3":
      calculatePrice(price);
      break;

    }
    alert(`Total price is ${totalPrice}`);
  }
}

const Tank = new Tanken();
Tank.calculate(prompt('Chose a sort: 1. 91, 2. 95, 3. 98'), prompt('How much liters?'));

