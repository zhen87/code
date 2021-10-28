package com.company.day8;

import java.util.Scanner;

/**
 * @Author: wangshuai
 * @Date: 2021/7/15 17:44
 * @Version: 1.0
 */
public class SortArr {

    public static void main(String[] args) {
        int [] arr  = new int[4];
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入数组的数据");
        boolean flag = true;
        for (int i =0; i<4;i++){
            String SC = sc.nextLine();
            try {
                arr[i] =Integer.parseInt(SC);
            }catch (Exception e){
                System.out.println("输入不正确");
                flag = false;
                break;
            }
            if (i > 1){
                if (!((arr[i] >= arr[i-1] && arr[i-1] >= arr[i-1-1]) || (arr[i] < arr[i-1] && arr[i-1] < arr[i-1-1]))){
                    flag = false;
                }
            }
        }
        System.out.println("校验结果："+ (flag ? "已排序":"未排序"));
    }
}
