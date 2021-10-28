package com.company.day4;


public class Prime {
    public static void main(String[] args) {
        /*  打印100以内的质数
        * */

        for(int i = 1;i<100; i++){
            if (i%2!= 0 && i%3!=0  && i%5!=0 && i%7!=0){
                System.out.println(i);
            }
            }
        }
    }
