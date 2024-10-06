class Book{

    getSumme(a,b){
        return a+b;
    }

    getQuadr(a){
        return a*a;
    }

    getIsPositive(a){
        if (a === 0){
            return "neutral";
        } else if (a > 0){
                return true;
        } else {
            return false;
        }
    }

    getFact(a){
        if (a === 0){
            return 1;
        } else {
            return a * this.getFact(a-1);
        };
    }

    getFib(a){
        /* Recursive method 
        if (a < 1){
            return 0;
        } else if (a <= 2){
            return 1;
        } else {
            return this.getFib(a-1) + this.getFib(a-2);
        }; */
        let firstNumb = 0;
        let secNumb = 1;
        let nextNumb = secNumb;
        let count = 1;
        let fibArr = [];

        while(count <= a){
            fibArr.push(nextNumb);
            count+=1;
            firstNumb = secNumb;
            secNumb = nextNumb;
            nextNumb = firstNumb + secNumb;
        }
        return fibArr;
    };
}

const book = new Book();

// Task 1
console.log(book.getSumme(2,3));
// Task 2
console.log(book.getQuadr(5));
// Task 3
console.log(book.getIsPositive(2));
// Task 4
console.log(book.getFact(3));
// Task 5
console.log(book.getFib(6));
