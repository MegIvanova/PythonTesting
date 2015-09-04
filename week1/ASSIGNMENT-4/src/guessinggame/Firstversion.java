package guessinggame;
import java.util.Scanner;

public class Firstversion {
	
	 private static Scanner keyboard;

	public static void main(String[] args) {
         
		int secretNumber;
        secretNumber = (int) (Math.random() * 10 + 1);           
        keyboard = new Scanner(System.in);
        int guess;
        
         do {
               System.out.print("Enter a guess (1-10): ");
               guess = keyboard.nextInt();
               if (guess == secretNumber)
                     System.out.println("Your guess is correct. Congratulations!");
               else if (guess < secretNumber)
                     System.out
                                .println("Your guess is smaller than the secret number.");
               else if (guess > secretNumber)
                     System.out
                                .println("Your guess is greater than the secret number.");
         } while (guess != secretNumber);
   }
}
			
// only 3 times