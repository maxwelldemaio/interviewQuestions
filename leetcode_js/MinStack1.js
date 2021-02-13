/**
 * initialize your data structure here.
 */
var MinStack = function() {
    this.items = {};
    this.size = 0;
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
    // Add item to stack
    this.items[this.size] = x;
    // Increment size
    this.size++;
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    // Make sure stack is not empty
    if (this.size < 1) {
        throw new Error('No items in the stack');
    }

    // Set top of stack
    const top = this.items[this.size - 1];
    // Delete top most item
    delete this.items[this.size - 1];
    // Decrement size
    this.size--;
    // Return top element
    return top;
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    // Make sure stack is not empty
    if (this.size < 1) {
        throw new Error('No items in the stack');
    }

    // Peek top most item in stack
    return this.items[this.size - 1];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    // Make sure stack is not empty
    if (this.size < 1) {
        throw new Error('No items in the stack');
    }

    let smallest = this.items[this.size - 1];

    // O(n) strategy, loop through and if item is smaller, update
    for (const [key, value] of Object.entries(this.items)) {
        console.log(`${key}: ${value}`);
        if (value < smallest) {
            smallest = value;
        }
    }
    return smallest;
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */

var obj = new MinStack()
obj.push(8);
obj.push(2);
obj.push(1);
obj.push(9);
console.log(obj.getMin());

 