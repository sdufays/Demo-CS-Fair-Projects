import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    String[] engColors = {"red", "green", "blue"};
    String[] spanColors = {"rojo", "verde", "azul"};
    
    Scanner scan = new Scanner(System.in);
    System.out.println("Would you like to translate: red, green, or blue?");
    String englishColor = scan.nextLine();

    String spanishColor = "";
    for (int i = 0; i < 3; i++) {
      if (engColors[i].equals(englishColor)) {
        spanishColor = spanColors[i];
      }
    }
    System.out.print("Your translated color is: ");
    System.out.println(spanishColor);
  }
