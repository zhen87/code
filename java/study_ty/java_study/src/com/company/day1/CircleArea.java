package com.company.day1;

import java.util.Scanner;

public class CircleArea {
    public static void main(String[] args) {
        double p = 3.14D;
        Scanner in = new Scanner(System.in);
        System.out.println("请输入圆的半径");
        double r;
        while(true) {
            String inR = in.nextLine();
            try {
                r = Double.parseDouble(inR);
                break;
            } catch (NumberFormatException var10) {
                System.out.println("输入的半径需要为数字");
            }
        }

        double circleArea = p * r * r;
        System.out.println("圆的面积" + circleArea);

    }
}
