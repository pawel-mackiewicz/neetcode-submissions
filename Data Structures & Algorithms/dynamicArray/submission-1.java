class DynamicArray {
    private int[] arr;
    private int size;

    public DynamicArray(int capacity) {
        arr = new int[capacity];
        size = 0;
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        // will user use this to add new values?
        arr[i] = n;
    }

    public void pushback(int n) {
        if (size == arr.length) {
            resize();
        }
        arr[size] = n;
        size++;
    }

    public int popback() {
        //will it work as expected?
        int val = arr[size-1];
        size--;
        return val;
    }

    private void resize() { 
        // there we will have to copy all el to the new arr with double the capacity
        int cap2 = arr.length * 2;
        int[] arr2 = new int[cap2];

        for (int i = 0; i<arr.length;i++) {
            arr2[i] = arr[i];
        }

        arr = arr2;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return arr.length;
    }
}
