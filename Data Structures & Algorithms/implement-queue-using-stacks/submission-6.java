class MyQueue {

    Stack<Integer> input = new Stack<>();
    Stack<Integer> output = new Stack<>();
    
    public MyQueue() {
        
    }
    
    public void push(int x) {
        input.push(x);
    }
    
    public int pop() {
        getOutput();
        return output.pop();
    }
    
    public int peek() {
        getOutput();
        return output.peek();
    }
    
    public boolean empty() {
        return input.isEmpty() && output.isEmpty();
    }

    private void getOutput() {
        if (output.isEmpty()) {
            while (!input.isEmpty()) {
                output.push(input.pop());
            }
        }
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */