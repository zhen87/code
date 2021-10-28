package com.company.day7;

public class getMin {

    /*
    定义一个函数，获取某个数组中的最小值/
     */
    public static double GetMinNumber(double[] list){
        double minNum = list[0];
        for(int i=0; i < list.length;i++){
            minNum= minNum<=list[i]?minNum:list[i];
//            minNum = Math.min(minNum,list[i]);
        }
        return minNum;
    }

    public static void main(String[] args) {
//        double[] Num ={12,4,5,767,222,1.23};
        double[] Num ={2,1, 3 ,4, 5};
        double minNum = GetMinNumber(Num);
        System.out.println(minNum);

    }

}
