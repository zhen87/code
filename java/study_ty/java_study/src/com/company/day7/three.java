package com.company.day7;

import java.util.Scanner;

public class three {
    /*
    题目一：
设计一个函数，内部通过使用三目表达式来实现两个整数大小的比较
     */
    public static int BigNum(int a,int b){

        return (a>=b)?a:b;
    }

    public static void main(String[] args) {
        System.out.println("请输入数值");
        Scanner SC = new Scanner(System.in);
        int a = SC.nextInt();
        System.out.println("请输入数值");
        int b = SC.nextInt();
        int bigNum = BigNum(a,b);
        System.out.println("较大值为"+bigNum);
    }
}
