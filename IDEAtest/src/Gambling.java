import java.util.Scanner;
/**
 * @author : Hierarch
 *玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
 *玩家如果摇出其他点数则玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
 *其他点数玩家继续摇骰子，直到分出胜负。
 *初始金2000,玩家可自行下注
*/
public class Gambling {
    public static void main(String[] args) {
        int principal = 2000;
        while(principal > 0) {
            int counter = 1;
            System.out.println("您的本金有：" + principal);
            Scanner sc = new Scanner(System.in);
            System.out.println("请下注：");
            int bet = sc.nextInt();
            if(bet <= 0 || bet > principal) {
                System.out.println("别扯犊子！");
                continue;
            }
            int num = (int)(Math.random()*6+1) + (int)(Math.random()*6+1);
            System.out.println("您第" + counter + "次摇的点数是：" + num);
            if(num == 7 || num == 11) {
                System.out.println("玩家胜！");
                principal += bet;
            }else if(num == 2 || num == 3 || num == 12) {
                System.out.println("庄家胜！");
                principal -= bet;
            }else {
                while(true) {
                    int num_2 = (int)(Math.random()*6+1) + (int)(Math.random()*6+1);
                    counter++;
                    System.out.println("您第" + counter + "次摇的点数是：" + num_2);
                    if(num_2 == num) {
                        System.out.println("玩家胜！");
                        principal += bet;
                        break;
                    }else if(num_2 == 7) {
                        System.out.println("庄家胜！");
                        principal -= bet;
                        break;
                    }
                }
            }
        }
        System.out.println("输光了！");
    }
}
