class Node{

	constructor(element){

		this.element = element; /*data goes here*/
		this.next = null; /*'pointer' to next memory location*/
	}
}

class LinkedList{

	constructor(){

		this.head = null; /*start of list*/
		this.tail = null; /*end of list*/
		this.size = 0; /*size of list*/
	}


	push(element){ /*add element to tail*/

		var node = new Node(element);

		var current;

		if (this.tail == null){ /*assign new node as head & tail of linked list if list is empty*/

			this.head = node;
			this.tail = this.head;
		}

		else{ /*if tail isn't null set current variable to tail node and its pointer next to new node*/

			current = this.tail;

			current.next = node;

			this.tail = current.next;

			// current = this.head;

			// while (current.next){

			// 	current = current.next;
			// }

			// current.next = node; /*add new node at end of list*/

		}

		this.size++; /*increment size when adding node*/
	}

	pushAtFront(element){

		var node = new Node(element);

		var current = this.head;

		node.next = current;

		this.head = node;

		if (this.tail == null){

			this.tail = this.head;
		}

		this.size++;
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

	popAtFront(){

		var current = this.head;

		if (this.head == null){
			throw "Empty List!";
		}

		this.head = current.next;

		if (this.head == null){
			this.tail = null;
		}

		this.size--;

		return console.log(current.element);
	}


	removeAt(idx){ /*return element at index with removal*/

		var current = this.head;

		var previous = null;

		var count = 0; /*to track list traversal*/
		

		if (current.next == null) { /*return head when index is 0 or list has 1 element*/
			

			this.head = null;

			this.size = 0;

			return console.log(current.element);

		}

		else if (idx == 0) {

			this.head = current.next;

			this.size--;

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

	lsize(){
		return console.log(this.size);
	}

	print(){

		var current = this.head;

		var result = [];
		

		if (current.next == null) {

			result.push(current.element);

			return console.log(result);

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

	isEmpty(){
		return console.log(this.size == 0);
	}
}

var ll = new LinkedList();

ll.push(1);
ll.push(2);
ll.push(3);
ll.push(4);
ll.push(5);

ll.lsize();

ll.print();

ll.removeAt(0);
//ll.removeAt(0);
//ll.removeAt(0);*/

ll.pushAtFront(55);
ll.pushAtFront(44);
ll.pushAtFront(33);

ll.print();

ll.popAtFront();
ll.popAtFront();

ll.print();

ll.lsize();

ll.getAt(0);

ll.print();

ll.isEmpty();

ll.pop();
ll.pop();
ll.pop();
ll.pop();
ll.pop();
ll.isEmpty();