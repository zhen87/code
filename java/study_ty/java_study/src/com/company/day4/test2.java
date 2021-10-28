package com.company.day4;

public class test2 {
    /*
    输出1-100之间能被5整除的数，每行输出3个
    */
    public static void main(String[] args) {
        int count = 0;
        for(int i = 1;i<100;i++){
            if (i%5 == 0){
                System.out.print(i+"\t");
                count++;
                if(count == 3){
                    System.out.println();
                    count = 0 ;

                }

            }
        }
    }
}
