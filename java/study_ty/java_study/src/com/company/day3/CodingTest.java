package com.company.day3;

import java.io.*;

public class CodingTest {
    public static void main(String[] args) {
        String encoding = "utf-8";
        String file_path = "D:\\java_study\\src\\com\\company\\test.txt";
        File file = new File(file_path);
        InputStreamReader read = null;
        try {
            if(file.exists()){
                 read = new InputStreamReader(
                        new FileInputStream(file),encoding);
                BufferedReader bufferedReader = new BufferedReader(read);
                String linetxt = null;
                while ((linetxt = bufferedReader.readLine())!=null){
                    System.out.println(linetxt);
                }
            }
        }catch (Exception e){
            System.out.println("读取异常");
        }finally {
            if(read != null){
                try {
                    read.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}

