var insert = function(array, rightIndex, value) {
    
    var temp;
    
    for (rightIndex; value < array[rightIndex] ; rightIndex--)
    {
        temp = array[rightIndex];
        array[rightIndex] = value;
        array[rightIndex + 1] = temp;
    }
    
    return array;

    // for(var j = rightIndex; j >= 0 && array[j] > value; j--) {
    //     array[j + 1] = array[j];
    // }   
    // array[j + 1] = value;
    
};

var insertionSort = function(array) {

    for(var i = 1; i < array.length; i++){
        insert(array, i-1, array[i]);
    }

    return array;

};

var array = [3, 5, 7, 11, 13, 2, 9, 6];

console.log(insertionSort(array));

// insert(array, 5, 9);
// console.log("Array after inserting 9:  " + array);
// //Program.assertEqual(array, [2, 3, 5, 7, 9, 11, 13, 6]);

// insert(array, 6, 6);
// console.log("Array after inserting 6:  " + array);
// //Program.assertEqual(array, [2, 3, 5, 6, 7, 9, 11, 13]);
