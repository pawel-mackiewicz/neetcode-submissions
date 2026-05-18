class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> values = new HashSet<Integer>();

        for (int val : nums) {
            if (!values.add(val)) {
                return true;
            }
        }
        return false;
    }
}