package com.company.day5;

public class test2 {
    /*
    题目二：
在控制台打印下面的菱形图案
                *
           * *
      *   *
         *     *
          *   *
           * *
            *

     */

    public static void main(String[] args) {

        for (int i =7;i>=1;i--){
            if (i %2==1){
                System.out.print("\t");
            }else {
                System.out.print("*");
                break;
            }





        }

    }
}
