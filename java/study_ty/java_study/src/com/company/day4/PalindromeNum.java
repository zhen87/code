package com.company.day4;

    /*
若一个数（首位不为0）从左到右读与从右到左读都是一样，这个数就叫做回文数，例如12521就是一个回文数。
给定一个正整数，把它的每一个位上的数字倒过来排列组成一个新数，然后与原数相加，如果是回文数则停止，如果不是，则重复这个操作，直到和为回文数为止。给定的数本身不为回文数。
例如：87则有：
STEP1: 87+78=165
STEP2: 165+561=726
STEP3: 726+627=1353
STEP4: 1353+3531=4884
编写一个程序，输入M（12<=M<=100）,输出最少经过几步可以得到回文数。如果在8步以内（含8步）不可能得到回文数，则输出0。
     */

public class PalindromeNum {
    //反转求和
    public static int getSum(int M ) {
        int x,y,z,sum,n;
        x = M % 100 % 10;
        y = M % 100 / 10;
        z = M / 100;
        n = (z==0)?x*10+y: x*100+y*10+z;
        sum = M+n;
        return sum;
    };
    // 判断是否为回文数
    public static boolean num(int M){
        int x,y,z;
         x = M % 100 % 10;
         y = M % 100 / 10;
         z = M / 100;
        if (z == 0){
            // x ==y，返回true，不然返回false
            return x == y;
        }else {
            // x ==z,返回true，不然返回false
            return x == z;
        }
    }

    public static void main(String[] args) {
        int count = 0;
        for(int i = 12 ; i <= 100;i++){
            int num_tmp =i;
            if (count <=8){
                boolean result = num(num_tmp);
                if (result){
                    System.out.println("次数为"+count);
                    System.out.println("是回文数"+i);
                }else {
                    int num1 =  getSum(num_tmp);
                    count +=1;
                    i= num1 - 1;
                }
            }

        }

    }
}







