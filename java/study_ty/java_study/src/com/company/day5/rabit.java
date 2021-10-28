package com.company.day5;


import java.util.Scanner;

public class rabit {
    /*
    题目三：
    一对兔子，从出生后第三个月起每个月都生一对兔子，小兔子长到第3个月起每个月又生一对兔子，假设兔子都不死，每个月的兔子对数是多少
     */
    public static int allRabit(int month) {

        if (month == 1 || month == 2) {
//            System.out.println("第" + month + "月有兔子1对");
            return 1;
        } else {
            System.out.println("qqqqq"+month);
            int all_rabbit = allRabit(month - 1) + allRabit(month - 2);
            System.out.println("mo"+month);
            System.out.println("第" + month + "月有兔子" + all_rabbit + "对");
             return all_rabbit;
        }
    }

    public static void main(String[] args) {
        int month;
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入1-40个月的兔子");
        month = sc.nextInt();
        if (month > 0 && month <= 40) {
            allRabit(month);
        } else
            System.out.println("输入错误");
    }
}


