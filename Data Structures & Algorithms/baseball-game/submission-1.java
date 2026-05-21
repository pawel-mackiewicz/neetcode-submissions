class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> record = new Stack<>();
        for(String op : operations) {
            if (op.equals("+")) {
                int a = record.pop();
                int b = record.pop();
                record.push(b);
                record.push(a);
                record.push(b+a);
            } else if (op.equals("C")) {
                record.pop();
            } else if (op.equals("D")) {
                record.push(record.peek() * 2);
            } else {
                int a = Integer.parseInt(op);
                record.push(a);
            }
        }
        int sum = 0;
        for (int a : record) {
            sum += a;
        }
        return sum;
    }
}