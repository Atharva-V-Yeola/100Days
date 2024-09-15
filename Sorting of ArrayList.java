import java.util.Scanner;
import java.util.*;

public class ArrayListSorting {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        ArrayList<Integer> inn = new ArrayList<>();
        System.out.println("For exit type 00");
        
        while (true) {
            int input = s.nextInt();
            if (input == 00) {
                break;
            }
            inn.add(input);
        }
        System.out.println(inn);
        Collections.sort(inn);
        System.out.println(inn);
        s.close();
    }
}
