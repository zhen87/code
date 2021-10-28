package com.company.day2;

public class TestOne {
    public static void main(String[] args) {
        int n = 1;
        int sum = 0;
        sum = n;
        System.out.println(sum);
        while (sum < 5050){
            n++;
            sum += n;
        }
        System.out.println(sum);
        System.out.println(n);



    }
}
