class Node{

	constructor(element){

		this.element = element; /*data goes here*/
		this.next = null; /*'pointer' to next memory location*/
	}
}

class LinkedList{

	constructor(){

		this.head = null; /*start of list*/
		this.size = 0;
	}


	push(element){ /*add element to tail*/

		var node = new Node(element);

		var current;

		if (this.head == null){ /*assign new node as head of linked list if head is null*/

			this.head = node;
		}

		else{ /*if head isn't null set current variable to head node and iterate to last node*/

			current = this.head;

			while (current.next){

				current = current.next;
			}

			current.next = node; /*add new node at end of list*/

		}

		this.size++; /*increment size when adding node*/
	}

	pop(){ /*remove & return element from tail*/

		var current = this.head;

		var previous = null;
		

		if (current.next == null) { /*in case of one element*/
			

			this.head = null;

			this.size = 0;

			return console.log(current.element);

		}

		else { /*iterate to end of list while moving next pointer forward*/

			while (current.next) {

				previous = current;

				current = current.next;

			}

			previous.next = current.next; /*pointer points to n-1 position*/

			this.size--; /*decrement size*/

			return console.log(current.element);
		}

		
	}


	removeAt(idx){ /*return element at index without removal*/

		var current = this.head;

		var previous = null;

		var count = 0; /*to track list traversal*/
		

		if (current.next == null || idx == 0) { /*return head when index is 0 or list has 1 element*/
			

			this.head = null;

			this.size = 0;

			return console.log(current.element);

		}

		else { /*iterate through till count == index & remove*/

			while (current.next && count < idx) {

				previous = current;

				current = current.next;

				count++;

			}

			previous.next = current.next;

			this.size--;

			return console.log(current.element);
		}

	}


	getAt(idx){ /*return values without removing*/

		var current = this.head;

		var count = 0;
		

		if (current.next == null || idx == 0) {

			return console.log(current.element);

		}

		else {

			while (current.next && count < idx) {

				current = current.next;

				count++;

			}

			return console.log(current.element);
		}

	}

	print(){

		var current = this.head;

		var result = [];
		

		if (current.next == null) {

			return console.log(current.element);

		}

		else {

			while (current.next) {

				result.push(current.element);

				current = current.next;

				if (current.next == null) {
					
					result.push(current.element);

					break;

				}

			}

			return console.log(result);
		}
	}

}

var ll = new LinkedList();