package com.company.day4;

public class guessNum {
    public static void main(String[] args) {
        /*
        题目四：生成一个1-100之间的随机数，如果这个数为88跳出循环
         */
        int num = 88;

        while (true){
            int sc = (int)(1+Math.random()*(100-1+1));
            if(num == sc){
                System.out.println("该随机数为88");
                break;
            }else {
                System.out.println(sc);
            }
        }
    }
}

