package com.company.day8;

import java.util.ArrayList;
import java.util.Scanner;

public class samNum {
    /*
    题目三：
编写一个程序，提示用户输入一个数组，如果这个数组中有四个连续的具有相同值的数，就显示true，否则为false
     */
    public static boolean samnum(ArrayList <String> arr){
        int count =0;
        for (int i = 0;i<arr.size()-1;i++){
            if (arr.get(i).equals(arr.get(i+1))){
                count+=1;
                if (count ==3){
                    return true;
                }
            }else {
                count =0;
            }
        }
        return false;
    }
    public static void main(String[] args) {
        ArrayList <String> arr = new ArrayList<String>();
        Scanner SC = new Scanner(System.in);
        System.out.println("请输入6个数字的数组");
        for(int i =0;i<6;i++){
            String sc = SC.nextLine();
            arr.add(sc);
        }
        boolean state = samnum(arr);
        if (state){
            System.out.println("该数组有存在大于4个相同的数据");
        }else {
            System.out.println("该数组中不存在4个相同的数据");
        }
    }
}
