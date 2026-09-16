import java.util.Scanner;

public class Age {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Quel âge as-tu ? ");
        int age = scanner.nextInt();

        if (age >= 18) {
            System.out.println("Tu es majeur.");
        } else {
            System.out.println("Tu es mineur.");
        }

        scanner.close();
    }
}
