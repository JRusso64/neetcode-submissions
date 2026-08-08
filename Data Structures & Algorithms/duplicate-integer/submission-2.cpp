class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> mySet;

        for(int i = 0; i < nums.size(); i++){
           if(mySet.count(nums[i]) == 1){
                return true;
           }
           mySet.insert(nums[i]);
        }

        return false;
    }
};