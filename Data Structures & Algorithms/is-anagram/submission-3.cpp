class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()){
            return false;
        }

        std::unordered_map<char, int> charMap;

        for(int i = 0; i < s.length(); i++){
            if(charMap[s[i]]) {
                charMap[s[i]] += 1;
            }else{
                charMap[s[i]] = 1;
            }
        }

        for(int i = 0; i < t.length(); i++){
            if(charMap[t[i]] > 0){
                charMap[t[i]] -= 1;
            }else{
                return false;
            }
        }
        return true;
    }
};
