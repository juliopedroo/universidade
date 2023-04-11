import java.util.Scanner;
import java.lang.Math;

public class quest1 {

    public static void main(String args[]) {
        int opcao;
        float n1 = 0, n2 = 0, resultado;

        Scanner sc = new Scanner(System.in);

        System.out.println("Qual a operação desejada? Digite os seguintes valores:\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Potenciação\n6-Raiz Quadrada\n7-Raiz Cubica");
        opcao = sc.nextInt();

        if(opcao > 0 && opcao <5) {
            System.out.println("Digite o primeiro número: ");
            n1 = sc.nextInt();
            System.out.println("Digite o segundo número: ");
            n2 = sc.nextInt();
        }else if(opcao>5 && opcao <8){
            System.out.println("Digite o numero: ");
            n1 = sc.nextInt();
        }

        switch(opcao) { //como decidi receber a operação por valores numericos, o switch case se aplica bem
            case 1:
                resultado = n1 + n2;
                System.out.println("O resultado é: "+resultado);
                break;
            case 2:
                resultado = n1 - n2;
                System.out.println("O resultado é: "+resultado);
                break;
            case 3:
                resultado = n1 * n2;
                System.out.println("O resultado é: "+resultado);
                break;
            case 4:
                if(n2 == 0) {
                    System.out.println("Impossivel dividir por zero!");
                    break;
                }
                resultado = n1 / n2;
                System.out.println("O resultado é: "+resultado);
                break;
            case 5:
                System.out.println("Digite o valor da base: ");
                n1 = sc.nextInt();
                System.out.println("Digite o valor do expoente: ");
                n2 = sc.nextInt();
                resultado = (float) Math.pow(n1, n2);
                System.out.println("O resultado foi: "+resultado);
                break;
            case 6:
                resultado = (float) Math.pow(n1, 0.5);
                System.out.format("Resultado: %.2f", resultado);
                break;
            case 7:
                resultado = (float) Math.pow(n1, 0.333);
                System.out.format("Resultado: %.2f", resultado);
                break;

        }
        System.out.println("\n\nPrograma Encerrado!");
    }

}