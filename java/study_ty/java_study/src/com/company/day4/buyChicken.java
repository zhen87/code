package com.company.day4;

public class buyChicken {
    public static void main(String[] args) {
        /*
        题目三：公鸡5元1只，母鸡3元一只，小鸡一元3只，问100元买100只鸡有哪些购买方法
        */
        int num = 0;
        for (int i =0;i<=100;i++){
            for(int j =0;j<=100;j++) {
                for (int x = 0; x <= 100; x++) {
                    if (x % 3 == 0){
                        num = x/3;
                        if( i+j+3*num == 100 && 5*i+3*j+num == 100){
                            System.out.println("公鸡" + i + "母鸡" + j + "小鸡" + num);
                        }
                    } else if (i+j == 100 && 5*i+3*j ==100){
                        System.out.println("公鸡" + i + "母鸡" + j + "小鸡" + x);
                        }
                    }
                }
            }
        }
    }
