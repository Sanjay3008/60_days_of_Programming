class Solution{
    public static int doUnion(int a[], int n, int b[], int m) 
    {
        HashSet<Integer> set = new HashSet<Integer>();
        
        int i=0;
        int j=0;
        
        while(i<a.length)
        {
            set.add(a[i++]);
        }
        while(j<b.length)
        {
            set.add(b[j++]);
        }
        
        return set.size();
        
    }
}
