import java.util.Scanner;

class MicrowaveTester
{
  public static void main(String args[])
  {
    Scanner myObj = new Scanner(System.in);
    System.out.println("Enter string");
    
    String string = myObj.nextLine(); 
    Microwave code = new Microwave(string);
  }
}
