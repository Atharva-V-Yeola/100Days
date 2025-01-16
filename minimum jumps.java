class Solution {
    static int minJumps(int[] arr) {
        // code here
        int n=arr.length;
        if(n==1) return 0;
        if(arr[0]==0) return -1;
        
        int lp=arr[0];
        int je=arr[0];
        int jump =1;
        for(int i=1;i<n;++i){
            if(i==n-1) return jump;
            lp=(Math.max(lp,i+arr[i]));
            if(i==je){
                jump++;
                je=lp;
                if(je>=n-1) return jump;
            }
            if(i>=lp) return -1;
        }
        return -1;
    }
}
