package com.company.day2;

public class GetJvm {
    public static void main(String[] args) {
        String s1 = "hello";
//        String s2 = "world";
        System.out.println(s1.hashCode());
        System.out.println(System.identityHashCode(s1));
        System.out.println(s1.hashCode());
    }
}
