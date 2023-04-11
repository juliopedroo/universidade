import java.util.Scanner;

public class quest4 {
    public static void main(String args[]) {
        int numero;

        Scanner leitor = new Scanner(System.in);

        System.out.println("Informe um numero: ");
        numero = leitor.nextInt();

        if(numero % 2 == 0) {
            System.out.format("O numero é par e sua raiz cubica é: %.2f", Math.pow(numero, 0.333));
        }else {
            System.out.format("O numero é impar e sua raiz quadrada é: %.2f", Math.pow(numero, 0.5));
        }

    }
}