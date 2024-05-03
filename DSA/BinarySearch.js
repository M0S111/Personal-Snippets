/* Returns either the index of the location in the array,
  or -1 if the array did not contain the targetValue */
var doSearch = function(array, targetValue) {
	var min = 0;
	var max = array.length - 1;
    var guess;
    var t_g = [];
    
    while (max >= min){
        guess = Math.floor((max + min)/2);
        t_g.push(guess);
        
        if (array[guess] === targetValue){
            console.log("Found prime in "+ t_g.length-1 +" guesses at index " + guess);
            return 0;
        }
        
        else if (array[guess] < targetValue){
            min = guess + 1;
        }
        
        else {max = guess - 1;}
        
        console.log(guess);
        
    }

	return -1;
};

var primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
		41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];

var result = doSearch(primes, 73);