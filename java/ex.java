import java.util.*;
public class ex {
    public static void main(String args[]){
        Scanner s= new Scanner(System.in);
                int num2=s.nextInt();
        int[] num=new int[5];

        for (int i=0;i<num2;i++){
            num[i]=s.nextInt();
            System.out.println(num[i]);
        }
         System.out.println(Arrays.toString(num));
    }
    
}
