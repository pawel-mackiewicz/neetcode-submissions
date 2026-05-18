class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) return false;

        HashMap<Integer, Integer> chars = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            int ch = s.charAt(i);
            var currVal = chars.getOrDefault(ch, 0);
            chars.put(ch, currVal + 1);
        }

        for (int i = 0; i < t.length(); i++) {
            int ch = t.charAt(i);

            if (chars.containsKey(ch)) {
                if (chars.get(ch) == 0) return false;
                int currVal = chars.get(ch);
                chars.put(ch, currVal-1);
            } else return false;
        }

        return true;
    }
}
