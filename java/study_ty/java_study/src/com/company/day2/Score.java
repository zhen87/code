package com.company.day2;

import java.util.Scanner;

public class Score {
    public static void main(String[] args) {
        Scanner input= new Scanner(System.in);
        System.out.println("请输入你的成绩");
        double score = 0;
            try {
                score = input.nextDouble();
                if (0<score && score<60){
                    System.out.println("成绩不及格");
                }else if(60<= score && score <90){
                    System.out.println("成绩良好");
                }else if(score <=100){
                    System.out.println("成绩优秀");
                }else{
                    System.out.println("成绩输入错误，不在成绩范围内");
                }
            }catch (Exception e){
                e.printStackTrace();
            }
        }
    }
