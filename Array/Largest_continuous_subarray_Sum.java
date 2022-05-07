class Solution{

    // arr: input array
    // n: size of array
    //Function to find the sum of contiguous subarray with maximum sum.
    long maxSubarraySum(int arr[], int n){
        
        int max_sum_end = 0;
        int max_sum = -99999999;
        for(int i=0;i<arr.length;i++)
        {
            max_sum_end = max_sum_end+arr[i];
            if(max_sum_end>max_sum)
            {
                max_sum = max_sum_end;
            }
            
            if(max_sum_end<0)
            {
                max_sum_end = 0;
            }
            
            
        }
        return max_sum;
        
    }
