// import java.util.Scanner;
public class HelloWorld {
    public static void main(String[] args) {
        /*
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入分数: ");
        int score = sc.nextInt();
        switch(score / 60) {
            case 1:
                System.out.println("合格");
                break;
            case 0:
                System.out.println("不合格");
                break;
         */

        /*
        for(int i = 1; i <= 150; i++) {
            System.out.print(i);
            if(i % 3 == 0) {
                System.out.print(" foo");
            }
            if(i % 5 == 0) {
                System.out.print(" bio");
            }
            if(i % 7 == 0) {
                System.out.print(" saz");
            }
            System.out.println();
         */

        /*
        for(int i = 1; i <= 150; i++){
            String str = "";
            str += i;
            if(i % 3 == 0){
                str += " foo";
            }
            if(i % 5 == 0){
                str += " bac";
            }
            if(i % 7 == 0){
                str += " lsk";
            }
            System.out.println(str);
         */

        /*
        int sum = 0;
        for(int i = 1; i <= 100; i++){
            if(i % 2 == 1){
                sum += i;
            }
        }
        System.out.println(sum);

        int sum2 = 0, j = 0;
        for(int i = 1; i <= 100; i++){
            if(i % 7 == 0){
                sum2 += i;
                j++;
            }
        }
        System.out.println("总和为：" + sum2);
        System.out.println("个数为：" + j);

        System.out.println("水仙花数有：");
        int x, y, z;
        double p;
        for(int i = 100; i < 1000; i++){
            x = i % 10;
            y = i / 10 % 10;
            z = i / 100;
            p = Math.pow(x, 3) + Math.pow(y, 3) + Math.pow(z, 3);
            if(p == i){
                System.out.println(i);
            }
         */

        //求1到100之间所有偶数的和


//        int sum_1 = 0;
//        for(int i = 1; i <= 100; i++){
//            if(i % 2 == 0){
//                sum_1 += i;
//            }
//        }
//        System.out.println(sum_1);
//
//        int sum_2 = 0;
//        int j = 0;
//        while(j <= 100){
//            if(j % 2 ==0){
//                sum_2 += j;
//            }
//            j++;
//        }
//        System.out.println(sum_2);
//
//        int x = 1, sum_3 =0;
//        do{
//            if(x % 2 == 0){
//                sum_3 += x;
//            }
//            x++;
//        }while(x <= 100);
//        System.out.println(sum_3);

//        String[][] str = new String[2][3];
//        str[0][0] = "凡";
//        str[0][1] = "凡凡";
//        str[0][2] = "吴亦凡";
//        str[1][0] = "肖战";
//        str[1][1] = "坤坤";
//        str[1][2] = "";
//        for (String[] strings : str) {
//            for (String string : strings) {
//                System.out.println(string);
//            }

//        int[] i1 = new int[]{2,1,4,5,6,8,9,3};
//        int max = i1[0];
//        for (int i = 1; i < i1.length; i++) {
//            max < i1[i] ? (max = i1[i]) : max;
//        }
//        System.out.println(max);
//        int[] array_1 = new int[] {2,3,5,7,11,13,17,19};
//        for (int i : array_1) {
//            System.out.print(i + "\t");
//        }
//        System.out.println();
//        int[] array_2 = new int[array_1.length];
//        int y = 0;
//        for (int j : array_1) {
//            array_2[y] = j;
//            y++;
//        }
//        for (int k = 0; k < array_2.length; k += 2) {
//            array_2[k] = k;
//        }
//        for (int x : array_2) {
//            System.out.print(x + "\t");
//        }
//        int[] array_2 = array_1;
//        for (int i : array_1) {
//            System.out.print(i + "\t");
//        }
//        System.out.println();
//        for (int j : array_2) {
//            System.out.print(j + "\t");
//        }
    }
}