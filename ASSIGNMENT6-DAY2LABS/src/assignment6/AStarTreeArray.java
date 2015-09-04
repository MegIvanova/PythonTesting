package assignment6;
import java.util.Scanner;

public class AStarTreeArray {
	private static Scanner input;

	public static void main(String[] args) {
	
		// Create a Tree of stars. The user decides the length of the tree. 
	   	
		 
		 double length = 0;
		 input = new Scanner (System.in);
		 System.out.println("Enter the length of the tree: ");
		 length = input.nextDouble();
	 
         for (int x = 1; x < length+1; x++)
         {
        	 for (int y = 0; y < x; y++)
        	 {
		 System.out.print("*");
        	 }
        	  System.out.print("\n");
         }
	} 
}
	
// length+1 is the number if stars 
// \n
