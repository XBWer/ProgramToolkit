package smu.bowen.epr.datapreparation;

import java.util.List;

import smu.bowen.epr.utils.FileUtil;

public class SRCUtil {

	public static void changePackage(String oriSRCPath, String dstSRCPath, String newPackName) {
		List<String> srcStrList = FileUtil.readFileToStrList(oriSRCPath);

		Boolean ifchanged = false;
		String wrtStr = "";
		for (int i = 0; i < srcStrList.size(); i++) {
			String line = srcStrList.get(i);
			if (line.trim().startsWith("package ") && !ifchanged) {
				line = "package " + newPackName + ";";
				ifchanged = true;
			}
			wrtStr += (line + "\n");
		}

		FileUtil.writeStringToFile(dstSRCPath, wrtStr);

	}

	public static void main(String[] args) {
		/*
		 * test purpose
		 */
		String oriPathString = "/home/appevolve/Desktop/2019_ISSTA_AE_225/run/Update_Example_Analysis+API-Usage_Update/EPR-Data/RepositoryWriter.java";
		String dstPathString = "/home/appevolve/Desktop/2019_ISSTA_AE_225/run/Update_Example_Analysis+API-Usage_Update/EPR-Data/RepositoryWriter_tmp.java";
		String newPackString = "main";
		changePackage(oriPathString, dstPathString, newPackString);
		System.out.println("Finished!");

	}

}
