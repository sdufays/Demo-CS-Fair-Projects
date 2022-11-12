
import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.println("What's your name?");
    String name = scan.nextLine();
    System.out.println("Hi " + name);
  }
}
