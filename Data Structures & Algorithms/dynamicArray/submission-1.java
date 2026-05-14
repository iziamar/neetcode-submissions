class DynamicArray {
    int[] arr;
    int cap;
    int size;

    public DynamicArray(int capacity) {
        arr = new int[capacity];
        cap = capacity;
        size = 0;
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        if (arr[i] == 0){
            size++;
        }
        arr[i] = n;
    }

    public void pushback(int n) {
        if (size == cap){
            resize();
        }
        arr[size] = n;
        size++;
    }

    public int popback() {
        if(size > 0){
            size--;
        }
        return arr[size];
    }

    private void resize() {
        int[] newArr = new int[cap*2];
        for(int i = 0; i < cap; i++){
            newArr[i] = arr[i];
        }
        arr = newArr;
        cap = cap * 2;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return cap;
    }
}
