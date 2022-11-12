import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.println("Welcome to our restaurant");
    System.out.println("How many burgers would you like?");
    int numBurgers = scan.nextInt();
    System.out.println("RECEIPT: You ordered " + numBurgers + " burgers");
  }
}
