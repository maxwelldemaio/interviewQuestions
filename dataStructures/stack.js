class Stack {
    constructor() {
        this.items = {};
        this.size = 0;
    }

    push(val) {
        // Push item to the stack
        this.items[this.size] = val;
        // Increase size of stack
        this.size++;
    }

    pop() {
        // Get reference to top item
        const top = this.items[this.size - 1];
        // Remove item from stack
        delete this.items[this.size - 1];
        // Decrement size
        this.size--;
        // Return popped item
        return top;
    }

    peek() {
        // Look at item at top of stack
        return this.items[this.size - 1]
    }

    size() {
        // Return size of stack
        return this.size;
    }

    isEmpty() {
        // Check if stack has no items
        return (this.size === 0);
    }
}

// Create a stack instance
let myStack = new Stack;

myStack.push(1);
myStack.push(2);
console.log(myStack);
console.log(myStack.pop());
console.log(myStack);