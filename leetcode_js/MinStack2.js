/**
 * initialize your data structure here.
 */
var MinStack = function() {
    this.items = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
    // Add item to stack
    this.items.push(x);
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    // Make sure stack is not empty
    if (this.size < 1) {
        throw new Error('No items in the stack');
    }
    this.items.pop();
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
    return this.items[this.items.length -1];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    // Make sure stack is not empty
    if (this.size < 1) {
        throw new Error('No items in the stack');
    }
    return Math.min(...this.items);
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

 