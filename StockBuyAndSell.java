//import java.util.*;
// import java.util.Scanner;

// public class StockBuyAndSell {
//     static int maxProfit(int n,int[] prices){
//         int diff = 0;
//         for(int i=0;i<n-1;i++){
//             for(int j=i+1;j<n;j++){
//                 diff = Math.max(diff, prices[j]-prices[i]);
//             }
//         }
//         return diff;
//     }
//     public static void main(String[] args) {
//         Scanner s = new Scanner(System.in);
//         int n = s.nextInt();
//         int[] prices = new int[n];
//         for(int i=0;i<n;i++){
//             prices[i] = s.nextInt();
//         }
//         System.out.println(maxProfit(n,prices));
//         s.close();
//     }
// }


import java.util.Scanner;
/**
 * StockBuyAndSell
 */
public class StockBuyAndSell {
    static int maxProfit(int n,int[] prices){
        int mini = prices[0];
        int diff = 0;
        for(int i= 0;i<n;i++){
            mini = Math.min(mini, prices[i]);
            diff = Math.max(diff, prices[i] - mini);
        }
        return diff;
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int[] prices = new int[n];
        for(int i=0;i<n;i++){
            prices[i] = s.nextInt();
        }
        System.out.println(maxProfit(n,prices));
        s.close();
    }
}