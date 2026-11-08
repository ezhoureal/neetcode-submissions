class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        deque<int> heap; // min-heap, keeping k largest number
        for (int i : nums) {
            heap.push_back(i);
            int index = heap.size() - 1;
            while (index > 0) {
                int parent = (index - 1) / 2;
                if (heap[index] > heap[parent]) {
                    break;
                }
                swap(heap[index], heap[parent]);
                index = parent;
            }
            if (heap.size() > k) {
                swap(heap[0], heap[k]);
                heap.pop_back();
                int index = 0;
                while (index * 2 + 1 < k) {
                    int next = index;
                    int left = index * 2 + 1;
                    int right = index * 2 + 2;
                    if (heap[left] < heap[index]) next = left;
                    if (right < k && heap[right] < heap[next]) next = right;
                    if (next == index) break;
                    swap(heap[index], heap[next]);
                    index = next;
                }
            }
        }
        return heap[0];
    }
};
