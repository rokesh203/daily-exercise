/*public class star {
public static void main(String args[]){
    for(int i=1;i<=3;i++){
        for(int j=1;j<=3;j++){
            System.out.print("*");
        
        }
        System.out.println();
    }
}
}
*/

        
class star{
    public static void main(String args[]){
        for(int i=1;i<=3;i++){
            System.out.println("hello");
            for(int j= 1;j<=i;j=j++){
                System.out.print("*");
            }
            System.out.println("");
        }
    } 
}