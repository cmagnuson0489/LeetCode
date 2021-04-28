
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
    map<int,int> m;
    vector<int> sol;
    int n = nums.size();        
        
    for(int i = 0; i<n; i++)
     {
        if(m[target - nums[i]])
        {
                sol.push_back(i);
                sol.push_back(m[target-nums[i]]-1);
                break;
        }
       
         
           
            m[nums[i]] = i + 1;     
       }
    
         return sol; 
    }      
    
   

};
