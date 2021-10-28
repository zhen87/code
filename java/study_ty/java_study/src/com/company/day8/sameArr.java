package com.company.day8;

import java.util.*;

public class sameArr {
    /*
    题目二：
编写一个测试程序，提示用户输入两个数组，判断两个数组是否相同
/
     */

    public static Boolean getSort(ArrayList<String> arr,ArrayList<String> arr1){
        return arr.equals(arr1);
    }

    public static void main(String[] args) {


        ArrayList<String> arr = new ArrayList<String>();
        ArrayList<String> arr2 = new ArrayList<String>();
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入数组1的6个数据");
        for (int i =0; i<6;i++){
            String SC = sc.nextLine();
            arr.add(SC);
        }
        System.out.println("请输入数组2的6个数据");
        for (int i =0; i<6;i++){
            String SC = sc.nextLine();
            arr2.add(SC);
        }
        Boolean state = getSort(arr,arr2);
        if(state){
            System.out.println("两个数组一致");
        }else {
            System.out.println("两个数组不一致");
        }



    }}
