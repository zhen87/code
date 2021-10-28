package com.company.day7;

import java.util.Arrays;
import java.util.List;

public class singScore {
    /*
    B哥去参加青年歌手大奖赛,有10个评委打分,去掉一个最高一个最低，求平均分?
     */
    public static double MaxScore(double[] list){
        double maxNum = list[0];
        for(int i=0; i < list.length;i++){
            maxNum = Math.max(maxNum,list[i]);
        }
        return maxNum;
    }

    public static double MinScore(double[] list){
        double minNum = list[0];
        for(int i=0; i < list.length;i++){
            minNum = Math.min(minNum,list[i]);
        }
        return minNum;
    }

    public static void main(String[] args) {
        double[] score = {90,88,22,43,55,77,22,99.3,60,100};
        double maxNum = MaxScore(score);
        System.out.println("最大值为"+maxNum);
        double minNum = MinScore(score);
        System.out.println("最小值为"+minNum);
        double sum = 0;
        for(int i = 0;i<score.length;i++){
            if(score[i] == maxNum){
               continue;
            }else if (score[i] == minNum){
                continue;
            }
            sum = sum+score[i];
        }
        System.out.println("整体得分为"+sum);
        double avg = sum/8;
        System.out.println("平均得分"+avg);

    }
}
