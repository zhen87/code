package com.company.day8;

import java.util.*;

public class sort {
    /*
    题目一：
编写一个程序，提示用户输入一个数组，判断该数组是否已经排好序
     */
    public static Boolean getSort(ArrayList<String> arr ){
        ArrayList<String> arr2 = new ArrayList<String>();
        System.out.println("源数据"+arr);
        for(String str : arr){
            arr2.add(str);
        }
        Collections.sort(arr);
        System.out.println("排序后"+arr);
        return arr.equals(arr2);
        }


    public static void main(String[] args) {
//        String [] arr  = new String[3];
        ArrayList<String> arr = new ArrayList<String>();
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入数组的数据");
        for (int i =0; i<6;i++){
            String SC = sc.nextLine();
            arr.add(SC);
        }
        Boolean state = getSort(arr);
        if(state){
            System.out.println("该数组已排序");
        }else {
        System.out.println("该数组未排序");
        }

    }
}

