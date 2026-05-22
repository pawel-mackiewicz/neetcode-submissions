class MyQueue {

    Stack<Integer> s1 = new Stack<>();
    Stack<Integer> s2 = new Stack<>();
    
    public MyQueue() {
        
    }
    
    public void push(int x) {
        if (s1.isEmpty()) {
            s1.push(x);
        } else {
            s2.push(x);
        }
    }
    
    public int pop() {
        int res = s1.pop();

        // move all but one
        for (int i = 0; i < s2.size()-1; i++) {
            s1.push(s2.pop());
        }

        // swap 
        var tmp = s1;
        s1 = s2;
        s2 = tmp;

        return res;
    }
    
    public int peek() {
        return s1.peek();
    }
    
    public boolean empty() {
        return s1.isEmpty();
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