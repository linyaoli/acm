class LRUCache {
    public:
        LRUCache(int capacity) {
            this.size = capacity;
        }

        int get(int key) {
            if(checkExistance(key)) {
                return key;
            }
            else {
                if (cacheQueue.size() < size)
                    cacheQueue.push(key);
                else {
                    return cacheQueue.pop();
                }
            }
        }
//whatever, its like this.
        void set(int key, int value) {

        }

        ~LRUCache() {

        }

    private:
        Queue<int> cacheQueue;
        int size;
        bool checkCapacity(int key) {
            while(int mKey = cacheQueue.front()) {
                //well suppose front() can iteratively search queue.
               if(key == mKey)
                    return true;
            }


        }
}
