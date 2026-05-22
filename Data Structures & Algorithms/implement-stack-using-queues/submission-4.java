class MyStack {

    Queue<Integer> q1 = new LinkedList<>();
    Queue<Integer> q2 = new LinkedList<>();

    public MyStack() {
    }
    
    public void push(int x) {
        q1.add(x);
    }
    
    public int pop() {
        int a = -1;
        while (q1.peek() != null) {
            a = q1.poll();
            if (q1.peek() != null) {
                q2.add(a);
            }
        }

        swap();
        return a;
    }
    
    public int top() {
        int a = -1;
        while (q1.peek() != null) {
            a = q1.poll();
            q2.add(a);
        }

        swap();
        return a;
    }
    
    public boolean empty() {
        return q1.peek() == null && q2.peek() == null;
    }

    private void swap() {
        var tmp = q1;
        q1 = q2;
        q2 = tmp;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */