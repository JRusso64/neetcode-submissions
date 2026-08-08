class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> indxToDiffMap;
        vector<int> res;
        for(int i = 0; i < nums.size(); i++){
            int diff = target - nums[i];
            if(indxToDiffMap.contains(diff)){
                vector<int> res = {indxToDiffMap[diff], i};
                return res;
            }
            indxToDiffMap[nums[i]] = i;
        }

        return res;
    }
};
