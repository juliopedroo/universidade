import java.util.Scanner;

public class quest2 {

    public static void main(String args[]) {
        int escala;
        float temperatura;

        Scanner leitor = new Scanner(System.in);

        System.out.println("Informe a temperatura: ");
        temperatura = leitor.nextFloat();

        System.out.println("Informe a escala da temperatura:\n1-Celsius\n2-Fahrenheit\n3-Kelvin");
        escala = leitor.nextInt();

        if(escala == 1) {
            System.out.format("A temperatura em Celsius é: %.2f", temperatura);
            System.out.format("\nA temperatura em Fahrenheit é: %.2f", ((temperatura * 9/5) + 32));
            System.out.format("\nA temperatura em Kelvin é: %.2f", (temperatura + 273.15));
        }else if(escala == 2) {
            System.out.format("A temperatura em Fahrenheit é: %.2f", temperatura);
            System.out.format("\nA temperatura em Celsius é: %.2f", ((temperatura - 32) * 5/9));
            System.out.format("\nA temperatura em Kelvin é: %.2f", ((temperatura - 32) * 5/9 + 273.15));
        }else if(escala == 3) {
            System.out.format("A temperatura em Kelvin é: %.2f", temperatura);
            System.out.format("\nA temperatura em Celsius é: %.2f", (temperatura - 273.15));
            System.out.format("\nA temperatura em Fahrenheit é: %.2f", ((temperatura - 273.15) * 9/5 + 32 ));
        }else {
            System.out.println("Escala inválida");
        }

        System.out.println("\nPrograma Encerrado!");
    }
}