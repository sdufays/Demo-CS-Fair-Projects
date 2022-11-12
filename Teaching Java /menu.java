
//you HAVE to name the file ‘main’
// these two slashes are for comments, which means the computer doesn’t count it as code

//importing all the java libraries
import java.util.Scanner;
import java.text.NumberFormat;

class Main {
 public static void main(String[] args) {
   //creating menu items
   final double burger = 9.99;
   final double salads = 6.99;
   final double fries = 3.50;
   // not making it 'final' because we will change the value later
   double drink = 2.59;
   // creating the variable to call the Scanner class
   Scanner in = new Scanner(System.in);
   System.out.println("How many burgers would you like?");
   //storing the input for the Burgers
   int numBurgers = in.nextInt();
   System.out.println("How many salads would you like?");
   //storing the input for the Salads
   int numSalads = in.nextInt();
   System.out.println("How many fries would you like?");
   //storing the input for the fries
   int numFries = in.nextInt();
   System.out.println("How many soft drinks would you like?");
   //storing the input for the soft drinks
   int numDrink = in.nextInt();
   // if the customer does not want a soft drink, ask if they want water
  
   if(numDrink==0){
     System.out.println("Would you like a water instead? Please write 'yes' or 'no'");
     in.nextLine();            
     String water = in.nextLine();
     //if they say 'yes' or 'Yes', change the cost of drink to 1 dollar
     if(water.toLowerCase().equals("yes")){
       drink = 1.00;
       numDrink = 1;
     }
     else{
       drink = 0.0;
     }
   }
   in.close();
   double cost = burger * numBurgers + fries * numFries + drink * numDrink + salads * numSalads;
   NumberFormat money = NumberFormat.getCurrencyInstance();
   System.out.print("Your order costs " +
                    (money.format(cost)));
 }
}
