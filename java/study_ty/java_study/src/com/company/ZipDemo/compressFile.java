package com.company.ZipDemo;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.zip.ZipOutputStream;

public class compressFile {
/*
设计一个类ZipDemo，类中提供名称为compressFile的相关方法，参数自己考虑，该方法可以将附件zipdemo目录中所有的文件以及文件夹打包成.zip文件
 */
    //压缩文件/
/*
https://blog.csdn.net/lidai352710967/article/details/89887978
1、压缩文件
srcpath ：源文件路径
outpath ：压缩后的文件路径
zipname ：压缩的文件名/
 */
    public static void  getZip(String srcpath, String outpath,String zipname) {
            File srcPath = new File(srcpath);
            File outPath = new File(outpath);
            if (! outPath.exists()){
                outPath.mkdir();
            }
            File zipfile = new File(outpath+File.separator+zipname);
            try(ZipOutputStream zos = new ZipOutputStream(new FileOutputStream(zipfile))) {
                writeZip(srcPath,"",zos);
                boolean flag = deleteDir(srcPath);
                System.out.println("删除被压缩的文件"+srcpath+"标志为：{}"+flag);


            }catch (Exception  e){
                System.out.println(e);
        }
            



    }
    /*
    删除文件
     */
    private static boolean deleteDir(File srcPath,) {
    }

    /*
    /遍历文件进行压缩
     */
    private static void writeZip(File srcfile, String parentPath, ZipOutputStream zos) {
    }


    public static void main(String[] args) {

        getZip("D:\\code_study\\java_study\\src\\com\\company\\ZipDemo",
                "D:\\code_study\\java_study\\src\\com\\company",
                "test.zip");
    }
}
