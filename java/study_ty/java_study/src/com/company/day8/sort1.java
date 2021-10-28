package com.company.day8;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class sort1 {

    /*
题目一：
编写一个程序，提示用户输入一个数组，判断该数组是否已经排好序
 */
    public static Boolean getSort(String[] arr) {
//        ArrayList<String> arr2 = new ArrayList<String>();
        String [] arr1 = new String[6];
        int count =0;
        System.out.println("源数据"+arr);
        arr1 = Arrays.copyOf(arr,arr.length);
        Arrays.sort(arr);
        System.out.println("排序后"+arr);
        for (int i =0;i<arr.length;i++){
            if (arr[i].equals(arr1[i])){
                count++;
            }
        }
        if(count == arr.length){
            return true ;
        }else {
            return  false;
        }
    }

    public static void main(String[] args) {
        String [] arr  = new String[4];
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入数组的数据");
        for (int i =0; i<4;i++){
            String SC = sc.nextLine();
            arr[i] =SC;
        }
        Boolean state = getSort(arr);
        if(state){
            System.out.println("该数组已排序");
        }else {
            System.out.println("该数组未排序");
        }

    }

}
