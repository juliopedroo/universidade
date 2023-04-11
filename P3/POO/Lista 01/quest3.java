import java.util.Scanner;

public class quest3 {

    public static void main(String args[]) {
        String nome, sobrenome;

        Scanner leitor = new Scanner(System.in);

        System.out.println("Informe seu nome: ");
        nome = leitor.nextLine();

        System.out.println("Informe seu sobrenome: ");
        sobrenome = leitor.nextLine();

        if(sobrenome.equals("Wayne")) {
            System.out.println("Acesso liberado, Sr. Wayne");
        }else if(sobrenome.equals("Kent")) {
            System.out.println("Saí daí, mané!");
        }else if(nome.equals("Diana")) {
            System.out.println("Bem-vinda, Princesa de Themyscara");
        }else {
            System.out.println("Cai fora!");
        }
    }
}