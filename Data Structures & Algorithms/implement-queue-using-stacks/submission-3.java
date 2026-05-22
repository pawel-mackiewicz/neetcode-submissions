class MyQueue {

    Stack<Integer> input = new Stack<>();
    Stack<Integer> output = new Stack<>();
    int size = 0;
    
    public MyQueue() {
        
    }
    
    public void push(int x) {
        input.push(x);
        size++;
    }
    
    public int pop() {
        if (output.isEmpty()) {
            getOutput();
        }
        size--;
        return output.pop();
    }
    
    public int peek() {
        if (output.isEmpty()) {
            getOutput();
        }
        return output.peek();
    }
    
    public boolean empty() {
        return size == 0;
    }

    private void getOutput() {
        while (!input.isEmpty()) {
            output.push(input.pop());
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