class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> indxToDiffMap;
        for(int i = 0; i < nums.size(); i++){
            int diff = target - nums[i];
            if(indxToDiffMap.contains(diff)){
                return {indxToDiffMap[diff], i};
            }
            indxToDiffMap[nums[i]] = i;
        }

        return {};
    }
};
