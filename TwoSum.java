import java.util.*;
import java.util.HashSet;
import java.sql.Array;
import java.util.Arrays;
import java.util.Scanner;

/**
 * TwoSum
 */


 //---------------Naive Approach ---------------------
//       Time Complexity -> O(n^2)
//       Space Complexity -> O(1)

public class TwoSum {
    static boolean naive(int n, int[] arr, int key){
        for(int i=0;i<n-1;i++){
            for(int j=i+1;j<n;j++){
                if (arr[i]+arr[j]==key) {
                    return true;
                }
            }
        }
        return false;
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i]=s.nextInt();
        }
        int key = s.nextInt();
        System.out.println(naive(n, arr, key));
        s.close();
    }
}


//-------------------    Better Apporach ------------------

//       Time Complexity -> O(n)
//       Space Complexity -> O(n)
/**
 * TwoSum
 */
public class TwoSum {

    static boolean better(int n,int[] arr,int key){
        HashSet<Integer> set = new HashSet<>();
        for(int i=0;i<n;i++){
            int com=key-arr[i];
            if(set.contains(com)){
                return true;
            }
            set.add(arr[i]);
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i]=s.nextInt();
        }
        int key = s.nextInt();
        System.out.println(better(n, arr, key));
        s.close();
    }    
}

//-------------- Best Approach ---------------------

//       Time Complexity -> O(n*log(n))
//       Space Complexity -> O(1)

public class TwoSum {

    static boolean bestone(int n,int[] arr,int key){
        Arrays.sort(arr);
        int left=0, right=n-1;
        while (left<right) {
            int sum = arr[left]+arr[right];
            if (sum==key) {
                return true;
            }
            else if (sum<key) {
                left++;
            }
            else{
                right--;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i]=s.nextInt();
        }
        int key = s.nextInt();
        System.out.println(bestone(n, arr, key));
        s.close();
    }   
}

public class TwoSum {
    static boolean bs(int[] arr,int left,int right,int key){
        while (left<=right) {
            int mid = left + (right - left)/2;
            if(arr[mid]==key){
                return true;
            }
            if (mid<key) {
                left = mid+1;
            }
            else{
                right = mid - 1;
            }
        }
        return false;
    }
    static boolean besttwo(int n,int[] arr,int key){
        Arrays.sort(arr);
        for(int i=0;i<n;i++){
            int complement = key - arr[i];

            if(bs(arr,i,n-1,complement)){
            return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i]=s.nextInt();
        }
        int key = s.nextInt();
        System.out.println(besttwo(n, arr, key));
        s.close();
    }
}
